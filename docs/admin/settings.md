# Workspace Settings

This guide shows how to work with the global workspace settings.

  

Prerequisites:

- Logged on as an administrator to <https://accsyn.io/admin/settings>.

## General

### Name

Change the name of the workspace.

*Note: Pages need to be reloaded and the desktop app needs to be restarted for changes to take effect in UIs.*

  

Code

The unique API identifier of workspace, as generated from the initial name chosen. This is also the same as the REST domain / hostname, e.g. https://<workspace code>.[accsyn.com/api/v3](http://accsyn.com/api/v3)

*Note: Changing the code is an operation that only can be performed by the accsyn Support team.*

  

### Logotype

The images to use for branding, in light and dark mode variants.  They are chosen from resources, and need to be uploaded here in advance: <https://accsyn.io/admin/resources>

*Note: logotype images will be scaled down to fit 140x40px which are the default accsyn logotype dimensions, make sure your imagery looks decent in this format.*

## Security

### Enforce MFA

Require multi-factor authentication before the workspace can be accessed. When applied, different scenarios play out at login depending on the auth provider:

- accsyn-email-password; accsyn will perform an MFA prompt sequence using method below before workspace can be accessed.
- accsyn-email-password - MFA enrolled; The user will be requested to enter the code displayed in their authenticator app at login.
- External identity provider (Google); User should setup (enroll) MFA with their provider before they access the workspace, if not enrolled yet accsyn will perform an MFA prompt sequence using method below before they can access the workspace.
- External identity provider (Google) - MFA enrolled; User is already MFA authenticated when entering the workspace, no further actions will be required.

  

accsyn will check if the user is MFA authenticated from login. If not, the method described below will be used to authenticate - by default a code sent to the user with an email message.

  

Method

The method to use to authenticate, if not already MFA authenticated at login.

The default method is email - a six (6) digit code is sent by email to the user and needs to be entered in the browser or app before login can be concluded.

Enforce for all roles

Require MFA for all users.

Enforce for administrators

Require MFA for users having the elevated administrator base role.

Enforce for employees

Require MFA for users having the elevated employee/operator base role.

Enforce for standard users

Require MFA for standard non-elevated users.

## Storage

### Create directories

Always create directories on volume when creating a Shared folder or Home share.

  

### Auto create homes

Automatically create a Home share for new users when they are created/invited.

  

### Homes directory

The directory where Home shares are created at the default volume. Must be a relative path.

  

### Enable cache

Enable volume cache - store directory structure in accsyn cache for fast retrieval / offline listings.

When listing files on a volume with the desktop app, the cached results will first be retrieved followed by the actual listing by the server that also updates the cache afterwards.

  

### Advanced

Advanced storage settings, see [accsyn Internal settings](../settings.md) for details.

## Job

### On missing file/frame

What to do when a file is missing at the sending party of a transfer job.

  

### Queue interrupt policy

The policy to use for interrupting transfer jobs below in the queue, by default accsyn interrupts active jobs with lower priority or below in the queue.

  

*Note: The transfer settings below can be overridden on volume, queue and job level.*

  

### Max retries

Maximum number of times accsyn should retry a transfer until it is considered as failed.

  

### Job retry delay

How long accsyn should wait, upon a failed transfer, before retrying.

## File Transfer

### Enable uploads

Enable file uploads to the workspace globally.

  

### Enable downloads

Enable file downloads from the workspace globally.

  

*Note: The transfer settings below can be overridden on volume, queue and job level.*

  

### Speed limit

The transfer speed limit to apply globally on all transfers, in MB/s (Megabytes per second).

  

### Transfer encryption

The encryption to apply during file transfers, protecting your data from insight during Internet transport. Note that encryption will be turned off by default if override IPs are involved (client config) - transfers are assumed to go over local LAN/encrypted VPN.

  

### Transfer mode

The algorithm accsyn should use during file transfers - copy or sync (delete files at the remote end not existing at sender side).

  

### File comparison rule

The methods accsyn should use to determine if a file is out of sync and needs to be transferred.

  

### File resume size limit

File size, in megabytes (MB), at which single file resume ('transfer\_resume') should start to apply. Files below this limit in size will never be resumed if interrupted mid-transfer.

Giving a value of -1 means that no limits should apply - limits disabled.

  

### Transfer attributes

Have accsyn preserve ownership and/or permissions of files during transfer. This only works when the two endpoints are running on a POSIX(Linux,Mac) based operating system, it will have no effect if any party is running Windows.

  

### Concurrent transfers

Define how many concurrent transfers server will allow for each remote client. A high value here could put high load on your network infrastructure and is only a benefit if you alternate between many quick simultaneous jobs, for example continuously adding tasks to jobs using APIs. Can be overridden at clients.

  

### Logging

What accsyn should log during transfer. The transfer log is stored per-task and can be retrieved by double-clicking a task in the accsyn desktop app.

  

### Advanced

Advanced transfer settings, see [accsyn Internal settings](../settings.md) for details.

## Email

*Note: The email settings can be overridden on volume and queue level.*

  

accsyn dispatches email notifications when different events occur. This settings page is divided in two parts:

- Overall global settings.
- Per-event settings.

  

### Global email settings

Enable

Enable or disable email notifications globally.

  

Default recipients

Who to include by default when accsyn sends emails in general, not related to an event below. These are overridden by specific event recipients (see below).

- Built-in; The default recipients as built into accsyn (role or explicit user)
- Additional; Add more recipients here as needed, by clicking the ADD button. Roles, users and explicit external email recipients can be chosen.

  

Global exclude:

What roles, users and email addresses to exclude globally. This applies to all email sent, including event specific ones.

  

Reply-to

The reply-to address to set for all emails.

  

### Issues

Define the recipients that will get email about issues that are detected within the accsyn platform.

  

### Client register

Define the recipients that will get email when a new client (desktop app, user server or general server) is registered somewhere.

  

### Job submit

Define the recipients that will get email when a job is submitted.

  

### Job failure

Define the recipients that will get email when a job fails.

  

### User

Define the recipients that will get email when a user is invited/created.

  

### Share

Currently not used.

## Hooks

See [Hooks documentation](../developer/hooks.md).

## Compute

In general, refer to [Render farm documentation](../developer/farm.md).

  

### Enable compute

Enable or disable the compute (render) feature for the workspace.

  

### Avoid client policy for failed executions

 How to act when a compute task fails: 

- enable-clear-on-resume (default) - avoid the compute node but clear when job is retried/resumed
- enable-permanent - avoid the compute node permanently
- disable - do not avoid the compute node

  

### Queue interrupt policy (compute)

See Queue interrupt policy above.

  

### Pools

Define server pools, that can be targeted in different ways during job submission.

## Publish

See [Publish documentation](../developer/publish.md).

## Metadata

### Metadata

Define global workspace metadata, these are passed on to hooks and compute jobs. Metadata can be defined on most accsyn entities such as shares, queues and so on.

- Internal; this metadata will not be exposed to hooks that execute client side, unless it is an elevated (admin/employee) user client.
- External; this metadata will be exposed to hooks that execute client (remote user) side also for standard users.

Related articles

[Desktop App](../desktop-app.md)

[accsyn Internal Settings](../settings.md)
