# Render farm

*NOTE: This feature is exposed to standard (not Lite) [BYOS](../admin/byos/index.md) workspaces only.*

This guide walks through how to set up a render farm with your accsyn Workspace.

## What is a Render farm?

Render farm, also called Compute Cluster, is software that is designed to queue up and execute resource (CPU and/or GPU) intensive long-running tasks on a group of computers.

It is commonly used in post-production for image processing, offloading heavy workloads from workstations to a set of dedicated render nodes.

accsyn has built-in render farm functionality, providing execution of render applications through Python script based engines. By combining file transfers with render jobs, accsyn supports building a render farm that spans multiple physical locations such as on-prem and cloud rendering.

## How does it work?

The accsyn render farm feature is API centric and is designed to be integrated into other Python enabled applications such as DCC (Digital Content Creation) software (Maya, Unreal, Houdini etc.), although render jobs can be submitted using the [accsyn Desktop app](../desktop-app.md) to some extent.

  

*Note: Reach out to the accsyn support if you need the desktop app extended to fully support render job submission.*

  

accsyn provides queue management out of the box, as part of the file transfer mechanism. Render jobs are just a different type of job that, instead of transferring files, execute applications through "engines". 

Render jobs can have file transfer dependencies, and these are set up if a job is submitted from another site or if the render job should render on a remote site. This makes accsyn the only render manager to fully support multi-site/cloud render workflows natively.

  

### Engines

Each render application, e.g. Houdini, FFmpeg, Unreal Engine and so on, is defined by an Engine in accsyn.

An engine consists of a freely customisable Python script that is synchronised and executed at runtime at render nodes.

There is the mandatory Common engine, that must be installed before any other engines can be installed. The common engine provides the base Python class for engines, and has shared functions and interfaces that are used by the engine.

  

### Lanes

To be able to provide parallelism, accsyn provides something called a "lane". A lane is a virtual render server on a physical server; each server can have one or more lanes.

Each lane can have one or more engines assigned, enabling basic planning of your render farm - define which machines are allowed to execute which applications.

  

### Filters

Filters are how you define the rules for each job, for example only render at machines having at least 64GB of RAM or on a certain pool (see below).

  

### Pools

To provide more advanced render farm scheduling, accsyn supports something called "pools". A pool is a group of render servers, and each render job can use a pool in different ways through filtering:

- Include; Only run at servers part of the pool.
- Exclude; Never run on servers part of the pool.
- If unused; Run on servers if no other job is including them.
- Dedicated; Always run on these servers, even if other jobs higher up in the queue are using them.

## Licensing

The accsyn Render farm feature is licensed per configured render server, where a configured render server is a server with at least one engine assigned and enabled. There are no restrictions on the number of engines or the amount of rendered jobs or frames.

The number of active render servers is measured each night at 00:00 CET and the monthly top notation is used as the reference for the next billing period invoice.

For more information, please visit <https://accsyn.com/pricing>. To check your current render farm usage, visit your workspace billing page @ <https://accsyn.io/signup>.

## Engine source code

accsyn provides a set of default engine scripts, available as open source on GitHub:

[GitHub](https://www.google.com/url?q=https%3A%2F%2Fgithub.com%2Faccsyn%2Fcompute-scripts&sa=D&sntz=1&usg=AOvVaw1HU23EYktAZKPIUbUC3yeS)

You are free to fork off these or create your own engine scripts, as needed. Feel free to reach out to support providing suggestions for improvement and pull requests.

## Prerequisites

- An active standard (not Lite) BYOS accsyn workspace and an active administrator login.
- One or more dedicated render computers, with the render application installed and licensed.

  

In this guide we will showcase how to set up rendering of Houdini 20.5 mantra scenes on a bunch of Windows machines, using the already available compute scripts provided on our GitHub.

## Enabling compute feature

As a first step, we need to enable compute:

1. Go to [admin.io/admin/settings](http://admin.io/admin/settings) and the Compute tab.
2. Check Enable compute.

## Installing engines

### Common engine

Before we can install any engines, we need to install the common engine - the base:

1. Log on as an administrator at [accsyn.io/admin/engines](http://accsyn.io/admin/engines) and click Create engine.
2. Giv it the engine name/code 'common' (Mandatory)
3. Open the common script on GitHub as raw, link: <https://raw.githubusercontent.com/accsyn/compute-scripts/refs/heads/main/source/common.py>
4. Copy the script and paste it in the Python script entry.
5. (Optional) Set description and vendor [accsyn]. Color has no effect here.
6. Click Create & Publish.

You now have the base setup.

### Application engine

Now you are ready to install arbitrary engines, we are providing a "Hello world" example engine that can be used for testing and will be used in this quide.

- Log on as an administrator at [accsyn.io/admin/engines](http://accsyn.io/admin/engines) and click Create engine.
- Enter the application engine name, we recommend giving the exact same name as the Python script is named, without the .py extension [hello-world.py]
- Open the common script on GitHub as raw, link: <https://raw.githubusercontent.com/accsyn/compute-scripts/refs/heads/main/source/hello-world.py>
- Copy the script and paste it in the Python script entry.
- (Optional) Set description
- (Optional) Set vendor [accsyn].
- (Optional) Set the color, used in farm view to distinguish applications.
- Click Create & Publish.

You now have a configured render farm and are ready to install nodes.

## Installing and configuring a render server

To be able to execute engine scripts, you will need a server. You can either configure an existing storage server to process render jobs or install one or more dedicated render servers:

1. Go to Workspace menu>Administrate>Servers (<https://accsyn.io/admin/servers>) and click INSTALL SERVER. Skip to step 4 if you want to enable an existing server.
2. Choose Render server role.
3. Conclude the server installation by installing the daemon and authenticating it using the code displayed.
4. Edit the server and go to Lanes & Engines tab.
5. One lane should be displayed; to change the number of lanes, go to the Attributes tab.
6. Right click on the lane, choose the engine [Mantra 20.5] and choose Available.


The render server is now set up and ready to run jobs. Reload the web admin pages to have the Farm menu option appear on the left-hand side - use it to monitor your render servers.

## Submitting a render job

### Prerequisites

Prepare the file to render and save it with dependencies to an accsyn volume. To be able to render, the input file(s) and dependencies have to reside on an accsyn volume. Also, the generated output file(s) need to be written back to a volume.

In this guide we need an exported .ifd 100-frame file sequence from Houdini ready to be rendered with Mantra in command line mode.

Finally, the submitting user account needs access to the volume. Standard users can be given explicit access to submit render jobs (see Manage render farm section).

  

### Submit using the accsyn Desktop app

Notes/hints: 

- Submitting render jobs from the accsyn web UI is not supported yet.
- Newly added engines, or your custom engines, are not automatically available/supported to submit with the desktop app. Please reach out to support to make an implementation request.
- To view the resulting render job submit API payload, click the JSON button next to the RENDER button - it is very helpful when designing your own API based submit logic.

In this guide, we will just submit a text (.txt) file to be processed by the Hello World engine:

1. Download and install the [accsyn Desktop app](../desktop-app.md).
2. Log in with a user that has permission to access the input files at the volume, and submit render jobs.
3. Open the Render tab.
4. Create/copy a text file to your accsyn storage. Drag and drop the input text file [README.text] on the area or click "Browse Storage" button to select the file.
5. Any input file sequence will be detected.
6. Check Parse input for dependencies to have accsyn parse ASCII input file(s) for dependencies when an engine is selected, and track them - enables proper cross-site rendering.
7. Select the engine [Hello World]
8. Enter the frame range to render, either as a single continuous range or a set of ranges [1001-1100]. See examples below.
9. (Optional) Enter one or more frames or ranges to render before the rest, it has to be within the main frame range above.
10. (Optional) Adjust the render job settings and attributes as needed, see below for descriptions.
11. Click SUBMIT RENDER in bottom right corner to submit the job to the farm.


Render job attributes/settings:

- Split mode (for engines supporting items); choose if it should render the entire job on a single machine without splitting (Single task) or if it should be split up in buckets (default: 5 frames per machine) across render servers.
- Filter:Estimated RAM usage; Only run on servers having at least the RAM amount chosen.
- Filter:Select which site(s) to render at (cross-site render only); Choose the sites to render at, default is to render on all available servers across all sites.
- Manual filter input; Manually enter filters, comma(,) separated list of filter expressions that all must be fulfilled before render is dispatched to a server. Syntax:

  - RAM spec; 

    - ram:>60GB only run at machines having at least 60GB ram.
    - ram:<60GB only run at machines having less than 60GB ram.
  - Cores spec; 

    - cores:=12 only run at machines having exactly 12 cores (threads). < and > operators work as well.
  - Site constraints; 

    - site:dupp+sthlm only run at the sites "dupp" and "sthlm".
    - site:-dupp exclude site "dupp".
  - Hostname constraints; 

    - hostname:ws01+ren01: only run at servers "ws01" & "ren01". Define site & hostname:
    - hostname:dupp/pc01. hostname:\*render\*: only render at servers having "render" in their hostname.
  - Pool constraints (each server can be member of one or more pools):

    - pool:+mypool only run at servers member of "mypool";
    - pool:-mypool avoid servers member of pool "mypool".
    - pool:~mypool use pool "mypool" if it is free - no other job includes the pool.
    - pool:@mypool have dedicated access to pool "mypool" servers, but also utilise other servers if they are available.
  - Dependencies; Enter the path to each dependency one entry per row, either a local path in the form "D:\picture.png" or an accsyn path in the form "volume=projects/picture.png". Will be uploaded to the workspace volume in the same manner as a local input file would, and distributed to the remote rendering site in a cross-site rendering setup.
  - Upload dependencies to <workspace name>; If selected, the dependencies will be uploaded as part of the render job. De-select this if you already have sorted the sync by other means.
  - Output; Browse/create folder on accsyn storage where the result should be written by the engine/render application.
  - Clear output directory; Define if the output directory should be cleared before render is started on a new site, mitigates stray files present from previous renders to the same folder.
  - Download output from <workspace name> on finished items(s)/tasks(s); Decide if output should be continuously synced back to the submitting machine when an engine completes execution on a render server.
  - Additional render parameters (advanced); Define default DCC render command line parameters and other advanced attributes.
  - Common and platform environment variables; Enter environment variables, one entry per row, in the form "FLEXLM_DIAGNOSTICS=2".
  - Bucket size; Define how many items/tasks should be collected and dispatched to each render server. Requires engines to support items - e.g. each input file can be used for rendering multiple images defined by sub frame ranges (Maya, Nuke etc).

  

### Submit using the accsyn Python API

The accsyn Python API allows for integrating render job submission inside the DCC application, or from another external tool. As mentioned above, you can use the JSON button in the desktop app submitter to inspect the REST payload as it would have been submitted to accsyn - very handy when developing your own submitter.

Detailed information about the Python API and how to submit render jobs is available within our Python API documentation:

[API Documentation](https://www.google.com/url?q=https%3A%2F%2Faccsyn-python-api.readthedocs.io%2Fen%2Flatest%2Frender.html&sa=D&sntz=1&usg=AOvVaw2SZZ54BWSGTwTnYJhDZX6D)

Compute job JSON payload examples can be found here:

[Job JSON Specification](job-specification.md)

You can also find an API example below in the section Building your own submitter.

## Cross-site rendering

Normally, all renders are executed on server computers physically located at the same premises as the file server where the accsyn storage server daemon is running, and there is no need to render elsewhere.

But in some scenarios, one would want to distribute the render of a job across multiple physical or cloud locations. This could be a remote office, a single power workstation located at an employee's home office or at cloud infrastructure like GCE or AWS.

accsyn is one of the few platforms that supports this, and it is called cross-site rendering.

  

### Prerequisites

- At least one active remote site, manage sites at <https://accsyn.io/admin/sites>.
- A site server running at the remote site, serving the volume(s) where render input files and dependencies are located.
- Verified working file transfers between main site (hq) and the remote site.

  

### Setting up remote render

As a first step, you will need to install at least one render server at the remote site. Follow the same instructions as you would for a render server at main premises - install & license DCC render applications and then install a new server @ <https://accsyn.io/admin/servers>. Remember to choose the remote rendering site when creating the server.

You are now basically all set to render. Existing render jobs cannot utilise the new site, but new render jobs will automatically have sync tasks created for the new tasks that will be activated as soon as an available render server is to be utilised.

  

### How it works

1. Before the first item/task is launched, the download sync task for the site is kicked into gear once. The sync task has sub tasks, one or more for the input file(s) and then one for each dependency. This is to make sure that all data required by the DCC render application is available on the site before launch.
2. Whenever an item/task finishes, the upload sync task for the site is retried unless already running. This is to make sure the result is "streamed" back to the main premises and available for review.

  

### Considerations

Cross-site rendering can be complex if the render process uses licences or other network assets that are not available on all sites. Make sure to have these dependencies synced properly each time they are updated, or add them as a sync dependency with the job API submit payload to be sure everything is ready to go.

Also, syncing assets during render can cause extra overhead especially if the dependencies are huge and/or the site network bandwidth is limited. Always lock down the scenarios where you allow users to submit renders to remote sites, to avoid congestion and long delays in production.

## Building your own submitter

As mentioned earlier, the accsyn farm feature is API-first, meaning that it is primarily designed to be integrated into other software or built into your own production toolset.

In this example we build a minimal Python (PySide) based submitter designed to be launched as a standalone desktop application. Source code:

```bash
pip install accsyn-python-api

pip install PySide6
```

**accsyn-submitter.py:**

```python
import os
import sys
import re
import traceback

import accsyn_api
 
from PySide6 import QtWidgets

from PySide6.QtWidgets import (
    QDialog, QApplication, QVBoxLayout, QHBoxLayout, QFormLayout,
    QComboBox, QLineEdit, QPushButton, QLabel, QMessageBox
)

from PySide6.QtCore import Qt

from PySide6.QtGui import QColor


class SubmitterDialog(QDialog):
    """Dialog for submitting a generic render job to accsyn"""
    def __init__(self, parent=None):
        super(SubmitterDialog, self).__init__(parent)
        self.setWindowTitle("Accsyn Render Farm Submitter")
        self.setMinimumWidth(600)
        # Create farm session object, requires environment variables set:
        #    ACCSYN_WORKSPACE=<workspace API code>
        #    ACCSYN_API_USER=<accsyn user ident (email)>
        #    ACCSYN_API_KEY=<secret API key, generated from https://accsyn.io/developer>
        self.session = accsyn_api.Session()

        self.engines = []
        self.setup_ui()
        self.load_engines()

    def setup_ui(self):
        """Setup the user interface"""
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(15, 15, 15, 15)
        # Engine selection row
        engine_row = QHBoxLayout()
        engine_label = QLabel("Engine:")
        engine_label.setMinimumWidth(80)
        self.engine_combo = QComboBox()
        self.engine_combo.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        engine_row.addWidget(engine_label)
        engine_row.addWidget(self.engine_combo)
        layout.addLayout(engine_row)
        # Input field row
        input_row = QHBoxLayout()
        input_label = QLabel("Input:")
        input_label.setMinimumWidth(80)
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("share=<share ident>/<path>/<to>/<a file>")
        self.input_field.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        input_row.addWidget(input_label)
        input_row.addWidget(self.input_field)
        layout.addLayout(input_row)
        # Range field row
        range_row = QHBoxLayout()
        range_label = QLabel("Range:")
        range_label.setMinimumWidth(80)
        self.range_field = QLineEdit()
        self.range_field.setPlaceholderText("1-100")
        self.range_field.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        range_row.addWidget(range_label)
        range_row.addWidget(self.range_field)
        layout.addLayout(range_row)
        # Output field row
        output_row = QHBoxLayout()
        output_label = QLabel("Output:")
        output_label.setMinimumWidth(80)
        self.output_field = QLineEdit()
        self.output_field.setPlaceholderText("share=<share ident>/<path>/<to>/<folder>")
        self.output_field.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        output_row.addWidget(output_label)
        output_row.addWidget(self.output_field)
        layout.addLayout(output_row)
        # Buttons row
        button_layout = QHBoxLayout()
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_button)
        button_layout.addStretch()  # Spacer in the middle
        self.submit_button = QPushButton("SUBMIT")
        self.submit_button.setStyleSheet("""
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

        self.submit_button.clicked.connect(self.on_submit)
        button_layout.addWidget(self.submit_button)
        layout.addLayout(button_layout)

    def load_engines(self):
        """Query all engines from accsyn that have type=compute"""
        try:
            engines = self.session.find("engine where type=compute")
            self.engines = engines if engines else []
            # Populate combobox
            self.engine_combo.clear()
            if self.engines:
                for engine in self.engines:
                    # Engine might be a dict with 'name' or 'code' field, or just a string
                    if isinstance(engine, dict):
                        name = engine.get('name') or engine.get('code') or str(engine)
                    else:
                        name = str(engine)
                    self.engine_combo.addItem(name, engine)
            else:
                self.engine_combo.addItem("No compute engines found", None)
                self.submit_button.setEnabled(False)
        except Exception as e:
            QMessageBox.warning(self, "Error Loading Engines", 
                              f"Failed to load engines from accsyn:\n\n{str(e)}\n\n{traceback.format_exc()}")
            self.engine_combo.addItem("Error loading engines", None)
            self.submit_button.setEnabled(False)

    def validate_input_path(self, path):
        """Validate input path format: share=<share ident>/<path>/<to>/<a file>"""

        if not path:

            return False, "Input path is required"

        # Pattern: share=<identifier>/<path components>

        pattern = r'^share=[^/]+(/[^/]+)+$'

        if not re.match(pattern, path):

            return False, "Input path must be in format: share=<share ident>/<path>/<to>/<a file>"

        return True, None

    def validate_output_path(self, path):
        """Validate output path as accsyn shaped folder path"""
        if not path:
            return False, "Output path is required"
        # Similar pattern to input, but should be a folder path
        # Accsyn paths typically start with share=
        pattern = r'^share=[^/]+(/[^/]+)+/?$'
        if not re.match(pattern, path):
            return False, "Output path must be a valid accsyn folder path (share=<share ident>/<path>/<to>/<folder>)"
        return True, None

    def validate_range(self, range_str):
        """Validate frame range format: 1-100"""
        if not range_str:
            return False, "Range is required"
        # Pattern: number-number
        pattern = r'^\d+-\d+$'
        if not re.match(pattern, range_str):
            return False, "Range must be in format: 1-100"

        # Check that start <= end
        try:
            start, end = map(int, range_str.split('-'))
            if start > end:
                return False, "Start frame must be less than or equal to end frame"
        except ValueError:
            return False, "Range must contain valid numbers"
        return True, None

    def validate_fields(self):
        """Validate all input fields"""
        errors = []
        # Validate engine
        if self.engine_combo.currentData() is None:
            errors.append("Please select a valid engine")
        # Validate input path
        input_path = self.input_field.text().strip()
        valid, error_msg = self.validate_input_path(input_path)
        if not valid:
            errors.append(f"Input: {error_msg}")
        # Validate range
        range_str = self.range_field.text().strip()
        valid, error_msg = self.validate_range(range_str)
        if not valid:
            errors.append(f"Range: {error_msg}")
        # Validate output path
        output_path = self.output_field.text().strip()
        valid, error_msg = self.validate_output_path(output_path)
        if not valid:
            errors.append(f"Output: {error_msg}")
        return errors

    def build_payload(self):
        """Build the accsyn API render farm submit JSON payload"""
        engine_data = self.engine_combo.currentData()
        # Get engine identifier (could be string or dict with 'code' or 'name')
        if isinstance(engine_data, dict):
            engine = engine_data.get('code') or engine_data.get('name') or str(engine_data)
        else:
            engine = str(engine_data)
        # Parse frame range
        range_str = self.range_field.text().strip()
        start_frame, end_frame = map(int, range_str.split('-'))
        payload = {
            'engine': engine,
            'input': self.input_field.text().strip(),
            'output': self.output_field.text().strip(),
            'range': f"{start_frame}-{end_frame}",
        }
        return payload

    def submit_job(self, payload):
        """Submit job to accsyn API"""
        try:
            result = self.session.create('job', payload)
            return True, result
        except Exception as e:
            return False, str(e)

    def on_submit(self):
        """Handle submit button click"""
        # Validate fields
        errors = self.validate_fields()
        if errors:
            error_msg = "Please correct the following errors:\n\n" + "\n".join(f"• {error}" for error in errors)
            QMessageBox.warning(self, "Validation Error", error_msg)
            return

        # Build payload
        payload = self.build_payload()
        # Submit job
        success, result = self.submit_job(payload)
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
                f"Failed to submit job:\n\n{result}\n\n{traceback.format_exc()}"
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = SubmitterDialog()
    dialog.show()
    sys.exit(app.exec())

```  

### Breakdown of the submitter

- Imports/dependencies; Besides standard Python libraries, the script requires the libraries "accsyn-python-api" and "PySide6" to be available in the running environment.
- Class init; Here the accsyn API session is created; it assumes accsyn API credentials stored in environment variables. They can also be submitted as arguments to the Session(..) call.
- setup_ui; Create the simple GUI where the user can choose engine, input the file to render, frame range and where to save the images.
- load_engines; This utility function loads available engines from accsyn. Requires at least one standard type (compute) engine to be available.
- validate_input_path & validate_output_path; Makes sure that the path is in accsyn form/notation.
- validate_range; Validate frame range number expression (start-end)
- validate_fields; Validates all values entered by the user.
- build_payload; Builds the API submit payload based on the user input.
- submit_job; Submits the render farm job to accsyn.
- on_submit; Handle submit button click.
- Main bootstrap; executed when launched like "python3 <path/to/[submitter.py](http://submitter.py)>"

  

Many more user inputs can be added depending on the engine and the different use cases.

  

### Conclusion

The simplistic accsyn API makes it easy to programmatically submit render jobs with minimal effort, either from Python scripts integrated within DCC applications or in standalone desktop tooling.

## Building your own render engine

Most likely, the default engines provided by accsyn do not cover your needs and you will need to create your own engine script. This guide walks through the basics; we recommend you take a look at the existing engine scripts to get inspiration.

  

### Developer guidelines/prerequisites

- A code editor (IDE) - Visual Studio Code, PyCharm or similar.
- Python 3
- (Recommended) Source code control - Git(hub)/Perforce/CVS.

  

### Script structure

Engine scripts must adhere to the following base structure:


```python
class Engine(Common):

    __revision__ = 1 

    # -- ENGINE CONFIG START --

    SETTINGS = {
      "items": True,
      "filename_extensions": ".nk",
      ..

    }

    PARAMETERS = {"mapped_share_paths": [], "arguments": ["-txV"], "input_conversion": "auto"}

    # -- ENGINE CONFIG END --

    ..

    def __init__(self, argv):
        super(Engine, self).__init__(argv)

    ..

    def get_executable(self, preferred_nuke_version=None):
        """Return path to executable as string"""
        ...


    def get_envs(self):

        """Get dynamic environment variables"""
        ..

    def get_commandline(self, item):
        """Construct the full command line to execute, returned as a list"""
        ..

    ..

  

if __name__ == '__main__':
     engine = Engine(sys.argv)
     engine.load()  # Load data
     engine.execute()  # Run

```

Breakdown of the engine script:

- Engine config; defines the settings for the engine, for example if the application supports items or the default command line arguments to pass on to the app.

  - items (boolean); True means each input file can be the source of multiple output files, for example the case for Maya, Nuke, Houdini. Some renderers like Houdini Mantra and Arnold take a file sequence as input; still, it will be executed as numbered items defined by a sub frame range on each render server. ffmpeg on the other hand does not support items - each input file is executed as a task and generates exactly one or more output files.
  - multiple_inputs (boolean); True means the engine script supports multiple inputs, this is false for Maya, Nuke etc. but true for ffmpeg.
  - filename_extensions (string);  Comma separated list of input filename extensions associated with the underlying (DCC) application, for example ".ma,.mb" for Maya.
  - binary_filename_extensions (string); Comma separated list of filename extensions that denote binary file format, this tells accsyn which input files can be parsed during submit with the desktop app or not.
  - binary (boolean); Tells accsyn that all input files are binary.
  - default_range (string); The default frame range to suggest in desktop app submitter.
  - default_bucketsize (number); The default bucket size to suggest in desktop app submitter.
  - max_bucketsize (number); The maximum bucket size the render application supports.
  - default_output_path (string); Suggest this default output path.
  - type; The type of engine, default is "compute" for DCC rendering applications. The rest are special engines not covered by this documentation.
- Init; instantiate the engine, and also define additional class variables.
- Get executable; Evaluate and return the path to the application binary executable, will be the first element of the command line.
- Get envs; (Optional) Build a dictionary holding environment variables to pass on to the application.
- Get commandline; Build the full command line to launch.

## Other resources

[Python API](python-api.md)

Get to learn more about the accsyn Python API.

[Case Study](https://www.google.com/url?q=https%3A%2F%2Faccsyn.com%2Fcasestudy-stillerstudios-hfs%2F&sa=D&sntz=1&usg=AOvVaw3qJqkJvfwSbH-PkgyzhFPl)

Learn how accsyn was implemented at Stiller Studios for rendering the Handbok För Superhjältar animated feature.
