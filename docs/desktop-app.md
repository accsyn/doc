# accsyn Desktop App

## What is the accsyn Desktop app?

  

The accsyn app is a desktop application primarily for providing accelerated accsyn p2p file transfers running in the background (tray), but also has a GUI enabling advanced functionality that includes extended [Delivery](/delivery/), [File Sharing](/collaboration/) and [Media Vault](/vault/) management.

![](/assets/admin_desktop-app-fa39d7dd7bb8.png)

Screenshot - manage title projects.

## When do I need to use the desktop app?

The app is required to facilitate accelerated and resumable file transfers - the core of the accsyn platform.

  

When creating a [delivery](/delivery/), or actioning a delivery on the web, the app installation is guided from the browser - no manual installation is required. The app will then run in the background (system tray / menu bar) as needed during transfer, and can then be closed.

  

Besides this, the app is mandatory when:

  

- Detailed monitoring and audit of jobs (deliveries, transfers, queues).
- Managing [file sharing](/collaboration/) on your cloud or on-prem storage.
- [Access](/collaboration/access/) shared folders.
- Manage the accsyn [Media Vault](/vault/) - ingest and manage your media, as a manager.
- Submit render jobs and publish files in BYOS configurations - part of [workflows](/developer/).

*Note: the desktop app is also included in the accsyn Daemon(service) installation, used for setting up [BYOS servers](/admin/server/).*

## Where to download

The app is written in Java and requires Java installed on Linux platforms, Windows & Mac installers have Java bundled. The desktop app is included in the accsyn daemon installation, there is no need to install it separately.

  

Find the links to the app installer below, log in with your personal accsyn account:

[DOWNLOAD APP](https://accsyn.io/getapp)

## Windows install

There are two options for installing the desktop app:

  

- Install only for the current user (default); Requires no administrator privileges, the app will be installed in your account profile @ %LOCALAPPDATA%\Programs\Accsyn by default.
- Run installer as administrator, making it available for all machine users; Will install the accsyn app in C:\Program Files by default.

  

Hint: Pin it to your task bar for easy access in the future.

## Mac install

Open the installer DMG and then drag-n-drop the app to where you want to install it.

  

Hint: Keep it in your dock for easy access in the future.

## Linux install

You can install accsyn on most major Linux distributions using the appropriate package format:

- `.deb` for Debian-based systems (Ubuntu, Debian, Linux Mint)
- `.rpm` for Red Hat-based systems (Fedora, RHEL, Rocky Linux, AlmaLinux, openSUSE)

1. Install Java (headless OpenJDK **17 or 21** LTS):

- **Ubuntu / Debian:** `sudo apt install -y default-jre-headless` (or pin `openjdk-17-jre-headless` / `openjdk-21-jre-headless`)
- **RHEL / Rocky / AlmaLinux 8–9:** `sudo dnf install -y java-17-openjdk-headless`
- **RHEL / Rocky / AlmaLinux 10:** `sudo dnf install -y java-21-openjdk-headless`
- **Fedora:** `sudo dnf install -y java-21-openjdk-headless`
- **openSUSE:** `sudo zypper --non-interactive install java-21-openjdk-headless`

See [Server administration — Linux prep](/admin/server/#linux-prep) for Amazon Linux, Alpine, Arch, and more.

2. Download the installer from <https://accsyn.io/getapp> — `.deb` (Debian-based) or `.rpm` (Red Hat-based); use the current release filename shown on the download page.
3. Install:

- **Debian / Ubuntu (.deb):** `sudo apt install ./accsyn_<version>.all.deb` (or extract and move: `sudo dpkg -x accsyn_<version>.all.deb && sudo mv usr/local/accsyn <folder>`)
- **Fedora / RHEL / Rocky / AlmaLinux (.rpm):** `sudo dnf install ./accsyn-<version>.x86_64.rpm`
- **openSUSE (.rpm):** `sudo zypper install ./accsyn-<version>.x86_64.rpm`

  

Verify the application by running it and logging on to accsyn.

  

### Linux desktop launchers

These are normally created by the installers, but can be manually created as required.

  

Ubuntu:

Create  ~/.local/share/applications/accsyn.desktop (system wide: /usr/share/applications)

```ini
[Desktop Entry]
Name=accsyn
Comment=Launch accsyn
Exec=/usr/local/accsyn/accsyn App
Icon=/usr/local/accsyn/accsyn_icon_512.png
Terminal=false
Type=Application
Categories=Utility
```

## Manage

### Updating

To stay on top of bug fixes, and get the latest features and improvements, update the accsyn desktop app regularly.

  

If installed for current user:

- Log on to the desktop app
- Click on the user account button in upper right corner.
- Choose "Check for updates" in the dropdown menu.

  

*Note: if the in-app update fails, download the installer using the link presented and re-install using the instructions above.*

  

If installed for all users (administrative rights required):

Download the installer and re-install using the instructions above.

  

### Log file location

The log files can contain useful hints during troubleshooting:

Windows

```bash
%APPDATA%\accsyn\log
```

Mac

~/Library/Logs/com.accsyn/log

Linux

```bash
~/.accsyn/log
```
  

### Local preferences

The app stores local preferences and user data at these locations: 

Windows

```bash
%APPDATA%\accsyn\data
```

Mac

```bash
~/Library/Logs/com.accsyn/data
```

Linux
```bash
~/.accsyn/data
```

## Troubleshooting

General/platform independent

### I have trouble logging in, it never gets past the login screen

Cause: the accsyn local preferences might have become corrupt. 

Solution: try removing these preference folders manually and retry the operation. 

  

Linux

### I am getting java.lang.UnsupportedOperationException: Setting a system-wide Policy object is not supported

Cause: You are trying to install the accsyn desktop app on a system that has the accsyn daemon installed.

Solution: Download and update using the daemon instead.

  
  

Having further issues? Please reach out to support providing your logs folder compressed together with screenshots and a detailed description of your issue.

### Related articles

[Daemon(service)](/admin/server/)

[File Sharing](/collaboration/)

[Media Vault](/vault/)
