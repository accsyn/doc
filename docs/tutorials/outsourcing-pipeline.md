# Tutorial - Outsourcing Pipeline

*Note: This tutorial is for on-prem BYOS deployments of accsyn. Please reach out to support if you need corresponding functionality with your cloud-hosted workspace.*

## Introduction

This tutorial walks through how to set up accsyn for automated end-to-end delivery of work material to a remote vendor, and ingest of produced asset(s) back into a media production pipeline, without any manual file transfer labour back and forth.

### Why automate outsourcing?

- Collecting and sending a work file package manually is time-consuming and error-prone.
- The receiving end needs to manually download the material and unpack it, which can be a challenge when in different time zones.
- When the work has been done, the vendor has no way of telling that their result aligns with your internal asset specifications.
- The assets uploaded must be manually unpacked, transferred into the production storage, validated and then ingested into the production pipeline (e.g. ftrack Publish / Autodesk Flow / Frame.io uploads).

*Summarised, providing an automated outsourcing pipeline saves a vast amount of time and leaves your staff to do creative work instead of file wrangling — invaluable when on tight deadlines and when vendors are in different time zones.*

### Why choose accsyn as the solution?

- accsyn can easily be set up to provide a turnkey solution facilitating a fully automated and streamlined outsourcing pipeline.
- Python API support facilitates programmable file transfers in workflows.
- Affordable, no hidden costs or limitations — comes with batteries included.
- Transfers go at maximum speed using ASC — the accsyn accelerated file transfer protocol.
- Full encryption during transfer (AES-128/256) and no passwords need to be set and sent to users.
- No server listening 24/7; accsyn only starts a temporary firewalled server for a brief moment during client connection establishment.
- No need to share/expose any on-prem data; have your scripts carefully collect and send exactly what the remote vendor should need to perform their work.
- Provides central monitoring, with advanced queue/bandwidth management, that is mobile phone/tablet friendly.
- Never-give-up transfers — resumes where left off when the connection is re-established, with no need for manual intervention.

### Tutorial overview

This tutorial will cover:

- Starting your trial accsyn workspace.
- Setting up a server on-prem (BYOS).
- Setting up a user server and mapping the storage volume at the vendor.
- The concepts of API-driven file transfers.
- How to build an outsourcing script that collects and delivers a work package to the vendor.
- Configuring a publishing pipeline that validates and ingests the finished assets produced by the vendor.

*Note: Made-up example data is provided in [brackets] throughout this tutorial.*

## Outsourcing Flow

![](/assets/tutorial_outsourcing_pipeline_flow.png)

## Schematics

![](/assets/tutorial_outsourcing_pipeline_schematics.png)

The schematics visualise two different scenarios:

- **Base setup** — expose production storage. In this setup you install accsyn and expose your main production area; there is no need to further sync assets to and from this server.
- **Hardened setup** (TPN or similar). For scenarios when production servers cannot be exposed to the Internet through a port forward, the storage server and accsyn "HQ" (main) are installed in a DMZ locally or in the cloud, with additional asset pre/post sync to an internal site server on the hardened internal production network.

In this tutorial, we assume the following:

- The company and workspace name is [**Acme VFX**] (API code: [**acmevfx**], API workspace endpoint: [**https://acmevfx.accsyn.com**]).
- A Linux storage server configured with an accsyn volume<sup>1</sup> [**Proj**] with API code **show**, having a project *"Something Completely Different"* located at [<code>/mnt/proj/scd</code>] that should be outsourced.
- An active workspace admin (or employee user with access to the proj volume) user: [**pipeline@acmevfx.co.uk**]. Script API sessions will run as this user.
- The project SCD has a shot with a cleanup task, with conformed source plates in the folder <code>scd_0010_0010_src</code> located at <code>/mnt/proj/scd/0010/0010/src/plates</code>.
- ftrack is used as the project management tool, holding all information about colourspace, delivery format, handles and so on. This could be any database such as Google Sheets, Autodesk Flow or even text/markup files on disk.
- The remote vendor [**Compers Inc**] has a Windows file server where work files should be downloaded and work performed on the Windows share [**clients**] on file server [**NAS**], subfolder **AcmeVFX**.
- At the remote vendor, the coordinator user email is [**emma@compersinc.com**].
- The asset produced by the vendor is published back into the pipeline via [accsyn Publish](/developer/publish/).

*<sup>1</sup> A "volume" is the root folder where accsyn has access; accsyn paths are then relative to this base folder.*

## Setting up your workspace

The first step is to create your own accsyn workspace trial. The whole process is described in detail [here](/trial/):

1. Open <https://accsyn.io/trial> in your web browser; you will be asked to sign up for your personal accsyn account (email address identifier).
2. Create a BYOS Workspace.
3. The BYOS setup wizard will be initiated; it will guide you through the process of setting up and configuring your on-prem server and storage — "Storage server" and "Storage" in the schematics above. [Storage volume configured at <code>/mnt/proj</code>]
4. Conclude the BYOS setup wizard. You now have a fully working accsyn workspace where you can start sending deliveries and sharing folders (FTP replacement) — all backed by the high-speed ASC transfer protocol.

## Setting up receipt of material at the remote vendor

Here we present three ways:

- Share a folder on storage and have the vendor manually download assets.
- For recurring vendors/partners, we recommend setting up an accsyn **User server**, which is an instance of the accsyn client running as a service/daemon in the background 24/7 transferring files.
- For other vendors, they only need to receive the delivery and will be guided through the process of installing the accsyn **Desktop App** for reliable ASC transfers.

### Folder sharing for manual asset download

This approach puts the labour on the remote vendor to download work assets themselves. For this we use standard accsyn folder sharing and grant access to relevant subfolders:

1. Log on to https://accsyn.io as an operator (admin or employee with access to the volume).
2. Go to the Storage view.
3. Browse to the project folder on storage.
4. Create a shared folder on the project folder, ready to be shared with users. Name it the same as the project [scd].
5. Go to the newly shared folder in the left-hand side share browser.
6. In this example, the user needs to download the source plates for scene 1, shot 1 — browse down to the folder [0010/0010/src].
7. On the right-hand side, click the Grant access button.
8. Choose the vendor user account [**emma@compersinc.com**].
9. Give read (download) access and then apply the permission.

The user will get a notification by email on how to use the app to download the source material themselves.

*Note: If accsyn Publish is not to be used and no Home share is created for the vendor, grant access to an output folder beneath the project where the user can upload the final work done [scd/_VENDORS/compersinc] (remember to also give write access, otherwise they will not be able to upload).*

### Installing the remote user server at the vendor

This is the most stable approach, allowing seamless and stable transfers that mitigate time-zone differences and speed up turnaround times.

First we need to have the vendor install and configure an accsyn **User server**. This enables us to push material to the vendor without them needing to manually choose where to download and store the files — **mirror paths** mode. It enables the vendor to expose their local storage, enabling you to pull missing material as needed.

Start by inviting the remote vendor account:

1. Log on as an administrator, or an employee with full access to volume [**proj**], to <https://accsyn.io/admin/users> in your browser and click INVITE USER.
2. Enter the email address of the vendor [**emma@compersinc.com**] and choose the standard user role.
3. (Optional but recommended) Check Create home share to provide the user with base access to your workspace. The home share folder is also a neat fallback in case the vendor needs to upload something manually, or you need to share something quickly.
4. The user will get an invitation email with instructions on how to activate their personal accsyn account.

Send these instructions to the vendor on how to install the accsyn user server:

1. Ask them to register the personal accsyn account and then log on to <https://accsyn.io/hosts>.
2. Go to "Daemon instances" and click INSTALL DAEMON.
3. Allocate a workstation or server computer that is powered on 24/7, with full access to the local storage, and can act as the file transfer endpoint [**accsyn vendor server**].
4. Download the installer and install the accsyn daemon; enter the code presented in the web browser when asked. Remember to configure the system user that runs the accsyn daemon process; the user needs full read and write access to the mapped share folder [<code>\\NAS\clients\AcmeVFX</code>]. There is no need to enter a "Delivery download path" when asked.
5. The daemon instance should appear shortly under "Daemon instances". At "Workspace user servers", click the "NEW" button.
6. Select workspace [**Acme VFX**] and click "Install accsyn user server for workspace 'Acme VFX'".
7. After a minute or so, the user server for your workspace should appear beneath the host.

More detailed information on how to set up a host and user server is [here](/admin/hosts/).

### Configuring local share mapping at the remote vendor user server

As a final step, we want to define the path at the vendor where all deliveries should be stored — with a mirrored (preserved) folder structure.

In this tutorial, we assume the vendor has a Windows file server named NAS, with a share clients and a designated folder AcmeVFX for I/O.

Send these additional instructions to the vendor for setting up a mapped share:

1. Shut down the accsyn daemon service on the accsyn vendor server.
2. Edit system environment variables and set variable **ACCSYN_PROJ_PATH** to <code>\\NAS\clients\AcmeVFX</code>. Note: the "PROJ" element must align with the unique volume code attribute.
3. Start the accsyn daemon again.
4. Launch and log on to the accsyn Desktop App, on the same server machine, as the vendor [**emma@compersinc.com**].
5. Open the Settings dialog by clicking the user account button in the upper-right corner.
6. Go to Share Mappings.
7. There should now be a new entry named "proj"; enable "Read" and "Write". This will enable Acme VFX operators to push files to, and pull files from, the local mapped storage folder at [<code>\\NAS\clients\AcmeVFX</code>].

*Note: The "PROJ" element in the environment variable definition must match the API code attribute on the default accsyn volume.*

## Send work files to the vendor

We now have a working sync setup, where assets can be transferred back and forth using high-speed file transfers over the home share created earlier.

Because we have mapped the accsyn volume proj at the vendor, and the vendor has granted read and write access, we are able to:

1. Create deliveries to the vendor, and they will be automatically transferred to the locally mapped volume.
2. Push material directly with the folder structure intact, using accsyn Transfer tooling.

We will walk through three different approaches:

### Send delivery to vendor

This is the option to use if the vendor has not mapped the volume at their end, but it also works if they have mapped the volume — a delivery download will in that case be spawned on delivery submission.

1. Log on to https://accsyn.io/storage as an operator (admin or employee role).
2. Choose the source assets to send to the vendor <code>scd/0010/0010/src/plates</code> at volume **proj**.
3. Click the **Share** button and then **Deliver**.
4. Enter the vendor email as recipient **emma@compersinc.com**.
5. Send the delivery.

The vendor will get a notification about the delivery. If they have mapped the volume **proj** at their end, a transfer will start immediately to download the assets to the vendor.

### Manual sync of work file assets

Here we simply use the accsyn Desktop App to push assets to the vendor manually:

1. Launch and log on to the accsyn Desktop App as an administrator, or an employee with read access to the (default) volume.
2. Go to the **Transfer** view/tab.
3. On the left-hand side, choose your workspace and browse to the folder containing the asset to push.
4. On the right-hand side, a user server entry should be available for the vendor [**emma@compersinc.com**].
5. Select the file/files to transfer; accsyn should suggest mirroring the paths at the receiving end.
6. Click the green submit button in the middle to start pushing file(s) to the user.

*Notes:*

- *If the user server entry does not appear in step 4, make sure they have mapped the volume locally via the environment variable and that they have enabled Read and Write access.*
- *The same procedure applies for pulling file(s) from the remote vendor's locally mapped volume — transfer from the vendor to your workspace (upload).*
- *If accsyn Publish is not to be used, remember to create a home share for the vendor so they have a means of uploading the final result back.*

### Automated API sync of work file assets

In this tutorial we will focus on API-driven automated transfers, controlled from within the project management tooling [ftrack].

1. Create the vendor user in ftrack [emma@compersinc.com].
2. Create a task on shot 0010 named cleanup and assign the vendor to it.
3. Craft a ftrack action script named "Outsource"; for detailed information see [ftrack Actions Documentation](https://www.ftrack.com/en/actions).
4. Design the script to operate on one or more selected tasks; have it produce a list of file asset paths relative to the proj volume that should be sent to the remote vendor.
5. Generate work description (notes) and technical metadata (colourspace, frame range, handles etc.) to a file named scd_0010_0010_cleanup_description.txt.

We are not going into detail on how to implement the ftrack logic of this script; it is fairly simple to derive from the official [ftrack Python API Documentation](https://help.ftrack-studio.backlight.co/hc/en-us/articles/13129838282519-Getting-Started-with-API).

With the list of relative file paths at hand, use the accsyn Python API to create a daily sync job that pushes the files to the vendor. For detailed information about the accsyn Python API:

[accsyn Python API Documentation](https://accsyn-python-api.readthedocs.io/)

Boilerplate code:

**Install accsyn Python API**

>pip install accsyn-python-api

**Inside the ftrack action script, implement code that collects/generates outsourcing file asset paths**

- Assume the list of file paths calculated from ftrack is generated and stored in the variable source_files:

```python
source_files = ["scd/0010/0010/src/plates/scd_0010_0010_src", "scd/0010/0010/cleanup/scd_0010_0010_cleanup_description.txt"]
```

**Import and create the accsyn session object**

It requires the following environment variables set:

```bash
ACCSYN_WORKSPACE=acmevfx

ACCSYN_API_USER=pipeline@acmevfx.co.uk

ACCSYN_API_KEY=...
```

**Note: Create a new API key at <https://accsyn.io/developer>**

```python
import accsyn_api

session = accsyn_api.Session()
```

*Note: API credentials can also be supplied with the Session object constructor.*

**Assume the vendor name is already looked up by task assignee and defined. Also assume the project name has been evaluated**

```python
vendor_name = "CompersInc"
project_name = "scd"
```

**Generate sync job name; optimal is to have one per project, vendor and day:**

```python
delivery_name = f"Outsource - deliver - {project_name} - {vendor_name} - batch 01 - {datetime.now().strftime('%y%m%d')}"
```

**Build accsyn sync transfer tasks:**

```python
tasks = []
for path_rel in source_files:
    tasks.append(f"volume=proj/{path_rel}")
```

**Create delivery:**

```python
delivery = session.create("Delivery", dict(
    name=delivery_name,
    recipients=["emma@compersinc.com"],
    tasks=tasks
))
```

A delivery is the recommended method if we have a mix of vendors with locally mapped volumes and without.

**Variant — Create transfer**

If we know that all vendors have mapped the volume locally, we can create a push transfer job directly:

```python
daily_job_name = f"Outsource - download - {project_name} - {vendor_name} - {datetime.now().strftime('%y%m%d')}"
daily_job = session.find(f'Transfer where name="{daily_job_name}"')
for path_rel in source_files:
    tasks.append(dict(
        source=f"volume=proj/{path_rel}",
        destination="emma@compersinc.com",
        mirror_paths=True
    ))
if not daily_job:
    daily_job = session.create("Transfer", dict(
        name=daily_job_name,
        tasks=tasks,
        mirror_paths=True
    ))
else:
    # Append tasks to existing sync job; will resume/retry finished job and retry (resend) existing duplicate tasks
    tasks = session.create("Task", tasks, entityid=daily_job['id'], allow_duplicates=True)
```

The transfer job will be queued with the rest of the jobs.

*Note: If multiple jobs (projects, or previous day) are active, operators can use the powerful accsyn queue mechanism to prioritise between sync jobs. Even within a sync job, tasks can be prioritised, enabling transfer of certain shots before others.*

**(Optional) Post**

```python
# End script with feedback to ftrack web UI session that outsource transfer was dispatched, providing job['name']/job['id'] for reference
```

## Configuring vendor asset publish

We now have the pipeline ready for sending material. The final part of the pipeline is the receiving endpoint enabling the vendor to publish produced assets back into the production workflow.

### What is accsyn Publish?

It is a variant of the standard accsyn Desktop App upload mechanism, designed to pre-validate material before uploading and deciding the destination path (without necessarily sharing the folder and granting ACL access). In addition, it supports entering a time report, taking notes, setting status and providing publishing guidelines.

The publish mechanism is driven by two scripted hooks:

- Pre-publish script (**pre-publish-server**). This validation script receives the path to a JSON file containing metadata about the remote user published folders, with directory tree and metadata such as size and date. The pre-publish script should provide per-asset feedback to the user in case there are any inconsistencies, or the upload destination path if validated. It also provides which fields the user should input (time report, notes and status are supported) and additional optional outsource guidelines.
- Publish script (**publish-server**). This ingest script is run after the upload has finished, with a path to the same data generated by the pre-publish script for reference. The publish script is designed to provide additional processing after the files have landed; this is typically proxy (JPEG/MP4/MOV) generation and publish to project management tools [ftrack] including the metadata (notes, time report and status) provided by the remote vendor.

Usually it is implemented as a single script, as their logic is very much the same but separated by a command-line argument like "--pre" or similar.

We recommend designing a pipeline where the remote vendor publishes one folder per task, named as the task. Example:

```bash
scd_0010_0010_cleanup_v001
scd_0010_0020_rotoscoping_v003
..
```

And then let each folder contain all the file sequences, geometry, documents etc. that constitute the final result.

### Post-processing publish (optional)

In the **publish-server** hook, routines for post-processing the published assets can be implemented. Examples:

- Scan files for viruses.
- Encode previews (.mp4/.jpeg/.png)
- Publish to PM (ftrack/Flow)
- Send Slack message

### Implementing the publish scripts

We are not going into great detail on how to design the publish script. For detailed information on how to create the scripts with examples, check out:

[Developer Hub - Publish](/developer/publish/)

The documentation provides links to our GitHub where template publish scripts can be downloaded. The scripts contain clear pointers on where to integrate into a production management tool like ftrack, for validating asset names against tasks and creating a version upload with a reviewable and notes/time report.

## TPN hardened setup

This setup is more involved, as we need these two additional steps:

- Before sending assets, we need to sync them from the protected show storage on the internal site to the DMZ proxy storage.
- When published assets arrive on the DMZ storage, they need to be downloaded (pushed) to the internal site protected show storage.

### Setting up the internal site and server

In this tutorial, we assume the following:

- We call the site [**internal**]
- We have a physical Linux machine or VM available on the protected network
- It has a proxied Internet connection to the accsyn backend ([**https://acmevfx.accsyn.com**]) and access to the Storage server in the DMZ

Setup site:

1. Log on as an administrator to https://accsyn.io/admin/sites
2. Click **New site**.
3. Use name & API code [**Internal**].
4. Create the site.

Install site server:

1. Open the site and click **Install site server**
2. Choose the site you just created.
3. Choose to serve the volume [**Proj**].
4. Conclude the server setup by downloading the Linux accsyn daemon installer, running it and entering the code shown in the web interface.

### Configuring upload of source assets to DMZ server

First we augment the project manager listener/hook to run a cascaded sync of assets all the way from internal storage to the remote vendor:

1. Create a site sync job that uploads the assets from internal protected storage to the DMZ storage, with metadata supplied:

```python

# Calculate the path to source assets from selection in PM (ftrack)
source_files = ["scd/0010/0010/src/plates/scd_0010_0010_src", "scd/0010/0010/cleanup/scd_0010_0010_cleanup_description.txt"]

batch_sync_job_name = f"Outsource - internal upload - {project_name} - {vendor_name} - batch 01 - {datetime.now().strftime('%y%m%d')}"
for path_rel in source_files:
    tasks.append(dict(
        source=f"site=internal:volume=proj/{path_rel}",
        destination="site=hq"
    ))
internal_sync_job = session.create("Transfer", dict(
    name=batch_sync_job_name,
    tasks=tasks,
    mirror_paths=True,
    metadata={
        "internal": {
            "action": "deliver",
            "vendor_name": "AcmeVFX",
            "vendor": "emma@compersinc.com"
        }
    }
))

```

2. Configure a hook **job-done-server** that gets executed when a job finishes, and sends the delivery to the vendor:

```python
#!/usr/bin/python3
hook_data = json.load(open(sys.argv[1], "r"))
metadata = hook_data['metadata'].get('internal', dict())
if metadata.get("action") == "deliver":
    vendor_name = metadata["vendor_name"]
    vendor_ident = metadata["vendor"]
    delivery_name = f"Outsource - deliver - {project_name} - {vendor_name} - batch 01 - {datetime.now().strftime('%y%m%d')}"
    tasks = []
    for task in list(hook_data['tasks'].values()):
        tasks.append(f"volume=proj/{task['source_path']}")
    delivery = session.create("Delivery", dict(
        name=delivery_name,
        tasks=tasks,
        recipients=[vendor_ident]
    ))
```

### Configuring post-processing of publish — sync to internal storage

The other way around: when a publish has landed on the DMZ storage, we need to download it to the internal storage:

1. Append a site sync transfer at the end of the ***publish-server*** hook script:

```python
#!/usr/bin/python3

# (Optional) Post-processing

# Build list of published asset paths, relative to volume root
published_files = ["scd/0010/0010/publish/cleanup/cleanup/scd_0010_0010_cleanup_v001"]

batch_sync_job_name = f"Outsource - internal download publish - {project_name} - {vendor_name} - batch 01 - {datetime.now().strftime('%y%m%d')}"
for path_rel in published_files:
    tasks.append(dict(
        source=f"site=hq:volume=proj/{path_rel}",
        destination="site=internal"
    ))
internal_sync_job = session.create("Transfer", dict(
    name=batch_sync_job_name,
    tasks=tasks,
    mirror_paths=True
))
```

## Conclusions

accsyn provides a versatile API-enabled file I/O platform, easy to integrate into an existing production workflow, with proper user interfaces for both desktop and web. This tutorial only shows a small subset of what accsyn can provide in terms of media production automation.

### Additional resources

[Case study: Filmgate VFX](https://accsyn.com/casestudy-filmgate/)

Learn how Filmgate Films use accsyn within their VFX pipeline for conform, data wrangling, outsourcing and rendering.

[accsyn Python API on GitHub](https://github.com/accsyn/accsyn-python-api)

Download the accsyn Python API source code from GitHub.
