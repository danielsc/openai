4. Select **Review + Update** to finish the update process. There will be notification when update is completed.

5. After update is completed, in the schedule detail page, you can view the new job definition.

#### Update in schedule detail page

In schedule detail page, you can select **Update settings** to update the basic settings and advanced settings (including job input/output and runtime settings) of the schedule.

:::image type="content" source="./media/how-to-schedule-pipeline-job/schedule-update-settings.png" alt-text="Screenshot of update settings showing the basic settings tab." lightbox= "./media/how-to-schedule-pipeline-job/schedule-update-settings.png":::


### Disable a schedule

# [Azure CLI](#tab/cliv2)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

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

# [Python SDK](#tab/python)

```python
job_schedule = ml_client.schedules.begin_disable(name=schedule_name).result()
job_schedule.is_enabled
```

# [studio UI](#tab/ui)

On the schedule detail page, you can disable the current schedule. You can also disable schedules from the **All schedules** tab.


### Enable a schedule

# [Azure CLI](#tab/cliv2)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

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

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
# Update trigger expression
job_schedule.trigger.expression = "10 10 * * 1"
job_schedule = ml_client.schedules.begin_create_or_update(
    schedule=job_schedule
).result()
print(job_schedule)
```

# [studio UI](#tab/ui)

On the schedule detail page, you can enable the current schedule. You can also enable schedules from the **All schedules** tab.


## Query triggered jobs from a schedule

All the display name of jobs triggered by schedule will have the display name as <schedule_name>-YYYYMMDDThhmmssZ. For example, if a schedule with a name of named-schedule is created with a scheduled run every 12 hours starting at 6 AM on Jan 1 2021, then the display names of the jobs created will be as follows:
