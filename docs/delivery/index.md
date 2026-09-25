# File Delivery - an introduction

This page serves as an introduction to the accsyn File Delivery subsystem - available either as a standalone tool or built into [File Sharing](../file-sharing/index.md) and the  [Media Vault](../vault/index.md), or driven through [Automisations](../developer/index.md).

## Get started

We recommend watching this 3 minute video, covering the basics - how to send a delivery and having the user receive it:

<iframe width="560" height="315" src="https://www.youtube.com/embed/mPgkwiBtQMs" title="accsyn Delivery introduction" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## What is a delivery?

An accsyn delivery is one or more files and/or folders that need to be transmitted to one or more recipients, in a speedy and secure manner. A delivery can also be an upload request, having users send large datasets back to you.

There are two types of deliveries:

- **Temporary delivery**; Files and folders are uploaded to a temporary folder on your accsyn cloud or on-prem storage, which then is delivered to recipient(s) and later remved upon finish.
- **Standard delivery**; You select files and folders to delivery on your accsyn cloud or on-prem storage.

## How does it work?

The delivery is created out of a set of uploaded files or from existing files, recipients are added and expiry date plus other options are set. The delivery job will stay active and more recipients can be added afterwards.

### How will the recipients action the delivery? 

The recipients will get an email sent to them with a link and clear instructions on how to download and save the files/folders on their local computer.

They will be guided through the process of download, installing and using the desktop app to download the files (default). If feasible, the recipient can also choose to download the files in their browser.

## How does accsyn handle transfer of very large files and folders?

Although accsyn supports file transfer in the browser, the platform is designed to have file transfers driven by the accsyn Desktop App running in the background on the user's computer.

The first time, the user will be asked if they want to use the web browser or install the Desktop App. The desktop app installation is very streamlined, and designed to be as quick and pain-free as possible. Here are the clear benefits from utilising the desktop app instead of the browser:

- Accelerated transfers; the accsyn app facilitates accelerated file transfers with its own proprietary file TCP transfer protocol based on standard SSL encryption.
- Possibility to transfer folders without needing to compress (e.g. ZIP) them, folders are not supported by web browsers.
- Large file transfer with single file resume;  if the transfer is interrupted in the middle of a large file, the accsyn app will continue where it left off.
- Prioritise transfers; pause and resume transfers as needed, depending on delivery priority.

## What authentication options do the recipients have?

### Standard authorisation

By default, only the users identified by the email addresses entered during delivery creation are allowed to download the files. They will have to create an accsyn account, or log in through one of our supported external authentication providers (e.g. Google), to be able to access the delivery.
  

### Public link

A delivery can be created as Public, this means that any registered accsyn user can download the files if they have the link. Public deliveries can have a password entered as an extra protection layer.

  
### Password protection

Public deliveries can be protected by an password, that recipients must enter before they can download the delivery.


### Anonymous access

Public deliveries can be set to be accessed anonymously, this means that anyone can access the delivery without needing to log in to accsyn.

  

**Warning: anonymous deliveries cannot be audited effectively, meaning that you cannot really control who gets access to your files. Use this option carefully!**

## What will happen when the delivery expires?

Before the delivery expires, users will be reminded twice so they do not forget to download the files. When the delivery has expired, it will be set to done status. 

Temporary deliveries will have their files deleted after 4h from the accsyn storage.

## Does accsyn support reverse deliveries - request upload from users?

Yes, accsyn has the Upload request feature (Inbound page) which allows for sending upload links to recipients, with clear instructions on how to upload their files and/or folders, for later download by the sender or any elevated user within the workspace - having admin or employee(operator) role.

## Can deliveries be sent from permanent storage?

Yes, from within the accsyn Desktop App you can send files and folders from the accsyn cloud storage or your own BYOS storage.

## Can recipients preview files/media with a delivery?

accsyn does not support thumbnail generation of arbitrary files, but with the accsyn Media Vault a title stream delivery can be created and sent to one or more recipients, allowing for high quality bandwidth aware streaming of media. Learn how to create a stream [here](../vault/stream.md).

Next: [Create your first delivery](create.md).
