    - `minutes` should be an integer or a list, from 0 to 59.
    - `weekdays` can be a string or list from `monday` to `sunday`.
    - If `schedule` is omitted, the job(s) will be triggered according to the logic of `start_time`, `frequency` and `interval`.

- (Optional) `start_time` describes the start date and time with timezone. If `start_time` is omitted, start_time will be equal to the job created time. If the start time is in the past, the first job will run at the next calculated run time.

- (Optional) `end_time` describes the end date and time with timezone. If `end_time` is omitted, the schedule will continue trigger jobs until the schedule is manually disabled.  

- (Optional) `time_zone` specifies the time zone of the recurrence. If omitted, by default is UTC. To learn more about timezone values, see [appendix for timezone values](reference-yaml-schedule.md#appendix).

### Create a time-based schedule with cron expression

# [Azure CLI](#tab/cliv2)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/schedule.schema.json
name: simple_cron_job_schedule
display_name: Simple cron job schedule
description: a simple hourly cron job schedule

trigger:
  type: cron
  expression: "0 * * * *"
  start_time: "2022-07-10T10:00:00" # optional - default will be schedule creation time
  time_zone: "Pacific Standard Time" # optional - default will be UTC

# create_job: azureml:simple-pipeline-job
create_job: ./simple-pipeline-job.yml
```

The `trigger` section defines the schedule details and contains following properties:

- **(Required)** `type` specifies the schedule type is `cron`.

List continues below.

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
schedule_name = "simple_sdk_create_schedule_cron"

schedule_start_time = datetime.utcnow()
cron_trigger = CronTrigger(
    expression="15 10 * * *",
    start_time=schedule_start_time,  # start time
    time_zone="Eastern Standard Time",  # time zone of expression
)

job_schedule = JobSchedule(
    name=schedule_name, trigger=cron_trigger, create_job=pipeline_job
)
```

The `CronTrigger` section defines the schedule details and contains following properties:

- **(Required)** To provide better coding experience, we use `CronTrigger` for recurrence schedule.

List continues below.

# [studio UI](#tab/ui)

When you have a pipeline job with satisfying performance and outputs, you can set up a schedule to automatically trigger this job on a regular basis.

1. In pipeline job detail page, select **Schedule** -> **Create new schedule** to open the schedule creation wizard.

2. The *Basic settings* of the schedule creation wizard contain following properties.

    - **Name**: the unique identifier of the schedule within the workspace.
    - **Description**: description of the schedule.
    - **Trigger**: specifies the recurrence pattern of the schedule, including following properties.
      - **Time zone**: the time zone based on which to calculate the trigger time, by default is (UTC) Coordinated Universal Time.
      - **Recurrence** or **Cron expression**: select cron expression to specify the recurring pattern. **Cron expression** allows you to specify more flexible and customized recurrence pattern.
      - **Start**: specifies the date from when the schedule becomes active. By default it's the date you create this schedule.
      - **End**: specifies the date after when the schedule becomes inactive. By default it's NONE, which means the schedule will always be active until you manually disable it.
      - **Tags**: tags of the schedule.

    After you configure the basic settings, you can directly select Review + Create, and the schedule will automatically submit jobs according to the recurrence pattern you specified.


- **(Required)** `expression` uses standard crontab expression to express a recurring schedule. A single expression is composed of five space-delimited fields:
