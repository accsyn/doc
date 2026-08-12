# Changelog

## Changelog

Back to support [main page](index.md).

CHANGELOG

(b=build)

v3.6-5 [26.06.24-29]

  MINOR FEATURES

     - [CORE/API] Introduced API rate limits and improved DDoS/abuse guard; sustained rate: 30 requests/s (burst: 60), max connections per IP: 100.

     - [CORE/APP] Ability to configure hook execution to be visible to standard users, changed default to be employees (was administrators only).

     - [CORE] Updated hook data, properly pass on task hierarchy.

     - [WEB] Create shared folders and homes, aligned grant access dialog with app.

     - [APP] Ability to perform file operations in source(download) file browser (rename, move, delete), if user has write permissions.

     - [WEB] Show delivery reminder dates on recipients, general improvements.

     - [PYTHON API 3.3.4] Documentation consolidated, aligned with support docs.

     - [DOCUMENTATION] Re-introduced internal settings documentation (https://support.accsyn.com/settings)

  BUG FIXES

    - [WEB] Fixed log CSV download bug.

    - [CORE] Fixed delivery ZIP compression delay bug.

    - [CORE] Fixed share code edit bug.

    - [WEB] Fixed standard user post invite bug.

    - [CORE/APP] Fixed bug where mapped share paths overwrite across app client and user server clients.

    - [CORE/APP] Fixed bug where files not could be pushed to/pulled from user mapped local volume (by env). 

v3.6-4 [26.06.10]

  MINOR FEATURES

     - [CORE/WEB/API] Set explicit permissions/rights on API keys.

     - [CORE/WEB] Improved and consolidated logging, show log entry device and geolocation data, download logs in CSV format.

     - [PYTHON API 3.3.2] Support for reading workspace and entity logs.

     - [WEB] User admin; All users tab (default), to improve search functionality. Click-to-open functionality for users(badges).

     - [WEB] Edit server/client enable/disable schedule.

     - [APP] Check if enough free space to download a delivery.

  BUG FIXES

     - [CORE/APP] Fixed internal database connection pooling issue.

     - [CORE/APP/WEB] Fixed bugs with assigning share to a queue.

     - [CORE/WEB] Fixed bug with inviting and granting employee access.

     - [APP] Fix rename/move folder bugs in delivery download browser dialog.

v3.6-4 [26.06.10]

  MINOR FEATURES

     - [CORE/WEB/API] Set explicit permissions/rights on API keys.

     - [CORE/WEB] Improved and consolidated logging, show log entry device and geolocation data, download logs in CSV format.

     - [PYTHON API 3.3.2] Support for reading workspace and entity logs.

     - [WEB] User admin; All users tab (default), to improve search functionality. Click-to-open functionality for users(badges).

     - [WEB] Edit server/client enable/disable schedule.

     - [APP] Check if enough free space to download a delivery.

  BUG FIXES

     - [CORE/APP] Fixed internal database connection pooling issue.

     - [CORE/APP/WEB] Fixed bugs with assigning share to a queue.

     - [CORE/WEB] Fixed bug with inviting and granting employee access.

     - [APP] Fix rename/move folder bugs in delivery download browser dialog.

v3.6-3 [26.04.19]

  MINOR FEATURES

     - [CORE/WEBAPP] Constrain API keys to one or more IP:s.

     - [WEBAPP] Workspace developer page, showing all issued API keys across all users.

     - [CORE/COMPUTE] New "compute\_avoid" setting, defining how to act on compute process failure when it comes to avoiding nodes.

     - [CORE] Support override & change queue for delivery/request/stream transfers.

     - [WEBAPP] Properly show site server usage on subscription/billing page. Further improved BYOS onboarding.

     - [APP] General improvements: better contrast, only bring message dialogs on top, improved grant user access bug, improved file browser address bar entry.

     - [PYTHON API] Support for reading and changing workspace and entity settings.

  BUG FIXES

     - [CORE/APP] Fixed bug where unconfigured site showed up as transfer party.

     - [WEBAPP/DELIVERY] Fixed bug where disabled recipient were not flagged properly.

     - [CORE/COMPUTE] Fix bugs when creating tasks beneath a parent task.

     - [VAULT] Removed orphaned media from delivery/transfer tasks.

     - [CORE/EMAIL] Fix email config exclude bug.

     - [APP] Fix main window split restore bug. Fix show all queues bug.

     - [APP] Fix bug with adding file to collection.

v3.6-1 [26.03.29]

  MAJOR FEATURES

      - [CORE/WEB] (Cloud workspaces) Instant web browser uploads and downloads without the standard job delays, with additional support for folder upload (drag-n-drop) and resume (download managers).

      - [PYTHON API] Major update to v3.2 - full support for delivery subsystem and site, added support for more entities(job & share raw entity types deprecated). Added full coverage test suite. API query language now supports 'in', 'contains' and 'matches'(regexp) operators.

      - [WEB] Support for resource files (png/jpg/jpeg) and configure workspace logotype (branding).

  MINOR FEATURES

      - [CORE] Improved backend performance and security, consolidated task creation factory and updated runtime to Python 3.11. Introduced pubsub (RabbitMQ) subsystem.

      - [APP] Consolidated UI for cloud workspaces, to align with BYOS workspace presentation. Larger work area with optimised menu, split job into type tabs.

      - [APP] Improved access grant widget, possibility to grant access to a user within Volume context from Share menu. Overall GUI improvements and optimisations.

      - [WEB/ONBOARDING] Select between cloud and BYOS workspace, with a proper BYOS setup wizard that has to be completed before workspace is activated.

      - [MEDIA VAULT] Nightly check for media and title existence, reflected on Vault titles page in app. Can be manually triggered from new media vault web admin page.

      - [COMPUTE] Support metadata on nested tasks, merged and supplied with engine execution.

      - [CORE/TRANSFERS] Improved default names of delivery transfer jobs.

      - [APP] Allow employees to read compute process service logs. Improved process log with additional initial metadata from execution.

      - [WEB] Improved storage view; show/hide disabled shares. Reflect user status properly (disabled/inactive).

      - [WEB] Improved delivery download page, compression (ZIP) status & single file download.

      - [CORE/WEB] Sites and Queues can be given names that does not have any constraints, API 'code' attribute is preserved and must be unique as before. Names will from now on be presented in UI:s instead of code.

  BUG FIXES

      - [WEB] Geolocation render bug.

      - [APP/CORE] Fixed bug where job log migrated process log entries were showing wrong date, dates in app are now logged with full timecode information.

      - [WEB/DELIVERY] Duplicated files on upload requests are not handled (replaced with latest).

      - [APP] Fixed bug in file browser where right click/context menu context were not taking focus file into account. 

      - [APP/SERVER] Fixed bug where compute logs took a long time to update.

      - [APP/CLIENT] Fixed bug where first WAN connection failure were not logged.

      - [APP] Fixed bug when app tried to access user disabled workspace on login.

v3.5-2 [26.01.04]

  MINOR FEATURES

      - [CORE/WEB] Possibility to add more storage volumes for cloud workspaces, enables workflows were employees can work on separate storage areas.

      - [CORE/WEB] Edit clients - change site.

      - [CORE] New 2026 pricing support - measure elevated user and compute server count on a monthly basis.

      - [CORE/WEB] Improved storage admin page - sort share table and perform share batch actions.

      - [CORE/WEB] Improved server admin page, categorising server into roles. Provide BYOS licensing info.

      - [WEB] Improved billing/signup page with new 2026 pricing info - elevated user and compute server usage count.

      - [APP] Improved folder share dialog and ACL/access grant widget. Polished file browser - consolidated refresh button.

    BUG FIXES

      - [APP/FILEBROWSER] Fixed bug in filebrowser were all shared folders not were annotated.

v3.5-1 [25.12.15]

  MAJOR FEATURES

      - [WEB] Legacy AngularJS v2 admin frontend removed, and fully replaced with modern v3 React frontend. Tutorial migration in progress.

      - [APP] Improved folder share and grant access dialogs, providing both shared folder creation and user access grant in one operation.

      - [CORE/LICENSING] Updated pricing for cloud plans, added 'Essentials' plan for small teams and trials. Support BYOS trials.

      - [CORE/LICENSING] Added fee for additional elevated users (role: admin & employee), not affecting existing subscriptions.

      - [CORE/WEB/APP] Improved UI response times facilitated by multithreaded GraphQL endpoint.

      - [API] Changed build mechanism from Setuptools to Poetry.

      - [SUPPORT] Finalised migration of legacy v2 admin pages, tutorial migration in progress.

  MINOR FEATURES

      - [APP/CORE] Measure GPUs and their usage (NVidia), show in app toolbar.

      - [APP] Fix app scaling issues on Windows 11, support providing scaling factor through command line option and configurable in preferences.

      - [APP/BROWSER] Have recent locations as tab instead of part of locations.

      - [ASC/APP] Improved error and warning transfer messages.

      - [APP] accsyn:// protocol driven login, replacing web server based login (kept as legacy option). Mitigates issues with browsers and firewalls blocking app auth callbacks.

      - [APP/TASK LIST] Improved visibility on narrow app windows - now shows destination path beneath each task with additional preferences for showing (full/accsyn) source path.

      - [APP/JOB MONITOR] Improved filtering, with direct access to transfer/render type and and upload/download direction filters. 

      - [SERVER INSTALLER] Properly preserve daemon/server login user during update, also support install only (no authentication) for restoring config manually.

      - [CORE/COMPUTE] New 'queue\_interrupt\_policy\_compute' affecting compute jobs only.

      - [CORE/WEB] Support for renaming workspace.

      - [CORE/WEB] Support volume path overrides at sites.

      - [CORE/DELIVERY] Browse folders within a delivery, also support download of subfolders and files beneath a folder.

      - [WEB/COMPUTE] Farm page rendering available compute servers, their lanes and assigned engines with process status.

      - [WEB/JOBS] Jobs page rendering all transfer/compute jobs with tasks and possibility to edit job attributes and settings. 

      - [WEB/JOBS] Added support for task previews, facilitating EXR>JPG web preview workflows with render farm setups.

      - [COMPUTE] Support executing progress for compute jobs.

      - [WEB ADMIN] Basic volume and share access editor.

      - [VAULT/WEB] Show media metadata in the right hand side drawer.

      - [COMPUTE SCRIPTS] Support registering task previews (JPGs). Define log policies. Support storing additional compute metrics in runtime.

  CHANGES

      - [APP/JOB MONITOR] Show deliveries moved to filter dropdown menu.

      - [APP/SUBMIT] Default is now to NOT add files as a new task to daily download/upload jobs, but instead create a new job each time.

      - [CORE/COMPUTE] Tags are now compute 'pools', configurable from workspace settings. Added 'weak' and 'dedicated' pool inclusion rules for compute jobs.

      - [API] Renamed 'domain' parameter to 'workspace' in Session constructor.

  BUG FIXES

      - [APP/SERVER] Fixed bug where volume write test directory were not deleted.

      - [APP] Fixed bug were a delivery could not be downloaded with app if already running.

      - [APP] Fixed bug causing a 'Client not found' error during delivery download.

      - [CORE] Fixed bug when pausing a compute job that is being dispatched to many servers at the same time.

      - [CORE] Fixed bug when paused status was not taken into account on submit.

      - [CORE] Fixed bug where job creator did not get email notifications on site transfers.

      - [CORE] Fixed geolocation WAN IP lookup bug.

      - [CORE/ASC] Fixed bug when transfer errors and warnings were not propagated from process log to job log.

      - [CORE] General bug fixes and internal performance optimisations.

      - [CORE/API] Properly support compute transfer child (dependency) tasks submitted through API.

      - [WEB ADMIN] Fixed exclude bug in email settings.

v3.4-3 [25.09.21]

MINOR FEATURES

     - [WEB] User developer page, with personal API key creation. Admins can now audit user API keys from user edit page.

     - [WEB] New Farm view for workspaces having engines deployed to compute servers, showing server metrics and engine execution. 

     - [WEB] Possibility to configure lane engines from server edit page.

     - [WEB] Improved jobs view with drag-n-drop for repositioning and/or re-queueing jobs. Improved job view with task selections and batch modifications. 

     - [WEB] Small improvements and overall bug fixes.

     - [APP/WEB/CORE] Prevent (default) volume from being accidentally deactivated;

     - [APP/DAEMON] Measure hardware metrics on launch - System, CPU and GPUs.

     - [APP/JOB] Bucket size input has more large value options.

     - [ENGINES/APP] Support for Unreal Movie Render Queue jobs.

BUG FIXES

     - [APP] Fixed image scaling issues on windows.

     - [APP/LIST WIDGET] Fixed CTRL+select bug on Windows.

     - [APP/LIST WIDGET] Right click on Windows now clears current selection and selects the clicked item.

     - [APP] Fixed wrong client enable/disable toggle switch orientation.

     - [CORE] Bug fixes and improvements.

     - [APP/BROWSER] Fixed bug where local mapped share path pasted in address field did not translate properly. 

v3.4-2 [25.09.07]

MINOR FEATURES

     - [WEB] Ported remaining legacy admin pages.

     - [WEB/ADMIN/USER] Improved invitation experience. Indicate if user has not signed up their personal account yet.

     - [WEB] My jobs indicator in upper right corner.

     - [WEB/SUBSCRIPTION] EU VAT# support on Sign Up. Cancel subscription.

BUG FIXES

     - [CORE] Fix Collection file relative path display bug with app.

     - [CORE] Fixed bug were user could not be deleted due to online/running client(s).

v3.4-1 [25.08.24]

MAJOR FEATURES

     - [CORE/APP/VAULT] Media quality and validation, with calculation and validation or MD5/SHA-1/SHA-256 user provided checksum. DCP validation using PKL package verifier.

     - [CORE/APP/VAULT] Allente streaming platform VOD exporter, reachable from the media processor.

     - [WEB] Compute engines and hooks config ported from legacy admin pages. New engine Python code editor with syntax highlighting.

MINOR FEATURES

     - [APP] Friendly hints/About dialog shown at first time use.

     - [APP] Tray icon now adheres desktop/operating system theme.

     - [WEB] Administrate sub menu beneath Workspace button, preventing menu to grow too big.

     - [APP] Overall styling alignments and improvements.

     - [WEB] Migrated clients from legacy admin pages. Clients are also shown when auditing a user.

     - [APP/BROWSER] Recent section are now expandable/retractable.

     - [APP/BROWSER] In Download/Upload mode, the destination side is now presented even if source files not chosen. Mirror paths is properly suggested on (re-)selection.

BUG FIXES

     - [ASC/TRANSFERS] Fixed bug were TCP socket count config not were taken into account during transfer. 

     - [CORE] Fixed bug with timezones differences not being handled properly.

     - [WEB] Fixed bug with transfer default settings not being provided on queue and volume.

     - [APP/BROWSER] Fixed bug in Storage view where collection ACLs were not properly shown.

     - [APP/BROWSER] Fixed bug with double-click to enter folder.

     - [APP] Fixed bug with mirrored uploads using locally mapped source volumes.

     - [APP] Fixed bug in job submit where selected queue did not apply.

     - [WEB] Bug fixes and improvements.

     - [APP/VAULT] Fixed bugs with showing media info on right click. Added button in title banner to show title info. 

     - [APP/BROWSER] Fixed bug in download showing upload-only shares.

     - [APP/BROWSER] Fixed bug were size calculation did not work on right click unless file selected.

     - [APP] Fixed bug in check for updates were new builds/patches were not picked up.

v3.3-3 [25.07.01]

MINOR FEATURES

     - [APP/VAULT] Unified clip and still image extractor, integrated in the player with clip list on right hand side improving usability, with real time clip updates.

     - [APP/VAULT] Clip extract; possibility to add and remove delivery recipients.

BUG FIXES

     - [APP] Restore proxy server (client "proxy\_server" setting) functionality lost during v2 migration.

     - [APP/VAULT] Fixed bug were title media were not loaded when coming from title files view.

v3.3-2 [25.06.25]

MAJOR FEATURES

     - [APP/CORE] New job repeat attribute, enabling periodic (hourly, daily, weekly & monthly) rewind and retry of finished (done/aborted) jobs.

     - [APP/VAULT] Clip and still image extraction available in processor, high quality (ProRes 422HQ/TIF) and medium (H264/JPG), running a transcode job on farm delivering or storing the result.

MINOR FEATURES

     - [WEB] Improved Linux downloads with debian, rpm and compressed artifacts.

     - [APP/STORAGE] Allow volume root folder to be shared multiple times.

     - [APP/STORAGE] Improved access info panel. Upon sharing a folder, user is asked if want to grant access. Only auto refresh file listings every 5min (was 1min)

     - [APP/JOB EDIT] Improved and fixed bug with editing job attributes having pull down selects.

     - [WEB] Only show last page when auditing/viewing logs, to improve performance on large log datasets.

     - [WEB] Queue management migrated from legacy admin pages.

BUG FIXES

     - [APP/JOB VIEW] Fixed task pagination bugs.

     - [APP/JOB VIEW] Removed debug logging that could affect GraphQL performance.

     - [CORE] Fixed bug where downloads had 0 bytes size reported in email.

     - [CORE] Fixed bug with ensuring/reviving inactive/archived users.

     - [CORE] Fixed bug when accessing home folders.

     - [VAULT/CORE] Fixed bug when ingesting media on Windows.

     - [VAULT/APP] Fixed proxy play seek bar precision bug on Windows.

v3.2-3 [25.05.20]

MINOR FEATURES

     - [APP/VAULT] Cache thumbnails on local disk to improve loading times, cleared after 6 months.

     - [APP/VAULT/PLAYER] Show elapsed time and added volume control.

     - [APP/BROWSERS] Auto refresh of file & media listings.

     - [APP/VAULT] Media are now grouped by content and category tag. Filter option button were this can be turned off.

     - [APP/VAULT] Show stream proxy status on media.

     - [APP/VAULT] Show and go to title when browsing media in global context.

     - [APP/VAULT] Go to title when browsing storage.

     - [APP/BROWSER] Do not show right hand side destination options until source file(s) are selected.

     - [APP/DELIVERY DOWNLOAD] If download path configured, user is still prompted and can browse to custom location.

     - [APP/BROWSER] Can share folders while browsing another shared folder.

     - [APP/BROWSER] Show workspace name in upper left area if no logo.

BUG FIXES

     - [APP/JOB EDIT] Fixed bug with queue edit, and real time updating.

     - [APP/JOB VIEW] Bug fixes and optimisations with task list and job progress bar.

     - [APP/DELIVERY DOWNLOAD] Fixed bug where configured path did not apply.

     - [APP/VAULT] Fixed bug where media were not updated on custom tail tag edit.

     - [APP/VAULT] Fixed bug were media proxy progress indicator was not hidden when finished.

     - [APP/VAULT] Fixed bugs when editing title, specifically title cover image and banner.

     - [APP/BROWSER] Fixed UI bug in path history dialog, aligned it with other dialogs.

     - [APP/JOB VIEW] Fixed hook exec start & end date ClassCast exception.

v3.2-1 [25.04.13-25]

MAJOR FEATURES

     - [CORE] Proper MFA support; Multi-Factor Authentication (MFA) is now supported with Google Authenticator or similar app, enabled through the user profile on the web. Fallback on standard email 2FA for users without MFA enabled. Security settings on the web.

     - [APP/VAULT] New "Files" view being the default view, making it more like a standard file and folder based MAM. The file browser now displays thumbnails and can view proxies.

     - [APP/VAULT] New merged media upload & ingest tool making it easier to upload and ingest media.

     - [APP/VAULT] Display thumbnails and ability to play video proxies on the web.

     - [APP/VAULT] Metadata side panel showing metadata for the selected media, tag editor and proxy information.

     - [MEDIA LAB] New "Orders" page on the web displaying media lab orders, with ability to create new orders and manage existing ones.

     - [APP/VAULT] Title types with ability to create "local" titles not bound to an IMDB ID. Ideal for general media titles and projects. Title type filters in titles view.

MINOR FEATURES

     - [WEB/USERS] Improved user administration with sortable table and action bar allowing multiple user edit. Brought back user compute enable setting ability.

     - [APP/STORAGE] Show 5 recent items (volumes, shares,..) accessed in the file browser.

     - [APP/STORAGE] Revamped file browser with the new action bar - making it much more clear what files are selected and what operations can be performed on these.

     - [APP/STORAGE] Move multiple files at the same time.

     - [APP/STORAGE] ACL info panel now hides employees and admins by default, collapsable.

     - [APP] The account/email button in upper right corner now displays an improved context menu on click.

     - [WEB/STREAMING] Improved player, removed update glitches. Subtitles now updating in real time.

     - [APP] Optimised and polished job listing, progress bar and job view.

BUG FIXES

    - [APP/FILE SHARING] Users can now see files while selecting destination folder within an upload session.

    - [APP/JOBS] Fixed sorting bug with paused jobs.

    - [WEB VAULT] Fixed bug were long delivery names overflowed.

    - [APP/JOBS] Fixed job edit queue bug.

    - [APP/SERVERS] Fixed bug where expanded server lanes could not be modified.

    - [WEB/CORE] Fixed bug were user last logged in date were not updated.

CHANGES

     - [APP/VAULT] Default video proxy standard is now 1280x720 @ 2 Mbit.

     - [APP] The workspace button is not only displayed if user has access to more than one workspace.

v3.1-5 [25.03.11-13]

MINOR FEATURES

  - [CORE/VAULT] Generate image and video proxies with thumbnails.

  - [APP/VAULT] Show thumbnails for media, view image and video proxies.

  - [APP/VAULT] New Subclip and Still image extraction lab order, supporting multiple clips and images.

  - [APP/CREATE ACL] Search users.

  - [APP/VAULT] Show selected media info & metadata in top banner.

  - [APP/VAULT] Improved media process dialog.

  - [CORE/VAULT] Create local titles / projects, not bound to an IMDB ID.

  - [CORE/VAULT] 5 most recent opened titles displayed on top.

  - [CORE/VAULT] Metadata panel on the right hand side.

  - [CORE/VAULT] Cleaned up media list, shortcuts and tag filter panel.

BUG FIXES

  - [DELIVERY] Fixed Nullpointer exception bug when delivering with app.

  - [APP/BROWSER] Pasting paths in address field not converted when in upload mode.

  - [APP/BROWSER] Fixed bug in transfer were mirror paths were not pre-selected.

  - [APP/SERVERS] Properly show and modify expanded lanes.

  - [APP/CREATE ACL] Properly show subfolder info.

  - [APP/LOGIN] Hide anonymous account.

v3.1-4 [25.02.21]

MINOR FEATURES

  - [APP/VAULT] New Lab order dialog were the work with associated attributes can be defined.

  - [APP/VAULT] Title group by creation date.

  - [APP/BROWSER] Improved storage access info panel, now grouped by path with possibility to revert in prefs.

  - [APP/BROWSER] Paths pasted in address field are converted to accsyn path notation if recognised.

  - [APP] Undo functionality in text fields.

  - [WEB] New "Vault" menu, redirecting users to install app to manage vault.

  - [WEB] Upload requests created from app now have the destination folder displayed properly.

  - [WEB] Group deliveries by not actioned and actioned (all recipients have taken action), show progress.

BUG FIXES

  - [APP/VAULT] Fixed bug where title view were not updated after banner and cover edit.

  - [APP/VAULT] Cleaned title folder name, not allowing non-US characters.

  - [APP/MONITOR] Fixed bugs with job sorting.

  - [APP/BROWSER] Remove transfer destination dropoff option.

  - [APP/BROWSER] Fixed bug were access info panel was not updated.

  - [APP/BROWSER] Fixed bug when selecting user during ACL/access grant, were disabled users existed. Anonymous user now hidden.

  - [WEB] Prevent download of upload request if now files uploaded yet. Remove speed indicator on streams.

  - [WEB] Fixed accsyn logo on legacy admin pages.

  - [APP/INSTALLER] Fixed bug in daemon installer were ID input were hidden if ACCSYN\_API\_KEY env set.

  - [APP] Fixed bug with transfers were changes in mapped shares for user endpoints were not updated properly.

CHANGES

  - [APP/VAULT] TITLES tab is now named VAULT and put first.

  - [APP/VAULT] Moved title delete button.

v3.1-3 [25.02.04]

MINOR FEATURES

  - [WEB/CORE] Anonymous delivery support - send deliveries, upload requests and video streams to recipients without requiring them to have an accsyn account.

  - [APP/STORAGE] Ability to download and upload files in the storage browser.

  - [APP/UPDATES] Ability turn off auto updates when prompted and in settings. Also configurable by setting environment variable ACCSYN\_SKIP\_UPDATE\_CHECK=1.

  - [APP] Improved status and progress bar updates.

  - [APP] Improved workspace switcher.

  - [WEB] Show IP & geodata for delivery recipients/jobs.

  - [LAB] accsyn Media Lab services released officially (https://accsyn.com/lab)

BUG FIXES

  - [WEB] Fixed bug where users could not abort their downloads/uploads on a delivery.

  - [APP] Fixed bug in settings dialog causing a NullPointerException on toUpperCase().

  - [CORE] Memory optimisations.

CHANGE

  - [CORE] Decreased background share cache updater to only scan 2 folders deep instead of 3 (workspace default 'share\_cache\_scan\_depth' setting)

  - [APP] Allow users to logon to app even if they do not have access to shared items such as folders, homes or collections.

v3.1-2 [25.01.26]

MINOR FEATURES

  - [APP/BROWSER] Local share cache, enabling instant file listing for previously visited storage locations. Not accessed paths expires within 2(two) months.

BUG FIXES

  - [APP] Fixed progress bar update for jobs and for jobs not entering finished state when done.

  - [APP] Fixed bug in workspace job listing were queues were not shown.

  - [WEB] Fixed bug were workspace not could be deleted.

v3.1-1 [25.01.24]

MINOR FEATURES

  - [APP/VAULT] New video proxy process, creating a 1Mbit SD preview mp4 file for previews in app and web.

  - [APP/SETTINGS] Ability to configure if downloads/uploads should be appended to recent daily transfer job or not.

  - [APP/SETTINGS] Ability to configure if folder metrics should be fetched while browsing shares (performance improvement).

  - [CORE] Introduced "vault" accsyn product, replacing previous "title library" notation. Documentation updated.

  - [APP/CORE] Tagging; Added IMAX category. Added Norsk Bokmål language.

  - [WEB] Outbound/Requested/Streams; Highlight unset deliveries in list.

  - [WEB] Send a remainder to recipients that has failed or aborted.

  - [WEB] Improved welcome dialogs.

  - [CORE] Polished mail, updated footer with relevant information, fixed graphical bugs.

BUG FIXES

  - [APP/VAULT] Media logger; Fixed bug were hidden tags were suggested (subtitles also got a subtitle tag). Improved DCP tagging.

  - [APP] Ability to view media transcode job logs, for troubleshooting within accsyn hosted farm.

  - [APP] Fixed NullPointerException bug on download through browser.

  - [APP] Fixed daemon/service updater bug on Windows.

  - [APP/VAULT] Fixed bug where media delivered from storage did not get metadata correctly.

  - [APP/VAULT] Fixed double scrollbar bug, made scrollbar thumb brighter.

  - [APP/VAULT] Fixed bug where titles is grid got cut off.

  - [APP] Fixed bug where upload requests could not be created.

  - [WEB] Fixed light mode styling bugs with app download page.

v3.1-0 [25.01.19]

MAJOR FEATURES

  - [SUPPORT] Brand new set of guides replacing the old documentation deployed at https://support.accsyn.com. Help links within web app and desktop app, pointing to the new guides per topic.

  - [CORE/WEB] Redefined pricing to be more dynamic having one permanent 1TB Cloud storage plan with all features included, with additional per-TB cost billed monthly.

  - [APP/STORAGE] Realtime GraphQL fetch of shares and ACLs for access info pane.

  - [APP] New improved ACL editor allowing quick share of a folder/collection to multiple users.

  - [VAULT/STREAMING] Support for subtitles with VOD streaming.

MINOR FEATURES

  - [APP/VAULT] Polished and optimized title and media view.

  - [APP] Optimised monitor when minimised - only fetch entity counts.

  - [APP] Show recipients and their status on deliveries.

  - [APP/VAULT] Cache proxy images on local disk for faster load.

  - [APP/STORAGE] Search shares box.

  - [APP/DELIVERIES] Show recipients and their action status on deliveries/upload requests.

  - [APP/VAULT] Media logging; Suggest dates in filenames as tail tag. Suggest image filename as tail tag to support large amount of images to be ingested.

BUG FIXES

  - [WEB] Restore publish functionality that were broken in 3.0.

  - [WEB] Fixed bug when choosing file transfer preference (browser or app transfer) causing page to flicker and options not selectable.

  - [APP] Fixed date display discrepancy bug.

  - [APP] Fix modal dialog bug were prompts came behind the dialog, for example make directory input on download dialog.

  - [APP/VAULT] Fixed bug where title cover could not be restored to default.

  - [BACKEND] Thread safe backend logging, to prevent deadlocks when writing NFS log storage (Related to 1h outage 25.01.07)

  - [CORE/APP] Fixed bug in storage browser with shares having different name than (API) code attribute. Fixed so share and volume names can be entered in the address field.

  - [APP/INVITE USER] Fixed bug with giving employees access to all volumes.

  - [APP] Fixed bug in task pagination, could not step forward. Page size is now remembered as a prefs.

  - [APP] Fixed bug when finished jobs did not vanish in the job list/queue, if only one left.

  - [CORE] Fixed bug when transfer tasks within a compute job did not autoretry directly.

  - [CORE/APP] Fixed bug on app login when cached workspace access state were provided.

  - [APP] Fixed bug when job progress bar did not update.

  - [APP] Fixed bug when not could search finished jobs on user ident (email).

  - [APP/WEB] Fixed bug when installing a new Host and two pending were added.

  - [APP] Fixed bugs in file browser when entering a share path in address field.

v3.0-26 [24.12.19]

MINOR FEATURES

  - [APP/MEDIA] Title covers, with additional banner, are now proper web proxies and editable.

  - [APP/MEDIA] Deliveries and streams are now collected in a "cart" before being submitted, to be ported to Storage view.

  - [APP/MEDIA] Web streams can now be mixed with standard file and folder content with the delivery.

  - [FRONTEND/ADMIN] Server admin pages with server installation, edit and delete.

  - [APP/MEDIA] Media probe on log.

  - [APP/MEDIA] New batch processor, initially supporting re-probe of media.

  - [APP/MEDIA] Refurbished media title creation and edit; now supports import of existing accsyn title, title folder template creation, banner removal and title cover reset.

  - [APP/MEDIA] Titles; new "End credits" attribute, on the form "hh:mm:ss".

  - [APP/MEDIA] Fixed bugs for employee role user when logging and managing media.

  - [APP] Cache resolved hosts and user data, in case master/accsyn.io is down.

BUG FIXES

  - [APP] Couldn't sort local file browser, rename and move not enabled.

  - [APP] Storage view; sometimes the browser splits wrong on shown.

  - [APP] File browser; Prevent “..” in file list to be selectable and actionable.

  - [APP] Fixed bug where progress bar not was updating, now refreshes every 2s overall.

  - [APP] Avoided nodes shown as ID.

  - [APP] Hosting/ffmpeg; fixed bug when retrying forever on failure, also is aborted 3 times before starting

  - [CORE] Transfer append to existing job; size not updated on job. Aborted job failed tasks are retried, instead put on hold.

  - [APP] Fixed issue with when appending to a finished job -  set tasks that not are done to excluded to prevent unwanted retries. Also retries finished jobs, and do not append to paused jobs.

  - [APP] List widget, right click on windows (mouse) does not work. Also optimized column widths.

  - [APP] Task list; buckets gone, also check realtime console log.

  - [APP] Delivery downloads; source displays with workspace icon instead of delivery name.

  - [APP] Transfer source/dest; Different icon for user clients running as daemons.

  - [APP] Transfer pull; when changing client, the exposed shares were not updated.

  - [APP] Make sure “No connection could be made to accsyn” notification does not get stuck.

  - [APP] Submit; no queues were loaded. Also fixed bug when creating share when no queues were loaded.

  - [CORE] Not storing duties file listing in client data, have it separate in memory.

  - [APP] Improved Storage sharing view when a collection is selected.

  - [APP] Job task list, showed -1 count.

  - [APP] Job view status footer showed null instead of user.

  - [APP] Fixed finished job pagination and job view tasks pagination.

  - [APP/DAEMON] Made sure log is rotated continuously, not only on startup. Increase log file size limit to 50MB.

  - [APP] Fixed mirror paths bugs with local mapped volume for standard users.

  - [APP] Fixed bad popup menu separator styling on Windows.

  - [APP] File browser; Optimized listing of huge folder contents.

  - [APP] Create share; Fixed bug where code generate did not work, also fixed bug where "null" was in the title when editing.

  - [CORE] Make sure invitation email is sent out when an admin is invited to workspace, or when a folder/collection is shared to a an employee/standard user.

  - [APP]  Fix transfer destination user server icon bug.

  - [APP] Fixed bug were client log got full of " Cannot find duty to remove" messages.

  - [APP] Fixed bug in job monitor were tab buttons could grow to twice their height.

  - [APP] Fixed transfer bug where files could not be modified on receiving end.

  - [APP] Fixed bug where login token not were saved in memory on login.

v3.0-24 [24.11.24]

MAJOR FEATURES

  - [FRONTEND] User>Hosts; Show running clients for each host, ability to install new daemon client to facilitate 24/7 push/pull to locally mapped shares/volumes.

MINOR FEATURES

  - [ASC/CORE] Only log repeating process output every 15s to the job log, to prevent it from blowing up.

  - [APP] Only show relevant client destinations (user exposing their local mapped shares, for push/pull transfers), filter out duplicates.

  - [APP] Detect privileged windows install on update.

  - [APP] Polish job listing; Polish file browser view.

  - [APP] Bring back standard and advanced submitter.

  - [APP] Https transfer server set keep-alive to true.

BUG FIXES

  - [APP] Fixed bug where mirrored paths were not picked up correctly.

  - [APP] Fixed transfer bug on mac where 'null/Contents/MacOS/accsyn' were picked up as executable path.

  - [APP] Fixed bug where clients running with local exposed shares did not show up as an selectable destination.

  - [APP] Remove client if register fails.

  - [APP] Fixed bug when trying to get token with refresh token on expiry.

  - [APP ]Longer double click delay.

v3.0-22 [24.11.18]

MAJOR FEATURES

  - [APP/CORE] Support for granting and revoking employee access to volumes.

  - [PYTHON API] New release 3.0.0 supporting accsyn 3.

BUG FIXES

  - [APP] Fixed bug where app closed directly on launch on a new system.

  - [APP] Fixed bug where users with employee role could not logon to the app.

v3.0-20 [24.11.15]

MAJOR FEATURES

  - [CORE/MEDIA] Support a new type of delivery - 'stream', that contains one or more streamable media files having HLS proxies playable in the browser. Can be combined with additional files for download as a standard delivery.

  - [CORE/HOSTING] Central ffmpeg transcode farm, available to all cloud hosted workspaces for transcode of media and their proxies.

MINOR FEATURES

  - [APP] Settings>Mapped shares; Clients affected by share mappings are listed.

  - [APP] Transfer; Expose transfer append toggle button below middle submit button. Remember setting.

BUG FIXES

  - [APP] Collection file add; Fixed bug.

v3.0-19 [24.11.08]

MINOR FEATURES

  - [APP] Improved file browser to align with Collection/Media browser.

  - [APP] Create multiple user API keys in user settings.

BUG FIXES

  - [APP] Share creation; Fixed bug where GUI did not update after creating a share.

  - [APP] Improved Storage view - sharing info.

  - [APP] Fixed bug in User invite where standard user could not be invited.

v3.0-18 [24.11.05]

MAJOR FEATURES

  - [CORE] New delivery subsystem; accsyn v3 features a new delivery system driven by https://accsyn.io - our brand new web application deprecating the current accsyn web interface. Delivering large content is now smoother than ever integrating the desktop app with the browser experience, still allowing content to be downloaded in the browser - with no practical file size limits. Content can be delivered both from your shares as before, or from a temporary folder that gets wiped when delivery expires.

  - [CORE] Upload requests and accelerated browser uploads; New in v3 is the ability to create a "reversed delivery" - ask users to upload contents to a temporary folder or to a folder on one of your shares. On top of that, we have written an accelerated browser uploader engine splitting and sending large files in chunks multithreaded with file resume functionality.

  - [CORE] File collections; You can now create a new type of share - collections, containing any files and/or folders from your accsyn storage, and share them with your users. Collections are not bound to a folder on disk, and can be seen as a collection of file links pointing to your files. With that, what was previously named a "share" is now a "Shared folder".

  - [CORE] Desktop app optimized; The desktop app has been rewritten to utilize the new accsyn GraphQL backend protocol, facilitating vast improvements in speed and responsiveness The app also supports SSO, enabling seamless access to all your workspaces without the need to close the app.

  - [HOSTING] Cloud hosted storage; In v2, BYOS was the only option. Now with v3, you can sign up for a workspace where we host the storage and the server - with reasonable pricing and high integrity within our ISO 9001/14001/27001 certified premises. The signup process has been revamped, starting with a cloud storage workspace that later can be converted to BYOS.

  - [SERVICES] Media lab services; With our cloud storage, we provide a wide range of professional media lab services such as title and media ingestion, mastering, DCP authoring, screenings, Q/C, color grading, DIT, post/VFX and tons of other DI work. And of course, if you are a BYOS customer you can still use our services in a hybrid setup.

  - [APP] Hosts replacing User servers; Previously you as a end user could install accsyn as a server running in the background accepting deliveries for a specific workspace, now with v3 you can install the accsyn daemon to accept deliveries for an user account - accepting automated 24/7 deliveries coming from any workspace.

  - [LICENSING] Licensing updates; What previously were our standard licensing are now called "BYOS" and are now licensed and billed per server and type - "storage", "site" and "compute", still with optional premium support as an add-on. The compute add-on has been removed and is unlocked for free when purchasing one or more compute server licenses. Find more information at accsyn.io.

  - [JS] Javascript API; With v3 we provide a JavaScript API allowing you to initiate and commence file transfers within your own web or backend(NodeJS) application.

MINOR FEATURES

  - [APP] "Send" view has been replaced with the new "Storage" view, giving a much better overview over shares and who have access to them.

  - [APP] Removed support for sending and receiving deliveries in app, but you can select files in the Storage manager and create a delivery from there concluding it at accsyn.io. With that, the app is primarily used for running in the background transferring deliveries, with the GUI designed for managing and access storage, render, publish and detailed monitoring.

  - [APP] The new "Transfer" view is now were you initiate arbitrary transfer between your sites, and users with mapped local shares (user servers deployments).

  - [APP] Deliveries and upload requests are managed at accsyn.io, but you can still view the deliveries and all jobs involved in the app job monitor.

  - [APP] Transmit job mechanism have been removed, as "Send" view were remove. It has been replaced with the new delivery system driven from accsyn.io.

  - [APP] With the introduction of Collections, Root shares are now called "Volumes", shares are called "Shared folders" and user shares are named "Homes". No changes are made to the API, you can still use the standard accsyn path notation "share=<id or code>/<path>".

  - [CORE/API] Shares now can have a human readable name that does not need to be workspace unique. Accessible as "name" through the API.

  - [CORE] Compute/render apps are now called "engines", Python scripts will need to be refactored. Please refer to our public Github compute repository for reference. The compute/render addon is not free and included when you purchase compute server licenses.

  - [APP] Transfer log are now appended to the job log to make it easier to understand and get the full picture.

  - [APP] With the new SSO login backend, API key's are now only used for API access and not for login. Previous API keys have been migrated to the workspace user and are now unique per user and workspace.

BUG FIXES

  - [APP] [APP] Flip file browser sorting arrows

  - [WEBAPP] Fixed bug where boolean setting indicator buttons were oriented the wrong way.

  - [APP] Improved client lock file handling - check if PID is running and not prevent start if gone.

  - [APP] Fixed bugs in finished jobs - retry button did not work

v2.7-9 [24.04.07]

FEATURES

  - [APP] Invite button in main menu.

  - [CLIENT] Properly log exceptions occurring during transfer/process init, for example disk permission problems.

BUG FIXES

  - [CORE] Fixed share cache performance issue.

  - [APP] Flip file browser sorting arrows

  - [WEBAPP] Fixed bug where boolean setting indicator buttons were oriented the wrong way.

  - [CORE] Fixed bug where retries from failed connection attempts could get stuck on a previously successful port.

  - [APP] Improved client lock file handling - check if PID is running and not prevent start if gone.

  - [APP] Fixed bugs in finished jobs - retry button did not work

v2.7-8 [24.02.04]

FEATURES

  - [APP] Web delivery can now be submitted to multiple recipients, using a whitespace( ) separated list.

  - [APP] Asks before aborting web deliveries.

BUG FIXES

  - [CORE] Properly delete ACLs when changing a standard user to be employee or admin

  - [CORE/FRONTEND] Improved audit of ACL creation, edit and removal

  - [APP] Properly log out user when client/desktop app is closed

  - [WEB DELIVERY] Fixed bug causing web delivery of multiple files (ZIP) were not uploaded.

  - [WEB DELIVERY] Fixed bug causing web delivery to be uploaded to the wrong cloud path.

  - [WEB DELIVERY] Fixed bug causing web delivery of multiple files have zero size.

  - [WEB DELIVERY] Fixed bug in app when choosing a month or longer expiry time.

  - [CORE] Fix bug when opening a send in browser, involving entire share; Remove 'Standard share:' prefix for default job name.

  - [APP] Fixed bug when checking stale lockfile PID, that it belongs to accsyn executable.

  - [APP] Fixed bug in web delivery send were accsyn delivery elements were not hidden.

  - [APP] Job view; abort button now enabled.

v2.7-7 [24.01.07]

MAJOR FEATURES

  - [CORE] On-prem support enabling user hosting of the accsyn workspace orchestrator (backend , DB & frontend), deployed as Docker composed images.

  - [APP+CORE] Optimised job and farm monitor traffic - minimise data sent with a refurbished protocol. Overall improvements and monitor bug fixes.

  - [ASC/APP] Single port/channel support, allowing multiple transfers on the same network TCP ports. Previous successful port is also remembered and prioritised next transfer. Solves problems if multiple clients need to share a low port on restricted networks.

FEATURES

  - [CORE|FRONTEND] Backend and frontend hosting/VPC and security updates, including improved handling of registry authentication tokens.

  - [APP] Updated to Java 18, and updated installer. Overall desktop app improvements and security  fixes.

  - [APP|WEBAPP] When creating a share, illegal characters are now removed/replaced with the code/name proposal.

  - [ASC,APP] Added a decimal to progress %

  - [APP,FARM] Using term "Engine" for describing an app based processor. Render job engine type displayed on submit button.

  - [APP] Show password while typing

  - [APP/DAEMON] Mute tracebacks in log on connection failure after the first one.

  - [APP] Prefs: Show ACCSYN\_DISABLE\_\* environment variables with help.

  - [APP] Lock file support, preventing multiple local instances of the accsyn file transfer client.

  - [APP] Edit settings for a web delivery - password, expiry date and download count.

  - [CORE,WEBAPP] Bind web transfers to a queue.

BUG FIXES

  - [APP] Fixed bug when checking stale lockfile PID, that it belongs to accsyn executable.

  - [CORE] Support non US letters in passwords. Give proper error if a password is entered that cannot be decoded - containing illegal characters.

  - [CORE] Pre-publish exceptions now properly output to job audit log.

  - [ASC] Fixed bug were the copy server reported back as ready before it was up and listening

  - [APP] Fixed bug where most recent destination mode were not remembered if mirror paths available as option.

  - [APP] Prefs; add scrollpane to handle if inputs are getting too wide.

  - [APP] Remove config button for non admins.

  - [APP] Fix ffmpeg/farm transcode issue with not displaying input media filename and profile.

  - [CORE] Disabled password reset request for pending invitees.

  - [APP] Fixed share subfolder creation, and other write operations issues, on standard upload.

v2.6-20 [23.11.09]

FEATURES

  - [APP] Improved local file browser with system drive names, showing /Volumes | /media | /mnt | /net devices on top.

  - [API,CORE] Filter (regexp supported) argument to ls() operation.

  - New job setting "job\_on\_missing"; "fail": Make the whole job fail when all other tasks has been exhausted (default), "ignore": Ignore and set task(s) as done.

  - [FARM] Support envs, with passed on to render app, and also replaces ${ENV} expressions in path.

  - [APP] Auto reload speed graph, show average speed.

  - [CORE,ASC] Show in job log from which computer and error or warning message originates.

BUG FIXES

  - [APP] Fixed bug with 2FA auth code prompt being too small.

  - [APP] Fixed bug were standard user finished jobs did not list properly.

  - [APP] Fixed bugs in publisher, also updated Github "publish-workflow" samples.

  - [APP] Fixed bug where copy&paste from Xfer log viewer does not work unless pasted in text document and copied a second time.

  - [APP] Fixed share browsing bug in basic downloader where path became out of sync if not share root was readable.

  - [APP] Fixed unknown domain compile error on startup.

  - [APP] Fixed bug in file browser recent locations where Recent: were empty.

  - Fixed bug where aborted job task retry does not retry the entire job. Also clear status notification properly on abort and such.

  - [CORE] Fix share cache update threading lock bug.

v2.6-17 [23.10.16]

FEATURES

  - [APP] Understand and follow Windows .lnk shortcut files.

v2.6-16 [23.10.16]

MAJOR FEATURES

  - [FARM] New Unreal Pixelstream render farm app.

  - [APP] Revamped file browser; labels with filtering on share list, foldable ACL lists with improved layouts and user interactions.

  - [APP] Custom bookmarks in file browser, to enable using local network shares by UNC names or other locations not present among system default volumes.

  - [CORE] Employee root share constraints - limit a user with Employee clearance to a single root share instead of having access to all (default). User will only be able to send/download/upload, share folders and view jobs with this root share.

  - [CORE,APP] Enhanced file browsing experience, featuring a cache of recent browsed folder and automatic refresh in the background or live refresh when manually reloading in GUI:s. Labels with filtering on share list, foldable ACL lists with improved layouts and user interactions.

  - [APP] Revamped landing page/home, clearly displaying incoming pending deliveries with a sticky (non hideable) behaviour and a fully visible download button. Enlarged submitter buttons and two submitter layouts - standard (simplified) and commander (current vertical split)

  - [CORE/APP] ffmpeg support, with transcode profiles.

  - [GUI ] Job speed metrics graph visible in GUI

FEATURES

  - [APP] Understand and follow Windows .lnk shortcut files.

  - [APP] Added environment variables to strip down and remove GUI elements - ACCSYN\_DISABLE\_HEADER, ACCSYN\_DISABLE\_SUBMIT, ACCSYN\_DISABLE\_ATTENTION\_JOBS, ACCSYN\_DISABLE\_ATTENTION\_ACLS, ACCSYN\_DISABLE\_TRAY.

  - [CORE,WEBAPP] New "user\_join\_login\_on\_activate" setting, having user become logged in when they have activated their account with password. This behaviour is disabled by default.

  - [CORE, WEBAPP] Logout user everywhere - delete a users active sessions.

  - [APP] Job settings in quick submit dialog.

  - [APP] New setting "security\_app\_session\_recover\_enable" (default: enabled), allowing user to continue a previous (locally stored) session instead of entering password.

  - [APP SUBMIT] More info on right hand side when no files is selected, also disable upload to sites - only show hq for now.

  - [ASC] Improved ETR calculation to consider throughput the last minute instead of entire transfer period - more accurate when bandwidth fluctuates.

  - [APP] When session expire, GUI is locked and user is asked for password instead of being logged out keeping the file transfer client running in the background. Decrease session time from 7 days to 10 hours.

  - [APP] Attach a message when adding an ACL / sharing folder with user.

  - [APP] Dark mode detect on Mac.

  - [APP] Raise window from system tray/menubar instead of giving already-logged-in error when launching second instance on desktop.

  - [APP] Added keyboard shortcuts: CTRL/Cmd+F for search, CTRL/Cmd+B add bookmark and CTRL/Cmd+R for reload.

  - [APP] Size up shares in file browser, add more spacing.

  - [APP] Search To: (Destination) field.

  - [ASC] New "single file resume" transfer log setting, off by default. When set, verbose single file resume log message will be displayed in transfer log.

BUG FIXES

  - [CORE] Fixed bug were a share could not be edited due to share:share error.

  - [ASC] Fixed bug where sub task status report fails.

  - [APP, WEBAPP] Preserve logotype aspect rate and limit to 100x40 in size.

  - [APP] Fixed bug were To: resets after inviting a new user, instead of pre-selecting it.

  - [ASC] Change prefix of temporary file from ".ASC\_TMP.\*" to ".ACCSYN\_TMP.\*" Changed prefix for single file resume checkpoint files from ".\_accsyn\_checkpoint" to ".ACCSYN\_CHECKPOINT." to fix some storage incompatibility issues. Changed prefix for partially transferred files from "\_accsyn\_incomplete." to "\_ACCSYN\_INCOMPLETE.".

-------------------------------------------------------------------------------------------------------------------------------

v2.4-8 [23.05.22]

FEATURES

  - [WEBAPP,CORE] Explicit site permissions that overrides role/API key permissions, to prevent writing (download, create directory,..) to a site or reading from (upload).

BUG FIXES

  - [CORE] Have jobs with only excluded tasks left finish up successfully instead of failing. Allows for submitting "placeholder" jobs that can have tasks added later.

  - [WEBAPP] Fixed bug when moving a share to another folder on the same root share.

  - [WEBAPP] Fix bug where servers are not displayed with root share listing. Also show how many shares beneath each root share.

  - [APP] Fixed bug were local source computer only selectable in send mode.

  - [APP] Fixed bug in share browser were type was not filtered properly.

  - [APP] Fixed bug in queue settings were transfer resume could not be enabled if disabled in workspace/global settings.

v2.4-6 [23.04.03]

MAJOR FEATURES

  - [WEBAPP, APP] Revamped delivery of packages and onboarding for unregistered users. Deliveries always has a web link that aids in onboarding - installing and authenticating the desktop app through the browser using a 6-digit PIN identification.

  - [WEBAPP] Web delivery send with ability to have files drag-n-dropped from local computer. Smoother package build and deliveries. Support for creating delivery from a share as an alternative.

  - [WEBAPP, APP] Revamped web browser download & upload with bug fixes and faster file delivery.

FEATURES

  - [WEBAPP] Support for converting an accsyn download to a browser download, if size of package allows.

  - [WEBAPP] Style change and UX improvements overall.

  - [WEBAPP] Web transfer settings moved to it's own tab out of File transfer settings. Web browser download and upload can now be disabled.

  - [APP] General UX improvements, more spacing and graphic bug fixes. Hide empty queues in job view by default, can be turned on from filter menu.

  - [WEBAPP,CORE] Explicit site permissions that overrides role/API key permissions, to prevent writing (download, create directory,..) to a site or reading from (upload).

BUG FIXES

  - [CORE] Fix bug where user queue constraint could not be removed.

  - [APP] Fixed bug enabling two running instances of accsyn due to expired API sessions.

-------------------------------------------------------------------------------------------------------------------------------

v2.3-1\_8 [22.12.21]

BUG FIXES

  - [CORE] Fixed bugs with inactive shares.Fixed bug when changing a root share path

  - [CORE] Small core Python 3 improvements and bug fixes.

v2.3-1 [22.12.09]

MAJOR FEATURES

   - [INTEGRATION] ftrack first level integration; Sync published components through the ftrack-accsyn-accessor and a sync Action.

-------------------------------------------------------------------------------------------------------------------------------

v2.2-8 [22.12.04]

FEATURES

   - [WEBAPP] Sort users alphabetically in selection combos.

   - [APP] Show description in job list view.

   - [APP, SUBMIT,SETTINGS] Amount of overridden settings are visualized on button, with tooltip.

BUG FIXES

   - [APP,FILE BROWSER] Fixed bug where shares were reloaded every 30s when not needed.

   - [WEBAPP, FINISHED TRANSFERS] Fix log view bug.

v2.2-7

MAJOR FEATURES

   - [CORE] Backend Python 3.10 upgrade, massive performance and security improvements.

   - [GUI, MY TRANSFERS/JOBS] Divided into areas with new download and upload buttons enabling fast and easy package submit. Larger jobs. Start accsyn default with this view maximised for standard users.

   - [CORE] Parallelise job size calculation, making file transfers start immediately instead of waiting for it to complete.

   - [GUI,JOB VIEW] Improved job and task(file/frame) view with task progress bar, division into buckets, recent line of console output on active task.

FEATURES

   - [COMPUTE/GUI] Arnold for Maya batch render support

   - [APP,BROWSER] Added "Inactivate share" option to enable fast cleanup. Also prevent locations (shares, local drives) to be updated on a reload or file operation.

   - [GUI, SUBMIT] Add preference for turning off go to recent directory behaviour.

   - [GUI] Move login errors to more visible location within login window

   - [APP SUBMIT] Proper send button in lower right corner replacing the arrow button when submitting a package, work in maximised view.

   - [APP JOB VIEW] Improved job tasks and hooks view.

   - [COMPUTE] Job filters can now include asterisk for matching values, e.g. hostname:+render0\*

   - [WEB DELIVERY] Improved web delivery job view with more information, disable web delivery in app if disabled in settings.

   - [GUI, SUBMIT] Settings are now visible during render submit. Fixed bug when minimizing submit with settings open and could not restore.

   - [GUI, OB VIEW/TASKS] Pagination if more then 1000 tasks.

   - [GUI, SUBMIT] When in package submit mode, the green arrow is changed properly to reflect

   - [ASC] When transferring multiple files/rendering multiple frames in on bucket, each task done will be reported back during execution instead of once at the end. The tasks reported as done will stay done in case of a failure or interruption.

   - [COMPUTE] Possibility to configure a compute default queue.

BUG FIXES

   - [COMPUTE] hq download task runs one final time at job finish to fix bug were frames were left behind.

   - [GUI,FILE I/O] Fixed bug when creating a local directory caused interface to tumble.

   - [WEBAPP] Human readable byte counts are now displayed in si (1000 base) and not 1024 based (GiB)

   - [APP,BROWSER] Fixed bug where delete share context menu option did not work.

   - [WEBAPP] Fixed bug where displayed dates were displayed in wrong timezone.

   - [WEBAPP] Improved error message on duplicate ACLs. Fixed broken Grant Access and Shared Directories link on edit user page.

   - [APP SUBMIT] Fixed bug in upload were a browsed destination not could be chosen when source files were on a locally mapped share.

   - [GUI,WEB DELIVERY] Fixed bug were duplicate recipients could be added

   - [GUI,PROCESS LOG] Fixed bug where switching to an earlier try did not update combobox or title. Also the refresh function loads the entire log instead of the difference.

-------------------------------------------------------------------------------------------------------------------------------

v2.1-8

MAJOR FEATURES

   - [CORE] 2FA - Multi factor authentication support, supporting a 6-digit token sent to email and required at login. Configurable for all users or per role.

   - [CORE] General speedups and optimisations

   - [APP,SUBMIT] Web delivery of file(s, ZIP:ed) on default root share, using a magic link (emailed) that can have a password set, expiry date and download count restriction.

   - [APP,SUBMIT] Overall improvements: submit button now sits between from and to areas. Shares can now be filtered to only show root shares (default for employees), standard or user shares. Right click a set of files and calculate the size. View job as JSON.

   - [APP,SUBMIT] Improved publisher, with support for choosing project database task for unidentified publishes, and selection of main asset.

   - [APP] Refurbished and improved, new dark style and view filters.

   - [WEBAPP+CORE] Shares can now be deactivated - unloaded from accsyn, to preserve resources, together with ACLs. New filters to share admin page allows display of inactive shares, and restore options.

   - [WEBAPP+CORE] Users can now be deactivated - unloaded from accsyn, to preserve resources, together with ACLs. New filters to share admin page allows display of inactive shares, and restore options.

   - [APP] Tray icon support. When closing app it minimises to the tray/dock on desktop. Clicking icon will re-open GUI, right-click will bring up a menu with options to open or exit. Logout button in interface to exit app.

   - [API] API documentation is updated and moved to accsyn-python-api.readthedocs.io

   - [RENDER/FARM] Houdini, Blender and Nuke 13 (Python 3) support.

FEATURES

   - [CORE] Downloads and/or uploads can be disabled globally.

   - [APP,SUBMIT] Now supports non-US (åäö) characters on folders/files and submit.

   - [APP Browser] Goto previous share path is now a preference and can be turned off.

   - [ASC] No TCP delay (Nagle's algorithm) support.

   - [ASC] If file post process fails - rename to final, these failure(s) are not taken into account until the end, to get transferable files through.

   - [ASC] Xfer log; Startup space requirement summary, and final transfer summary shows how many bytes were in sync.

   - [ASC] Improved security for listening server process.

   - [APP] Improved log viewer; copy to clipboard button.

   - [WEBAPP] Admin dashboard now displays available cloud storage for web transfers.

   - [API] New assign and deassign methods, initially for configuring (site) servers for root shares.

   - [RENDER/FARM] Only the render output is displayed in process logs, to see output from render Python wrapper there is a service log checkbox that enables it.

   - [APP,BROWSER] Added "Inactivate share" option to enable fast cleanup. Also prevent locations (shares, local drives) to be updated on a reload or file operation.

BUG FIXES

   - [CORE] Fixed bug when upgrading a user to employee did not take fully effect.

   - [CORE] Fixed bug where inactive servers where deleted on inactivity, with restore of deleted servers.

   - [CORE] Improved audits; now showing correct user and geo data / device, and who modified as client/app

   - [APP,SUBMIT] Now supports non-US (åäö) characters on folders/files and submit.

   - [APP,SUBMIT] Initial job settings does not take effect.

   - [APP] fixed unresponsive share browser if many (+100) shares.

   - [APP] Finished job listing has been optimised to return faster results across UI:s.

   - [APP] Compute retry logs could not be viewed.

   - [ASC] Wrong progress and ETA were shown when resuming a previously interrupted transfer.

   - [ASC] Fixed bug when required space not shown properly, only 0(0). Improved pre and post transfer stats reports overall.

   - [APP,BROWSER] Fixed bug where delete share context menu option did not work.

-------------------------------------------------------------------------------------------------------------------------------

v1.4-4

FEATURES

   - Webapp; Refurbished UI featuring new dark style layout.

   - Compute/render farm job submit now enabled for standard/restricted users, with permission check on share upload and download locations.

   - Admin; Multiple users can be invited when giving access to a share.

   - Webapp; Admin menu now available throughout the session.

   - Job init; If file(s) are missing during size check, task(s) are set to failed instead of failing the entire job, so transfer can start and transfer what is possible.

CHANGES

   - Desktop app file browser; Removed new feature that descends directly into a clicked folder, now uses old behaviour - double click. Support new single click descend on the folder icon only.

   - ASC; With single file resume disabled, pre 1.4 .ASC\_TMP.. file is used. Two processes writing to the same file; detects if the partially written file is being written and steps back.

   - Admin; Settings on queues/shares that are not overridden are now greyed out instead of disabled - enables inspection of options.

   - API; Add support for file sequence notation without range specification: "dir/sequence.####.png". Also fixed bug where sequences were written into a subdirectory.

   - GUI Submit; Edit and delete share shortcut icons/button on shares has been removed, now available from context (right click) menu.

   - API submit; Source site is autodetected from WAN IP if tasks given on the ambiguous form "source":"share=...", "destination":"hq".

   - API; Updated to v1.4.1 with support for creating a new session with a given lifetime.

   - (b27) Servers that serves a share is never archived anymore.

BUGFIXES

   - Fixed bug in single file resume - large resumed files contained corrupt 0-bytes blocks randomly. Single file resume disabled automatically for v1.4-3 clients and earlier.

   - ASC; Fixed bug where \_accsyn\_incomplete files were written if single file resume disabled. Also enabled file resume setting for shares, queues and jobs.

   - Windows executables are now correctly signed.

   - Fixed bug where standard users could not disable/enable their client.

   - Fixed bug where restricted user paths were translated to root share/share paths if they matched server paths.

   - Audit logs are now read reversed - presenting the latest record first. ACL changes (Grant access, change access) is now properly logged on user, share and domain.

   - (b22) Desktop app; fixed bug when switching from upload to download, and could not browse up from previous upload folder.

   - (b27) Editing users caused errors in backend regarding metadata.

v1.4-3

FEATURES

   - Compute addon; possibility to configure 'compute' apps that makes accsyn act as a render farm executing render jobs, with app definitions as Python scripts. Enable cross-site file transfers to support rendering on-prem from another site or working from home. Also supports rendering on computers at a remote site, for example AWS or GCE cloud. Compute script repository: https://github.com/accsyn/compute-scripts

   - ASC; Improved transfer log, showing size of current file transferred and also made sure speed measurements are in SI units - multiples of 1000, not 1024.

   - Global API keys - can be configured to inherit user role (clearance & permissions, have a fixed role or have explicit permissions but role inherited from user. New admin section and overall improved security with improved performance.

   - ASC; Single file resume support - if large file transfer is interrupted it will resume next transfer. Managed by a new setting 'transfer\_resume'.

   - Desktop app/Submit; Button to swap to <> from.

   - ASC; Huge file sets optimisations, less data sent and memory consumed during transfer. 1:1 sync file deletion algorithm speed up.

   - Desktop app/submit; Removed Add selected to the package button, available instead in file browser context/right click menu and toolbar.

   - Desktop app/Submit; Goto button moved to address bar "History" button. Address bar is now editable and a path can be entered directly followed by ENTER key press.

   - ASC/API; File sequence notation support when declaring source, on the form ../prefix####|%04dsuffix[100-200].

   - Job submit; Duplicate tasks with the same source and destination are now ignored.

   - Desktop app visual improvements.

BUG FIXES

   - Desktop app; scrollbar on issues header box if very many.

   - ASC; Mac "Icon^M", Windows "Thumbs.db" and Mac "DS\_Store" files are now excluded by default.

   - Desktop app/file browser; When deleting on the destination side, selected files are now taken into account instead of the entire parent directory.

   - Desktop app; Fixed bug with rename button not showing when browsing shares.

   - Desktop app bug fixes.

   - Desktop app bug fixes.

v1.3-5

   FEATURES

     - Support for multiple destinations when sending/transmitting. Desktop app; New [ + ADD ] button on destination enabling this (users & sites only). API; new recipients job data parameter: ..,'recipients'=['<party1>','<party2>',..], omit recipient in task destination job spec.

     - Task priorities, 0(lowest)-1000(highest), tasks/files with higher priority will be dispatched first.  Desktop app; Create a package and select tasks, toolbar will present priority assign dropdown. API; Supply priority in task job spec: ..,'tasks':[{'source':'..','destinatino':'..','priority':<0..1000>}]

     - Job/API; Transmit job destinations now supports both intermediate server path and relative delivery path, on the form: ..,'destination':'user@mail.com:share=project-delivery/201012:deliverysubdir/deliveryfilename'.

     - Share/API; Standard & user shares can now be created without providing parent root share share, if root share is not given - the default root share will be used.

     - ACL write only access allowed on share, denying download attempts - only allowing browsing and upload. (b19)

   BUG fixes

     - Transfer; Required space check now only takes into account files in need of sync, not entire package size.

     - Watchdog; If daemon hangs during launch (REST call stuck or similar), the daemon watchdog attempts continuous restarts.

     - Hooks; Fixed bug were backslashes in Windows path were not escaped properly.

     - Job API submit; Fixed bug where destination on the form 'share=<share>', without a directory or filename, caused files to be dropped off to home share instead.

     - Desktop app, submit; Fixed bugs when mirroring paths during download/upload from shares (non-root) that are mapped locally. (b19)

-------------------------------------------------------------------------------------------------------------------------------

 v1.3-4

FEATURES

  - One-way sync support, deletes files on receiving end that does not exist at source before transfer starts. Corresponds to \*NIX rsync --delete(-before) option. New domain setting transfer\_mode, with options 'copy'(default) and 'onewaysync'.

  - Empty folders are now transmitted.

  - Desktop app; Job encryption can now be set upon submit, and modified for an existing job.

  - Transfer include and exclude now supports regular expressions (case sensitive and insensitive). Exclude now also supports files in sub directories (path/to/file\_or\_dir\_to\_exclude). Include now supports inclusion of directories, not only files.

  - Desktop app, submit; When selecting a share, browsing starts in the directory with download/upload access - not root directory if not accessible.

  - Desktop app, submit; When going back (..) from a share, user now ends up at root share above share path instead of share listing (non restricted users).

  - User Name can now be changed in profile. (b12)

  - API key are now only visible once and have to be re-generated if lost. (b13)

  - TMP data directory removed on transfer exit. (b14)

  - Job done actions support (setting: job\_done\_actions), with initial "delete\_excluded" option that triggers Accsyn to delete excluded tasks on receiving end. Suitable for backup jobs with one project folder per task. (b15)

  - Issues; if a server serving multiple root share is offline, issue message is merged into one instead of multiple issues. (b18)

  - Queue interrupt policy setting, rearranged webapp admin>settings. (b24)

  - Open and view buttons on job and tasks/files, enlarged if user is involved. (b26)

  - Global reserved space setting (transfer\_reserved\_space), have job fail if the Accsyn transfer would make free space fall below this limit. (b30)

  - Speed limits can now be configured on servers. (b31)

 BUG FIXES

  - Transfer include and exclude are now merged upstream with settings from queue, (root)share and domain/global. Not replaced by job settings as previously.

  - Desktop app, job view; New tasks now appear as they are added elsewhere.

  - CLI job submit now properly follows job. (b11)

  - CLI setting delete now works. (b14)

  - Python API bug fixes. (b23)

  - Fixed bug in job listing, causing job list to render empty once after switching to All transfers from My transfers. (b26)

  - Desktop app, submit; Fixed bug were local paths were not shown properly when having local share mappings. (b29).

  - When transferring an entire share, job gets a proper auto-generated name. (b29).

  - Fixed bug with human readable file sizes, all sizes are now in SI format (multiplier 1000 instead of 1024 as before in different places. (b30)

  - Fixed bug were a late crashing server transfer party could give a false positive. (b33)

  - Added mechanism to prevent server port bind failures, detect and attempts to kill processes listening on port prior to spawn. (b33)

  - Webapp>Admin>Users; Fixed bug with unavailable Grant Access button when giving user access to a share. (b35)

  - ASC; Fixed bug when Accsyn tmp files (.\*ASC\_TMP\*) not were removed during transfer cleanup. (b35)

  - Web transfer/server; Fixed bug when wrong folder were created during share upload. (b39)

v1.3-3

 FEATURES

  - Email notifications when a directory has been shared with user.

  - Desktop app; Notification banners on-top of window.

  - Configurable transmit subfolder (Admin>Settings>Share>Transmit directory).

  - Desktop app; Create queue button i "All transfers" view, queue configurable when creating/editing a share.

  - Share "last accessed" attribute, updated upon file operations and transfers.

  - ReCAPTCHA on join/register, login and password reset.

  - Videos presenting features updated @ https://www.youtube.com/channel/UCui\_aQxTp-ftpwx8AJC5tzQ.

  - Desktop app; Hostname, IP and geolocation shown with transfer logs, both for client and server endpoints. File operation audits are complemented with geolocation data.

  - Number of concurrent transfers, between server and client, can now be configured globally or at servers.

  - Log view/audit pagination, showing default 200 entries per page, with free text search function.

 \*b3; If files/tasks on hold, job will be kept waiting until files/tasks are re-queued.

 \*b4; Removed client side hooks of security reasons, will be replaced with user configurable hooks in desktop app.

 \*b4; Desktop app; Finished job reload button. List reloads every 2 minutes, reloads when job is modified.

 \*b9; Disk log; Log entries are now stored on disk internally for better performance/lesser resource usage.

 BUG FIXES

 \*b4; Progress bar not up to date with progress.

 \*b4; Desktop app; Fixed view minimise/maximise bugs.

 \*b4; Linux GUI theme bug fixes.

 \*b4; Desktop app; All ACLs were not listed in file browser.

 \*b4; Desktop app; New version, update now dialog fixed - update now always should apply.

 \*b12; Desktop app; Fixed password reset bug.

v1.3-2

  FEATURES

  - Desktop App; Redesigned faster job submits, submit now integrated into main window and stays there. Publish still using old job submit dialog.

  - Desktop App; New "My transfers" section only showing user jobs, default during job submit.

  - Desktop App; Share management now enabled from job submit browser. Create, edit and delete shares while browsing root share. View and delete ACLs for current directory. Share directory while browsing a share, displays summary of #shares, #unique users and #shared directories for listed files.

  - Now supports upload to/from sites as a user (employee/admin).

  - Now supports pulling files from a remote user that has enabled read access to their local share mappings. File management (create dir, rename, move and delete) can also be performed on mapped local share paths if write access enabled in Desktop App preferences. Read and write access are off by default.

  - Optimised backend; x4 lower CPU load when processing many jobs.

  - Optimised memory and cpu usage, 25% less RAM usage for Desktop App when displaying large jobs.

  - LAN connection fallback; if client cannot connect to server using WAN or configured IP override, it tries to contact server on its LAN IP addresses.

  - PSK security enhancement; A secret Pre Shared Key is supplied and validated by server before a connection is accepted.

  - Desktop app file browser; Multiple files/directories can now be deleted, with interruptible progress meter.

  - GUI; Proper interruptible progress bars on modifying jobs/queues.

  \*b2; Python API; getsize boolean attribute to ls (file listing), calculates sizes for all directories returned in operation.

  \*b2; File listing are more responsive, ~0.4s time cut.

  \*b12; GUI; Prepared for future MFA (Multi Factor Authentication) implementation.

  \*b13; Employees may now edit shares.

  \*b13; GUI; Create queue function, delete queue.

  BUG FIXES

  \*b2; Job progress updates were lagging behind in previous versions, improved internal event propagations.

  \*b2; Desktop app file browser; Write permissions are now reflected properly when mkdir, rename, move and delete buttons are presented.

  \*b13; GUI; Fixed bug were progress bar did not scale properly.

  \*b15; GUI; Mirrored uploads and downloads with user mapped root shares now works.

-------------------------------------------------------------------------------------------------------------------------------

v1.2-7

  FEATURES

  - Submit; Partially redesigned submit window, to comply to upcoming v1.3.

  - Submit browser; Share are now visible all the time, as it were before.

  BUG FIXES

  \*b1; Submit browser; Fixed bug were wrong share were displayed in address bar.

  \*b1; Submit; Fixed bug were a user could not upload with mirrored paths from a local mapped (root) share.

  \*b1; Submit browser; Local paths are now displayed correctly in address bar.

  \*b2; Retry bug fix in site-site transfers, IP overrides were switched in some scenarios.

  \*b3; Webapp; Fixed bug when browsing new root share  - could not descend into some folders.

v1.2-6

  FEATURES

  - Geodata is recorded for user logins and clients, based on IP.

  - Web app; Transmit function that complements browser upload - upload a file using browser followed by a send to user.

  - Desktop app; Rewritten share browser to align with new web app file browser.

  - Web app; File browser now have Goto option - allows manual entry of share path or by selecting from history (most commonly used & most recent)

  - Total and free space is now measured for root shares, visible @ admin dashboard.

  - A global reply-to email address can be configured - an existing user with admin or employee clearance. If no reply-to address is configured, the most recent admin account will be used.

  - Improved internal security with API/CLI calls and attributes returned.

  - Mac OS Catalina support.

  \*b2; Task creation date and finish date now stored in backend, showed when hovering task in desktop app.

  \*b5; Root share space usage visualised @ admin dashboard (webapp).

  \*b8; Client geodata collected.

  \*b9; User geodata collected.

  \*b10; Webapp; Account activity can be audited beneath user profile page.

  \*b11; Python API; Log session activity to disk option.

  \*b13; App submit; Destination can now browsed during site transfers, path mirror not the only option.

  \*b14; Mac OS Catalina support.

  \*b14; Webapp; Files are now shown while sharing a folder with user.

  \*b17; Submit; relative paths are now assumed being relative default root share, Accsyn no longer tries to identify first relative path element as a share (code or ID). This to decrease ambiguity and make submit definition clearer, use "share=../.." syntax do define share relative paths always from now on, or full absolute server paths.

  BUG FIXES

  \*b2; Desktop app; Fixed bug in job submit - Settings view were corrupt and file browser were not aligned when leaving settings.

  \*b3; Web app; Disabled shares can now be viewed.

  \*b12; App submit; Fixed bugs with new share browser.

  \*b15; Copy; Fixed bug when fast 0 bytes transfers failed even if they were successful (process kill flushed stdout).

  \*b16; Copy; Not overwriting an existing file with a directory (+E#J0058).

  \*b16; GUI; Links to Accsyn warning and error codes now available in log view.

  \*b16; ASC; Fixed bug where finished transfers could hang after they were done, now Accsyn retries indefinitely to report back - prevents stuck transfers is backend is temporarily down.

  \*b16; Fixed bug when site<>site transfers were submitted as corrupt jobs.

  \*b16; Fixed bug when override IP:s did not apply properly for site<>site transfers.

  \*b17; Submit; Fixed bug when submitting JSON on the form "tasks":[{..}] having tasks in a list, only one task was previously created.

v1.2-5

  FEATURES

  - Backbone optimisations and performance improvements.

  - Web app; Preview support of formats: .mp4,.jpg,.tiff,.png,.pdf,.svg,.ico,.ogg,.mkv,.jpeg,.apng,.bmp,.gif,.txt,.html,.json,.xml,.wav, & .webm. Setting beneath Misc for turning previews off.

  - Web app; General improvements, visibility in mobile devices with responsive toolbars. Improved volume, share and file browsing. Removed hashtag(#) from url paths.

  - Python API; Improved job queries - "finished" boolean attribute to match GUI:s.

  - Web app; Support for file resources upload (ADMIN>Resources).

  - Replaced "Push" and "Pull" terms with "Site download" and "Site upload".

  \* b2; Turned off default job submit E-mail notifications.

  \* b10; Webapp/Mail; Global Email config now supports resources as attachments for "registered" (invite) and "joined" Emails sendouts.

  \* b11; App; Now asks if a new revision exists, remembers user choice and will not ask again until next new revision.

  \* b12; App; Clear history option in prefs - makes Accsyn forget previous entered user input and logins.

  \* b13; Webapp; Process logs can now be viewed for a task.

  \* b14; ASC; Zero bytes jobs/tasks are now allowed.

  \* b15; Python API/Create task; If another tasks exists with same source and destination, it is retried instead of added as duplicate. If argument 'allow\_duplicates' is supplied as False, an exception will be thrown.

  BUG FIXES

  \* b2; Transmit; browsed subfolders were ignored.

  \* b6; Browser upload; fixed bug in Safari.

  \* b17; Fixed bug when delivery Emails to user was not sent when submit E-mails were configured disabled.

  \* b17; Fixed bug in web preview of job with multiple tasks - picked wrong task.

v1.2-4

  FEATURES

  \* b1; Webapp; Admin pages improvements, fixed proper page history and URI:s allowing going back to were you were before.

  \* b2; Webapp; "+NEW TRANSFER" option instead of "SEND>" that aligns with GUI app.

  \* b2; GUI; Edit queue now has link to more settings in webapp.

  \* b3; Webapp; Improved transfer/job list.

  \* b4; Webapp; Removed reports and added log view for admin sections.

  \* b5; Publish; Additional metadata support, in key=value or JSON format.

  \* b7; Webapp; admin pages bug fixes and improvements.

  \* b8; Metadata support; metadata can now be configured on domain(global), user, share, site, client/server, queue and job level. This metadata is supplied to hooks. Divided into internal and external, where external metadata is exposed to client side hooks/jobs.

  \* b9; GUI; Queue now shown when opening a delivered job.

  \* b10; GUI,Send job; Disabled user are now hidden by default. Sending a package to a disabled user now enables user.

  \* b11; SOCKS (v4 & v5) support for desktop app, configured through environment variables or during login.

  \* b12; Webapp; During server install and edit, the root shares it is supposed to server can now be selected.

  \* b13; If no client is serving a root share, and root share is not disabled, an issue will be recorded.

  \* b14; GUI Submit; Proper warning if trying to add the same source file twice.

  \* b14; Webapp & GUI; Consolidated/improved further.

  \* b15; GUI; Status bar, show upload/download speed and current transfer going on.

  \* b15; GUI; Process logs now shows client and server log side by side, with option to turn off server log. Refreshes automatically.

  \* b17; Redefined proxy environment variables, consolidated into one - ACCSYN\_PROXY having format "<type>:<addr>:<port>" where type can be 'accsyn' or 'socks/socks5'. Backward compatible with old format "addr:port" which interprets as an Accsyn proxy type.

  \* b18; Webapp>Admin>Sites; Built-in default sites are now hidden by default.

  \* b19; Webapp; When creating a queue, job done Email recipients can be defined.

  \* b21; Python API; Pre-publish support.

  \* b22; Python API; Query and update job tasks support.

  \* b23; GUI Submit; Absolute path are now visible in browsers for employees/admins.

  \* b23; GUI Submit; Create dir, rename, move and delete buttons now also visible during download.

  \* b25; Disabled users/shares is enabled when being shared / ACL created.

  \* b26; GUI Submit; Improved transmit function, now allows you to browse were file(s) should be uploaded before being sent to user.

  \* b28; GUI Submit; Add files from list of /abs/path or share=../path entries.

  BUG FIXES

  \* b1; GUI; Search box did not stay minimized.

  \* b14; GUI Submit; Fixed bug during download with mirrored share paths - was not enabled during certain circumstances.

  \* b20; Webapp; Fixed bug were invite user buttons did not work and a few other issues.

  \* b23; GUI Submit; Fixed bug where Dropoff radio button randomly disappeared.

  \* b26; GUI Submit; Fixed bug were mkdir/rename/move/delete button became invisible to users.

  \* b28; Fixed bug in E-mail send.

  \* b30; GUI Submit; Fixed bug were destination could not be browsed during upload.

v1.2-3

  FEATURES

  \* b1; Publish feature; allow user to upload files and metadata directly into production workflow. Defined through hook scripts that validate input and post process data.

  \* b2; Webapp; Improved application download dialog, now detecting and suggesting operating system.

  \* b3; Webapp; MD5 sum are now listed with installer packages.

  \* b5; Desktop application now have RPM and DEB builds as well.

  \* b6; UI improvements.

  \* b9; Additional RPM (RHEL/CentOS) and DEB (Ubuntu) desktop app installers.

  \* b14; Auto join now have a password setting, enabling only authorized guests to register and account and upload files.

  BUG FIXES

  \* b1; Invite user option now back again when choosing user upon sending out files.

  \* b8; GUI; Now showing PUSH/PULL options in main interface if on hq or a site..

  \* b11; Fixed dispatch bug - jobs in a queue created by a user that was enabled got stuck, without proper warning message.

  \* b12; Webapp; Fixed bug in transfer>Delivered - first job were always viewed regardless which where opened.

  \* b13; Webapp; Fixed bug if many tabs open and login/logout occur they became out of sync.

v1.2-2

  FEATURES

  \* b1; Webapp; Rehaul of admin pages, improved looks on mobile devices.

  \* b1; GUI; Admins and employees now have NEW button instead of UPLOAD, DOWNLOAD and SEND.

  \* b3; Site/Internet location is now autodetected, and affects upload/download buttons in GUI.

  \* b5; GUI/Job view; Job chat function. Description is now the first message in a job chat thread. Chat can be extended to other future entities.

  \* b6; Server/Daemon watchdog, restarts daemon if hangs - no activity in 5 minutes. Can take on stop/restart/start requests. (requires reinstall).

  \* b6; GUI; Improved user and site selected dialogs that remembers last entry.

  \* b6; ASC; File permissions can be configured to be preserved during transfer if both sides POSIX compliant operating systems (Mac OS, Linux, Unix).

  \* b7; GUI/Login; Now remembers previously used accounts to aid user switching.

  \* b18; GUI; Rehauled prefs view.

  \* b20; GUI; Support for auto update. New "Check for updates" prefs button and dialog, will now download and update Accsyn instead of launching browser download.

  BUG FIXES

  \* b1; WWW/admin; Fixed bug were transfer\_conf/notmp & transfer\_conf/nolock could be set on queues.

  \* b1; File locking now turned OFF by default - usually causes problems with certain storage subsystems.

  \* b3; GUI; Fixed bug when right clicking job and about to change position - now taking selected job in account, not the clicked one.

  \* b4; GUI/Submit; Hide shares during PUSH, PULL or TRANSFER.

  \* b9; [ASC]; Fixed causing infinite connection attempts even if all ports are blocked/unreachable.

  \* b10; General bug fixes and improvements.

  \* b12; Deleting a user now migrates ownership of queues and servers to user performing delete.

v1.2-1

   FEATURES

   \* b1; Porting to AccSyn (v1.2, product rename with additional features) initiated.

   \* b2; GUI/Job submit; A ongoing dir listing may be interrupted. File listing rows now highlighted when hovered. Right click menu now have Refresh option & Add selected file(s).

   \* b8; FHC; 3x less memory consumption during file reading at sending party.

   \* b9; FHC; Attempts to log out of memory errors.

   \* b12; GUI/Submit; Goto now accepts entering a raw share name.

   \* b24; Web submit; Download/Upload now supports site push/pull.

   \* b26; Consolidated fonts with desktop app and www frontend/web page (Roboto/Roboto Thin).

   \* b28; GUI/Goto path; Option to sort by common or recent. Remembers choice.

   BUG FIXES (b=build)

   \* b2; GUI/Job submit; Fixed bug were upload from local mapped share did not enable Mirror path destination option.

   \* b3; Fixed bug were a function in instance could stop update internal state (user activation status).

   \* b4; GUI/Job submit; Bug fixes: (mirror paths to local share) switching shares did not update GUI,  (mirror paths to local share) strange paths in file list - now only showing absolute local path, already added files were affected when changing destination mode. Sorting by filename now always puts '..' on top.

   \* b10; FHC; Fixed bug when picking up setting transfer\_ignore\_existing per task- mixed up 'file' and 'directory'.

   \* b11; FHC; Fixed bug where task indexes got reordered during transfer init phase.

   \* b12; GUI/Submit; Fixed bug where Add selected were unavailable when dest mode was Share mirror.

   \* b13; FHC; Crashes without a leaving a non-zero exitcode are now detected, i.e. segfaults.

   \* b14; GUI; Fixed bug when transferring an entire root share failed.

   \* b17; FHC; Bug fixes in file list building causing relative names to end up wrong at other end.

   \* b18; GUI/Submit; Bug fixes with local share path mirror on dropped files.

   \* b23; FHC; Further bug fixes/optimisations in protocol.

   \* b26; GUI/Submit; Bug fixes in file listing, now sorting alphabetically default and sorting by file size properly.

   \* b26; GUI/Submit; Now remembers to mirror share paths if was chosen previous submit.

   \* b26; Webapp; Allows Adblock (& similar) to block Raven javascript tracer.

   \* b28; GUI/Submit; Share listing should have a minimum width.

   \* b27; GUI; Password entry slided with garbage placeholder chars. Window titles had wrong spacing.

-------------------------------------------------------------------------------------------------------------------------------

v1.1-4

   FEATURES

   (b=build)

   \* b1; Users can now be configured to be bound to a queue.

   \* b1; Improved UI - log button displayed on failed jobs.

   \* b4; Do not fail immediately upon a single file/directory - attempt transfer rest of package and then fail at end.

   \* b6; Improved E-mails and web app overall.

   \* b10; Webapp; Improved download and upload progress bars.

   \* b11; "User shares/server"; Users to install FilmHUB as server and configure fixed path for shares on their side - enables receiving files without interaction. Enables future pull of files from user.

   \* b12; Descriptions on job queues, show when hovering queue in UI:s.

   \* b12; FHC; If server cannot bind to port, ban the port for a couple of minutes and retry it later.

   \* b12; Python API; Tasks(files) can now be added to transfers destined users, not only site transfer.

   \* b13; Web transfers; Cloud instance are boosted to 500Mbps during transfers for maximum throughput (expires after 4 minutes).

   \* b14; Admin/shares; Enable/disable shares directly from list. Hides disabled shares by default.

   \* b14; Admin/users; Hides disabled users by default;

   \* b16; GUI/Submit; Shares now grouped by 1) Root shares 2) Standard shares 3) Home shares. Disabled shares are hidden by default, right click context menu gives option to show/load them.

   \* b17; Improved web transfer speeds.

   \* b21; Show queue and change queue from web app.

   \* b21; Optimized FilmHUB to dispatch faster when many jobs queued up.

   \* b22; GUI/Job view; Can now load transfer logs from previous retries.

   \* b26; Admin/Audits; New section for viewing failed logins, jobs submit failures and find jobs containing a path element - first iteration.

   \* b28; GUI Submit/browser; [Goto] folder button.

   \* b33; Dynamic bandwidth limit during transfer, no need to restart transfer.

   \* b35; Submit/browse, GUI&Webapp; On Goto path, show history of latest locations. Store browse history per user.

   \* b37; Detect stalling transfers - fails after 5 minutes of inactivity letting other jobs pass.

   BUG FIXES

   (b=build)

   \* b1, GUI; Sort by name did not work.

   \* b4; ZIP on web transfer; Skips files that cannot be compressed.

   \* b11; GUI; Error in log if source file size calculation fails.

   \* b18; Fixed bug in admin pages - leaving browser on listing might hang/cause javascript lockups.

   \* b20; GUI Submit; Now recognizes local share mappings for users - support for mirror paths between local and remote share.

   \* b21; Drag-n-drop file does not show SEND option or PUSH/PULL.

   \* b21; Fixed bug that caused transmit jobs to fail.

   \* b32; Fixed bug that caused bandwidth limited encrypted jobs to fail.

   \* b38; Job submit; Add more files after drag-n-drop did reset selected destination.

v1.1-3

   FEATURES

   \* Server can now be installed both using PIN (simplified setup) or by password login, enable future user servers.

   \* Hook job data now includes list of clients, human readable source & dest. Remote paths are obscured.

   \* Optimised logging at clients - now only rotating 10x10MB log files.

   \* Last 512KB or client app log files can now be appended to client report (CLI: '--include\_client\_log' option).

   \* Removed port blacklisting feature, replaced with connect failure tracking and weighed proposals to server.

   \* Servers can now be updated from their Admin page.

   \* Clients will automatically update on launch if behind in version.

   \* Rehauled submit dialog first step - select type to include descriptive help text.

   \* Upload now suggest to browse shares if have no home share or home share disabled.

   \* Submit job; file list now shows sorting arrows.

   \* Additional pointers when entering and leaving setup wizard.

   \* API session now expire 30 days after last accessed.

   \* Clients/desktop app are allowed to be behind backend in version, prevent auto update in these cases.

   \* Create root share; paths can now be added, for example UNC paths on Windows, that is not listed.

   \* Admin dashboard with latest shared directories and license info.

   \* Progress bar now shows total progress and not only progress of files out of sync. Progress is now saved permanently and kept visible for paused/aborted jobs.

   \* Send option now available in web app - build and send a package to an existing or new user.

   \* Detects if a root share is missing and drops it to offline + spawns an issue.

   \* Rewrote E-mail configuration for domain, overridable at share and queue level.

   \* Grace for invites, defaults to 7 days. Configurable beneath ADMIN>SETTINGS>User.

   \* Umask setting for server side Linux/UNIX transfer processes, configurable beneath ADMIN>SETTINGS>File Transfer.

   \* \_20; Improved desktop app upload file management @ share, with right click menu.

   \* \_20; Clients admin listing, with possibility to set site for a non-user client.

   \* \_26; API sessions now attempts to renew and reuse expired sessions properly.

   BUG FIXES

   \* Performance fixes.

   \* Admin>Servers; Override IP now lists all clients.

   \* Temporary file renaming & locking issues now logged properly.

   \* Fixed bugs in job submit, mirrored paths did not preview correctly.

   \* Backend performance optimised.

   \* Fixed SSL cert issues with web transfers, now relaying files over backend instead of direct server connection.

   \* Fix bug were WAN IP and ports could not be configured for a server.

   \* Fixed bug in installer - GUI installer could not re-use existing config, only command line installer.

   \* Files having paths with a mixture of whitespaces (' ') and ampersands ('&') could not be transferred.

   \* Fixed bug where Mac OS X servers could not be updated through web admin.

   \* Fixed multiple bugs in site server installation @ ADMIN>SERVERS.

v1.1-2\_23

FEATURES

  \* Web application reloads if FilmHUB has been updated.

    \* Hook execution are now logged to file.

    \* Scrollbars now have increment/decrement arrows.

    \* When browsing destination, directory has to be entered to be chosen - not only selected.

    \* The domain is not shown during login, only the name. Domain now shown as tooltip.

    \* Client Java runtime now at version 1.8-202.

    \* Mail queue sending mail in background, with logarithmic fallback retries on fail.

    BUG FIXES

    \* Improved web transfer upload and download, fixed major bugs.

    \* Edit shares could cause parent, root share and path to be lost.

    \* Create root share failed on listing client root/mounts.

v1.1-2\_18

FEATURES

\* Refactored workareas > shares, complete rehaul of internal path specifications for transfer jobs.

\* New 'transfer\_bucketsize' (submit: bucket size) setting for transfer jobs - tell how many tasks at time should be dispatched.

\* Optimized submit - fetch list of sites & users.

\* Cleaned up/improved transfer logs.

\* Removed old beta "workarea" concept - replaced with shares. Previous shares are now "root shares".

\* New client install routine involving a 6-digit PIN for ease-of-use.

\* Setup wizard for new installations.

\* Added 'transfer\_ignore\_existing' setting, valid @ domain, queue, job & task level.

\* Made sure that job submit post hooks finished before transfer starts.

\* Added 'transfer\_include' & 'transfer\_exclude' settings @ global, queue and job level. Similar to rsync --include & --exclude

\* FilmHUB copy now allows for files in subfolders to change/disappear during transfer, without failure.

\* Additional advanced transfer settings for adjusting buffers and file locking.

\* Share transfer settings that overrides domain settings, applied for shared involved @ server side.

\* Logo displayed in desktop app.

-------------------------------------------------------------------------------------------------------------------------------

v1.0-1b

FEATURES

\* Setup wizard supporting server install>firewall config>share browse and final settings + guides.

\* Custom portal backend supporting spawn of new domain VM.

-------------------------------------------------------------------------------------------------------------------------------

v0.9-18\_24b

FEATURES

\* Site to site transfer support, requires local IP overrides (preferred) or FilmHUB standard ports 45190-45209 forwarded to site servers a both ends.

v0.9-18\_22b

    FEATURES

    \* GUI Submit; Recognizes local share path overrides in ENVs.

    \* Web app; First iteration of admin pages, supporting users/shares and settings.

    \* Cloud; Backend for supporting demo installations/customer portal.

    \* Overall optimizations in network traffic.

    \* GUI; Improved job view - toggle between list tasks and edit job.

    BUG FIXES

    \* Employees could not browse download, just mirror paths.

v0.9-18\_18b

    FEATURES

    \* CLI; 'client find' now includes FilmHUB version.

    \* Copy; Optimized file transfer protocol, this version is NOT backward compatible with lower versions!

v0.9-18\_17b, 20181211

FEATURES

    \* Job submit (cmdline/API); Support for trailing slash on destination path - treats last path element as the destination folder to put source file in (rsync notation).

    \* Jobs; Metadata support, both on job level and task lever. Provided at hook execution.

    \* GUI; Job edit now sharing same inputs as during job submit.

    \* Python API; 'ls': Recursive, maxdepths, directories\_only, files\_only options. New 'exists' function.

    \* Copy; Protection against files overwriting folders, will now put file beneath folder instead.

\* GUI; Resend option, for packages destined users. Allows user to re-download package on different client/other folder.

BIG FIXES

\* GUI; Workarea queue constraints did not apply if changing workarea during job submit.

\* Support for local volumes containing non-US (unicode) characters and whitespaces.

v0.9-18\_7b, 20181130

FEATURES

\* GUI Login; Feedback if unknown E-mail/user. Selects all when entering E-mail.

\* Network server proxy support; For client/API endpoints not having Internet access.

\* GUI; Improved progress on actions.

\* Copy; Handles blocked outgoing ports, attempt lowest ports.

\* Copy; Allow files to disappear during transfer - no crash.

BUG FIXES

\*  GUI; Second maximise did not apply.

\*  Copy; Fixed bugs causing crashes when transfer has finished.

\*  GUI/API; If authenticated with API KEY, a new session is automatically acquired when the old one expires.

v0.9-17, 20181112

FEATURES

    \*  App;Job search function.

    \*  Portal; A first take dashboard showing jobs.

    \*  Portal; Change password.

    \*  App; Admins does not get to answer questions when modifying jobs/queues.

    \*  API; Support for huge payloads (GZIP).

\*  App; Improved login and job submit dialogues.

\*  Copy; Define how a file is determined to be in sync (domain/que settings: transfer\_comparison)

\*  Copy; Preserve ownership on created folders and files (domain/que setting: transfer\_attributes)

\*  Copy; Additional transfer logging (domain/que settings: transfer\_log)

\*  Improved detailed job view.

\*  Web transfer downloads; A direct download web link is provided in E-mail if package less than 2GB. Supplies a ZIP with contents.

\*  Error and warning codes; Specified in admin manual, displayed on jobs upon failure. Global warnings/error codes shown in GUI.

\*  Improved detailed job view.

\*  Optimizations; Old inactive clients are kept offline in database until needed.

BUG FIXES

\*  App; window resize bug fixes.

    \*  User invite; Links to app installer were removed by mail provider, fixed by linking to new web "app" section.

\*  Fixed bug when size were calculated wrong if files on multiple shares.

v0.9-15, 20180821

FEATURES

\* Python API.

\* Command line interface (CLI).

BUG FIXES

\* Many
