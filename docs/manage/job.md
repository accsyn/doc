# Monitoring and Queue management

This guide walks through how to monitor and manage accsyn ongoing jobs - file transfers and render/compute jobs.

  

Covered elsewhere:

- [Monitor deliveries and upload requests](../delivery/index.md).
- [Monitor web streams](../vault/stream.md).
- Monitor render/compute farm.

  

Prerequisites:

- Logged on to <https://accsyn.io/jobs> as an elevated user - having employee or admin role.
- Logged on to the desktop app as an elevated user - having employee or admin role. Download the app [here](https://accsyn.io/getapp).

## Job monitoring

### My jobs

On the web, your current running job is visualised in the upper right corner on the activity icon:

![](../assets/manage_job-f038b0847e7d.png)

It shows the progress and the ETR, if you have many jobs running it will display the oldest (first submitted). Click the my jobs icon to bring up a drawer showing all your active and finished jobs.

  

In  the desktop app, you will find your jobs at the expandable bottom area in the MY JOBS tab.

### Workspace jobs

Jobs are spawned:

- When someone uploads or downloads from a delivery, request or web stream.
- From the accsyn Desktop app, with [File Sharing](../file-sharing/index.md) or when submitting a compute/render job.
- With the accsyn API (Python/JS), for more information see [Workflows](../developer/index.md).

  

To monitor all ongoing and finished transfers, go to the Jobs page (<https://accsyn.io/jobs>) on the web.

The page displays all file transfers and compute jobs currently running, grouped by queues:

![](../assets/manage_job-8cae36b217c6.png)

Choose between displaying active or finished(and aborted) jobs. Change grouping between queue(default) or status, search jobs.

  

### Job view

Expand a job to view detailed information about the job, including tasks/files within the job.

  

Toolbar:

- Pause, resume, abort job buttons.
- View job log - all events related to the job during its lifetime.
- Queue and position within brackets.
- Size of job

  

### Task list

A task is a single file or folder within a file transfer, or a compute/render task:

- Select; Select one or more tasks to modify the status.
- Number/uri; The task number/identifier.
- Name; The filename
- Size; The size of the file being processed.
- Status; The status of processing.
- Tries; The number of times the task has processed.
- Start; The time the task started processing.
- Time: The time the task processed.
- Logs; Bring up the detailed task process log.
- Description; (Optional) Task description.

  

### Footer

- Source > destination
- Create date
- Finished date
- ID (API).

## Job and queue management

This section covers more advanced operations that involve managing jobs (transfers/compute) on a larger scale. accsyn has been designed to be a central hub for all file transfers and long running background tasks within an organisation, enabling operators to prioritise single jobs or groups of jobs depending on project needs.

  

### Manage job states

How to manage job states using your web browser:

- Pause (active only); To pause a job, either select the job in the list and choose Pause from the action bar, or open the job and click the pause icon. The job will stop executing immediately and be de-queued.
- Retry/resume; To retry a paused/failed active job or a finished/aborted job, either select the job in the list and choose Resume/Retry from the action bar, or open the job and click the play icon. The job will be put at the bottom of the queue and resume operations once the job(s) above have given way.
- Abort;  To abort a job, either select the job in the list and choose Abort from the action bar, or open the job and click the stop icon. The job will stop executing immediately and be flagged as finished.

  

### Queue system

Under the hood, accsyn provides a queue management system.  Each job, including deliveries, is always placed in a queue. If not provided during submission, the default queue is used. Each queue has a priority number, defining which  jobs should run before others. Jobs cannot have a priority number set, to change job priority the job has to be moved to another queue. 

  

Three standard queues are supplied in accsyn:

1. High, priority: 999.
2. Medium, priority: 500 - the default queue.
3. Low, priority: 1.

  

### Concurrent file transfers

A queue makes sure only one job, between two endpoints, runs at a time. That means in theory that a virtual queue exists for each p2p pair of endpoints. This is because accsyn cannot measure, control and adjust for bandwidth consumption on a higher router level - a very complicated algorithm.

  

A queue can be configured to allow more than one concurrent transfer, see transfer\_concurrent setting.

  

### Re-queue jobs

To change the queue a job is in:

1. Check Show all queues if the destination queue is not visible.
2. Drag the job to the new queue.

  

To change the order of jobs in a queue:

1. Drag the job to a new position in the queue by dropping it on the drop zones that appear between jobs.

  

Different rules apply by default depending on job type:

- File transfers; They are interrupted immediately to give way to the job(s) above in the queue.
- Renders: They are allowed to finish processing before giving way.

  

To learn how to configure your accsyn workspace queues, head over to [Queue administration](../admin/queue.md). 

  

### (Advanced) Manage task states

The state of individual tasks can also be altered to fine-tune which parts of a job should run. Expand the job and select one or more tasks in the task list:

- Retry (non waiting tasks only): Force retry of an executing, failed, on hold or finished task.
- Put on hold: Pause the task temporarily, for manual retry at a later stage.
- Set failed: Set task manually as failed.
- Set done: Set task manually as done.
- Exclude: Exclude the task, has the same function as delete but the task is kept for auditing reasons.

  

### Retry mechanism

accsyn is designed to provide robust self-healing file transfers, which means that if interrupted it will retry with an exponential fall-off rate. Several reasons for interruptions can exist:

- The job is paused/aborted or another job is brought above the job in the queue or has a higher priority.
- One of the file transfer endpoints (clients) goes offline or loses its network connection.
- The storage volume goes offline, file(s) disappear or runs out of space.

  

The number of retries to perform can be configured as  job\_max\_retries and job\_autoretray\_delay\_s settings on queue level and globally on workspace level.
