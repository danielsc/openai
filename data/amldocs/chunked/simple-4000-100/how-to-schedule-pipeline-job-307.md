
# [studio UI](#tab/ui)

1. Sometimes you may want the jobs triggered by schedules have different configurations from the test jobs. In **Advanced settings** in the schedule creation wizard, you can modify the job inputs/outputs, and run time settings, based on the current job.

    In the substep **Job inputs & outputs**, you can modify inputs and outputs for the future jobs triggered by schedules. You may want the jobs triggered by schedules running with dynamic parameters values. Currently you can use following MACRO expression for job inputs and outputs path.

    | Expression                           | Description             |
    |--------------------------------------|-------------------------|
    | `${{name}}`                          | name of the job         |
    | `${{creation_context.trigger_time}}` | trigger time of the job |

      :::image type="content" source="./media/how-to-schedule-pipeline-job/create-schedule-advanced-settings-inputs-outputs.png" alt-text="Screenshot of create new schedule on the advanced settings job inputs and outputs tab." lightbox= "./media/how-to-schedule-pipeline-job/create-schedule-advanced-settings-inputs-outputs.png":::

    In the substep **Job runtime settings**, you can modify compute and other run time settings for jobs triggered by the schedule.

    :::image type="content" source="./media/how-to-schedule-pipeline-job/create-schedule-advanced-settings-runtime.png" alt-text="Screenshot of schedule creation wizard showing the job runtime settings." lightbox= "./media/how-to-schedule-pipeline-job/create-schedule-advanced-settings-runtime.png":::


2. Select **Review + Create** to review the schedule settings you've configured.

    :::image type="content" source="./media/how-to-schedule-pipeline-job/create-schedule-review.png" alt-text="Screenshot of schedule creation wizard showing the review of the schedule settings." lightbox= "./media/how-to-schedule-pipeline-job/create-schedule-review.png":::

3. Select **Review + Create** to finish the creation. There will be notification when the creation is completed.


Following properties can be changed when defining schedule:

| Property | Description |
| --- | --- |
|settings| A dictionary of settings to be used when running the pipeline job. |
|inputs| A dictionary of inputs to be used when running the pipeline job. |
|outputs| A dictionary of inputs to be used when running the pipeline job. |
|experiment_name|Experiment name of triggered job.|

> [!NOTE]
> Studio UI users can only modify input, output, and runtime settings when creating a schedule. `experiment_name` can only be changed using the CLI or SDK.

### Expressions supported in schedule

When define schedule, we support following expression that will be resolved to real value during job runtime.

| Expression | Description |Supported properties|
|----------------|----------------|-------------|
|`${{creation_context.trigger_time}}`|The time when the schedule is triggered.|String type inputs of pipeline job|
|`${{name}}`|The name of job.|outputs.path of pipeline job|

## Manage schedule

### Create schedule

# [Azure CLI](#tab/cliv2)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

After you create the schedule yaml, you can use the following command to create a schedule via CLI.

```azurecli
# <create_schedule>
# This action will create related resources for a schedule. It will take dozens of seconds to complete.
az ml schedule create --file cron-schedule.yml --no-wait
# </create_schedule>

# <show_schedule>
az ml schedule show -n simple_cron_job_schedule
# </show_schedule>

# <list_schedule>
az ml schedule list
# </list_schedule>

# <update_schedule>
az ml schedule update -n simple_cron_job_schedule  --set description="new description" --no-wait
# </update_schedule>

# <disable_schedule>
az ml schedule disable -n simple_cron_job_schedule --no-wait
# </disable_schedule>

# <enable_schedule>
az ml schedule enable -n simple_cron_job_schedule --no-wait
# </enable_schedule>

# <query_triggered_jobs>
# query triggered jobs from schedule, please replace the simple_cron_job_schedule to your schedule name
az ml job list --query "[?contains(display_name,'simple_cron_schedule')]" 
# </query_triggered_jobs>

# <delete_schedule>
az ml schedule delete -n simple_cron_job_schedule
# </delete_schedule>

```
