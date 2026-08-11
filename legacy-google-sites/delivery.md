# File Delivery - an introduction

This page serves as an introduction to the accsyn File Delivery subsystem - available either as a standalone tool or built into [File Sharing](file-sharing.md) and the  [Media Vaul](vault.md)t, or driven through [Workflows](developer.md).

## Get started

We recommend watch this 3 minute video, covering the basics - how to send a delivery and having user receive it:

## What is a delivery?

An accsyn delivery is one or more files and/or folders that needs to be transmitted to one or more recipients, in a speedy and secure manner. A delivery can also be an upload request, having users send large datasets back to you.

## How does it work?

You upload the file and/or folders to be sent to the accsyn temp accsyn Cloud storage (Outbound page), define the the recipient email addresses, set the expiry date of delivery and then submit the delivery. Files can also be delivered from the permanent accsyn Cloud storage or from BYOS volumes/shares, either from your browser or by using the the accsyn Desktop app - from storage (File Sharing) tool or within the Media Vault.

  

The recipients will get an email sent to them with a link and clear instructions on how to download and save the files/folders on their local computer.

## How does accsyn handle transfer of very large files and folders?

Although accsyn supports file transfer in the browser, the platform is designed to have file transfers driven by the accsyn Desktop App running in the background on the user's computer.

First time, the user will be asked if they want to use the web browser or install the Desktop App. The desktop app installation is very streamlined, and designed to be as quick and pain-free as possible. Here are the clear benefits from utilising the desktop app instead of the browser:

- Accelerated transfers; the accsyn app facilitates accelerated file transfers with its own proprietary file TCP transfer protocol based on standard SSL encryption.
- Possibility to transfer folders without needing to compress (e.g. ZIP) them, folders are not supported by web browsers.
- Large file transfer with single file resume;  if transfer is interrupted in the middle of a large file, the accsyn app will continue were it left off.
- Prioritise transfers; pause and resume transfers as needed, depending on delivery priority.

## What authentication options does the recipients have?

### Standard authorisation

By default, only the users identified by the email addresses entered during delivery creation are allowed to download the files. They will have to create an accsyn account, or login through one of our supported authentication vendors (e.g. Google), to be able to access the delivery.

  

### Public link

A delivery can be created as Public, this means that any registered accsyn user can download the files if they have the link. Public deliveries can have a password entered as an extra protection layer.

  

### Anonymous access

Public deliveries can be set to be access anonymously, this means that anyone can access the delivery without needing to login to accsyn.

  

Warning: anonymous deliveries cannot be audited effectively, meaning that you cannot really control who gets access to your files. Use this option carefully!

## What will happen when the delivery expires?

Before the delivery expires, users will be reminded twice so they don't forget to download the files. When delivery has expired, it will be set to done status and after 4h the temp files on the accsyn cloud storage will be deleted.

## Does accsyn support reverse deliveries - request upload from users?

Yes, accsyn have the Upload request feature (Inbound page) which allows for sending upload links to recipients, with clear instructions on how to upload their files and/or folders, for later download by the sender or any elevated user within the workspace - having admin or employee(operator) role.

## Can deliveries be sent from permanent storage?

Yes, from within the accsyn Desktop App you can send files and folders from the accsyn cloud storage or your own BYOS storage.

## Can recipients preview files/media with a delivery?

accsyn does not support thumbnail generation of arbitrary files, but with the accsyn Media Vault a title stream delivery can be created and sent as to one or more recipients, allowing for high quality bandwidth aware streaming of media. Learn how to create a stream [here](vault/stream.md).

Next: [create your first delivery](delivery/create.md).
