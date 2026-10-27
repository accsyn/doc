# JavaScript API

The accsyn JavaScript API is the same workspace API as the [Python API](/developer/python-api/), for Node.js 18+ and for browsers.

*Important Note: API is NOT available for Cloud Essentials or [BYOS](/admin/byos/) Lite type workspaces.*

## How to create and manage API keys

API keys are created the same way as for the Python API. See [How to create and manage API keys](/developer/python-api/#how-to-create-and-manage-api-keys).

## Install

```bash
npm install accsyn
```

## Using

Create one session and reuse it. Workspace backends rate-limit REST calls per IP.

```javascript
import { Session } from "accsyn";

const session = await Session.connect({
  workspace: "acmefilm",
  username: "john@user.com",
  apiKey: process.env.ACCSYN_API_KEY,
});

const job = await session.create("transfer", {
  source: "volume=projects/A001_C064_09224Y_001.mp4",
  destination: "client=664f53b16aa9149860da9d9c:/tmp/A001_C064_09224Y_001.mp4",
});
```

On Node, `workspace`, `username`, and `apiKey` can be omitted when `ACCSYN_WORKSPACE`, `ACCSYN_API_USER`, and `ACCSYN_API_KEY` are set.

The API queues transfers. It does not move the file bytes itself.

## Reading logs

`logs` returns backend logs for a scope, or for one entity. The return value is the backend response, with the rows in `result`.

```javascript
// Workspace log
const { result } = await session.logs({ entityType: "workspace" });

// Log of one job, filtered by text
const job = await session.logs({ entityType: "job", entityId: "6aad45ce991535260e495da9", search: "error" });
```

The backend sorts a log oldest first. To read it in pages, use `paginationStart` and `paginationSize`. `paginationStart` is the first row, counted from 1, and `-1` returns the last page, that is the newest `paginationSize` rows. The response has `pagination` with `start`, `end` and `total`. The options `paginationPage`, `paginationLimit` and `paginationSkip` exist for parity with the Python API, but the backend does not read them.

```javascript
// The newest 50 rows of the workspace log
const { result, pagination } = await session.logs({ paginationStart: -1, paginationSize: 50 });
console.log(`${result.length} of ${pagination.total} rows`);
```

### Process logs

`processLogs` returns the detailed process log (console output) of a job, for example the detailed transfer log. The job is identified by its ID.

```javascript
// Log of the first task of the job that has been processed, latest try
const response = await session.processLogs("6aad45ce991535260e495da9");
console.log(response.text_master);
console.log(`Tries: ${response.try_count}`);
```

The console output of the master process is in `text_master` and in `text_slave`for the slave (file server) process. The returned try is in `try`, the total number of tries in `try_count`, and earlier tries in `process_history`, if there are any.

Without `uri`, the log of the first task that has been processed is returned. Give `uri` to read the log of a specific task, and `tryNum` (counted from 0) to read an earlier try. The latest try is the default.

```javascript
// The first try of a specific task
const first = await session.processLogs("6aad45ce991535260e495da9", { uri: "<task uri>", tryNum: 0 });

// The slave (file server party) log. Only operators can read it, and only for transfer jobs.
const slave = await session.processLogs("6aad45ce991535260e495da9", { master: false, slave: true });
console.log(slave.text_slave);
```

## Source code

[https://github.com/accsyn/javascript-api](https://github.com/accsyn/javascript-api)

## Further resources

[Job JSON Spec](/developer/job-specification/)

[Tutorial | Remote Office Sync](/tutorials/remote-office-sync/)

## Changelog

Changes to the JavaScript API, most recent release first. The accsyn platform changelog is [here](/changelog/).

<div class="release-card" markdown>

### v3.6-8 <small>October 23, 2026</small>

**Minor features**

- [JS API] Support for reading process logs - `session.processLogs()` returns the detailed console output of a job task, for example the detailed transfer log. Select task and try, and read the master or slave process log.
- [JS API] Page through logs with `paginationStart` and `paginationSize` in `session.logs()`, for example the newest 50 rows of a log.

**Changes**

- [JS API] Aligned versioning with accsyn. The package version now follows the accsyn release instead of the Python API version. This release is published to npm as `3.6.8`, because npm versions cannot contain a hyphen.

</div>

<div class="release-card" markdown>

### v3.4.0 <small>October 16, 2026</small>

**Minor features**

- [JS API] Initial version, published to npm as [`accsyn`](https://www.npmjs.com/package/accsyn). Mirrored from the Python API 3.4.0, with the same session, entity, access, file, setting and log operations as async methods.
- [JS API] Works in Node.js 18+ and in browsers, as ES module and CommonJS, with TypeScript types included.

</div>

<!-- api-reference:start -->

## API reference

### Classes

#### AccsynError

Error raised when an accsyn API call fails.

##### Extends

- `Error`

##### Constructors

###### Constructor

> **new AccsynError**(`message`): [`AccsynError`](#accsynerror)

####### Parameters

####### message

`string`

####### Returns

[`AccsynError`](#accsynerror)

####### Overrides

`Error.constructor`

##### Properties

###### cause?

> `optional` **cause?**: `unknown`

####### Inherited from

`Error.cause`

###### message

> **message**: `string`

####### Inherited from

`Error.message`

###### name

> **name**: `string`

####### Inherited from

`Error.name`

###### stack?

> `optional` **stack?**: `string`

####### Inherited from

`Error.stack`

###### stackTraceLimit

> `static` **stackTraceLimit**: `number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured _after_ the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

####### Inherited from

`Error.stackTraceLimit`

##### Methods

###### captureStackTrace()

> `static` **captureStackTrace**(`targetObject`, `constructorOpt?`): `void`

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack;  // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

####### Parameters

####### targetObject

`object`

####### constructorOpt?

`Function`

####### Returns

`void`

####### Inherited from

`Error.captureStackTrace`

###### prepareStackTrace()

> `static` **prepareStackTrace**(`err`, `stackTraces`): `any`

####### Parameters

####### err

`Error`

####### stackTraces

`CallSite`[]

####### Returns

`any`

####### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

####### Inherited from

`Error.prepareStackTrace`

***

#### Session

accsyn API session.

Create one with [Session.connect](#connect) and reuse it. Workspace backends rate-limit REST traffic per IP.

##### Properties

###### connectTimeout

> `readonly` **connectTimeout**: `number`

###### timeout

> `readonly` **timeout**: `number`

###### username

> `readonly` **username**: `string`

##### Methods

###### access()

> **access**(`targetType`, `targetId`, `options?`): `Promise`\<[`Entity`](#entity)[]\>

List recipients on a delivery, or ACL entries on a share.

####### Parameters

####### targetType

`string`

####### targetId

`string`

####### options?

[`AccessOptions`](#accessoptions) = `{}`

####### Returns

`Promise`\<[`Entity`](#entity)[]\>

###### activateOne()

> **activateOne**(`entityType`, `entityIdent`): `Promise`\<`unknown`\>

Bring a deactivated entity back. `entityIdent` may be an id or a code.

####### Parameters

####### entityType

`string`

####### entityIdent

`string`

####### Returns

`Promise`\<`unknown`\>

###### appIsRunning()

> **appIsRunning**(): `Promise`\<`boolean` \| `null`\>

Whether the desktop app is online on this machine for the logged-in user.

####### Returns

`Promise`\<`boolean` \| `null`\>

###### assign()

> **assign**(`parentType`, `entityType`, `data`): `Promise`\<`unknown`\>

Assign a server or client to a volume or share.

####### Parameters

####### parentType

`string`

####### entityType

`string`

####### data

[`JsonObject`](#jsonobject)

####### Returns

`Promise`\<`unknown`\>

###### assignments()

> **assignments**(`entityType`, `entityId`): `Promise`\<[`Entity`](#entity)[]\>

List servers assigned to a volume or share.

####### Parameters

####### entityType

`string`

####### entityId

`string`

####### Returns

`Promise`\<[`Entity`](#entity)[]\>

###### create()

> **create**(`entityType`, `data`, `options?`): `Promise`\<[`Entity`](#entity) \| [`Entity`](#entity)[]\>

Create an entity.

`data` may be an object, a list of tasks, a JSON string, or (on Node) a path to a JSON file.

####### Parameters

####### entityType

`string`

####### data

[`CreateData`](#createdata)

####### options?

[`CreateOptions`](#createoptions) = `{}`

####### Returns

`Promise`\<[`Entity`](#entity) \| [`Entity`](#entity)[]\>

###### daemonIsRunning()

> **daemonIsRunning**(): `Promise`\<`boolean` \| `null`\>

Whether a server or user-server daemon is online on this machine for the logged-in user.

####### Returns

`Promise`\<`boolean` \| `null`\>

###### deactivateOne()

> **deactivateOne**(`entityType`, `entityId`): `Promise`\<`unknown`\>

Deactivate an entity, keeping it for audit.

####### Parameters

####### entityType

`string`

####### entityId

`string`

####### Returns

`Promise`\<`unknown`\>

###### deassign()

> **deassign**(`parentType`, `entityType`, `data`): `Promise`\<`unknown`\>

Remove a server assignment from a volume or share.

####### Parameters

####### parentType

`string`

####### entityType

`string`

####### data

[`JsonObject`](#jsonobject)

####### Returns

`Promise`\<`unknown`\>

###### delete()

> **delete**(`path`, `force?`): `Promise`\<`unknown`\>

Delete a file or directory on a share. Set `force` to remove a non-empty directory.

####### Parameters

####### path

[`FilePath`](#filepath)

####### force?

`boolean` = `false`

####### Returns

`Promise`\<`unknown`\>

###### deleteMany()

> **deleteMany**(`entityType`, `entityId`, `data`): `Promise`\<`unknown`\>

Delete files beneath a collection.

####### Parameters

####### entityType

`string`

####### entityId

`string`

####### data

[`JsonObject`](#jsonobject)

####### Returns

`Promise`\<`unknown`\>

###### deleteOne()

> **deleteOne**(`entityType`, `entityId`, `data?`): `Promise`\<`unknown`\>

Archive an entity. ACLs must be removed with [Session.revoke](#revoke).

####### Parameters

####### entityType

`string`

####### entityId

`string`

####### data?

[`JsonObject`](#jsonobject) \| `null`

####### Returns

`Promise`\<`unknown`\>

###### deleteSetting()

> **deleteSetting**(`entityType`, `name`, `entityId?`): `Promise`\<`boolean`\>

Delete a setting.

####### Parameters

####### entityType

`string`

####### name

`string`

####### entityId?

`string` \| `null`

####### Returns

`Promise`\<`boolean`\>

###### exists()

> **exists**(`path`): `Promise`\<`unknown`\>

Whether a share path exists.

####### Parameters

####### path

[`FilePath`](#filepath)

####### Returns

`Promise`\<`unknown`\>

###### find()

> **find**(`query`, `options?`): `Promise`\<[`Entity`](#entity) \| [`Entity`](#entity)[] \| `null`\>

Query entities, `entitytypes`, or `attributes`.

####### Parameters

####### query

`string`

####### options?

[`FindOptions`](#findoptions) = `{}`

####### Returns

`Promise`\<[`Entity`](#entity) \| [`Entity`](#entity)[] \| `null`\>

###### findOne()

> **findOne**(`query`, `options?`): `Promise`\<[`Entity`](#entity) \| `null`\>

Return a single entity, or null.

####### Parameters

####### query

`string`

####### options?

`Omit`\<[`FindOptions`](#findoptions), `"singleEntityQuery"` \| `"limit"` \| `"skip"` \| `"create"` \| `"update"`\> = `{}`

####### Returns

`Promise`\<[`Entity`](#entity) \| `null`\>

###### getApiKey()

> **getApiKey**(): `Promise`\<`string`\>

Fetch the user API key. Often disabled server-side.

####### Returns

`Promise`\<`string`\>

###### getEntity()

> **getEntity**(`entityType`, `entityId`): `Promise`\<[`Entity`](#entity) \| `null`\>

Fetch an entity by type and 24-character id, including inactive and archived records.

####### Parameters

####### entityType

`string`

####### entityId

`string`

####### Returns

`Promise`\<[`Entity`](#entity) \| `null`\>

###### getLastMessage()

> **getLastMessage**(): `string` \| `null`

Error message from the last failed API call, if any.

####### Returns

`string` \| `null`

###### getSetting()

> **getSetting**(`name?`, `options?`): `Promise`\<`unknown`\>

Read one setting value.

####### Parameters

####### name?

`string` \| `null`

####### options?

[`SettingScope`](#settingscope) = `{}`

####### Returns

`Promise`\<`unknown`\>

###### getSettings()

> **getSettings**(`options?`): `Promise`\<[`JsonObject`](#jsonobject)\>

Read the settings object for an entity. Defaults to the workspace.

####### Parameters

####### options?

[`SettingsOptions`](#settingsoptions) = `{}`

####### Returns

`Promise`\<[`JsonObject`](#jsonobject)\>

###### getSize()

> **getSize**(`path`, `include?`, `exclude?`): `Promise`\<`unknown`\>

Size of a file or directory on a share.

####### Parameters

####### path

[`FilePath`](#filepath)

####### include?

`string` \| `string`[]

####### exclude?

`string` \| `string`[]

####### Returns

`Promise`\<`unknown`\>

###### grant()

> **grant**(`entityType`, `entityId`, `targetType`, `targetId`, `data?`): `Promise`\<`unknown`\>

Grant a user access to a delivery, request, stream, or share.
`entityType` must be `user`. `entityId` may be an id or, for unique types, a code such as an email.

####### Parameters

####### entityType

`string`

####### entityId

`string`

####### targetType

`string`

####### targetId

`string`

####### data?

[`JsonObject`](#jsonobject) \| `null`

####### Returns

`Promise`\<`unknown`\>

###### integration()

> **integration**(`name`, `operation`, `data`): `Promise`\<`unknown`\>

Call an integration utility.

####### Parameters

####### name

`string`

####### operation

`string`

####### data

[`JsonObject`](#jsonobject)

####### Returns

`Promise`\<`unknown`\>

###### logs()

> **logs**(`options?`): `Promise`\<[`JsonObject`](#jsonobject)\>

Backend disk logs for an entity scope.

####### Parameters

####### options?

[`LogOptions`](#logoptions) = `{}`

####### Returns

`Promise`\<[`JsonObject`](#jsonobject)\>

###### ls()

> **ls**(`path`, `options?`): `Promise`\<`unknown`\>

List files on a share. `path` uses the form `share=<share>/<path>`.

####### Parameters

####### path

[`FilePath`](#filepath)

####### options?

[`FileListOptions`](#filelistoptions) = `{}`

####### Returns

`Promise`\<`unknown`\>

###### metrics()

> **metrics**(`query`, `attributes?`, `time?`): `Promise`\<[`JsonObject`](#jsonobject)\>

Metrics for an entity query, typically a job.

####### Parameters

####### query

`string`

####### attributes?

`string`[] \| `null`

####### time?

`string` \| `null`

####### Returns

`Promise`\<[`JsonObject`](#jsonobject)\>

###### mkdir()

> **mkdir**(`path`): `Promise`\<`unknown`\>

Create a directory on a share.

####### Parameters

####### path

[`FilePath`](#filepath)

####### Returns

`Promise`\<`unknown`\>

###### move()

> **move**(`pathSrc`, `pathDst`): `Promise`\<`unknown`\>

Move a file or directory on a share.

####### Parameters

####### pathSrc

[`FilePath`](#filepath)

####### pathDst

[`FilePath`](#filepath)

####### Returns

`Promise`\<`unknown`\>

###### prepublish()

> **prepublish**(`data`): `Promise`\<`unknown`\>

Pre-process a publish file list. Directory sizes are filled in when omitted.

####### Parameters

####### data

[`JsonObject`](#jsonobject)[]

####### Returns

`Promise`\<`unknown`\>

###### processLogs()

> **processLogs**(`entityId`, `options?`): `Promise`\<[`JsonObject`](#jsonobject)\>

The detailed process log (console output) of a job task, for example the detailed transfer log.

The console output is in `text_master` for the master process and `text_slave` for the slave process. The returned
try is in `try`, the total number of tries in `try_count` and earlier tries in `process_history`, if any.

####### Parameters

####### entityId

`string`

ID of the job to read the process log of.

####### options?

[`ProcessLogOptions`](#processlogoptions) = `{}`

####### Returns

`Promise`\<[`JsonObject`](#jsonobject)\>

###### rename()

> **rename**(`path`, `pathTo`): `Promise`\<`unknown`\>

Rename a file or directory within the same parent directory.

####### Parameters

####### path

[`FilePath`](#filepath)

####### pathTo

[`FilePath`](#filepath)

####### Returns

`Promise`\<`unknown`\>

###### report()

> **report**(`query`): `Promise`\<`string`\>

Support report for an entity query.

####### Parameters

####### query

`string`

####### Returns

`Promise`\<`string`\>

###### revoke()

> **revoke**(`entityType`, `entityId`, `targetType`, `targetId`): `Promise`\<`unknown`\>

Revoke a user's access.
Returns false when no matching recipient or ACL exists.

####### Parameters

####### entityType

`string`

####### entityId

`string`

####### targetType

`string`

####### targetId

`string`

####### Returns

`Promise`\<`unknown`\>

###### setSetting()

> **setSetting**(`entityType`, `name`, `value`, `entityId?`): `Promise`\<`boolean`\>

Set a setting. `value` must already be a string; serialize objects and dates first.

####### Parameters

####### entityType

`string`

####### name

`string`

####### value

`string`

####### entityId?

`string` \| `null`

####### Returns

`Promise`\<`boolean`\>

###### update()

> **update**(`entityType`, `entityId`, `data`): `Promise`\<[`Entity`](#entity) \| `undefined`\>

Update one entity. ACLs must be changed with [Session.grant](#grant).

####### Parameters

####### entityType

`string`

####### entityId

`string`

####### data

[`JsonObject`](#jsonobject)

####### Returns

`Promise`\<[`Entity`](#entity) \| `undefined`\>

###### updateMany()

> **updateMany**(`entityType`, `entityId`, `data`): `Promise`\<[`Entity`](#entity)[] \| `undefined`\>

Update tasks beneath a job. `entityType` must be `task`.

####### Parameters

####### entityType

`string`

####### entityId

`string`

####### data

[`JsonObject`](#jsonobject)[]

####### Returns

`Promise`\<[`Entity`](#entity)[] \| `undefined`\>

###### connect()

> `static` **connect**(`options?`): `Promise`\<[`Session`](#session)\>

Authenticate and open a session.

On Node, omitted credentials are read from the environment or a `.env` file.

####### Parameters

####### options?

[`SessionOptions`](#sessionoptions) = `{}`

####### Returns

`Promise`\<[`Session`](#session)\>

###### getHostname()

> `static` **getHostname**(): `Promise`\<`string`\>

Hostname of this computer. Returns `unknown` in the browser.

####### Returns

`Promise`\<`string`\>

### Interfaces

#### AccessOptions

##### Properties

###### entityId?

> `optional` **entityId?**: `string`

###### entityType?

> `optional` **entityType?**: `string`

###### recursive?

> `optional` **recursive?**: `boolean`

***

#### CreateOptions

##### Properties

###### allowDuplicates?

> `optional` **allowDuplicates?**: `boolean`

Allow duplicate tasks and retry the existing task.

###### entityId?

> `optional` **entityId?**: `string`

Parent id when creating sub-entities such as tasks.

###### replaceDuplicates?

> `optional` **replaceDuplicates?**: `boolean`

Replace duplicate tasks instead of retrying them.

***

#### Entity

JSON object returned by the accsyn backend.

##### Indexable

> \[`key`: `string`\]: `unknown`

##### Properties

###### id?

> `optional` **id?**: `string`

***

#### FileListOptions

##### Properties

###### directoriesOnly?

> `optional` **directoriesOnly?**: `boolean`

###### exclude?

> `optional` **exclude?**: `string` \| `string`[]

###### filesOnly?

> `optional` **filesOnly?**: `boolean`

###### getSize?

> `optional` **getSize?**: `boolean`

###### include?

> `optional` **include?**: `string` \| `string`[]

###### maxDepth?

> `optional` **maxDepth?**: `number`

###### recursive?

> `optional` **recursive?**: `boolean`

***

#### FindOptions

##### Properties

###### archived?

> `optional` **archived?**: `boolean`

###### attributes?

> `optional` **attributes?**: `string`[]

###### create?

> `optional` **create?**: `boolean`

When querying attributes, return create attributes.

###### entityId?

> `optional` **entityId?**: `string`

###### finished?

> `optional` **finished?**: `boolean`

###### inactive?

> `optional` **inactive?**: `boolean`

###### limit?

> `optional` **limit?**: `number`

###### ~~offline?~~

> `optional` **offline?**: `boolean`

####### Deprecated

Use `inactive`.

###### singleEntityQuery?

> `optional` **singleEntityQuery?**: `boolean`

###### skip?

> `optional` **skip?**: `number`

###### update?

> `optional` **update?**: `boolean`

When querying attributes, return update attributes.

***

#### LogOptions

##### Properties

###### entityId?

> `optional` **entityId?**: `string` \| `null`

###### entityType?

> `optional` **entityType?**: `string` \| `null`

###### paginationLimit?

> `optional` **paginationLimit?**: `number`

###### paginationPage?

> `optional` **paginationPage?**: `number`

Accepted for parity with the Python API. The backend does not read `page`, `limit` and `skip`, use
`paginationStart` and `paginationSize` instead.

###### paginationSize?

> `optional` **paginationSize?**: `number`

Number of rows to return. All rows are returned when omitted.

###### paginationSkip?

> `optional` **paginationSkip?**: `number`

###### paginationStart?

> `optional` **paginationStart?**: `number`

First row to return, counted from 1 in the sort order (oldest first by default). `-1` returns the last page,
that is the newest `paginationSize` rows.

###### search?

> `optional` **search?**: `string`

###### sort?

> `optional` **sort?**: `string`

###### sortReverse?

> `optional` **sortReverse?**: `boolean`

***

#### ProcessLogOptions

##### Properties

###### master?

> `optional` **master?**: `boolean`

Fetch the master process log, the main process. Defaults to true.

###### slave?

> `optional` **slave?**: `boolean`

Fetch the slave process log, the file server party process. Can only be done by operators, for transfer jobs.

###### tryNum?

> `optional` **tryNum?**: `number`

Zero-based try (attempt) number. Defaults to the latest try.

###### uri?

> `optional` **uri?**: `string`

URI of the task to read the log of. Defaults to the first task of the job that has been processed.

***

#### SessionOptions

##### Properties

###### apiKey?

> `optional` **apiKey?**: `string`

API key. Falls back to ACCSYN_API_KEY.

###### connectTimeout?

> `optional` **connectTimeout?**: `number`

Connection timeout in seconds. Defaults to 10. Recorded for parity; fetch uses `timeout` as the abort deadline.

###### dev?

> `optional` **dev?**: `boolean`

Talk to a local backend on 127.0.0.1:8181. Falls back to AS_DEV.

###### ~~domain?~~

> `optional` **domain?**: `string`

####### Deprecated

Use `workspace`.

###### hostname?

> `optional` **hostname?**: `string`

Override the workspace hostname.

###### pathEnvfile?

> `optional` **pathEnvfile?**: `string`

Path to a .env file. Falls back to ACCSYN_CREDENTIALS_PATH, then ./.env on Node.

###### port?

> `optional` **port?**: `number`

Override the workspace port. Defaults to 443.

###### prettyJson?

> `optional` **prettyJson?**: `boolean`

Pretty-print JSON in verbose logs.

###### proxy?

> `optional` **proxy?**: `string`

Proxy setting. Falls back to ACCSYN_PROXY. SOCKS proxies are not supported.

###### timeout?

> `optional` **timeout?**: `number`

Response timeout in seconds. Defaults to 120.

###### username?

> `optional` **username?**: `string`

User email. Falls back to ACCSYN_API_USER.

###### verbose?

> `optional` **verbose?**: `boolean`

Print REST traffic to the console.

###### workspace?

> `optional` **workspace?**: `string`

Workspace code. Falls back to ACCSYN_WORKSPACE, ACCSYN_DOMAIN, then ACCSYN_ORG.

***

#### SettingScope

##### Properties

###### data?

> `optional` **data?**: [`JsonObject`](#jsonobject) \| `null`

###### entityId?

> `optional` **entityId?**: `string` \| `null`

###### entityType?

> `optional` **entityType?**: `string`

###### integration?

> `optional` **integration?**: `string`

***

#### SettingsOptions

##### Properties

###### entityId?

> `optional` **entityId?**: `string` \| `null`

###### entityType?

> `optional` **entityType?**: `string` \| `null`

###### omitDefaults?

> `optional` **omitDefaults?**: `boolean`

###### recursive?

> `optional` **recursive?**: `boolean`

###### share?

> `optional` **share?**: `string`

###### upstream?

> `optional` **upstream?**: `boolean`

### Type Aliases

#### CreateData

> **CreateData** = `string` \| [`JsonObject`](#jsonobject) \| [`JsonObject`](#jsonobject)[]

***

#### FilePath

> **FilePath** = `string` \| [`JsonObject`](#jsonobject) \| `string`[]

***

#### JsonObject

> **JsonObject** = `Record`\<`string`, `unknown`\>

### Variables

#### ACCSYN\_BACKEND\_DOMAIN

> `const` **ACCSYN\_BACKEND\_DOMAIN**: `"accsyn.com"` = `"accsyn.com"`

***

#### ACCSYN\_BACKEND\_MASTER\_HOSTNAME

> `const` **ACCSYN\_BACKEND\_MASTER\_HOSTNAME**: `"master.accsyn.com"`

***

#### ACCSYN\_PORT

> `const` **ACCSYN\_PORT**: `443` = `443`

***

#### CLEARANCE\_ADMIN

> `const` **CLEARANCE\_ADMIN**: `"admin"` = `"admin"`

***

#### CLEARANCE\_EMPLOYEE

> `const` **CLEARANCE\_EMPLOYEE**: `"employee"` = `"employee"`

***

#### CLEARANCE\_NONE

> `const` **CLEARANCE\_NONE**: `"none"` = `"none"`

***

#### CLEARANCE\_STANDARD

> `const` **CLEARANCE\_STANDARD**: `"standard"` = `"standard"`

***

#### CLEARANCE\_SUPPORT

> `const` **CLEARANCE\_SUPPORT**: `"support"` = `"support"`

***

#### CLIENT\_STATE\_DISABLED

> `const` **CLIENT\_STATE\_DISABLED**: `"disabled"` = `"disabled"`

***

#### CLIENT\_STATE\_DISABLED\_OFFLINE

> `const` **CLIENT\_STATE\_DISABLED\_OFFLINE**: `"disabled-offline"` = `"disabled-offline"`

***

#### CLIENT\_STATE\_INIT

> `const` **CLIENT\_STATE\_INIT**: `"init"` = `"init"`

***

#### CLIENT\_STATE\_OFFLINE

> `const` **CLIENT\_STATE\_OFFLINE**: `"offline"` = `"offline"`

***

#### CLIENT\_STATE\_ONLINE

> `const` **CLIENT\_STATE\_ONLINE**: `"online"` = `"online"`

***

#### CLIENT\_TYPE\_ACCSYN\_VPX

> `const` **CLIENT\_TYPE\_ACCSYN\_VPX**: `5` = `5`

***

#### CLIENT\_TYPE\_APP

> `const` **CLIENT\_TYPE\_APP**: `0` = `0`

***

#### CLIENT\_TYPE\_BROWSER

> `const` **CLIENT\_TYPE\_BROWSER**: `3` = `3`

***

#### CLIENT\_TYPE\_COMPUTE\_LANE

> `const` **CLIENT\_TYPE\_COMPUTE\_LANE**: `4` = `4`

***

#### CLIENT\_TYPE\_SERVER

> `const` **CLIENT\_TYPE\_SERVER**: `1` = `1`

***

#### CLIENT\_TYPE\_USERSERVER

> `const` **CLIENT\_TYPE\_USERSERVER**: `2` = `2`

***

#### JOB\_TYPE\_COMPUTE

> `const` **JOB\_TYPE\_COMPUTE**: `3` = `3`

***

#### JOB\_TYPE\_DELIVERY

> `const` **JOB\_TYPE\_DELIVERY**: `7` = `7`

***

#### JOB\_TYPE\_QUEUE

> `const` **JOB\_TYPE\_QUEUE**: `2` = `2`

***

#### JOB\_TYPE\_REQUEST

> `const` **JOB\_TYPE\_REQUEST**: `8` = `8`

***

#### JOB\_TYPE\_STREAM

> `const` **JOB\_TYPE\_STREAM**: `10` = `10`

***

#### JOB\_TYPE\_TRANSFER

> `const` **JOB\_TYPE\_TRANSFER**: `1` = `1`

***

#### UNIQUE\_ENTITY\_TYPES

> `const` **UNIQUE\_ENTITY\_TYPES**: readonly \[`"user"`, `"workspace"`, `"share"`, `"volume"`, `"folder"`, `"home"`, `"collection"`, `"site"`, `"engine"`, `"queue"`\]

***

#### VERSION

> `const` **VERSION**: `"3.4.0"` = `"3.4.0"`

Package version. Matches accsyn-python-api 3.4.0.

<!-- api-reference:end -->
