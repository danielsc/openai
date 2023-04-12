- **(Required)** `expression` uses standard crontab expression to express a recurring schedule. A single expression is composed of five space-delimited fields:

    `MINUTES HOURS DAYS MONTHS DAYS-OF-WEEK`

    - A single wildcard (`*`), which covers all values for the field. So a `*` in days means all days of a month (which varies with month and year).
    - The `expression: "15 16 * * 1"` in the sample above means the 16:15PM on every Monday.
    - The table below lists the valid values for each field:
 
        | Field          |   Range  | Comment                                                   |
        |----------------|----------|-----------------------------------------------------------|
        | `MINUTES`      |    0-59  | -                                                         |
        | `HOURS`        |    0-23  | -                                                         |
        | `DAYS`         |    -  |    Not supported. The value will be ignored and treat as `*`.    |
        | `MONTHS`       |    -  | Not supported. The value will be ignored and treat as `*`.        |
        | `DAYS-OF-WEEK` |    0-6   | Zero (0) means Sunday. Names of days also accepted. |

    - To learn more about how to use crontab expression, see  [Crontab Expression wiki on GitHub ](https://github.com/atifaziz/NCrontab/wiki/Crontab-Expression).

    > [!IMPORTANT]
    > `DAYS` and `MONTH` are not supported. If you pass a value, it will be ignored and treat as `*`.

- (Optional) `start_time` specifies the start date and time with timezone of the schedule. `start_time: "2022-05-10T10:15:00-04:00"` means the schedule starts from 10:15:00AM on 2022-05-10 in UTC-4 timezone. If `start_time` is omitted, the `start_time` will be equal to schedule creation time. If the start time is in the past, the first job will run at the next calculated run time.

- (Optional) `end_time` describes the end date and time with timezone. If `end_time` is omitted, the schedule will continue trigger jobs until the schedule is manually disabled.  

- (Optional) `time_zone`specifies the time zone of the expression. If omitted, by default is UTC. See [appendix for timezone values](reference-yaml-schedule.md#appendix).

Limitations:

- Currently Azure Machine Learning v2 schedule doesn't support event-based trigger.
- You can specify complex recurrence pattern containing multiple trigger timestamps using Azure Machine Learning SDK/CLI v2, while UI only displays the complex pattern and doesn't support editing.
- If you set the recurrence as the 31st day of every month, in months with less than 31 days, the schedule won't trigger jobs.

### Change runtime settings when defining schedule

When defining a schedule using an existing job, you can change the runtime settings of the job. Using this approach, you can define multi-schedules using the same job with different inputs.

# [Azure CLI](#tab/cliv2)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/schedule.schema.json
name: cron_with_settings_job_schedule
display_name: Simple cron job schedule
description: a simple hourly cron job schedule

trigger:
  type: cron
  expression: "0 * * * *"
  start_time: "2022-07-10T10:00:00" # optional - default will be schedule creation time
  time_zone: "Pacific Standard Time" # optional - default will be UTC

create_job: 
  type: pipeline
  job: ./simple-pipeline-job.yml
  # job: azureml:simple-pipeline-job
  # runtime settings
  settings:
    #default_compute: azureml:cpu-cluster
    continue_on_step_failure: true
  inputs:
    hello_string_top_level_input: ${{name}} 
  tags: 
    schedule: cron_with_settings_schedule
```

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
# set run time settings
pipeline_job = pipeline_with_components_from_yaml(
    training_input=Input(type="uri_folder", path=parent_dir + "/data/"),
    test_input=Input(type="uri_folder", path=parent_dir + "/data/"),
    training_max_epochs=20,
    training_learning_rate=1.8,
    learning_rate_schedule="time-based",
)

# set pipeline level compute
pipeline_job.settings.default_compute = "cpu-cluster"
```
