# File Delivery — an introduction

This page introduces the accsyn File Delivery subsystem. Delivery is available as a standalone tool, built into [File Sharing](../file-sharing/index.md) and the [Media Vault](../vault/index.md), or driven through [automations](../developer/index.md).

The core benefit: send **terabyte-scale folders with large numbers of files** using a simple link. Recipients download with the secure, accelerated [ASC](../whitepaper.md) protocol — no FTP servers, no fragile browser ZIPs for huge packages.

## Get started

We recommend this short video covering the basics — sending a delivery and receiving it:

<iframe width="560" height="315" src="https://www.youtube.com/embed/mPgkwiBtQMs" title="accsyn Delivery introduction" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## What is a delivery?

An accsyn delivery packages one or more files and/or folders for transmission to one or more recipients — quickly and securely. A delivery can also be an **upload request**, asking users to send large datasets back to you.

There are two types of deliveries:

- **Temporary delivery** — Files and folders are uploaded to a temporary folder on your accsyn cloud or on-premises storage, delivered to the recipient(s), then removed when finished.
- **Standard delivery** — You select files and folders that already reside on your accsyn cloud or on-premises storage.

## How does it work?

You create a delivery from uploaded files or from existing storage content, add recipients, and set the expiry date and access options. The delivery job stays active so you can add more recipients later. Recipients receive an email with a link and clear instructions; they use that link to pull the package — including multi-terabyte folders — over ASC when using the Desktop App.

### How do recipients action the delivery?

Recipients receive an email with a link and instructions for downloading (or uploading) the files on their computer.

They are guided to install and use the Desktop App (recommended default) for accelerated ASC transfers. For smaller packages, they may download in the browser instead.

## How does accsyn handle very large files and folders?

Browser transfer is supported for convenience, but large deliveries are designed around the **accsyn Desktop App** running in the background. That is how you send folders with many files at terabyte scale over a link: ASC handles acceleration, encryption, and resume — without requiring recipients to stage a ZIP of the whole package.

The first time, the user chooses the web browser or the Desktop App. App installation is streamlined. Benefits of the Desktop App over the browser:

- **Accelerated ASC transfers** — proprietary TCP file transfer with strong encryption (see the [Whitepaper](../whitepaper.md)).
- **Native folders** — transfer folder trees without compressing them first; browsers do not support folder download/upload the same way.
- **Resume** — if a transfer is interrupted mid-file, the app continues where it left off.
- **Control** — pause, resume, and prioritise transfers as needed.

## What authentication options do recipients have?

### Standard authorisation

By default, only users identified by the email addresses entered when the delivery was created may download the files. They must create an accsyn account, or sign in with a supported external provider (for example Google), before they can access the delivery.

### Public link

A delivery can be marked public so any registered accsyn user with the link can download. Public deliveries can also use a password as an extra protection layer.

### Password protection

Public deliveries can require a password before download.

### Anonymous access

Public deliveries can allow anonymous access — anyone can open the delivery without signing in to accsyn.

**Warning: anonymous deliveries cannot be audited effectively. You cannot reliably control who obtains your files. Use this option with care.**

## What happens when the delivery expires?

Before expiry, recipients are reminded twice so they do not forget to download. When the delivery expires, it is set to done status.

Temporary delivery files are deleted from accsyn storage after a 4-hour grace period.

## Does accsyn support reverse deliveries — upload requests?

Yes. The **Upload request** feature (Inbound / Requested) sends upload links to recipients with instructions on how to upload files and folders. When complete, the sender — or any elevated workspace user (admin or employee/operator) — can download the material.

## Can deliveries be sent from permanent storage?

Yes. From the accsyn Desktop App you can deliver files and folders from accsyn Cloud storage or your own BYOS storage.

## Can recipients preview files or media with a delivery?

accsyn does not generate thumbnails for arbitrary files. With the Media Vault, however, you can create a title stream delivery so recipients watch high-quality, bandwidth-aware streaming in the browser. Learn how to [create a stream](../vault/stream.md).

Next: [Create your first delivery](create.md).
