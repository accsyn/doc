# Tutorial — API driven delivery

## Introduction

This tutorial walks through sending a delivery (and an upload request) with the accsyn Python API — useful when you want deliveries to fall out of your own tools or scripts instead of clicking through the UIs every time.

It works for both **Cloud** and **BYOS** workspaces. The idea is the same: files already sit on your default volume, you create a delivery with a short Python script, and the recipient gets the usual email with a download link. Large packages still go over the accelerated [ASC](/whitepaper/) protocol when they use the Desktop App.

We will cover:

- Starting a workspace (Cloud or BYOS)
- Assuming a simple project folder on volume `storage`
- Creating an API key
- Installing the Python API (with pyenv)
- Creating a delivery from an existing file on storage
- Creating an upload request into an existing folder

*NOTE: Made-up example data is provided in [brackets] throughout this tutorial.*

## Setting up your workspace

If you already have a working Cloud or BYOS workspace, skip ahead.

Otherwise create a trial workspace — the process is described in detail [here](/trial/):

1. Open <https://accsyn.io/trial> in your browser and sign up with your personal accsyn account (email).
2. Create either a **Cloud** workspace or a **BYOS** workspace, depending on whether you want hosted storage or your own server.
3. For BYOS, install and connect your storage server as guided in the UI (more in [BYOS](/admin/byos/)).

Hint: your workspace API code / domain is shown at <https://accsyn.io/admin/settings> under the General tab. You will need it when creating the API session.

*Note: The API is not available on Cloud Essentials or BYOS Lite.*

## Example storage layout

Throughout this tutorial we assume:

- Default volume name / code: **storage**
- Folder structure: `MYPROJECT/FINALS/`
- A large graded master on storage: `MYPROJECT/FINALS/MP_Final_graded_v002.mov`

Put that file on your volume however you normally would (Desktop App upload, file sharing, or BYOS disk). Paths in the API are relative to the default volume unless you spell out `volume=` / `folder=` / `share=` notation.

We will deliver that MOV to [demo.user@accsyn.com], and later ask them to upload pitch material into a folder `PITCH_MATERIAL` on the same volume.

## Create an API key

You need an API key for the user that should create deliveries (admin or employee with access to the files).

1. Open <https://accsyn.io/developer> (user menu → **Developer**).
2. Click **Create API Key**.
3. Optionally set lifetime, IP restrictions and permissions.
4. Copy the key when it is shown — it is only displayed once. Treat it like a password.

More detail: [Python API — API keys](/developer/python-api/).

## Install the Python API

We will use Python 3. A virtual environment keeps things tidy — [pyenv](https://github.com/pyenv/pyenv) is a good way to manage Python versions and envs on Mac/Linux.

Example with pyenv:

```bash
pyenv install 3.12.0
pyenv virtualenv 3.12.0 accsyn-api
pyenv activate accsyn-api
pip install accsyn-python-api python-dateutil
```

On Windows you can use `venv` the same way:

```bash
python -m venv accsyn-api
accsyn-api\Scripts\activate
pip install accsyn-python-api python-dateutil
```

`python-dateutil` is handy for parsing expiry timestamps in the examples below.

Full install options (pip, Poetry, from source) are in [Python API](/developer/python-api/).

## Deliveries and the Python API

A delivery in the API is the same thing you create in the web app: one or more files/folders, one or more recipients, optional message and expiry. When you create a delivery with files already on storage and a recipient list, accsyn submits it and emails the recipients a link — they download with the Desktop App (ASC) or the browser for smaller packages.

You can also create **upload requests** (reverse deliveries) that point at a folder on storage so people can send material back to you.

The API does not push the file bytes itself for a storage-based delivery — it creates the delivery job and notifications. Recipients still pull the package with their client. Temporary deliveries that need a local upload first work differently (transfer job into the delivery); this tutorial sticks to files already on storage.

Reference: [Deliveries in the Python API docs](https://accsyn-python-api.readthedocs.io/en/latest/deliveries.html).

## Example — create a delivery

Save something like `create_delivery.py`. Replace workspace, username and API key with your own.

```python
import accsyn_api
import dateutil.parser

session = accsyn_api.Session(
    workspace="[acmefilm]",
    username="[admin@acmefilm.com]",
    api_key="[YOUR_API_KEY]",
)

delivery = session.create(
    "Delivery",
    {
        "name": "MP Final graded v002",
        "tasks": ["myproject/FINALS/MP_Final_graded_v002.mov"],
        "recipients": ["lisa@example.com"],
        "description": "Here is the finaly delivery",
        "expires": dateutil.parser.parse("2026-11-06T08:23:08.629+0000"),
    },
)

print("Created delivery:", delivery["id"], delivery.get("name"))
```

What this does:

1. Opens a session against your workspace with the API key.
2. Creates a delivery named *API test del* containing the graded MOV (path relative to default volume `storage`).
3. Invites `demo.user@accsyn.com`, sets a short description and an explicit expiry.
4. Submits straight away — the recipient gets the email with the download link.

Check the delivery under **Outbound** at <https://accsyn.io/outbound>, or have the recipient follow [Receive a delivery](/delivery/receive/).

## Example — create an upload request

Same session idea; this asks the user to upload into an existing folder on storage (here `PITCH_MATERIAL` on the default volume):

```python
import accsyn_api
import dateutil.parser

session = accsyn_api.Session(
    workspace="[acmefilm]",
    username="[admin@acmefilm.com]",
    api_key="[YOUR_API_KEY]",
)

upload_request = session.create(
    "Request",
    {
        "name": "API req test",
        "destination": "PITCH_MATERIAL",
        "recipients": ["lisa@example.com"],
        "description": "Please upload the pitch material here",
        "expires": dateutil.parser.parse("2026-12-06T08:23:08.629+0000"),
    },
)

print("Created upload request:", upload_request["id"], upload_request.get("name"))
```

Make sure the destination folder exists on storage first (create it in the Desktop App or Storage view). The request is submitted immediately and the recipient gets an upload link. You can monitor it under **Requested** / Inbound in the web app.

## Where to go next

- [Deliveries API reference](https://accsyn-python-api.readthedocs.io/en/latest/deliveries.html) — temporary deliveries, recipients, abort/finish, listing transfers
- [Create a delivery](/delivery/create/) — same concepts in the UI, including the short API section
- [Job specification](/developer/job-specification/) — richer job JSON when you outgrow the simple create calls
- [Remote office sync](/tutorials/remote-office-sync/) — another Python API tutorial focused on site sync
