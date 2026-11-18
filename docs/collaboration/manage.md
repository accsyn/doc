# Manage collaboration

This guide explains how to use accsyn as a file-sharing service — similar in role to an FTP server, but with fine-grained ACLs and transfers over the secure, accelerated [ASC](/whitepaper/) protocol.

You can expose **specific subfolders of a project tree on production storage** to external users and partners without giving them the whole volume. That is the usual pattern for integrating vendors into production safely.

Day-to-day sharing is managed in the **browser** on the **Storage** page (`/storage`). The [Desktop App](#desktop-app-storage-view) remains available if you prefer that workflow.

## Storage page (browser)

### Preparations

1. Sign in at [accsyn.io](https://accsyn.io) (or your workspace hostname) as an elevated user — an administrator, or an employee with access to at least one volume.
2. Open **Storage** from the workspace navigation.

![](/assets/admin_collaboration_manage_web.png)

*Manage accsyn storage collaboration.*

The Storage page has three areas:

### Location list

On the left, locations are grouped under each **volume**:

- **Volumes** — root folders/drives exposed to accsyn. The default cloud volume is often named `storage` (marked with a check). Expand a volume to see its nested groups.
- **Shared folders** — folders beneath that volume shared with users (nested under the parent volume).
- **Homes** — per-user home shares on that volume (collapsed by default under each volume).
- **Collections** — virtual folders of files/folders from one or more volumes (separate top-level group).


Hover a location for details (name, code, type, path, creator). Right-click a location for **New**, **Edit**, **Deactivate**, **Delete**, **Show/Hide disabled**, and **Refresh**. Use the address bar breadcrumbs above the file list to jump up the path quickly.

### File list

The centre pane lists files and folders for the selected location. Use the toolbar to go back/up, create folders, delete, and reload. Folders that are shared (or contain sharing beneath them) show a shared-folder icon and a small badge with share, user, and shared-folder counts.

With nothing selected, open **Share** for:

- **Request upload here** — start an upload request targeting the current folder.
- **Grant employee access** — (volumes only) share the volume with employees.
- **Share folder** — (volumes only) create a shared folder at the current path.

With files or folders selected, **Share** offers:

- **Deliver** — create a delivery from the selection.
- **Create new collection** — build a collection from the selection.
- **Add to collection** — append the selection to an existing collection.

![](/assets/admin_collaboration_manage_share.png)

*Share menu.*

### Access info

On the right, the access panel shows who can reach the current location and path:

- Shared folders / collections / homes that apply here, with ACL entries.
- **Share folder** when the current volume path is not yet a share.
- **Employees with access to volume** (when browsing a volume), including grant and revoke.
- Administrators (informational).


Use **Grant access** on a share card to open the ACL dialog for standard users.

## Sharing a volume with employees

*Note: To invite administrators, go to [Users](https://accsyn.io/admin/users) or use **Invite user** in the Desktop App.*

1. On Storage, select a **volume** (not a nested shared folder, collection, or home).
2. Either:
   - Click **Share** → **Grant employee access**, or
   - In the access panel under **Employees with access to volume**, use the grant control.
3. Add one or more employees (search existing users, or invite where allowed).
4. Confirm permissions and optional notification message.
5. Confirm and grant access.

![](/assets/admin_collaboration_manage_grant_employee.png)

*Grant employee access to a volume.*


Revoke access from the employee list in the access panel (trash can on the ACL).

## Sharing a folder with standard users

*Note: accsyn does not share a single file as a bare link. Put the file in a [collection](#creating-a-collection) instead.*

Typical production pattern: create a **shared folder** on a project path, then grant ACLs on the whole share or only a **subfolder** (for example a vendor drop zone). Partners see only what you grant; transfers run over ASC when they use the Desktop App or a User server.

### Create a shared folder

1. Select the volume and browse to the folder to share (or stay at the volume root).
2. Click **Share** → **Share folder**, or **Share folder** in the access panel when the path is not already shared.
3. Name the share. Optionally set **code** (API identifier), **queue**, description, and project.
4. Optionally add users in the **Grant access** section of the create dialog — they are confirmed after the share is created.
5. Click **Share folder** / create.

![](/assets/admin_collaboration_manage_share_folder.png)

*Share a folder and grant access in one operation*


The new shared folder appears under that volume in the location list. If the path already has a share, you can still create another share on the same path after confirming.

### Grant access to a shared folder

1. Select the shared folder in the location list (or browse the volume into a path covered by that share).
2. In the access panel, open **Grant access** on the share card (or browse to a subfolder first so the ACL path matches that subfolder).
3. Add users by search or invite.
4. Choose **Read** and/or **Write**, optional notify + message.
5. Confirm the grant prompt, then finish with **Done**.

![](/assets/admin_collaboration_manage_grant_user_access.png)

*Grant standard user access to a share.*

To revoke access, use the trash can on the ACL entry in the access panel or grant dialog.

### Edit, deactivate, or delete a shared folder

- Right-click the share → **Edit** (opens admin storage editor for that share), or use Admin → Storage.
- Right-click → **Deactivate** to archive (keeps files on disk).
- Right-click → **Delete** to remove the share entity (files on disk are not deleted).

Restore or manage inactive shares from [Admin → Storage](https://accsyn.io/admin/storage). Use **Show disabled** in the location context menu if you need to see deactivated locations in the browser list.

## Creating a collection

1. In the file list, select one or more files and/or folders.
2. Click **Share** → **Create new collection**.
3. Name the collection and optionally grant users in the same dialog.
4. Confirm create (and confirm grants if you added users).

![](/assets/collaboration_manage_web_create-collection.png)

*Screenshot placeholder: Create collection dialog after selecting files/folders.*

Add more items later: select files → **Share** → **Add to collection** → choose the collection.  
Remove items while browsing the collection (with manage enabled): select entries → delete / remove from collection.

### Share a collection with users

Select the collection in the location list and use **Grant access** in the access panel — same ACL flow as folders (path is not used for collections).

### Removing a collection

Right-click → **Delete**, or **Deactivate** to archive. Manage inactive shares from Admin → Storage / Shares.

## Accessing a shared folder

Standard users: see [Access shared folders](/collaboration/access/).

Administrators and employees: use **Download** / **Upload** in the browser or Desktop App, or the **Transfer** tool. Large ongoing transfers are best with the Desktop App over ASC.

## Remove access for a folder or collection

1. Select the shared folder or collection.
2. In the access panel, revoke ACL entries with the trash can.
3. Or open **Grant access** and remove entries from the assigned-users list.

Users are not notified when access is revoked.

*Note: If a standard user no longer has access to any shared folder or collection, they cannot sign in to the Desktop App for your workspace.*

## Create a home

A home share gives a user a personal upload/download area. accsyn can create homes automatically — see **Storage** under Workspace → Administrate → Settings.

### Create a home from Storage (browser)

1. Sign in as an administrator (or employee with rights on the target volume).
2. Open **Storage**, expand the volume, and ensure **Homes** is visible under that volume.
3. Right-click in the location list (or on a home/volume context where **New** → home is available) and create a **Home**.
4. Choose the parent volume and user, then create.

![](/assets/collaboration_manage_web_create-home.png)

*Screenshot placeholder: Create home dialog (volume + user).*

Read/write ACLs are created for that user. You can also create homes from [Admin → Storage](https://accsyn.io/admin/storage) on the volume’s Homes tab.

## Renaming and moving shared content

Shared folders, homes, ACLs, and collection entries store paths relative to storage. When those paths change, accsyn must update its records so access stays correct.

### Inside accsyn

When you rename, move, or delete via the Storage file browser (browser or Desktop App):

- **Shared folders and homes** — path updates if the folder (or a parent) is renamed or moved. If the folder is **deleted**, the share is inactivated (related ACLs too).
- **ACLs** — paths update when their target subfolder is renamed or moved. If a folder moves *out* of the share, or a folder beneath the share is **deleted**, those ACLs are removed and the change is logged.
- **Collection** entries — paths update for renamed/moved items; entries for **deleted** items are removed.

Prefer changing shared content inside accsyn so references stay consistent.

### Outside accsyn

If the same paths change on disk outside accsyn (Finder, Explorer, tools on the storage host), accsyn does **not** learn about it. Shares, ACLs, and collection entries can become orphaned until you fix them manually.

*Note: Deleting a share in accsyn does not delete files on disk. Deleting or moving files outside accsyn does not remove or repair related shares and ACLs.*

## Manage shares with the Python API

Shared folders, homes, collections, and volume ACLs can be automated with the [accsyn Python API](/developer/python-api/). A common pattern is to create a shared folder on a project path, then grant a partner access to a **subfolder** only.

Example — create a shared folder, then grant read/write on a vendor subpath:

```python
share = session.create("Folder", {
    "parent": "664b6d76e43eb396e5e55419",
    "path": "projects/theproject",
    "name": "Shared project assets",
})

acl = session.grant(
    "User", "61779c54b80099ea066b0604",
    "Folder", share["id"],
    {
        "path": "FROM_VENDORS/acmevfx",
        "read": True,
        "write": True,
        "notify": True,
        "message": "Please upload your files here.",
    },
)
```

Omit `path` (or use `"/"`) to grant the entire shared folder. Transfers to and from these shares use ASC when clients run the Desktop App or a User server.

For volumes, collections, revoke/deactivate, and more, see the full [Collaboration](https://accsyn-python-api.readthedocs.io/en/latest/collaboration.html) chapter. API keys and installation: [Developer Hub — Python API](/developer/python-api/).

*Note: The API is not available for Cloud Essentials or BYOS Lite workspaces.*

---

## Desktop App Storage view

The steps below are for users who prefer the **Desktop App**. Browser Storage covers the same sharing concepts; use this section when working in the app.

### Preparations

1. Download and [install the accsyn Desktop App](/desktop-app/).
2. Sign in as an elevated user — an administrator, or an employee with access to at least one volume.

File sharing is driven from the **Storage** view:

![](/assets/manage_storage_app.png)

*Example screenshot of the Storage view in the Desktop App.*

The view has three areas:

### Share list

On the left, the share list shows:

- **Recent** — the five most recently visited shares.
- **Volumes** — root folders/drives exposed to accsyn. The default cloud volume is often named `storage`. BYOS setups may define as many volumes as needed.
- **Shared folders** — folders beneath a volume shared with users.
- **Collections** — virtual folders of files/folders from one or more volumes.
- **Homes** — per-user home shares.

Right-click a share for its context menu. Use the eye icon to show or hide share-type sections (homes are hidden by default).

### File list

The centre pane lists files and folders for the selected share. It behaves like a normal file browser, with a toolbar and context menu for create, move, rename, and delete.

When you rename, move, or delete content **inside accsyn**, share paths, ACL paths, and collection references are updated where possible. See [Renaming and moving shared content](#renaming-and-moving-shared-content).

### Access info

On the right, the access panel shows which users have access to the current share and path.

### Sharing a volume with employees (Desktop App)

1. Select the volume on the left (not while browsing a shared folder, collection, or home).
2. In the access panel, click **Share** and choose **Grant employees access**, or click the green **+** under **Employees with access to volume**. The ACL dialog opens:

![](/assets/collaboration_manage_grant-employee-access.png)

3. Enter an email or use the list icon to pick an existing employee. You can invite new employees here.
4. Choose permissions: **Read** (download only) or **Write** (upload and modify).
5. (Optional) **Notify employee** — enter a message, or clear the option to skip email.
6. Click **Grant access**.

### Create a shared folder (Desktop App)

1. In Storage view, select the volume and browse to the folder to share.
2. Click **Share** in the toolbar and choose **Create shared folder**, or use **Create shared folder** in the access panel.

![](/assets/collaboration_manage_create-share.png)

3. Give the share a name.
4. (Optional) Set the share **code**, **queue**, and initial grants.
5. Click **Create**.

### Grant access to a shared folder (Desktop App)

1. Select the shared folder in the share list.
2. Browse to the subfolder to share, or stay at the root to share the entire folder.
3. Click **Share** → **Grant user access**, or **Grant access** in the access panel:

![](/assets/collaboration_manage_grant-user-access.png)

4. Enter an email or pick an existing user, set permissions, optional notify, then **Grant access**.

### Create a collection (Desktop App)

Select file(s) and/or folder(s), then **Share** → **Create new collection**, or right-click → **Share → Create new collection**, or **NEW** in the collections section. Add more items with **Share → Add to collection**.

### Create a home (Desktop App)

Click **NEW** under Homes, or **+** in the homes section header: choose the user, optional description, then **Create**. The home is created on the default volume under the configured home path.

### Related articles

[BYOS](/admin/byos/)

[Python API](/developer/python-api/)

[Access shared folders](/collaboration/access/)
