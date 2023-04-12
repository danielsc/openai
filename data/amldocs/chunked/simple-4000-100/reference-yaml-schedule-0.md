
# CLI (v2) schedule YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The source JSON schema can be found at https://azuremlschemas.azureedge.net/latest/schedule.schema.json.

[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `$schema` | string | The YAML schema. | |
| `name` | string | **Required.** Name of the schedule. | |
| `version` | string | Version of the schedule. If omitted, Azure ML will autogenerate a version. | |
| `description` | string | Description of the schedule. | |
| `tags` | object | Dictionary of tags for the schedule. | |
| `trigger` | object | The trigger configuration to define rule when to trigger job. **One of `RecurrenceTrigger` or `CronTrigger` is required.** | |
| `create_job` | object or string | **Required.** The definition of the job that will be triggered by a  schedule. **One of `string` or `JobDefinition` is required.**| |

### Trigger configuration

#### Recurrence trigger

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | string | **Required.** Specifies the schedule type. |recurrence|
|`frequency`| string | **Required.** Specifies the unit of time that describes how often the schedule fires.|`minute`, `hour`, `day`, `week`, `month`|
|`interval`| integer | **Required.** Specifies the interval at which the schedule fires.| |
|`start_time`| string |Describes the start date and time with timezone. If start_time is omitted, the first job will run instantly and the future jobs will be triggered based on the schedule, saying start_time will be equal to the job created time. If the start time is in the past, the first job will run at the next calculated run time.|
|`end_time`| string |Describes the end date and time with timezone. If end_time is omitted, the schedule will continue to run until it's explicitly disabled.|
|`timezone`| string |Specifies the time zone of the recurrence. If omitted, by default is UTC. |See [appendix for timezone values](#timezone)|
|`pattern`|object|Specifies the pattern of the recurrence. If pattern is omitted, the job(s) will be triggered according to the logic of start_time, frequency and interval.| |

#### Recurrence schedule

Recurrence schedule defines the recurrence pattern, containing `hours`, `minutes`, and `weekdays`.

- When frequency is `day`, pattern can specify `hours` and `minutes`.
- When frequency is `week` and `month`, pattern can specify `hours`, `minutes` and `weekdays`.

| Key | Type | Allowed values |
| --- | ---- | -------------- |
|`hours`|integer or array of integer|`0-23`|
|`minutes`|integer or array of integer|`0-59`|
|`week_days`|string or array of string|`monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, `sunday`|


#### CronTrigger

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | string | **Required.** Specifies the schedule type. |cron|
| `expression` | string | **Required.** Specifies the cron expression to define how to trigger jobs. expression uses standard crontab expression to express a recurring schedule. A single expression is composed of five space-delimited fields:`MINUTES HOURS DAYS MONTHS DAYS-OF-WEEK`||
|`start_time`| string |Describes the start date and time with timezone. If start_time is omitted, the first job will run instantly and the future jobs will be triggered based on the schedule, saying start_time will be equal to the job created time. If the start time is in the past, the first job will run at the next calculated run time.|
|`end_time`| string |Describes the end date and time with timezone. If end_time is omitted, the schedule will continue to run until it's explicitly disabled.|
|`timezone`| string |Specifies the time zone of the recurrence. If omitted, by default is UTC. |See [appendix for timezone values](#timezone)|
