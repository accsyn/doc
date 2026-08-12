# accsyn warning codes

Error codes are listed [here](errors.md). Get help troubleshooting through [this](troubleshooting.md) article.

A complete listing of all accsyn warning codes that can appear as:

- GUI (Desktop app or web app); A notification banner at the top of the GUI and within the job log.
- CLI; Printed together with the result.
- Python API; Printed and also made available through the call.

## Global warning codes

| Code/ID | Description | Suggestion(s) for action |
|---|---|---|
| W#G001 | .. days left of Accsyn trial license,.. | The trial is close to ending, contact sales@accsyn.com to purchase your permanent licence. |

## Job warning codes

| Code/ID | Description | Suggestion(s) for action |
|---|---|---|
| W#J008 | An network communication error occurred during transfer. .. | This is probably due to the remote end not terminating the connection properly and can safely be ignored under most circumstances. |
| W#J009 | An internal error occurred when checking local mounts: .. | accsyn could not check locally mounted filesystems, this is usually due to a filesystem error or a network issue. |
| W#J050 | No clients are online. | Neither at the server nor at the remote computer is an accsyn client booted up and running. |
| W#J051 | Could not auto retry failed job. | Non critical internal error, the job should recover automatically. |
| W#J052 | Job cannot be dispatched: .. | Internal state prevents the transfer from starting, could be a disabled site or share. |
| W#J053 | Queued, will run when job(s) above in queue are finished | The server or remote accsyn client is already occupied with a transfer of another job above in the queue/with higher priority. |
| W#J054 | Server is out of free channels. | The server will need to be configured with more channels (forwarded ports) to be able to handle additional file transfers. |
| W#J055 | .. is unavailable. | Boot up the server and/or remote client/desktop app to get the transfer going. |
| W#J056 | Could not bind channel allocate tmp server to port: .. | Consider reconfiguring server ports - other services are listening. |
| W#J057 | Access denied, an authorized connection were made from ... | Ongoing break-in attempts hammering the ports on the server side? |
| W#J058 | Cannot ... job, server for default share is is down. | Boot up the server to have the job initialised. |
| W#J059 | (Deprecated as of v2.4) Waiting for job user .. to join. | Have the user activate their account and join accsyn. |
| W#J060 | File disappeared during transfer: .. | Files are in motion during transfer, allowed by accsyn by default (subject to being configurable in future versions). |
| W#J061 | Waiting for server.. to come online for hook execution | Make sure the accsyn server app is running properly. |
| W#J062 | Failed to delete temporary file: .. | Another process or the operating system is preventing accsyn from cleaning up temp files, check the filesystem. |
| W#J063 | Could not release lock for: ... | accsyn cannot release the lock it had on the file during writing, this is usually due to file system limitations/errors. |
| W#J064 | Failed to set modification time for: ... | accsyn could not store the file modification time, needed to be able to establish the sync protocol and evaluate what needs to be sent. Check the filesystem. |
| W#J065 | Failed to delete existing file: ... | accsyn could not delete the destination file prior to renaming the temp file, usually this means that the destination file is locked/accessed by another process. accsyn will attempt to move the file away to a subfolder named 'ASC_LOCKED_DESTINATION_FILES' and retry. If this fails, accsyn will move the transferred temp file to the 'ASC_RENAME_FAILED' directory. |
| W#J066 | Job on hold - free accsyn trial license has expired | The job will not run unless you have an active licence, demo or permanent. Contact sales@accsyn.com to resolve this issue. |
| W#J067 | .. status is ... | The job cannot be dispatched due to a parent queue or its own status. |
| W#J068 | Domain .. is ... | The job cannot be dispatched as the entire accsyn domain/organisation has a specific status. |
| W#J069 | File sequence member is missing: ... | An expected member of a file sequence cannot be found. |
| W#J070 | All client\|node(s) are currently occupied. | There are no clients or nodes available to run the job. |
| W#J071 | Cannot be dispatched, ... jobs are currently disabled... | Downloads, uploads or compute jobs have been disabled within the entire accsyn workspace or for a role / user. |
