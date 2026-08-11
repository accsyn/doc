# Developer Hub

This section guides you through how to develop with accsyn.

Contents:

[Introduction](developer.md)

[Developing with accsyn](developer.md)

[Python API](developer.md)

[Job JSON specification](developer.md)

[Hooks](developer.md)

[Publish](developer.md)

[Rendering/compute](developer.md)

## Introduction

accsyn is designed from ground-up to facilitate API-driven file transfers and compute workflows, enabling advanced automated workflows and integration into third party tools.

  

This developer hub covers four main areas:

- The accsyn Python API; Being API-first, all you can do within an accsyn GUI can be done through the API, in fact all internal communication within accsyn is API driven.
- Hooks; Have scripts run on your server on specific events (BYOS only)
- Publish; Setup a publishing workflow, facilitating ingestion of remote work into your production pipeline (BYOS only)
- Rendering/compute; Use accsyn for heave compute processing, such as 3D image rendering, 2D compositing render, GPU processing (ML) or any custom resource intensive calculation that needs to run in the background (BYOS only)

## Developing with accsyn

Before diving into the accsyn API, we recommend learning about the terms and definition used in accsyn. Here is schematic covering the basic internal accsyn entities and their relationship:

![](assets/developer-049170eb0ce9.png)

For complete list of accsyn terms, please refer to the [API glossary page](https://accsyn-python-api.readthedocs.io/en/latest/glossary.html).

## Python API

[Python API](developer/python-api.md)

Learn how to programatically launch and manage file transfers, create deliveries and manage file sharing.

### Job JSON specification

[Job JSON Spec](developer/job-specification.md)

Learn the accsyn job JSON format, for use with the Python API and workflows in general.

Note: the following features are currently only available for BYOS Workspaces.

## Hooks

[Hooks](developer/hooks.md)

Configure scripts that will be executed by an accsyn server on events such as job submit and job done.

## Publish

[Publish](developer/publish.md)

Enable controlled validation and ingest of data into your production pipeline.

## Rendering/compute

[Compute](developer/farm.md)

Setup a render farm driven by highly configurable Python scripted engines, multi-site enabled.
