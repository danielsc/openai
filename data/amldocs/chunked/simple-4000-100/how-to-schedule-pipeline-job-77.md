List continues below.

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
schedule_name = "simple_sdk_create_schedule_recurrence"

schedule_start_time = datetime.utcnow()
recurrence_trigger = RecurrenceTrigger(
    frequency="day",
    interval=1,
    schedule=RecurrencePattern(hours=10, minutes=[0, 1]),
    start_time=schedule_start_time,
    time_zone=TimeZone.UTC,
)

job_schedule = JobSchedule(
    name=schedule_name, trigger=recurrence_trigger, create_job=pipeline_job
)
```

`RecurrenceTrigger` contains following properties:

- **(Required)** To provide better coding experience, we use `RecurrenceTrigger` for recurrence schedule.

List continues below.

# [studio UI](#tab/ui)

> [!NOTE]
> Currently, Azure Machine Learning schedules (v2) only support pipeline job.
>
>The UI functions are only for Azure Machine Learning schedules (v2), which means v1 schedules created based on published pipelines or pipeline endpoints are not supported in UI - will NOT be listed or accessed in UI. However, you can create v2 schedules for your v1 pipeline jobs using SDK/CLI v2, or UI.

When you have a pipeline job with satisfying performance and outputs, you can set up a schedule to automatically trigger this job on a regular basis.

1. In pipeline job detail page, select **Schedule** -> **Create new schedule** to open the schedule creation wizard.  

    :::image type="content" source="./media/how-to-schedule-pipeline-job/schedule-entry-button.png" alt-text="Screenshot of the jobs tab with schedule button selecting showing the create new schedule button." lightbox= "./media/how-to-schedule-pipeline-job/schedule-entry-button.png":::

2. The *Basic settings* of  the schedule creation wizard contain following properties.

    :::image type="content" source="./media/how-to-schedule-pipeline-job/create-schedule-basic-settings.png" alt-text="Screenshot of schedule creation wizard showing the basic settings." lightbox= "./media/how-to-schedule-pipeline-job/create-schedule-basic-settings.png":::

    - **Name**: the unique identifier of the schedule within the workspace.
    - **Description**: description of the schedule.
    - **Trigger**: specifies the recurrence pattern of the schedule, including following properties.
      - **Time zone**: the time zone based on which to calculate the trigger time, by default is (UTC) Coordinated Universal Time.
      - **Recurrence** or **Cron expression**: select recurrence to specify the recurring pattern. Under **Recurrence**, you can specify the recurrence frequency as minutely, hourly, daily, weekly and monthly.
      - **Start**: specifies the date from when the schedule becomes active. By default it's the date you create this schedule.
      - **End**: specifies the date after when the schedule becomes inactive. By default its NONE, which means the schedule will always be active until you manually disable it.
      - **Tags**: tags of the schedule.

    After you configure the basic settings, you can directly select **Review + Create**, and the schedule will automatically submit jobs according to the recurrence pattern you specified.

> [!NOTE]
> The following properties that need to be specified apply for CLI and SDK.

- **(Required)** `frequency` specifies the unit of time that describes how often the schedule fires. Can be `minute`, `hour`, `day`, `week`, `month`.
  
- **(Required)** `interval` specifies how often the schedule fires based on the frequency, which is the number of time units to wait until the schedule fires again.
  
- (Optional) `schedule` defines the recurrence pattern, containing `hours`, `minutes`, and `weekdays`.
    - When `frequency` is `day`, pattern can specify `hours` and `minutes`.
    - When `frequency` is `week` and `month`, pattern can specify `hours`, `minutes` and `weekdays`.
    - `hours` should be an integer or a list, from 0 to 23.
    - `minutes` should be an integer or a list, from 0 to 59.
    - `weekdays` can be a string or list from `monday` to `sunday`.
