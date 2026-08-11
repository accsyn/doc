# Render farm

NOTE: This feature is exposed to BYOS workspaces only.

[BYOS](../admin/byos.md)

This guide walks through how to setup a render farm with your accsyn Workspace

CONTENT

[What is a Render farm?](farm.md)

[How does it work?](farm.md)

[Engines](farm.md)

[Lanes](farm.md)

[Filters](farm.md)

[Pools](farm.md)

[Licensing](farm.md)

[Engine source code](farm.md)

[Prerequisites](farm.md)

[Enabling compute feature](farm.md)

[Installing engines](farm.md)

[Common engine](farm.md)

[Application engine](farm.md)

[Installing and configuring a render server](farm.md)

[Submitting a render job](farm.md)

[Prerequisites](farm.md)

[Submit using the accsyn Desktop app](farm.md)

[Submit using the accsyn Python API](farm.md)

[Cross-site rendering](farm.md)

[Prerequisites](farm.md)

[Setting up remote render](farm.md)

[How it works](farm.md)

[Considerations](farm.md)

[Building your own submitter](farm.md)

[Breakdown of the submitter](farm.md)

[Conclusion](farm.md)

[Building your own render engine](farm.md)

[Developer guidelines/prerequisites](farm.md)

[Script structure](farm.md)

[Other resources](farm.md)

## What is a Render farm?

Render farm, also called Compute Cluster, is a software that is designed to queue up and execute resource (CPU and/or GPU) intensive long running tasks on a group of computers.

It is commonly used in post production for image processing, offloading heavy workloads from workstations to a set of dedicated render nodes.

accsyn has built in render farm functionality, providing execution of render applications through Python script based engines. By combining file transfers with render jobs, accsyn supports building a render farm that spans multiple physical locations such at on-prem and cloud rendering.

## How does it work?

The accsyn render farm feature is API centric and is designed to be integrated into other Python enabled applications such as DCC (Digital Content Creation) softwares (Maya, Unreal, Houdini etc), although render jobs can be submitted using the [accsyn Desktop app](../admin/desktop-app.md) to some extent.

  

Note: Reach out to the accsyn support if you need the desktop app extended to fully support render job submission.

  

accsyn provides queue management out of the box, as part of the file transfer mechanism. Render jobs are just a different type of jobs that instead of transferring files, execute applications through "engines". 

Render jobs can have file transfer dependencies, and these are set up if a job is submitted from another site or if the render job should render on a remote site. This makes accsyn the only render manager to fully support multi-site/cloud render workflows natively.

  

### Engines

Each render application, e.g. Houdini, FFmpeg, Unreal Engine and so on, is defined by an Engine in accsyn.

An engine consist of a freely customisable Python script, that is synchronised and executed in runtime at render nodes.

There is the mandatory Common engine, that must be installed before any other engines can be installed. The common engine provides the base Python class for engines, and has shared functions and interfaces that is used by the engine.

  

### Lanes

To be able to provide parallellism, accsyn provide something called a "lane". A lane is a virtual render server on a physical server, each server can have one ore more lanes.

Each lane can have one or more engines assigned, enabling basic planning of your render farm - define which machines are allowed to execute which applications.

  

### Filters

Filters are how you define the rules for each job, for example only render at machines having at least 64GB of RAM or on a certain pool (see below).

  

### Pools

To provide more advanced render farm scheduling, accsyn supports something called "pools". A pool is a group of render servers, and each render job can use a pool in different ways through filtering:

- Include; Only run at servers part of the pool.
- Exclude; Never run on servers part of the pool.
- If unused; Run on servers if no other job is including them.
- Dedicated; Alwas run on these servers, even if other jobs higher up in queue are using them.

## Licensing

The accsyn Render farm feature is licensed per configured render server, were a configure render server is a server with at least on engine assigned and enabled. There is no restrictions on number of engines or amount of rendered jobs or frames.

The amount of active render servers are measured each night at 00:00 CET and the monthly top notation is used as reference for next billing period invoice.

For more information, please visit <https://accsyn.com/pricing>. To check your current render farm usage, visit your workspace billing page @ <https://accsyn.io/signup>.

## Engine source code

accsyn provides a set of default engine scripts, available as open source on Github:

[Github](https://www.google.com/url?q=https%3A%2F%2Fgithub.com%2Faccsyn%2Fcompute-scripts&sa=D&sntz=1&usg=AOvVaw1HU23EYktAZKPIUbUC3yeS)

You are free to fork off these or create your own engine scripts, as needed. Feel free to reach out to support providing suggesting for improvement and pull requests.

## Prerequisites

- An active BYOS accsyn workspace and an active administrator login.
- One or morededicated render computers, with the render application installed and licensed.

  

In this guide we will showcase how to setup render of Houdini 20.5 mantra scenes on a bunch of Windows machines, using the already available compute scripts provided on our Github.

## Enabling compute feature

As a first step, we need to enable compute:

1. Go to [admin.io/admin/settings](http://admin.io/admin/settings) and Compute tab.
2. Check Enable compute.

## Installing engines

### Common engine

Before we can install any engines, we need to install the common engine - the base:

1. Logon as an administrator at [accsyn.io/admin/engines](http://accsyn.io/admin/engines) and click Create engine.
2. Enter the engine name common.
3. Open the common script on Github as raw, link: <https://raw.githubusercontent.com/accsyn/compute-scripts/refs/heads/main/source/common.py>
4. Copy the script and paste in Python script entry.
5. (Optional) Set description and vendor [accsyn]. Color has no effect here.
6. Click Create & Publish.

You now have the base setup.

  

### Application engine

- Logon as an administrator at [accsyn.io/admin/engines](http://accsyn.io/admin/engines) and click Create engine.
- Enter the application engine name, we recommend giving the exact same name as the python script is named, without the .py extension [mantra-20.5]
- Open the common script on Github as raw, link: <https://raw.githubusercontent.com/accsyn/compute-scripts/refs/heads/main/source/mantra-20.5.py>
- Copy the script and paste in Python script entry.
- (Optional) Set description
- (Optional) Set vendor (SideFX).
- (Optional) Set the color, used in farm view to distinguish applications.
- Click Create & Publish.

You now have a configured render farm and are ready to install nodes.

## Installing and configuring a render server

To be able to execute engine scripts, you will need a server:

1. Go to Workspace menu>Administrate>Servers (<https://accsyn.io/admin/servers>) and click INSTALL SERVER.
2. Choose Render server role.
3. Conclude the server installation by installing the daemon and authenticate it using the code displayed.
4. Edit the server and go to Lanes & Engines tab.
5. One lane should be displayed, to change the number of lanes - go to Attributes tab.
6. Right click on the lane, choose the engine [Mantra 20.5] and choose Available.

  

The render server is now setup and ready to run jobs, reload the web admin pages to have the Farm menu option appear on left hand side - use it to monitor your render servers.

## Submitting a render job

### Prerequisites

Prepare the file to render and save it with dependencies to an accsyn volume. To be able to render, the input file(s) and dependencies has to reside on an accsyn volume. Also the generated output file(s) needs to be written back to a volume.

In this guide we need an exported .ifd 100 frames file sequence from Houdini ready to be rendered with Mantra in command line mode.

Finally, the submitting user account needs access to the volume. Standard users can be given explicit access to submit render jobs (see Manage render farm section).

  

### Submit using the accsyn Desktop app

Notes/hints: 

- Submitting render jobs from the accsyn web UI is not supported yet.
- Newly added engines, or your custom engines, are not automatically available/supported to submit with desktop app. Please reach our to support making a implementation request.
- To view the resulting render job submit API payload, click the JSON button next to RENDER button - it is very helpful when designing your own API based submit logic.

  

1. Download and install the [accsyn Desktop app](../admin/desktop-app.md).
2. Login using with a user that has permission to access the input files at the volume, and submit render jobs.
3. Open the Render tab.
4. Drag and drop the input file [render.01001.ifd] on the area or click Storage button and browse to the file.
5. Eventual input file sequence will be detected.
6. Check Parse input for dependencies to have accsyn parse ascii input file(s) for dependencies when engine is selected, and track them - enables proper cross-site rendering.
7. Select the engine [Mantra 20.5]
8. Enter the frame range to render, either as a single continuous range or a set of ranges [1001-1100]. See examples below
9. (Optional) Enter one or more frames or ranges to render before the rest, it has to be within the main frame range above.
10. (Optional) Adjust the job attributes as needed, see below for descriptions.
11. Click RENDER in bottom right corner to submit the job to the farm.

  

Render job attributes/settings:

- Split mode (for engine supporting items); choose if should render the entire job on a single machine without splitting (Single task) or if it should be split up in buckets(default: 5 frames per machine) across render servers.
- Filter:Estimated RAM usage; Only run on servers having at least the ram amount chosen.
- Filter:Select which site(s) to render at (cross-site render only); Choos the sites to render at, default is to render on all available server across all sites.
- Manual filter input; Manually enter filters, comma(,) separated list of filter expressions that all must be fulfilled before render is dispatched to a server. Syntax:

  - RAM spec; 

    - ram:>60GB only run at machines having at least 60GB ram.
    - ram:<60GB only run at machines having less than 60GB ram.
  - Cores spec; 

    - cores:=12only run at machines having exactly 12 cores (threads). < and > operators works aswell.
  - Site constraints; 

    - site:dupp+sthlm only run at the sites "dupp" and "sthlm".
    - site:-dupp exclude site "dupp".
  - Hostname constraints; 

    - hostname:ws01+ren01: only run at servers "ws01" & "ren01". Define site & hostname:
    - hostname:dupp/pc01. hostname:\*render\*: only render at servers having "render" in their hostname.
  - Pool constraints (each server can be member of one or more pools):

    - pool:+mypool only run a servers member of "mypool";
    - pool:-mypool avoid servers member of pool "mypool".
    - pool:~mypool use pool "mypool" if it is free - no other job includes the pool.
    - pool:@mypool have dedicated access to pool "mypool" servers, but also utilise other servers if they are available.
  - Dependencies; Enter path to each dependency one entry per row, either a local path on the form "D:\picture.png" or an accsyn path on the form "volume=projects/picture.png". Will be uploaded to workspace volume in the same manner as a local input file would, and distributed to remote rendering site in a cross-site rendering setup.
  - Upload dependencies to <workspace name>; If selected, the dependencies will be uploaded as part of the render job. De-select this if you already have sorted the synk by other means.
  - Output; Browse/create folder on accsyn storage were the result should be written by the engine/render application.
  - Clear output directory; Define if the output directory should be cleared before render is started on a new site, mitigates stray files present from previous renders to the same folder.
  - Download output from <workspace name> on finished items(s)/tasks(s); Decide if output should be continously synked back to submitting machine when a engine completes execution on a render server.
  - Additional render parameters (advanced); Define default DCC render command line parameters and other advanced attributes.
  - Common and platform environment variables; Enter environment variables, one entry per row, on the form "FLEXLM\_DIAGNOSTICS=2".
  - Bucket size; Define how many items/task should be collected and dispatched to each render server. Requires engines to support items - e.g. each input file can be used for rendering multiple images defined by sub frame ranges (Maya, Nuke etc).

  

### Submit using the accsyn Python API

The accsyn Python API allows for integrating render job submission inside the DCC application, or from another external tool. As mentioned above, you can use the JSON button in desktop app submitter to inspect the REST payload as it would have been submitted to accsyn - very handy when developing your own submitter.

Detailed information about the Python API and how to submit render jobs, are available within our Python API documentation:

[API Documentation](https://www.google.com/url?q=https%3A%2F%2Faccsyn-python-api.readthedocs.io%2Fen%2Flatest%2Frender.html&sa=D&sntz=1&usg=AOvVaw2SZZ54BWSGTwTnYJhDZX6D)

Compute job JSON payload examples can be found here:

[Job JSON Specification](job-specification.md)

You can also find an API example below in the section Building your own submitter.

## Cross-site rendering

Normally, all renders are executed on server computes physically located at the same premises as the file server were the accsyn storage server daemon is running, and there is no need to render elsewhere.

But in some scenarios, one would want to distribute the render of a job across multiple physical or cloud locations. This could be a remote office, a single power workstation located at an employee home office or at cloud infrastructure like GCE or AWS.

accsyn are one of the few platforms that supports this, and it is called cross-site rendering.

  

### Prerequisites

- At least one active remote site, manage sites at <https://accsyn.io/admin/sites>.
- A site server running at the remote site, serving the volume(s) were render input files and dependencies are located.
- Verified working file transfers between main site (hq) and the remote site.

  

### Setting up remote render

As a first step, you will need to install at least one render server at the remote site. Follow the same instructions as you would for a render server at main premises - install & license DCC render applications and then install a new server @ <https://accsyn.io/admin/servers>. Remember to choose the remote rendering site when creating the server.

You are now basically all set to render, existing render jobs cannot utilise the new site but new render jobs will automatically have sync tasks created for the new tasks that will be activated as soon as an available render server is to be utilised.

  

### How it works

1. Before the first item/task is launched, the download sync task for site is kicked into gear once. The synk task has sub tasks, one or more for the input file(s) and then one for each dependency. This to make sure that all data required by the DCC render application is available on the site before launched.
2. Whenever an item/task finishes, the upload sync task for site is retried unless already running. This to make sure the result is "streamed" back to the main premises and available for review.

  

### Considerations

Cross-site rendering can be complex if the render process uses licenses or other network assets that are not available on all sites. Make sure to have these dependencies synced properly each time they are update, or add them as a sync dependency with the job API submit payload to be sure everything is read to go.

Also, syncing assets during render can cause extra overhead especially if the dependencies are huge and/or the site network bandwidth is limited. Always lock down the scenarios were you allow users to submit renders to remote sites, to avoid congestion and long delays in production.

## Building your own submitter

As mentioned earlier, accsyn farm feature is API first meaning that it is primarily designed to be integrated into other software or built into your own production toolset.

In this example we build a minimal Python (PySide) based submitter designed to be launched as a standalone desktop application, source code.

  

accsyn-submitter.py:

import os

import sys

import re

import traceback

  

# pip install accsyn-python-api

import accsyn\_api

  

# pip install PySide6

from PySide6 import QtWidgets

from PySide6.QtWidgets import (

    QDialog, QApplication, QVBoxLayout, QHBoxLayout, QFormLayout,

    QComboBox, QLineEdit, QPushButton, QLabel, QMessageBox

)

from PySide6.QtCore import Qt

from PySide6.QtGui import QColor

  

class SubmitterDialog(QDialog):

    """Dialog for submitting a generic render job to accsyn"""

    def \_\_init\_\_(self, parent=None):

        super(SubmitterDialog, self).\_\_init\_\_(parent)

        self.setWindowTitle("Accsyn Render Farm Submitter")

        self.setMinimumWidth(600)

        # Create farm session object, requires environment variables set:

        #    ACCSYN\_WORKSPACE=<workspace API code>

        #    ACCSYN\_API\_USER=<accsyn user ident (email)>

        #    ACCSYN\_API\_KEY=<secret API key, generated from https://accsyn.io/developer>

        self.session = accsyn\_api.Session()

  

        self.engines = []

        self.setup\_ui()

        self.load\_engines()

    def setup\_ui(self):

        """Setup the user interface"""

        layout = QVBoxLayout(self)

        layout.setSpacing(10)

        layout.setContentsMargins(15, 15, 15, 15)

        # Engine selection row

        engine\_row = QHBoxLayout()

        engine\_label = QLabel("Engine:")

        engine\_label.setMinimumWidth(80)

        self.engine\_combo = QComboBox()

        self.engine\_combo.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

        engine\_row.addWidget(engine\_label)

        engine\_row.addWidget(self.engine\_combo)

        layout.addLayout(engine\_row)

        # Input field row

        input\_row = QHBoxLayout()

        input\_label = QLabel("Input:")

        input\_label.setMinimumWidth(80)

        self.input\_field = QLineEdit()

        self.input\_field.setPlaceholderText("share=<share ident>/<path>/<to>/<a file>")

        self.input\_field.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

        input\_row.addWidget(input\_label)

        input\_row.addWidget(self.input\_field)

        layout.addLayout(input\_row)

        # Range field row

        range\_row = QHBoxLayout()

        range\_label = QLabel("Range:")

        range\_label.setMinimumWidth(80)

        self.range\_field = QLineEdit()

        self.range\_field.setPlaceholderText("1-100")

        self.range\_field.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

        range\_row.addWidget(range\_label)

        range\_row.addWidget(self.range\_field)

        layout.addLayout(range\_row)

        # Output field row

        output\_row = QHBoxLayout()

        output\_label = QLabel("Output:")

        output\_label.setMinimumWidth(80)

        self.output\_field = QLineEdit()

        self.output\_field.setPlaceholderText("share=<share ident>/<path>/<to>/<folder>")

        self.output\_field.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

        output\_row.addWidget(output\_label)

        output\_row.addWidget(self.output\_field)

        layout.addLayout(output\_row)

        # Buttons row

        button\_layout = QHBoxLayout()

        self.cancel\_button = QPushButton("Cancel")

        self.cancel\_button.clicked.connect(self.reject)

        button\_layout.addWidget(self.cancel\_button)

        button\_layout.addStretch()  # Spacer in the middle

        self.submit\_button = QPushButton("SUBMIT")

        self.submit\_button.setStyleSheet("""

            QPushButton {

                background-color: #4CAF50;

                color: white;

                font-weight: bold;

                padding: 8px 20px;

                border: none;

                border-radius: 4px;

            }

            QPushButton:hover {

                background-color: #45a049;

            }

            QPushButton:pressed {

                background-color: #3d8b40;

            }

        """)

        self.submit\_button.clicked.connect(self.on\_submit)

        button\_layout.addWidget(self.submit\_button)

        layout.addLayout(button\_layout)

    def load\_engines(self):

        """Query all engines from accsyn that have type=compute"""

        try:

            engines = self.session.find("engine where type=compute")

            self.engines = engines if engines else []

            # Populate combobox

            self.engine\_combo.clear()

            if self.engines:

                for engine in self.engines:

                    # Engine might be a dict with 'name' or 'code' field, or just a string

                    if isinstance(engine, dict):

                        name = engine.get('name') or engine.get('code') or str(engine)

                    else:

                        name = str(engine)

                    self.engine\_combo.addItem(name, engine)

            else:

                self.engine\_combo.addItem("No compute engines found", None)

                self.submit\_button.setEnabled(False)

        except Exception as e:

            QMessageBox.warning(self, "Error Loading Engines", 

                              f"Failed to load engines from accsyn:\n\n{str(e)}\n\n{traceback.format\_exc()}")

            self.engine\_combo.addItem("Error loading engines", None)

            self.submit\_button.setEnabled(False)

    def validate\_input\_path(self, path):

        """Validate input path format: share=<share ident>/<path>/<to>/<a file>"""

        if not path:

            return False, "Input path is required"

        # Pattern: share=<identifier>/<path components>

        pattern = r'^share=[^/]+(/[^/]+)+$'

        if not re.match(pattern, path):

            return False, "Input path must be in format: share=<share ident>/<path>/<to>/<a file>"

        return True, None

    def validate\_output\_path(self, path):

        """Validate output path as accsyn shaped folder path"""

        if not path:

            return False, "Output path is required"

        # Similar pattern to input, but should be a folder path

        # Accsyn paths typically start with share=

        pattern = r'^share=[^/]+(/[^/]+)+/?$'

        if not re.match(pattern, path):

            return False, "Output path must be a valid accsyn folder path (share=<share ident>/<path>/<to>/<folder>)"

        return True, None

    def validate\_range(self, range\_str):

        """Validate frame range format: 1-100"""

        if not range\_str:

            return False, "Range is required"

        # Pattern: number-number

        pattern = r'^\d+-\d+$'

        if not re.match(pattern, range\_str):

            return False, "Range must be in format: 1-100"

        # Check that start <= end

        try:

            start, end = map(int, range\_str.split('-'))

            if start > end:

                return False, "Start frame must be less than or equal to end frame"

        except ValueError:

            return False, "Range must contain valid numbers"

        return True, None

    def validate\_fields(self):

        """Validate all input fields"""

        errors = []

        # Validate engine

        if self.engine\_combo.currentData() is None:

            errors.append("Please select a valid engine")

        # Validate input path

        input\_path = self.input\_field.text().strip()

        valid, error\_msg = self.validate\_input\_path(input\_path)

        if not valid:

            errors.append(f"Input: {error\_msg}")

        # Validate range

        range\_str = self.range\_field.text().strip()

        valid, error\_msg = self.validate\_range(range\_str)

        if not valid:

            errors.append(f"Range: {error\_msg}")

        # Validate output path

        output\_path = self.output\_field.text().strip()

        valid, error\_msg = self.validate\_output\_path(output\_path)

        if not valid:

            errors.append(f"Output: {error\_msg}")

        return errors

    def build\_payload(self):

        """Build the accsyn API render farm submit JSON payload"""

        engine\_data = self.engine\_combo.currentData()

        # Get engine identifier (could be string or dict with 'code' or 'name')

        if isinstance(engine\_data, dict):

            engine = engine\_data.get('code') or engine\_data.get('name') or str(engine\_data)

        else:

            engine = str(engine\_data)

        # Parse frame range

        range\_str = self.range\_field.text().strip()

        start\_frame, end\_frame = map(int, range\_str.split('-'))

        payload = {

            'engine': engine,

            'input': self.input\_field.text().strip(),

            'output': self.output\_field.text().strip(),

            'range': f"{start\_frame}-{end\_frame}",

        }

        return payload

    def submit\_job(self, payload):

        """Submit job to accsyn API"""

        try:

            result = self.session.create('job', payload)

            return True, result

        except Exception as e:

            return False, str(e)

    def on\_submit(self):

        """Handle submit button click"""

        # Validate fields

        errors = self.validate\_fields()

        if errors:

            error\_msg = "Please correct the following errors:\n\n" + "\n".join(f"• {error}" for error in errors)

            QMessageBox.warning(self, "Validation Error", error\_msg)

            return

        # Build payload

        payload = self.build\_payload()

        # Submit job

        success, result = self.submit\_job(payload)

        if success:

            QMessageBox.information(

                self,

                "Job Submitted",

                f"Job were submitted successfully to accsyn!\n\nID: {result['id']}"

            )

            self.accept()

        else:

            QMessageBox.critical(

                self,

                "Submission Failed",

                f"Failed to submit job:\n\n{result}\n\n{traceback.format\_exc()}"

            )

  
  

if \_\_name\_\_ == '\_\_main\_\_':

    app = QApplication(sys.argv)

    dialog = SubmitterDialog()

    dialog.show()

    sys.exit(app.exec())

### Breakdown of the submitter

  

- Imports/dependencies; Besides standard python libraries, the script requires the libraries "accsyn-python-api" and "PySide6" to be available in the running environment.
- Class init; Here the accsyn API session is created, it assumes accsyn API credentials stored in environment variables. They can also be submitted as arguments to the Session(..) call.
- setup\_ui; Create the the simple GUI were the user can choose engine, input the file to render, frame range and were to save the images.
- load\_engines; This utility function loads available engines from accsyn. Requires at least one standard type (compute) engine to be available.
- validate\_input\_path & validate\_output\_path; Makes sure that path is on accsyn form/notation.
- validate\_range; Validate frame range number expression (start-end)
- validate\_fields; Validates all values entered by the user.
- build\_payload; Builds the API submit payload based on the user input.
- submit\_job; Submits the render farm job to accsyn.
- on\_submit; Handle submit button click.
- Main bootstrap; executed when launched like "python3 <path/to/[submitter.py](http://submitter.py)>"

  

Many more user inputs can be added depending on the engine and the different use cases.

  

### Conclusion

The simplistic accsyn API makes it easy to programatically submit render jobs with minimal effort, either from Python scripts integrated within DCC applications or in standalone desktop tooling.

## Building your own render engine

Most likely, the default engines provided by accsyn does not cover your needs and you will need to create your own engine script. This guide walks through the basics, we recommend you take a look at the existing engine scripts to get inspiration.

  

### Developer guidelines/prerequisites

- A code editor (IDE) - Visual Studio Code, PyCharm or similar.
- Python 3
- (Recommended) Source code control - Git(hub)/Perforce/CVS.

  

### Script structure

Engine scripts must adhere the following base structure:

..

class Engine(Common):

    \_\_revision\_\_ = 1  # Will be automatically increased each publish

    # -- ENGINE CONFIG START --

    SETTINGS = {

      "items": True,

      "filename\_extensions": ".nk",

      ..

    }

  

    PARAMETERS = {"mapped\_share\_paths": [], "arguments": ["-txV"], "input\_conversion": "auto"}

    # -- ENGINE CONFIG END --

  

    ..

    def \_\_init\_\_(self, argv):

        super(Engine, self).\_\_init\_\_(argv)

    ..

  

    def get\_executable(self, preferred\_nuke\_version=None):

        """Return path to executable as string"""

        ...

  

    def get\_envs(self):

        """Get dynamic environment variables"""

        ..

  

    def get\_commandline(self, item):

        """Construct the full command line to execute, returned as a list"""

        ..

    ..

  

if \_\_name\_\_ == '\_\_main\_\_':

    ..

        engine = Engine(sys.argv)

        engine.load()  # Load data

        engine.execute()  # Run

Breakdown of the engine script:

- Engine config; defines the settings for engine, for example if the application supports items or the default command line arguments to pass on to app.

  - items (boolean); True means each input file can the source of multiple output files, for example the case for Maya, Nuke, Houdini. Some renderers like Houdini Mantra and Arnold takes a file sequence as input, still it will be executed as numbered items defined by a sub frame range on each render server. ffmpeg on the other hand does not support items - each input file is executed as a task and generates exactly one or more output files.
  - multiple\_inputs (boolean) True means the the engine script supports multiple inputs, this is false for Maya, Nuke etc but true for ffmpeg.
  - filename\_extensions (string);  Comma separated list of input filename extensions associated with the underlaying (DCC) application, for example ".ma,.mb" for Maya.
  - binary\_filename\_extensions (string); Comma separated list of filename extensions that denotes binary file format, this tells accsyn which input files can be parsed during submit with the desktop app or now.
  - binary (boolean); Tells accsyn that all input files are binary.
  - default\_range (string); The default frame range to suggest in desktop app submitter.
  - default\_bucketsize (number); The default bucket size to suggest in desktop app submitter.
  - max\_bucketsize (number); The maximum bucket size render application supports.
  - default\_output\_path (string); Suggest this default output path.
  - type; The type of engine, default is "compute" for DCC rendering applications. The rest is special engines not covered by this documentation.
- Init; instantiate the engine, and also define additional class variables.
- Get executable; Evaluate and return the path to application binary executable, will be the first element of command line.
- Get envs; (Optional) Build a dictionary holding environment variables to pass on to application.
- Get commandline; Build the full command line to launch.

## Other resources

[Python API](python-api.md)

Get to learn more about the accsyn Python API.

[Case Study](https://www.google.com/url?q=https%3A%2F%2Faccsyn.com%2Fcasestudy-stillerstudios-hfs%2F&sa=D&sntz=1&usg=AOvVaw3qJqkJvfwSbH-PkgyzhFPl)

Learn how accsyn were implemented at Stiller Studios for rendering the Handbok För Superhjältar animated feature.
