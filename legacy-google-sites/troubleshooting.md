# Troubleshooting accsyn

This section approaches issues that appear when accsyn attempts to transfer a file package or run a compute/render job. 

We try to cover as many aspects as possible but there might still be errors that are not directly recognisable by accsyn and have to be identified by accsyn service personnel. 

Included in your BYOS subscription contract is office hours debugging of failing transfers and updates to software to remedy these issues when possible.

  

IMPORTANT NOTE: We cannot make accsyn solve issues that are out of our control, this includes misconfiguration of the software, errors in your software/operating system/drivers or hardware errors such as failing disks/network/controllers.

Contents:

[accsyn setup](troubleshooting.md)

[Directory listing crashes during BYOS setup](troubleshooting.md)

[Transfers cannot be submitted](troubleshooting.md)

[Job warning and error codes](troubleshooting.md)

[Transfer does not start](troubleshooting.md)

[The remote client is offline](troubleshooting.md)

[The remote client is disabled](troubleshooting.md)

[The accsyn trial period has ended](troubleshooting.md)

[The server is offline](troubleshooting.md)

[The user is disabled](troubleshooting.md)

[The share is offline](troubleshooting.md)

[The share is disabled](troubleshooting.md)

[The involved site is disabled](troubleshooting.md)

[A free channel/port cannot be allocated](troubleshooting.md)

[Transfer failures](troubleshooting.md)

[Missing source file(s)](troubleshooting.md)

[Network connection lost](troubleshooting.md)

[Files cannot be written](troubleshooting.md)

[Firewalls are blocking connections or scramble the connection during transfer](troubleshooting.md)

[Error and warning codes](troubleshooting.md)

[Having further issues?](troubleshooting.md)

## accsyn setup

Issues related to accsyn workspace installation only.

### Directory listing crashes during BYOS setup

Happens when browsing the root share:

- Windows; The service process (AccsynDaemon.exe) might be blocked by Windows Defender or other antivirus software running on the server. Solution: configure an exception for accsyn.
- Linux: The daemon process (/usr/local/accsyn/accsyndaemon) is blocked by SELinux or other security enforcing mechanism. Solution:  configure an exception for accsyn and the storage path involved if necessary.
- Mac OS X;  The launchctl process (/usr/local/accsyn/accsyn) is blocked by GateKeeper(sandboxd), Antivirus software or other security enforcing mechanism. Solution:  for GateKeeper(sandboxd, Catalina+), add an exception: Open System Preferences>Security & Privacy, go to Privacy tab>Full Disk Access and add the "/bin/sh" binary to the list. Make sure the checkbox is checked.

## Transfers cannot be submitted

The most common cause is a user lacking permission to download or upload to the specific location and usually happens when submitting a job through CLI or API:

- Users; Will be presented with sparse information regarding what is causing the error, reach out to your contact at the workspace and have them troubleshoot. As an employee/admin they can then view the job audit logs (ADMIN>LOGS>Job) to track the submit event and find full information about why the job could not be submitted.

- Employees/Admins; Will be told the cause of the error making it possible for you to either configure accsyn to allow transfer or adjust your transfer job parameters. Usually it is a misspelling when submitting jobs through CLI/API or a share has been removed whilst you were submitting the job.

## Job warning and error codes

From here on, accsyn attempts to give feedback on why a transfer cannot be finalised.

The software can detect most of the common errors that occur, they are listed as either job warning codes or job error codes and each has a number identification assigned.  They are included in log messages as a suffix on the form W#Jnnn for warnings and E#Jnnn for errors, and are described in detail in separate support articles:

- [Job warning codes](warnings.md).

- [Job error codes](errors.md). 

If no log messages are presented or have no code attached, accsyn service personnel attempt to teach accsyn about the issue and include it in the next upgrade cycle. Please help us map these issues for us to make accsyn a better software experience - making it easy for all users out there to find and remedy transfer issues!

## Transfer does not start

This can occur due to many reasons, here follows a listing of issues sorted depending on how commonly they occur:

  

### The remote client is offline

Description: This is the most common cause of sitting duck transfers - accsyn relies on both parties in the transfer to be online and enabled in order for a transfer to launch. This error is usually displayed when hovering the job or when viewing the job and looks like this: “No clients are online. (W#J050)”. To find out the last time the client was online, go to ADMIN>CLIENTS and record the “last checkin” entry for the specific client. 

Solution: Make sure the remote client transfer party is online, functioning and has network (Internet or LAN/VPN) connectivity as required depending on your setup.

  

### The remote client is disabled

Description: You can disable a certain client, and the user can disable its client for a reason.  Again accsyn relies on both parties in the transfer to be online and enabled in order for a transfer to launch, this issue is usually displayed when hovering the job or when viewing the job and looks like this: “No clients are online. (W#J050)”.

Solution: Make sure the user enables their client to have the transfer commence.

  

### The accsyn trial period has ended

Description:

Note: Affects trial licensed accsyn workspaces only.

When the accsyn trial ends, no transfer jobs will be executed until the trial is extended or a valid permanent subscription licence is made active. The message “Accsyn demo license as expired. (W#J066)” should be displayed on the job. This is a global issue and should be displayed as a top bar notification in your UI. 

Solution: For information on how to obtain an accsyn licence, please head over to [Pricing](https://accsyn.com/pricing).

  

### The server is offline

Description: At the same time, the server party (or server parties if it is a site-site transfer) has to be online and enabled for transfers to happen. An offline server is usually displayed as a global issue and should be clearly displayed as a top bar notification in your UI.

Solution: Go to ADMIN>SERVERS to locate the offline or disabled server and remedy the issue, usually it involves enabling the server or restarting it and making sure it has network connectivity (Internet or LAN/VPN depending on your setup).

  

### The user is disabled

Description: No transfers will happen if the user is disabled, this includes the admin user that installed the server software. 

Solution: Check that the remote user is enabled and the user of the server (or servers if a site-site transfer) is enabled.

  

### The share is offline

Code: W#J052

Description: If an involved root share is offline, the transfer will not start. This includes an explicit standard or user share, or if the parent root share is offline.

A root share turns offline if the server cannot find its folder and usually is caused by a dismounted local or network filesystem.

Solution: Check your server and make sure the storage is available at the configured path known by accsyn. If changed/relocated, edit the share (ADMIN>SHARES) and browse the new path. 

  

### The share is disabled

Code: W#J052

Description: If an involved share is disabled, the transfer will not start. This applies both to the standard or user share involved, or if the parent root share is disabled (recall that shares are descendants of root shares and depend on their availability).

Solution: Enable the share and/or root share to have the transfer happen.

  

### The involved site is disabled

Code: W#J052

Description: (Site-hq/site-site transfers only)  If the site involved in the transfer is disabled, no transfers will happen.

Solution: Enable the site(s) to have the transfer happen.

  

### A free channel/port cannot be allocated

Description: Each ongoing p2p(point-to-point) transfer in or out from a server on your premises occupies one channel/port. For example having the default port range 45190-45209 configured means that 20 concurrent high speed transfers can happen between the server and desktop apps or the server and another (site) server. This does not include web transfers, they do not require p2p channels.

Solution: Either configure a wider port range or wait for other transfers to finish.

## Transfer failures

Failing transfers are most commonly due to a missing source file or destination storage having space/write issues.  To troubleshoot the failure - get more information about the issues, follow these procedures:

UI (desktop app or web app):

- Hover the job and a description of the issue should be presented.

- A blue "Log" button is presented at the job, press it to bring up the log for troubleshooting.

- View the job and double-click the failed task/file in the list, this will bring up the detailed transfer log for deeper troubleshooting.

CLI (command line):

- List job(s) by issuing: ‘accsyn job find’, a description of the issue should be presented.

  

Here follows a listing of issues sorted depending on how commonly they occur:

  

### Missing source file(s)

Code: E#J001

Description: accsyn states that one or more file(s) are missing.

Solution: Try to bring the file/directory back if it is intended to be there. Otherwise exclude the tasks (files) in the GUI and retry the job for the rest of the files in the package to complete.

  

### Network connection lost

Code: E#J008

Description: accsyn states: A network communication error occurred during transfer. This happens to a transfer that has been going on for a while and suddenly the network drops out.

Solution: Make sure the network/Internet connection is stable and is not disconnected during transfer. A good starting point is to have a ping running during transfer in combination with doing trace routes to find out where the route is cut off.

  

### Files cannot be written

Code(s): E#J053, E#J055, E#J056, E#J057

Description: Usually this is due to the destination disk being full or the system user accsyn is running as on the server or client end has insufficient write permissions on the disk or volume. 

Solutions:

- Check disk space on the receiving end, free up space if necessary.
- Make sure files can be written to the disk, is it locked due to filesystem corruption or in another readonly state?
- Check the system user the accsyn process is running as, can this user create the required folders and/or write files where it needs to?

  

### Firewalls are blocking connections or scramble the connection during transfer

Code(s): E#J003, E#J004, E#J009, E#J010

Description: This is usually due to a change in configuration in the firewall blocking one or more ports configured in accsyn for WAN transfers.

Solutions:

- Edit the server and reconfigure the ports once more - make sure accsyn can make the TCP connections from WAN side as required.
- If transferring from a computer inside the same network (behind the same router) as the server is located, some firewalls might scramble the traffic. In this case you need to make IP overrides at the server towards the client for traffic to pass smoothly.
- Too many transfers are happening, configure more ports (channels) for accsyn to use. Some clients might have restricted outgoing ports, make sure to configure a couple of low ports like 443:TCP to get those transfers going.

## Error and warning codes

Complete list of accsyn error and warning codes:

[Error codes](errors.md)

[Warning codes](warnings.md)

## Having further issues?

Do not hesitate to contact [support](mailto:support@accsyn.com), be sure to describe your matter as thoroughly as possible and supply screenshots when possible. This shortens our response times and saves your time considerably.  For more guidelines on how to deal with the accsyn support, please head over [here](home.md).
