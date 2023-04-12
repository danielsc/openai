
# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
job_schedule = ml_client.schedules.begin_create_or_update(
    schedule=job_schedule
).result()
print(job_schedule)
```

# [studio UI](#tab/ui)

See [Create a time-based schedule with recurrence pattern](#create-a-time-based-schedule-with-recurrence-pattern) or [Create a time-based schedule with cron expression](#create-a-time-based-schedule-with-cron-expression).


### List schedules in a workspace

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
schedules = ml_client.schedules.list()
[s.name for s in schedules]
```

# [studio UI](#tab/ui)

In the studio portal, under **Jobs** extension select the **All schedules** tab, where you can find all your job schedules created by SDK/CLI/UI in a single list.
In the schedule list, you can have an overview of all schedules in this workspace.

:::image type="content" source="./media/how-to-schedule-pipeline-job/schedule-list.png" alt-text="Screenshot of the all schedule tabs showing the list of schedule in this workspace." lightbox= "./media/how-to-schedule-pipeline-job/schedule-list.png":::


### Check schedule detail

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
created_schedule = ml_client.schedules.get(name=schedule_name)
[created_schedule.name]
```

# [studio UI](#tab/ui)

You can select a schedule name to show the schedule detail page. The schedule detail page contains the following tabs:

- **Overview**: basic information of this schedule.

    :::image type="content" source="./media/how-to-schedule-pipeline-job/schedule-detail-overview.png" alt-text="Screenshot of the overview tab in the schedule detail page." lightbox= "./media/how-to-schedule-pipeline-job/schedule-detail-overview.png":::
