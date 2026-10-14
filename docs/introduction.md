# An introduction to accsyn

accsyn is a complete **file I/O platform** for film and media — underpinned by the high-speed encrypted **[ASC](/whitepaper/)** (Accelerated Secure Copy) protocol.

It is offered as **two product variants**, each aimed at a different stage of the media life-cycle. Most organisations use one or the other; if you need both production I/O and a cloud master archive, sign up for **two workspaces** (BYOS + Cloud) rather than combining them in one.

| Variant | Stage | Storage model |
| --- | --- | --- |
| **[accsyn for media production](#accsyn-for-media-production)** *(default)* | Shoot, DIT, post, VFX, collaboration, site sync, automation | [BYOS](/admin/byos/) — your on-premises or cloud VPC storage |
| **[accsyn for media distribution](#accsyn-for-media-distribution)** | Masters, archival, streaming, sales/festival delivery, lab | [accsyn Cloud](/vault/) — hosted vault storage |

Both move **large folders and many files** securely and efficiently over ASC. Product videos for each variant are planned under the same names.

## accsyn for media production

**Default path for studios and post.** Expose production storage you already own — on-premises or in your cloud VPC — with accelerated, secure file I/O. This is the [BYOS](/admin/byos/) (Bring Your Own Storage) workspace.

Watch video to get started:

<iframe width="560" height="315" src="https://www.youtube.com/embed/D9Ng_yDVW1Y" title="accsyn Delivery introduction" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Main features:

- Deliver and receive multi-terabyte packages over a link ([Delivery](/delivery/))
- Share **specific project subfolders** with vendors and partners via ACLs ([Collaboration](/file-sharing/))
- Sync remote offices and cloud sites ([Sites](/admin/byos/site/)); push/pull with operators via [Transfer](/manage/transfer/)
- Push/pull with remote users via mapped shares and User servers ([Hosts](/admin/hosts/))
- Automate with [hooks](/developer/hooks/), [publish](/developer/publish/), [Python API](/developer/python-api/), and [render/compute](/developer/farm/)
- Central monitoring with [Job & Wueue management](/manage/job/)

Start with [BYOS](/admin/byos/) and a [free trial](/trial/) (one storage server).

*Media Vault (tagging, proxies, browser streaming of masters) is not available on BYOS. For that, use a separate Cloud workspace — see below.*

## accsyn for media distribution

**For distributors, festivals, sales agents, and archives.** Host masters and deliverables in a **secure cloud location**, with tagging, streaming, delivery, collaboration, and lab handoff. This is an accsyn **Cloud** workspace with [Media Vault](/vault/).

Typical capabilities:

- Tag and organise masters in the Media Vault (IMDb linkage, proxies, QC-oriented workflows)
- Stream and deliver to cinemas, buyers, and partners ([Stream](/vault/stream/), [Delivery](/delivery/))
- Collaborate on sales and festival packages ([Collaboration](/file-sharing/))
- Transcode deliverables, validate media including DCP check.
- Central monitoring with [Job & Wueue management](/manage/job/)
- Professional [Lab services](/vault/media-lab/) for mastering, VOD export, QC, and more

Start with a [Cloud trial](/trial/) (500 GB) and the [Media Vault](/vault/) guides.

### Production + distribution together?

There is no benefit today to combining BYOS production storage and Media Vault in a **single** workspace. If you need both:

1. A **BYOS** workspace for production I/O on your own storage  
2. A separate **Cloud** workspace for the master archive, streaming, and lab  

See also the note under [Media Vault](/vault/).

## Why accsyn?

Slow transfers and fragmented tools still dominate media pipelines. Accsyn is the **file hub from set to screen** — cinema or streaming — with ASC for accelerated peer-to-peer transfers, central orchestration, and audit.

Security highlights: HTTPS for control-plane traffic; AES-encrypted ASC for data; on-demand listeners (no ASC port open 24/7). Full detail: [Whitepaper](/whitepaper/).

## How does it work?

The accsyn cloud backend orchestrates high-speed P2P transfers, compute jobs, and (on Cloud) media management. The Desktop App (and background daemon / User server / BYOS storage server) acts as the transfer endpoint on each machine.

![](/assets/introduction-679212a60583.png)

## Free trial

Start a **30-day trial** at <https://accsyn.io/trial> — full features, no credit card:

- **Media production (BYOS)** — one storage server on your premises or VPC  
- **Media distribution (Cloud)** — 500 GB hosted storage  

1. Register at <https://accsyn.io> and verify your email.
2. Click **Start 30 days free trial** and create the workspace type you need.
3. For production: [BYOS setup](/admin/byos/), [delivery](/delivery/), or [file sharing](/file-sharing/). For distribution: [Media Vault](/vault/).

Step-by-step: [Trial](/trial/).

## Licensing and pricing

An accsyn licence includes unlimited traffic, bandwidth, and standard users (delivery recipients and file-sharing users). Operator seats and storage (Cloud) or servers (BYOS) are licensed separately.

| | **accsyn Cloud** *(distribution)* | **Cloud Essentials** | **accsyn BYOS** *(production)* | **BYOS Lite** |
| --- | --- | --- | --- | --- |
| Storage | 1 TB + PAYG | 500 GB | Unlimited (your disk) | Unlimited (your disk) |
| Operators | 2 + PAYG | 1 | 2 + PAYG | 2 + PAYG |
| Users | Unlimited | Unlimited | Unlimited | Unlimited |
| Traffic / bandwidth | Unlimited | Unlimited | Unlimited | Unlimited |
| Storage servers | 1 (Cloud) | 1 (Cloud) | 1 included | 1 included |
| Site / render servers | N/A | N/A | PAYG | PAYG |
| Media Vault / streaming / deliverable transcode | :material-check:{ .feature-yes } | :material-check:{ .feature-yes } | N/A | N/A |
| Hooks / publish / render | N/A | N/A | :material-check:{ .feature-yes } | :material-check:{ .feature-yes } |
| API | :material-check:{ .feature-yes } | N/A | :material-check:{ .feature-yes } | N/A |
| Lab services | :material-check:{ .feature-yes } | :material-check:{ .feature-yes } | N/A | N/A |
| Professional services | :material-check:{ .feature-yes } | :material-check:{ .feature-yes } | :material-check:{ .feature-yes } | :material-check:{ .feature-yes } |

Usage is measured at midnight CET; peak usage bills into the next cycle. Price list: [Pricing](https://accsyn.com/pricing).

**Essentials / Lite** are budget variants: Essentials is 500 GB Cloud with one operator and no API; Lite is one BYOS storage server with two operators and no API.

## Lab and professional services

**[Media Lab](/vault/media-lab/)** — Partner lab work (mastering, VOD export, QC, grading, and more), charged per order item, hours, and deliverable. Place orders from the Desktop App on **Cloud** (distribution) workspaces.

**Professional services** — With **25+ years of media IT experience**, billed hourly for:

- Deploying and configuring accsyn (BYOS production, Cloud distribution, or hybrid with two workspaces)
- Integration and pipeline design (deliveries, sharing, sites, hooks, compute)
- Media IT advice (storage, networking, security, operations)
- Education and onboarding

## Where to go next

| Goal | Start here |
| --- | --- |
| **accsyn for media production** (BYOS) | [BYOS](/admin/byos/) |
| **accsyn for media distribution** (Cloud Vault) | [Media Vault](/vault/) |
| Send / receive large packages over a link | [Delivery](/delivery/) |
| Share project subfolders with partners | [Collaboration](/file-sharing/) |
| Sync HQ ↔ sites / mapped users | [Transfer](/manage/transfer/) |
| Automate transfers and farms | [Developer Hub](/developer/) |
| Protocol and security deep dive | [Whitepaper](/whitepaper/) |
| Desktop App install | [Desktop App](/desktop-app/) |
| Specs and platforms | [Specifications](/specifications/) |

## What does “accsyn” mean?

**acc**elerated file **syn**chronisation.

More at <https://accsyn.com>.
