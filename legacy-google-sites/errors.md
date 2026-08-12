# accsyn error codes

Warning codes are listed [here](warnings.md). Get help troubleshooting through [this](troubleshooting.md) article.

A complete listing of all accsyn error codes that can appear as:

- GUI (Desktop app or web app); A notification banner at the top of the GUI and within the job log.
- CLI; Printed together with the result.
- Python API; Printed and also made available through the call.

## Global error codes

| Code/ID | Description | Suggestion(s) for action |
|---|---|---|
| E#G001 | Cloud database down. | Contact support@accsyn.com. |
| E#G002 | Your Accsyn free trial has EXPIRED, .. | Contact sales@accsyn.com to purchase your permanent licence and get transfers going. |

## Job error codes

| Code/ID | Description | Suggestion(s) for action |
|---|---|---|
| E#J001 | File or directory not found at server\|client: ... | Try to bring the file/directory back if it is intended to be there. Otherwise exclude the tasks (files) in the GUI and retry the job for the rest of the files in the package to complete. |
| E#J002 | Could not bind accsyn server to TCP port: .. | Another application is listening to a port that the accsyn server utilises, or a previous accsyn zombie file transfer process is still running. Shut down the application/kill zombie processes/restart the server. |
| E#J003 | Network communication\|Socket timeout error when reading control channel data from server: ... | Communication between file parties seems to have been interrupted, make sure no firewall on the route is blocking/interfering with the traffic and no antivirus software is intercepting the traffic. |
| E#J004 | Could not connect to accsyn server ..: ... | Communicating with the serving part seems to fail, make sure ports are forwarded properly to the server machine within the premises and no additional firewall on the route is blocking the traffic. |
| E#J005 | Could not read file\|An internal error occurred when reading '..' from disk at server\|client: ... | Make sure file(s) are not being accessed/written by another application while accsyn is reading from them. |
| E#J006 | Job failed due to failing .. hook, need to be manually retried. | Debug hooks, make sure they function and do not time out (>5 min execution time). |
| E#J007 | Failed, check logs for clues. .. | Not an identifiable error, check the job log for clues. |
| E#J008 | An network communication error occurred during transfer. .. | Make sure the network/Internet connection is stable and not disconnected during transfer. A good starting point is to have a ping running during transfer in combination with doing traceroutes to find out where the route is cut off. |
| E#J009 | Could not create temp execution folder at server\|client: ... | Make sure accsyn has write permission in temp and specifically the '.accsyn' folder where intermediate files are stored. |
| E#J010 | An internal error occurred when initialising tasks/files at server\|client: ... | A crash occurred while accsyn was building absolute paths for files and directories, please contact accsyn support so we can investigate the issue and provide better feedback in the future. |
| E#J013 | An error occurred when listing ... | The file transfer process is having problems listing and accessing files on disk - check file permissions, file locks and such. |
| E#J014 | An error occurred when reading object during control channel communication: ... | An error occurred when reading data arriving over the network, make sure no firewall on the route is blocking/interfering with the traffic and no antivirus software is intercepting the traffic. |
| E#J020 | An internal error occured during accsyn transfer, we are sorry for this and hope take the time to send this log to support@accsyn.com. | accsyn crashed without being able to give proper feedback about the error, contact accsyn support so we can investigate the issue and provide better feedback in the future. |
| E#J050 | Job is corrupt and cannot be dispatched. | This is due to an internal error/bug in accsyn, please contact accsyn support. |
| E#J051 | User '..' not enabled. | Enable the user in order to get the job running again. |
| E#J052 | An internal error occurred when spawning transfer at .. | Contact accsyn support. |
| E#J053 | Could not create parent directory ..! | Make sure accsyn has write permission on the share. |
| E#J054 | Could not read .. , file size: .. != total bytes read: .. | Files might be changing while accsyn is reading, or accsyn is having trouble measuring the size of files on the volume. |
| E#J055 | ..:Is a directory | An attempt is being made to overwrite a directory with a file, and accsyn could not attempt to write the file beneath the directory due to an existing file. |
| E#J056 | Cannot create zero bytes stub: .. | A file could not be created for some reason, make sure the media is writable/has free space and you have sufficient permissions. Could also be that an attempt is being made to overwrite a file with a directory. |
| E#J057 | Could not write .. | A file could not be written to disk for some reason. Most likely due to insufficient free disk space, free up some space and retry the transfer. |
| E#J058 | : Not overwriting existing file with a directory. | The file exists at the receiving end, and would have been overwritten by a directory with the same name. Default accsyn behaviour is to refuse this. |
| E#J059 | Failed to rename temporary file: ... | accsyn could not rename the transferred temporary file to the final destination filename, usually this happens if the destination file is locked/accessed by another process/software. |
| E#J060 | Unable to create directory: ... | Make sure the directory contains filenames that are supported on the destination platform and accsyn has write access. |
| E#J061 | (Size calculation) .. | The size of the source file(s) could not be calculated due to an error, usually one or more files have disappeared or cannot be read by the server due to permissions or underlying disk issues. |
| E#J062 | Aborting stuck transfer - no data transfered since: .. | accsyn has encountered a deadlock and cannot transport data anymore, typically this is due to a locked file during read from/write to disk or a network issue. |
| E#J063 | accsyn has run out of memory! Details: .. | There is not enough memory for accsyn to operate, usually this is due to A) running on a machine with a tiny RAM footprint B) a huge number of files within a deep file structure is about to be transferred. Try to send the package in chunks with 1 task per transfer, also consult the admin manual for information on how to increase transfer process memory limits. |
| E#J064 | Could not spawn transfer .. | accsyn could not initiate the transfer, most likely this is due to not having a volume path configured for a specific operating system. |
| E#J065 | User '..'(..) dissappeared. | The job/queue user has been removed from accsyn and ownership has not been migrated. If it is a queue, you can take ownership at queue edit. |
| E#J066 | Not enough space ... | Reserved space (`transfer_reserved_space`) is configured globally or at the volume and there is not enough free space on the destination storage to write file(s). |
| E#J069 | No files found to send from ... | No files could be evaluated for send, due to empty folders and/or files removed by include+exclude filters (check `transfer_include` & `transfer_exclude` settings). |
| E#J070 | Job on hold ... | The trial licence has expired, preventing any job from being dispatched. Subscribe to a permanent licence to solve the issue. |
| E#J071 | Maximum number of concurrent transfers reached ... | The 'Lite' accsyn licence only allows for two (2) concurrent file transfers. Upgrade to a Standard or Premium licence to resolve the issue. |
