# Collaboration - File sharing — introduction

This page introduces the accsyn File Sharing subsystem — available on Cloud or on-premises (BYOS) storage, and integrated with the [Media Vault](/vault/).

The core idea: **share specific subfolders of a project tree on production storage** — not the whole volume — so external users and partners can work inside production safely. Access is controlled with ACLs; transfers use the secure, accelerated [ASC](/whitepaper/) protocol via the Desktop App.

## Get started

We recommend this short video introducing file sharing:

<iframe width="560" height="315" src="https://www.youtube.com/embed/PqQLXAfZF5M" title="accsyn File Sharing introduction" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Tutorial

Set up file sharing step by step with this tutorial:

[FTP server replacement](/tutorials/ftp-server-replacement/)

## What is accsyn File Sharing?

In short, it is an FTP replacement: strong ACL-based access control combined with fast, secure, resumable transfers over ASC — without exposing broad production disks to partners.

## Why file sharing?

Film and media production move large file sets between studios, vendors, and remote teams. Operators need precise control over *who* sees *which* folder, with audit trails when access must be reviewed later.

accsyn is built for that: share only the project subfolders partners need (for example `FROM_VENDORS/acme` beneath a larger project tree), keep the rest of production storage private, and still give them a seamless download/upload experience over ASC.

## How does file sharing work with accsyn?

The simplest one-shot transfer is a [delivery](/delivery/) — a time-limited package. **File sharing** is for ongoing access: permanent (or long-lived) folders, homes, and collections on your storage.

A **share** is an accsyn entity you can expose long term to one or more users. It is similar to a delivery, except a share stays active for as long as the project (or collaboration) needs it, while a delivery can expire. Shares are often thought of as **projects** — typically mapped 1:1 to production projects — in a way that is comparable to a Windows SMB share: a named place on storage that people connect to with controlled permissions.

There are four types of shares:

- **Volume** — Disk storage or network share: the root folder. Accsyn cannot access files outside this folder. Administrators have full access. Employees can be granted read (download) and/or write (upload) on a volume. A workspace can have multiple volumes, served by different storage servers.
- **Shared folder** — A folder beneath a volume (or the volume itself) shared with standard-role users. You can share the entire folder or only a particular subfolder. Administrators and employees may create shares beneath volumes they can access.
- **Home** — A special shared folder designated and tied to a single user (typically named after their email), for personal upload/download outside the main production tree. Off by default; enable in Settings.
- **Collection** — A virtual shared folder: a named set of files and folders picked from across a volume, or even spanning multiple volumes, shared like a shared folder.

Accsyn uses **ACLs** (Access Control Lists) on shares to define what each user may do. The share API `code` must be unique within the workspace; in the API, paths often use `share=<ident>/…` notation.

That model means you do **not** need to copy files into a temporary account folder just to share them (as you often would with FTP). Instead you can share a project folder and use ACLs so partners only get download and/or upload on specific subfolders — keeping the rest of the tree private.

Access by role:

- **Administrators** — Full access to all volumes. Invite admins carefully.
- **Employees** — Access to volumes granted by administrators; can create shares, deliveries, and audit activity.
- **Standard users** — Apart from deliveries sent to them, only shared folders, homes, and collections they are granted via ACL.

## Can I share titles and media in the vault?

Yes. The title library sits on a normal folder structure on storage, so you can share folders and create collections as with any other content.

A common pattern is a permanent **DCP** collection shared with selected users.

## Can I share files on my own local or cloud storage?

Yes. With [BYOS](/admin/byos/) you install on-premises or cloud servers so file sharing and delivery run against your own storage.

## Can my clients share folders on their local machine?

Yes. This is **local file sharing**: a user maps a shared folder (or volume path) to a folder on their computer and grants workspace operators read and/or write on that mapping.

While their client is online, elevated users (administrators and employees) can:

- **Pull** — with read access, upload from the mapped folder onto main storage or a site.
- **Push** — with write access, download from main storage or a site onto the mapped folder.

Typical uses: working from home, or vendors keeping a local work area that mirrors production folder structure. Transfers use ASC when the Desktop App or User server is the endpoint.

Configure mappings in the **Desktop App** (app running and user signed in). For 24/7 access without a logged-in desktop session, install a **User server** (accsyn daemon/service). See [Hosts](/admin/hosts/).

## Can I share files and folders on a remote office or cloud site?

Yes. In a [BYOS](/admin/byos/) (or Enterprise) workspace you define **sites** — remote offices or cloud locations — usually with one or more **site servers**. Assign servers and elevated clients so accsyn knows where they are.

Site servers sync material between HQ and the remote site, serve shared storage there, and can take over transfers initiated by clients on that site so jobs continue when individual Desktop Apps close.

See [Site administration](/admin/byos/site/) and the [Remote office sync](/tutorials/remote-office-sync/) tutorial.

Next: [Work with accsyn File Sharing](/file-sharing/manage/)
