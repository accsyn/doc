# Monitor and manage deliveries

This guide explains how to manage your deliveries - check if recipients have responded and modify them.

### Prerequisites

- An active accsyn workspace trial or subscription.
- A web browser, preferably Google Chrome.

## Monitor delivery

Logon to accsyn in your web browser and go to Outbound section and then click the delivery you want to monitor.

![](../assets/delivery_manage-1245ed300e63.png)

Screenshot of the delivery status view.

A delivery is presented in the following way:

  

- Files; A list of files on folders in the delivery, with size.
- Public link; (If a public delivery) The link to delivery/upload request.
- Transfers in progress; The file transfers that are running right now - e.g. list of recipients that currently are downloading a delivery, or uploading to upload request.
- Pending; List of recipients that have not addressed the delivery/upload request yet, with the ADD RECIPIENTS button (see below).
- Failed or aborted; Failed of aborted transfers.
- Done; Completed deliveries.
- Uploads; The initial uploads performed when deivery were created.
- Created: The date delivery were created.
- Expires: The expiry date of delivery.
- View logs; Monitor job logs, see below.

  

Each user is displayed with email and when they last logged in. Actioned deliviers also have estimated geographical location, etr and speed notation.

### Logs

The delivery has a log that can be investigated in order to find out what has happened within the lifecycle of delivery, useful for debugging purposes and security audits. 

To access the log from Outbound page, click on the three-dot icon on the right hand side of delivery and choose Log from the menu. On the delivery status page, the log can be opened by clicking the View logs button.

Each file transfer also have an associated log, it can be viewed by clicking the log icon on the right hand side of each recipient.

## Manage delivery

### Notify recipients

By default, recipients that has not actioned deliveries are notified automatically twice:

- A first remainder when 2/3 of the time has passed up until expiry.
- A second remainder three(3) days before expiry.

Note: When delivery expires, the files will be kept on storage for another 4h after they will be permanently deleted. This applies to standard deliveries uploaded to a temp space, when delivering permanent files residing on the accsyn Cloud storage or BYOS storage, files will not be touched.

To manually notify a recipient, click the paperplane button on the right hand side of the recipient in the Pending section. A remainder email will be dispatched to user, if they do not receive it - have them check their spam filters.

### Add more recipients

At any time, more recipients can be added to a delivery/upload request. Open the delivery and click the ADD RECIPIENTS button in the Pending section. A prompt will be displayed were you can enter one or more email addresses, press TAB to add and enter the next address and so on. Finish up by clicking INVITE RECIPIENTS.

New recipients will be sent an email with a link to the delivery, with clear instructions on how to download or upload files.

### Remove recipients

To remove a recipient, click the cross button on the the right hand side of the recipient, a confirm prompt will be displayed.

### Edit delivery

To edit a delivery, click Edit from the delivery context menu or lick the pen button in upper right corner of delivery status page.

Files can not be added once a delivery have been created, but you can change:

  

- Message; Enter a new message that recipients will get in their email and displayed when they open the delivery.
- Expiry date; Give a new expiry date.

### Troubleshoot a delivery

Usually, deliveries goes smoothly. But sometimes users need help getting their files downloaded, or uploaded to a request:

  

- They have not received any delivery email; Sometimes, the accsyn delivery emails get catched by spam filters. Ask users to check their spam mail. Another thing as that you have not sent the delivery yet, recall that you need to actively Submit a new delivery before users can download/upload. If emails cannot be dispatched, ask them to login to <https://accsyn.io> with the same email as you have added as recipient, they should be able to locate their delivery in the Downloads section (or Uploads section, if an upload request).
- The file transfer won't start, keeps failing; Have user check their antivirus and firewalls, so accsyn desktop app is whitelisted and traffic are allowed (TCP ports 45190 and upwards needs to be allowed towareds the Internet and accsyn infrastructure servers).
- The transfer goes for a while but fails or just stops; Make sure they have not logged out and/or shut down their computer, it is needed for transfers to complete. If they are transferring in the web browser, they can't reload or close the accsyn web page before transfer is completed. Also, their disk might be full - have them check free space.

  

If you have further issues with deliveries that can't be resolved, don't hesitate to reach out to our support team either through Chat or email.

### Delete/abort delivery

To delete a delivery, either choose Delete from the delivery context menu (three-dot icon on Outbound page) or click the trashcan icon when editing delivery.

## Archived deliveries

Finished deliveries and upload requests are listed under Archive section accessible from the workspace menu on the left.
