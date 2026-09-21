# accsyn Internal Settings

This page lists all internal settings available for accsyn entities such as workspace, share (volumes, share), queues, jobs (transfers, deliveries).

## Introduction

A setting is a key=value pair defining the behaviour of an accsyn entity.

  

An example of a setting is "transfer\_speedlimit" that defines the maximum bandwidth a transfer can consume.

  

### How to modify settings:

- Settings can be modified from the accsyn webapp, log in to access: <https://accsyn.io>
- Job settings can be modified from the [accsyn Desktop app](desktop-app.md).
- Settings can be read, created and modified with the [accsyn Python API](developer/python-api.md).

## Global (Workspace) settings

| Setting | Default value | Other values | Description |
|---|---|---|---|
| security_enable_mfa | true | false | Require multi-factor authentication for all users on the workspace. Users can enroll MFA with the default accsyn-email-password (Auth0) or will have to be enrolled with their external MFA provider (Google). If not enrolled, accsyn will issue an email to the user with a One-Time-Password (OTP) to be used for authentication. |
| security_app_client_auth_enable | true | false | Enable app clients to authenticate using their secret client key. |
| security_conf | `{"mfa_method":"email", "mfa_methods":{"email":{"default":true}}, "mfa_all":false, "mfa_admin":false, "mfa_employee":false, "mfa_standard":false}` | | Multi-factor authentication configuration: **mfa_method** — the method to use for accsyn multi-factor authentication, when the token provided by auth provider is not MFA authenticated; **mfa_methods** — the methods to use for accsyn multi-factor authentication; **mfa_all** — whether to require multi-factor authentication for all users; **mfa_admin** — whether to require multi-factor authentication for admin users; **mfa_employee** — whether to require multi-factor authentication for employee users; **mfa_standard** — whether to require multi-factor authentication for standard users. |
| share_create_directories | true | false | Always create directories on volume when creating a Shared folder or Home share. |
| share_auto_create_homes | true | false | Automatically create a Home share for new users when they are created/invited. |
| share_homes_directory | true | false | The directory where Home shares are created at the default volume. Must be a relative path. |
| share_check | true | false | Check volume status — reflect server status on volume. |
| share_measure | true | false | Measure volume free space, and report an issue if below a certain threshold. |
| share_cache_enable | true | false | Enable volume cache — store directory structure in accsyn cache for fast retrieval / offline listings. When listing files on a volume with the desktop app, the cached results will first be retrieved followed by the actual listing by the server that also updates the cache afterwards. |
| share_cache_background_scan | true | false | Enable background updating of the cache during night time. |
| share_conf | `{"user_dropoff_date_directory_enable":true, "user_dropoff_date_directory_format":"%Y%m%d", "home_template":[{"path":"/","read":true,"write":true}], "warning_free_percentage":0.05, "error_free_gb":0, "cache_scan_depth":2, "cache_refresh_h":24}` | | Advanced share settings: **user_dropoff_date_directory_enable** — enable creation of a destination date directory, when uploading to a home share when no path is not provided; **user_dropoff_date_directory_format** — the format of the user dropoff date directories; **home_template** — the directory template to use for home shares; **warning_free_percentage** — the percentage of free space at which a warning will be issued; **error_free_gb** — the amount of free space at which an error will be issued; **cache_scan_depth** — the folder depth of the background cache scan; **cache_refresh_h** — the number of hours between cache refreshes. |
| queue_interrupt_policy | order | priority \| never | The policy to use for interrupting transfer jobs below in the queue: **order** (default) — interrupt jobs if they have lower priority than the current job and are below in the queue; **priority** — interrupt jobs that are of lower priority; **never** — never attempt to interrupt jobs. |
| queue_interrupt_policy_compute | priority | order \| never | The policy to use for interrupting compute jobs below in the queue: **order** — interrupt jobs if they have lower priority than the current job and are below in the queue; **priority** (default) — interrupt jobs that are of lower priority; **never** — never attempt to interrupt jobs. |
| job_max_retries | 3 | | Maximum number of times accsyn should retry a transfer until it is considered as failed. |
| job_autoretry_delay_s | 15 | | How long accsyn should wait, upon a failed transfer, before retrying. |
| job_done_actions | | delete_excluded | Define what actions to perform when a job is done: **delete_excluded** — delete excluded files/directories at receiving end for excluded tasks. |
| task_bucketsize | 0 (transfers) \| 1 (compute jobs) | | The amount of tasks to collect and include in each transfer, default is 0 which means transfer/compute all tasks. Set this to 1 to have each task processed separately, suitable for large folders that can cause accsyn to run out of memory during transfer (or long running compute/render tasks). |
| upload_enable | true | false | Enable file uploads to the workspace globally. |
| download_enable | true | false | Enable file downloads from the workspace globally. |
| job_on_missing | fail | ignore | What to do when a file is missing at the sending party of a transfer job: **fail** (default) — fail the job, after all other tasks has been exhausted; **ignore** — ignore the missing file. |
| transfer_speedlimit | | Float greater than zero | The transfer speed limit to apply globally on all transfers, in MB/s (Megabytes per second). |
| transfer_encryption | aes128 | aes256 \| none | The encryption to apply during file transfers, protecting your data from insight during Internet transport. Note that encryption will be **turned off** by default if override IPs are involved (client config) — transfers are assumed going over local LAN/encrypted VPN. |
| transfer_mode | copy | onewaysync | The algorithm accsyn should use during file transfers: **Copy** (copy) — copy files and folders from source to destination that differ based on the comparison rules defined below (`transfer_comparison`). Corresponds to *NIX `rsync -rtv <source> <destination>`; **One-way sync** (onewaysync) — copy files and folders from source to destination that differ based on the comparison rules defined below (`transfer_comparison`), deleting files on destination that do not exist on source before transfer starts. Corresponds to *NIX `rsync -rtv --delete(-before) <source> <destination>`. |
| transfer_comparison | size+modified | size \| modified | The accsyn file transfer protocol behaves by default as [RSYNC](https://en.wikipedia.org/wiki/Rsync) — only transferring files that are missing, have different size or differ in modification dates. |
| transfer_resume | enable | disable | Single file resume mode, applies to files larger than `transfer_resume_limit`: **enable** — resume partially transferred files; **disable** — never resume files (pre v1.4-3 behaviour). |
| transfer_resume_limit | 50 | -1 (disable) or integer greater than zero | File size, in megabytes (MB), at which single file resume (`transfer_resume`) should start to apply. Files below this limit in size will never be resumed if interrupted mid-transfer. Giving a value of -1 means that no limits should apply — limits disabled. |
| transfer_ignore_existing | | file \| directory \| file+directory | Tell accsyn to ignore files or/and directories that already exist on the receiver end. |
| transfer_attributes | | owner (+) group (+) permissions | Have accsyn preserve ownership and/or permissions of files during transfer. This only works when the two endpoints are running on a POSIX (Linux, Mac) based operating system; it will have no effect if any party is running Windows. |
| transfer_concurrent | 1 | 1..10 | Define how many concurrent transfers the server will allow for each remote client. A high value here could put high load on your network infrastructure and is only a benefit if you alternate between many quick simultaneous jobs, for example continuously adding tasks to jobs using APIs. Can be overridden at clients. |
| transfer_log | info,comparison,files | info \| warning (,) files (,) comparison (,) ownership (,) group | What accsyn should log during transfer. The transfer log is stored per-task and can be retrieved by double-clicking a task in the accsyn desktop app: **info** — show informational messages; **warning** — only show warnings; **files** — show name of files transferred/directories created; **comparison** — show additional information regarding file comparison decisions; **ownership** — show additional ownership modifications; **group** — show additional group modifications; **permissions** — show additional permission modifications. |
| transfer_include | info | | Files must match these names in order to be included in transfer, entries separated by commas (,), case insensitive. Examples: **filename** — include all files and directories named "filename"; **\*suffix** — include all files and directories ending with text "suffix"; **prefix\*** — include all files and directories beginning with text "prefix"; **re('[a-d]')** — regular expression — include only files and directories that consist of the letters a to d (case sensitive); **re('output','I')** — regular expression — include only files and directories that are named "output" (case insensitive). *Notes: Commas (,) need to be escaped (\,). Entries are merged with volume, queue and job includes upon transfer.* |
| transfer_exclude | | | Name of files that match any of these filters are excluded from transfer, entries separated by commas (,), case insensitive. Examples: **filename** — exclude all files and directories named "filename"; **\*suffix** — exclude all files and directories ending with text "suffix"; **prefix\*** — exclude all files and directories beginning with text "prefix"; **re('[a-d]')** — regular expression — exclude all files and directories that consist of the letters a to d (case sensitive); **re('tmp','I')** — regular expression — exclude all files and directories that are named "tmp" (case insensitive); **path/to/file** — exclude file or directory "file" in sub directory "path/to". Path elements may contain wildcards. *Note: Commas (,) need to be escaped (\,). Entries are merged with volume, queue and job excludes upon transfer.* |
| transfer_reserved_space | 100000000 | -1 (disable) or integer greater than zero | The amount of space, in bytes, to reserve for the transfer process. This is used to prevent the transfer process from running out of space. |
| transfer_conf | `{"io_buffer_size":"4194304", "sockets":10, "socket_buffer_size":"1048576", "disk_readers":1, "disk_writers":1, "nolock":true, "notmp":false, "umask":""}` | | Advanced transfer tuning parameters in JSON format: **io_buffer_size** — size of disk I/O buffers used during transfer; **sockets** — number of TCP sockets to use; **socket_buffer_size** — size of network buffers to use during transfer; **disk_readers** — number of disk reader threads to spawn during transfer; **disk_writers** — number of writer threads to spawn during transfer; **notmp** — do not write to TMP files and rename afterwards — write directly to destination file; **nolock** — do not attempt to lock file before writing. Tick this setting if your file systems does not support locking; it is recommended to configure this for the specific share(s) and not here; **umask** — (Mac/Linux/Unix only) the umask to set for transfer process on launch. Leave empty and umask will not be touched. |
| compute_enable | false | true | Enable compute — allow users to submit and run accsyn compute jobs. |
| compute_avoid | enable-clear-on-resume | | How to act when a compute task fails: **enable-clear-on-resume** (default) — avoid the compute node but clear when job is retried/resumed; **enable-permanent** — avoid the compute node permanently; **disable** — do not avoid the compute node. |
| job_compress_tmp_limit | 100000000000 (100GB) | Integer greater than zero | The largest size a folder/multi-file delivery can have and be allowed to be compressed; anything above this size must be downloaded in app. |
| mail_conf | `{"enable":true, "default":{"to":["admin"]}, "issue":{"enable":true,"to":["admin"]}, "client-registered":{"enable":true,"to":["admin"]}, "submit":{"enable":true,"to":["admin","user"]}, "fail":{"enable":true,"to":["admin","user"]}, "done":{"enable":true,"to":["admin","user"]}}` | | Email configuration in JSON format. |
| hook_conf | `{"enable":true,"hooks":{}}` | | Hook configuration in JSON format. |
| publish_enable | false | true | Enable publish workflow — allow users to publish their files through accsyn app. Requires pre-publish-server & publish-server hooks to be configured. |
| ui_job_create_show_share_path | false | true | Show the share's relative volume path in UIs to standard users. |
| job_compress_tmp_directory | accsyn/tmp/compressed_jobs | | Directory used for temporary compressed job packages. |

## User settings

| Setting | Default value | Other values | Description |
|---|---|---|---|
| compute_enable | false | true | Allow standard user to submit and run accsyn compute jobs. By default only employees with access to volume (and admins) can submit compute jobs. |

## Client settings

Server, Desktop app, User server

| Setting | Default value | Other values | Description |
|---|---|---|---|
| client_ports | 45190-45210 | | The ports used by the client to communicate with the accsyn server during file transfers, ASC or https (web transfers) protocol. |
| client_wan_ip | | ip address | The primary WAN IP address of the client. This is used to identify the client to the accsyn server; by default this is auto-detected by the accsyn backend. |
| client_proxy_server | | | The proxy server to use for the client. This is used to proxy the client's traffic through a proxy server. |
| client_wan_ips | | ip address | The secondary WAN IP addresses associated with the client, see `client_wan_ip` above. |
| client_compute_lanes | 1 | Positive integer greater than zero | The number of compute lanes to use for the client. This is used to limit the number of compute jobs that can be run concurrently by the client. |
| client_channel_whitelisted | | | The channels (ports) to always whitelist for the client, regardless of any failed attempts to connect to the server. |
| client_conf | `{...}` | JSON object | Advanced client configuration in JSON format. |
| transfer_concurrent | | | See workspace setting. |
| transfer_speedlimit | | | See workspace setting. |
| client_offline_grace_m | | | See workspace setting. |

## Share settings

Volume, shared folder, home share, collection

| Setting | Default value | Other values | Description |
|---|---|---|---|
| transfer_encryption | | | See workspace setting. |
| transfer_mode | | | See workspace setting. |
| transfer_comparison | | | See workspace setting. |
| transfer_resume | | | See workspace setting. |
| transfer_resume_limit | | | See workspace setting. |
| transfer_attributes | | | See workspace setting. |
| transfer_log | | | See workspace setting. |
| transfer_speedlimit | | | See workspace setting. |
| transfer_ignore_existing | | | See workspace setting. |
| transfer_include | | | See workspace setting. |
| transfer_exclude | | | See workspace setting. |
| transfer_reserved_space | | | See workspace setting. |
| transfer_conf | | | See workspace setting. |
| job_max_retries | | | See workspace setting. |
| job_autoretry_delay_s | | | See workspace setting. |
| email_conf | | | See workspace setting. |

### Inheritance

- Volumes inherit workspace/global settings by default and can have settings overrides (see below).
- Shared folders and Home folders inherit settings from their volume by default and can have settings overrides (see below).

## Job settings

Queue, Transfer, Delivery, Request, Stream, Compute

| Setting | Default value | Other values | Description |
|---|---|---|---|
| job_max_retries | | | See workspace setting. |
| job_autoretry_delay_s | | | See workspace setting. |
| job_done_actions | | | See workspace setting. |
| job_on_missing | | | See workspace setting. |
| transfer_encryption | | | See workspace setting. |
| transfer_speedlimit | | | See workspace setting. |
| transfer_mode | | | See workspace setting. |
| transfer_comparison | | | See workspace setting. |
| transfer_resume | | | See workspace setting. |
| transfer_resume_limit | | | See workspace setting. |
| transfer_attributes | | | See workspace setting. |
| transfer_concurrent | | | See workspace setting. |
| transfer_log | | | See workspace setting. |
| transfer_ignore_existing | | | See workspace setting. |
| transfer_include | | | See workspace setting. |
| transfer_exclude | | | See workspace setting. |
| transfer_conf | | | See workspace setting. |
| compute_avoid | | | See workspace setting. |
| task_bucketsize | | | See workspace setting. |
| hook_conf | | | See workspace setting. |
| email_conf | | | See workspace setting. |

### Inheritance

- Queues inherit workspace/global settings by default and can have settings overrides (see below).
- Jobs inherit settings from their queue and can have settings overrides (see below).
- Tasks/processes inherit both settings from their job and the involved source and destination shares (volume, shared folder,..). Settings cannot be overridden for process entities.
