# accsyn Internal Settings

This page lists all internal settings available for accsyn entities such as workspace, share (volumes, share), queues, jobs (transfers, deliveries).

## Introduction

A setting is a key=value pair defining the behaviour of an accsyn entity.

  

Example of a setting is "transfer\_speedlimit" that defines that maximum bandwidth a transfer can consume.

  

### How to modify settings:

- Settings can be modified from the accsyn webapp, login to access: <https://accsyn.io>
- Job settings can be modified from the [accsyn Desktop app](admin/desktop-app.md).
- Settings can be read, created and modified with the [accsyn Python API](developer/python-api.md).

## Global (Workspace) settings

## User settings

## Client settings

Server, Desktop app, User server

## Share settings

Volume, shared folder, home share, collection

### Inheritance

- Volumes inherits workspace/global settings by default and can have settings overrides (see below).
- Shared folders and Home folders inherits settings from their volume by default and can have settings overrides (see below).

## Job settings

Queue, Transfer, Delivery, Request, Stream, Compute

### Inheritance

- Queues inherits workspace/global settings by default and can have settings overrides (see below).
- Jobs inherit settings from their queue and can have settings overrides (see below).
- Tasks/processes inherits both settings from their job and the involved source and destination shares (volume, shared folder,..). Settings cannot be overridden for process entities.
