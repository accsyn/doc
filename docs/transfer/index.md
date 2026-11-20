# Transfer

This guide is for operators (admin or employee) who need to move files between endpoints over the secure, accelerated [ASC](/whitepaper/) protocol.

Typical operations:

- **Download from / upload to a site** — Sync files between main (HQ) storage and a remote office or cloud site, or between two sites.
- **Push to / pull from a remote user** — Sync files with a user who has one or more shares [mapped locally](/admin/hosts/#map-shares-locally) (Desktop App or User server) and has been [granted access](/collaboration/manage/).
- **Push to / pull from your own clients** — Sync files with a Desktop App or User server that you run yourself, when those clients have shares mapped locally.

You can use the **workspace endpoint** (main site / HQ storage), a **remote site**, a **remote user**, or **your own client** as source or destination. Transfers are peer-to-peer between the selected endpoints; they do not have to pass through HQ when both sides are sites or a site and a mapped user/client.

Day-to-day transfers are created in the **browser** on the **Transfer** page. The [Desktop App Transfer tool](#desktop-app-transfer) remains available if you prefer that workflow.

## Transfer page (browser)

### Preparations

1. Sign in at [accsyn.io](https://accsyn.io) (or your workspace hostname) as an administrator or employee.
2. Open **Transfer** from the workspace navigation.
3. For **site** transfers: sites and site servers configured — see [Site administration](/admin/site/).
4. For **remote user** push/pull: the user has mapped the relevant share(s) locally (ideally with a [User server](/admin/hosts/) for unattended access) and has been granted access to those shares. Read on the mapping allows operators to **pull** (take files from the user); write allows **push** (send files to the user).
5. For **own client** push/pull: your Desktop App or User server is online and has at least one share [mapped locally](/admin/hosts/#map-shares-locally).

![](/assets/transfer_web.png)

*Transfer page in the browser (source left, controls middle, destination right).*

### Layout

The Transfer page is a dual-pane browser with controls in the middle:

- **Source (left)** — Choose the **From** party (workspace / cloud or BYOS, a site, a remote user, or one of your own clients). Browse and select the file(s) and/or folder(s) to send. On user and client parties, the location list shows only [locally mapped shares](/admin/hosts/#map-shares-locally). You can also import a list of accsyn paths instead of picking files in the browser.
- **Middle** — The green **>** button submits the transfer. Below it, **json** previews the create-transfer payload. The **settings** (cog) opens job settings (name, queue, retries, transfer options, and so on). A red badge on the cog shows how many settings you have overridden.
- **Destination (right)** — Choose the **To** party. When the destination supports it, **Mirror paths** is available and preferred — the relative folder structure from the source selection is preserved. Otherwise use **Browse** and pick a destination folder.

Refresh parties with the refresh control next to the source selector (parties also refresh periodically). Progress appears under **My Jobs** / **Transfers**; pause, resume, and abort from there or from [Job monitoring](/manage/job/). Re-queue and prioritise via [Queue management](/manage/queue/).

### Create a transfer

1. Select the **source** party on the left, then select files/folders (or import paths).
2. Select the **destination** party on the right.
3. Prefer **Mirror paths** when enabled; otherwise **Browse** to a destination folder.
4. Optionally open **settings** to set a job name, queue, or transfer options.
5. Click the green **>** button to submit.


## Site transfer (download and pull)

Use a **site** as source or destination to sync with a remote office or cloud site (or to move data between two sites).

- **Download / pull from a site** — Source is the site; destination is the workspace (HQ) or another site. Browse the site’s volumes and shared folders, select content, then submit (mirror paths when the destination shares the same share context).
- **Upload / push to a site** — Source is the workspace (or another site); destination is the site. Same dual-pane flow; mirror paths when the site serves the matching volume/share.

Sites must be online (site server status) for browse and transfer. Configure sites under [Site administration](/admin/site/).

## Remote user push and pull

Use a **remote user** party when that user has mapped shares locally and you (or an ACL) have granted them access. The Transfer page lists those users as sources and destinations; the file browser shows only mapped shares the user can read (source) or write (destination).

- **Pull from a remote user** — Source is the user; destination is the workspace, a site, or another allowed party. Requires a mapped share with **read** enabled so operators can take files from the user’s machine/User server.
- **Push to a remote user** — Source is the workspace or a site; destination is the user. Requires a mapped share with **write** enabled so files can be written to the user’s local mapping. Prefer **Mirror paths** when the selection matches a mapped share.

Unattended 24/7 push/pull works best with a [User server](/admin/hosts/). See [Manage collaboration](/collaboration/manage/) for granting access and [Hosts](/admin/hosts/) for local mapping.


## Own clients push and pull

Your own **Desktop App** and **User server** clients appear as parties (for example labelled *My Desktop App* / *My User Server*) when they have active [local share mappings](/admin/hosts/#map-shares-locally). If a client is online but has no mappings yet, it still appears; the location panel warns that no local mapped shares are configured.

- **Pull from your client** — Source is your client; destination is the workspace, a site, or another party. Browse only the shares mapped on that client, select content, then submit.
- **Push to your client** — Source is the workspace or a site; destination is your client. Use **Mirror paths** when mappings allow it, or **Browse** into a mapped share folder.

This is useful for moving data between HQ/site storage and the machine you are running, without treating yourself as a separate “remote user” ACL party.


---

## Desktop App Transfer

The steps below are for users who prefer the **Desktop App**. Browser Transfer covers the same endpoint combinations; use this section when working in the app.

### Preparations

1. Download and [install the accsyn Desktop App](/desktop-app/).
2. Sign in as an administrator or employee.
3. For **site** transfers: sites and site servers configured — see [Site administration](/admin/site/).
4. For **remote user** push/pull: the user has mapped the relevant share(s) locally, ideally with a [User server](/admin/hosts/) for unattended 24/7 access. Read access on the mapping allows operators to **pull** (upload from the user); write access allows **push** (download to the user).

### Create a transfer

Open **Transfer** in the Desktop App top menu. You get a dual-pane browser: source on the left, destination on the right. Settings are available from the Transfer UI (cog / settings panel), similar to the browser page.

![](/assets/manage_transfer.png)

*Example: transferring selected files from HQ storage to a remote site with mirror paths enabled.*

1. **Select the source endpoint** on the left (main storage / HQ, a site, or a user with mapped shares), then select the file(s) and/or folder(s) to send.
2. **Select the destination** on the right (main storage / HQ, a site, or a mapped user).
3. If the destination has a matching share context (volume served on that site, or a share the user mapped locally), **Mirror paths** is available and selected by default — the relative folder structure is preserved. Otherwise use **Browse** to choose a destination folder.
4. Click the green **>** button in the middle to start the transfer.

Progress appears under **My Jobs** / **Transfers** in the bottom panel. Pause, resume, and abort from there or from [Job monitoring](/manage/job/); re-queue and prioritise via [Queue management](/manage/queue/).

### Related articles

- [Site administration](/admin/site/) — Add sites and site servers for office/cloud sync.
- [Hosts](/admin/hosts/) — Install a User server and map shares locally for remote push/pull.
- [Job monitoring](/manage/job/) — Monitor transfer jobs.
- [Queue management](/manage/queue/) — Prioritise and re-queue transfer jobs.
- [Collaboration](/collaboration/) — Shares, ACLs, and local mapping concepts.
- [Manage collaboration](/collaboration/manage/) — Grant access to shared folders.
- [Remote office sync](/tutorials/remote-office-sync/) — API-driven site synchronisation tutorial.
