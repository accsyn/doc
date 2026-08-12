# File sharing - Introduction

This page serves as an introduction to the accsyn File Sharing subsystem - the standalone feature available on Cloud or On-prem storage, integrated into the accsyn [Media Vault](vault.md).

## Get started

We recommend watching this 1:30 minute video, providing an introduction to file sharing:

## What is accsyn File Sharing?

In principle, it is an FTP replacement combining powerful ACL mechanisms with fast, secure and resumable file transfers / deliveries.

## Why File Sharing?

With film production, and basically any type of workflow that involves files, large file sets need to be uploaded and further distributed/delivered to remote teams.

  

accsyn has been streamlined for sharing folders efficiently, giving operators full control of who has access, combined with audit functions so file access can be backtracked.

## How does file sharing work with accsyn?

The most basic form of file sharing is making a delivery - collecting the files and/or folders to send to a user, available for a limited time. Learn about file deliveries [here](delivery.md).

  

To understand how accsyn file sharing works we first declare some terms used throughout this guide:

- ACL; Access Control List, defines which employees have access to volumes, and which standard users have access to Shared folders.
- Share; Is a common abbreviation and the internal accsyn entity for a container that contains files and folders sharable with users, a share could be a volume, shared folder, collection or home share (see below). Shares must be unique within the workspace and cannot have the same name. When using the accsyn API, shares are usually targeted using the common "share=<ident>/.." notation.
- Volume; A volume is the root folder exposed to accsyn on a file server. accsyn cannot access files outside this root folder, and all file sharing (and delivering, title management and so on) happens within this folder. In a BYOS setup, you can have as many volumes as you need. Administrators have full access to volumes, employees have full access to the volumes they have been granted access to. Standard users do not have direct access to a volume.
- Shared folder; A folder beneath a volume, or the volume root folder, intended to be shared with standard users through ACLs.
- Collection; Files and folders collected from one or more volumes and put into a virtual folder that can be shared with users the same way a shared folder would.
- Home; A special shared folder, named as the user (email), giving users a place to upload and download material outside the default production area. By default, this feature is turned off and can be turned on in Settings.

  

Users get access to shared files depending on their role:

- Administrators; Have full access to all volumes, be careful who you invite to be an administrator.
- Employees; Are granted access to one or more volumes by administrators, giving them full access to the files and folders - create shares, deliveries, monitor and audit.
- Standard users; Except for deliveries sent to them, standard users only have access to shared (home) folders beneath a volume or collections.

## Can I share Titles and associated media within the vault?

Yes, the title library just sits on top of a basic folder structure on your accsyn storage, allowing for sharing folders and creating collections just as you would do with any regular content.

A good example is to create a permanent "DCP" collection, with a set of DCPs to permanently share with one or more users.

## Can I share files on my own local or cloud storage?

Yes, accsyn provides a BYOS licensing option allowing you to install on-prem our cloud servers facilitating file sharing and delivery on your storage solutions.

  

Read more about BYOS here.

Next: [work with accsyn File Sharing](file-sharing/filesharing-workingwith.md)
