# Queue management

This guide covers how accsyn queues prioritise file transfers and compute jobs. For monitoring jobs and changing pause/resume/abort state, see [Job monitoring](/manage/job/).

**Prerequisites**

- Signed in at <https://accsyn.io/jobs> as an elevated user (employee or admin).

## Queue system

Every job — including deliveries — is placed in a queue. If none is specified at submit time, the default queue is used. Each queue has a priority that decides which jobs run before others. Jobs do not have their own priority number; to change priority, move the job to another queue.

Three standard queues ship with accsyn:

1. **High** — priority 999  
2. **Medium** — priority 500 (default)
3. **Low** — priority 1  

### Default queue

One queue must be designated as the **default** queue, the default queue is were jobs lands when no queue is defined during the submit. 

A separate setting

## Concurrent file transfers

A queue ensures only one job between a given pair of endpoints runs at a time — effectively a virtual queue per P2P endpoint pair. accsyn cannot measure or shape bandwidth at the router, so concurrency is controlled this way.

A queue can allow more than one concurrent transfer via the `transfer_concurrent` setting.

## Re-queue jobs

To move a job to another queue:

1. Enable **Show all queues** if the destination queue is hidden.
2. Drag the job onto the new queue.

To reorder jobs within a queue:

1. Drag the job onto the drop zones that appear between jobs.

Default pre-emption by job type:

- **File transfers** — Interrupted immediately so higher-priority jobs can run.
- **Renders** — Allowed to finish the current work before yielding.

Configure workspace queues in [Queue administration](/admin/queue/).


## Configure queues

Create and configure workspace queues: [Queue administration](/admin/queue/)


## Related articles

Monitor jobs and manage pause, resume, abort, and task states: [Job monitoring](/manage/job/)



Create site and remote-user transfers: [Transfer](/transfer/)

Queue-level retry and concurrency settings: [Internal settings](/settings/)
