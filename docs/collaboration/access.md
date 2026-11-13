# Access shared folders

This guide is for end users who have been granted download and/or upload access to an accsyn shared folder or collection.

You typically get access to a **specific project subfolder** on production storage — not the whole disk. Transfers can run in the browser for simple cases, or over the secure, accelerated [ASC](/whitepaper/) protocol via the Desktop App for large or resumable work.

**Important:** If you received a **delivery**, use the link in the delivery email and follow [Receive a delivery](/delivery/receive/). This page is for **permanent** (or long-lived) shared folders and collections on accsyn storage.

## Email notification

When someone grants you access to a folder in an accsyn workspace, you should receive an email with a direct link to that share. Example link:

```html
https://accsyn.io/shared/VuPd4yGxNVE5ryBo
```

If this is your first time on the platform, you also receive an invitation explaining how to activate your accsyn account.

*Note: If you cannot find these emails, check spam. Search for sender [noreply@accsyn.com](mailto:noreply@accsyn.com).*

If you received no email, sign up at <https://accsyn.com/signup> with the same address the share was sent to. After sign-in you are taken to **Shared with me**, where you can open the share.

## Primary method — open the share in the web browser UI

The **primary** way to access a share is to follow the link in the email. That opens the share in the accsyn web app, where you can browse folders you are allowed to see.

![](/assets/collaboration_access_web.png)

*Access a share with the web browser.*

### Permissions

What you can do depends on the ACL for the folder you are browsing:

- **Read** — browse and download.
- **Write** — upload files into the current folder.
- **Rename / move / delete** — change or remove items (where granted). These rights usually follow write access on that path.

If you try to create a folder, upload, rename, move, or delete without permission, the web app warns you and asks you to navigate into a folder where you have write (or the relevant) permission.


### Download

1. Select one or more files or folders in the browser.
2. Click **DOWNLOAD**.
3. Prefer the **Desktop App** for folders, multiple files, large sets, and resumable transfers (ASC).
4. For a **single file**, you can also download in the **browser**. Browser download does **not** currently support ZIP packaging of folders or multi-file selections — use the Desktop App for those. Browser multi-file / ZIP support may improve in future releases.

![](/assets/collaboration_access_download.png)

*Download a directory from the share page.*

### Upload

1. Browse into a folder where you have **write** permission.
2. Click **UPLOAD**.
3. Prefer the **Desktop App** for large uploads, folders, and resumable transfers.
4. For smaller **single-file** (or modest browser) uploads, you can use the browser drop zone in the upload dialog. Very large selections may require the Desktop App.


![](/assets/collaboration_access_upload.png)

*Share upload dialog.*

### Rename, move, and delete

In the browser file list you can:

- **Rename** — right-click an item → **Rename**, enter the new name.
- **Move** — right-click → **Move**, pick a destination folder inside the same share (destination must allow write).
- **Delete** — right-click → **Delete**, or select one or more items and use the trash icon in the toolbar. Confirm before deletion.

![](/assets/collaboration_access_rename.png)

*File modification right click context menu*

### When to use the browser vs the Desktop App for transfering files

| Task | Recommended |
|------|-------------|
| Quick look / browse the share | Browser (email link) |
| Small single-file download or upload | Browser *or* Desktop App |
| Folders, many files, large volume | **Desktop App** (ASC, resumable) |
| Rename / move / delete in place | Browser (or Desktop App Storage tools for operators) |

**Overall recommendation:** transfer using the Desktop App for day-to-day production transfers. Use the browser for convenience on single files and light management; browser folder ZIP / multi-file packaging is not available yet and may improve later.

## Secondary method — Desktop App GUI

Use the Desktop App when you need accelerated, resumable ASC transfers, large folders, or the advanced dual-pane **Transfer** tools.

### Installing the accsyn Desktop App

Follow [Install Desktop App](/desktop-app/).

### Downloading files (Desktop App)

1. Launch the Desktop App.
2. Sign in with the email address the share was sent to. You should see notifications for accessible items:

3. Click the green **Download** button.

*Note: If you dismissed notifications, open **Download** in the top area to launch the download tool.*

![](/assets/collaboration_access_app.png)

*Share notification and action buttons.*


4. Select which files and folders to download and the local destination:

5. Click **Download** to start the transfer (ASC via the Desktop App).

Monitor progress in **My jobs** at the bottom of the app — ETR, and clues if the disk is full or permissions/network fail.

### Upload files (Desktop App)

Launch the app, sign in, and click **Upload**:


Choose the file(s) and/or folder(s), set **Destination** to the shared folder, then **Upload**.

### Advanced mode — Transfer

If you are used to FTP clients, use the **Transfer** view:


Source on the left, destination on the right. Click the green arrow in the middle to start the transfer.

## Manage app

### Installation location

Default locations for standard users (no admin rights):

- **Windows** — `C:\Users\<user account>\AppData\Local\Programs\Accsyn`
- **Mac** — chosen by user; recommended: `/Users/<user account>/Applications`
- **Linux** — chosen by user; recommended: `/home/<user account>/.local`

If installed as administrator / with elevated privileges:

- **Windows** — `C:\Program Files\Accsyn`
- **Mac** — recommended: `/Applications`
- **Linux** — recommended: `/usr/local/accsyn`

### Data files location

- **Windows** — `C:\Users\<user account>\AppData\Roaming\accsyn\data` (under `%APPDATA%`)
- **Mac** — `~/Library/Application Support/com.accsyn`
- **Linux** — `/home/<user account>/.accsyn/data`

Elevated installs:

- **Windows** — `C:\ProgramData\accsyn\data`
- **Mac** — `/Library/Application Support/com.accsyn`
- **Linux** — `/var/lib/accsyn`

Hint: back up and migrate this folder when moving machines to keep login and client credentials.

### Log files location

- **Windows** — `C:\Users\<user account>\AppData\Roaming\accsyn\log`
- **Mac** — `~/Library/Logs/accsyn`
- **Linux** — `/home/<user account>/.accsyn/log`

Elevated installs:

- **Windows** — `C:\ProgramData\accsyn\log`
- **Mac** — `/var/log/accsyn`
- **Linux** — `/var/log/accsyn`

Hint: ZIP this folder and attach it when opening a support ticket for stability issues.

### Uninstall app

As a standard user:

- **Windows** — run `C:\Users\<user account>\AppData\Local\Accsyn\uninstall.exe`
- **Mac** — move the `.app` bundle to Trash
- **Linux** — remove the application folder

Elevated installs:

- **Windows** — run `C:\Program Files\Accsyn\uninstall.exe`
- **Mac** — typically remove from `/Applications`
- **Linux** — typically remove from `/usr/local`

*Note: The uninstaller does not remove data and log files; delete those manually if needed.*

## Troubleshooting

**I am not allowed to install apps on my computer**

You can still open the share from the email link in the browser for browsing and single-file transfer. For large folders and resumable ASC transfers, ask IT to whitelist the Desktop App, or use another machine (for example a personal laptop), then move files via USB if needed.

**Download turns red and fails (Desktop App)**

- Check free disk space on the destination drive.
- Whitelist the executable and allow outbound TCP from port **45190** upwards (ASC).
- Confirm the app can write to the download folder (or read files you are uploading).

**Browser download or upload fails**

- Confirm you have read (download) or write (upload) on the current folder.
- Try a single file; folders / multi-file browser packaging is not supported yet — use the Desktop App.
- Switch the transfer preference to the Desktop App if prompted for large sizes.

**Can I download from several machines?**

Yes. Access lasts until revoked. You may use the browser and/or install the app on as many machines as you need.

**Is the transfer encrypted?**

Yes. accsyn uses AES encryption (AES-128 by default). The Desktop App accelerates transfers with the proprietary [ASC](/whitepaper/) protocol — suited to large folders and many files.

**The Desktop App freezes or crashes**

Email [support@accsyn.com](mailto:support@accsyn.com) with log files attached (see log locations above).

Further questions: chat or [support@accsyn.com](mailto:support@accsyn.com).

**Related articles:**

[Collaboration](/collaboration/) — share folders with employees and external users.

[Hosts](/admin/hosts/) — automated deliveries and locally mapped shares.

[Python API](/developer/python-api/) — automate shares and ACLs.
