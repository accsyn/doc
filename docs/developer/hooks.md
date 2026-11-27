# Hooks

*Important Note: This feature is exposed to [BYOS](/admin/byos/) workspaces only.*

[BYOS](/admin/byos/)

This documentation explains accsyn hooks and walks through how to configure them within your Workspace.

## What is a hook?

A hook is a configured command line that points to a script on your servers, that is executed by accsyn on certain triggers within accsyn:

- pre-submit-server; Executed on the server before a job is submitted, with job data provided. If hook execution fails, the job fails to fully submit.
- pre-submit-client; Executed on elevated\* clients before a job is submitted, with job data provided. If hook execution fails, the job fails to fully submit.
- post-submit-server;  Executed on the server after a job is submitted, with job data provided.
- post-submit-client;  Executed on  elevated\* clients after a job is submitted, with job data provided.
- post-failed-server;  Executed on the server every time a job fails, with job data provided.
- post-failed-client;  Executed on the remote elevated\* client every time a job fails, with job data provided.
- post-done-server;  Executed on the server when a job has finished, with job data provided.
- post-done-client;  Executed on the elevated\* client after a job has finished, with job data provided.
- pre-publish-server;  Executed on the server when a remote user requests to publish one or more files, with publish file data provided and expecting feedback to be provided back to accsyn (see [Publish workflow](/developer/publish/))
- publish-server;  Executed on the server when the published files from the remote user have been uploaded, with publish file data provided (see [Publish workflow](/developer/publish/))

  

\* These client hooks only apply to clients owned by an elevated accsyn user (admin or employee), like for example a site server. They will not execute on standard user clients due to privacy and security concerns.

## How does it work?

When a hook execution event triggers, accsyn executes the configured hook script on the server:

1. Data related to the specific hook is compiled and written to a temp JSON file, see syntax below.
2. The configured script command line is loaded and the expression "${PATH_JSON_INPUT}" is replaced with the full absolute path to the temp JSON input file. This enables the script to load the metadata from arguments.
3. When required (pre-publish-server hook), a temp path is generated and replaces  "${PATH_JSON_OUTPUT}". This enables the script to write back data to accsyn as needed.
4. The script is executed by the same system user as accsyn (daemon) is running on the server.

## Hook data input format

### Job lifecycle hooks

Here follows example hook input data, as being passed on to the **job-post-done-server** hook after the file "moonshot.tif" was uploaded to a project share:

```json
{
    "metadata": {
        "external": {
            "dev": true
        },
        "internal": {
            "volume": "X",
            "method": "rules",
            "index": 0
        }
    },
    "clients": [
        {
            "site": {
                "code": "hq",
                "main": true,
                "id": "66fc222ebeabd25ad64f04ec"
            },
            "code": "CoruscantVII.local",
            "role": "client",
            "os": "mac",
            "user_hr": "demo.user@accsyn.com",
            "wan_ip": "127.0.0.1",
            "id": "6a4102788e7ddf61d0305b03",
            "type": 2,
            "user": "6676f3e9c7ef4e27da254e57",
            "version": "3.7-0_3",
            "status": "online"
        },
        {
            "metadata": {
                "index": 0
            },
            "site": {
                "code": "hq",
                "main": true,
                "id": "66fc222ebeabd25ad64f04ec"
            },
            "code": "CoruscantVII.local",
            "role": "server",
            "os": "mac",
            "user_hr": "demo.admin@accsyn.com",
            "wan_ip": "127.0.0.1",
            "id": "664b5db8ed9dc749a06f9bd6",
            "type": 1,
            "user": "661014984428048969323147",
            "version": "3.7-0_3",
            "status": "online"
        }
    ],
    "code": "Delivery 'Auto del push volume 1' auto push to CoruscantVII.local: proj_task001_v001_completed",
    "user_hr": "demo.user@accsyn.com",
    "destination": "user:6676f3e9c7ef4e27da254e57",
    "engine_hr": "builtin-accsyn-transfer",
    "source_hr": "seagull",
    "source": "workspace:6645fbca9f8c4d3e7a3b678d",
    "version": "3.7-0_9",
    "queue_hr": "Auto del push volume 1",
    "destination_hr": "demo.user@accsyn.com",
    "hook": "job-post-done-server",
    "size": 118141,
    "engine": "664b6db9e43eb396e5e5542e",
    "name": "Delivery 'Auto del push volume 1' auto push to CoruscantVII.local: proj_task001_v001_completed",
    "id": "6afd7e279a94681659d4691e",
    "job": "Delivery 'Auto del push volume 1' auto push to CoruscantVII.local: proj_task001_v001_completed",
    "user": "6676f3e9c7ef4e27da254e57",
    "queue": "6afd7dcf9a94681659d46919",
    "tasks": {
        "0": {
            "destination_path": "download/cinemotion/proj_task001_v001_completed",
            "destination": "proj_task001_v001_completed",
            "source": "/Volumes/projects/FilmProj001/download/cinemotion/proj_task001_v001_completed",
            "source_share_path": "FilmProj001",
            "uri": "0",
            "destination_share": "672c827fb66ea1e50b153386",
            "size": 118141,
            "source_share": "672c827fb66ea1e50b153386",
            "destination_volume": "664b6d76e43eb396e5e55419",
            "source_path": "download/cinemotion/proj_task001_v001_completed",
            "source_volume": "664b6d76e43eb396e5e55419",
            "destination_share_path": "FilmProj001",
            "status": "done"
        }
    },
    "status": "running"
}
```

Breakdown of JSON data:

1. metadata; Job metadata, aggregated upstream over queue, share, volume and workspace (global). For server side hooks, both internal (workspace private) and external (public) metadata are provided separately. For client side hooks, only the external metadata is provided in case the party is a user having the standard role.
2. clients; The client(s) involved in execution, identified by role attribute:server = the main site transfer part or compute execution server, client = the remote side of a transfer, either a user's desktop app/server or the site server.
3. client.metadata; Client metadata, aggregated upstream over workspace.
4. code & name; The job's human readable identifier.
5. source; accsyn raw source party ident, in the form "<entitytype>:<entityid>".
6. source_hr; Source party in human readable form.
7. destination; accsyn raw destination party ident, in the form "<entitytype>:<entityid>".
8. destination_hr; Destination party in human readable form.
9. version; The accsyn backend version.
10. hook; The name of the hook.
11. size; The size of the job - sum of non-excluded task sizes.
12. engine; The engine ID.
13. engine_hr; The engine name (code).
14. id; The ID of the job.
15. user; The ID of the user that created the job.
16. user_hr; The email address of the user creating the job.
17. created; The date the job was created.
18. queue; The ID of the parent queue the job is in.
19. queue_hr; The name of the parent queue the job is in.
20. tasks; Job tasks dictionary, providing detailed information about transfer source and destination (full path and share/volume relative paths).
21. status; The status of the job during hook execution.

### Publish hooks

For detailed information about the publish hooks, head over to the [Publish documentation](/developer/publish/).

## Configure hooks

To configure hooks globally, log on as an administrator to <https://accsyn.io/admin/settings>:

1. Click on the Hooks settings tab.
2. Click the edit(pen) icon on Hook configuration setting.

![](/assets/developer_hooks-29bd8cf120a1.png)

3. Click Enable hooks to have the hook subsystem enabled.

4. If you want to run the hooks on a different server than the default (serving default volume at main site), choose the server @ Hook execution server.

5. Audit; Define by base role, which users are allowed to audit the hooks and read the execution logs.

6. Choose which hook you want to configure.

6. Click Enable.

7. Choose the entry matching the operating system your server is running, enter the local full path to your script. Keep the token "${PATH_JSON_INPUT}" - it will be replaced with the path to the temp JSON input data at runtime. (Same goes for ${PATH_JSON_OUTPUT} with the pre-publish-server hook)

  

Click [ Save ] when done to apply your hooks configuration. Test the hook by submitting a job / performing a publish.

  

### Configure queue hooks

Hooks can be overridden, or just be configured on a queue. See [Queue administration](/admin/queue/).

## Further resources

[Python API](/developer/python-api/)

Use the Python API within your hook, for example to program chained file transfer workflows.

[Outsourcing Pipeline](/tutorials/outsourcing-pipeline/)

A tutorial going through how to set up an outsourcing pipeline with accsyn, using publish hooks.
