All the display name of jobs triggered by schedule will have the display name as <schedule_name>-YYYYMMDDThhmmssZ. For example, if a schedule with a name of named-schedule is created with a scheduled run every 12 hours starting at 6 AM on Jan 1 2021, then the display names of the jobs created will be as follows:

- named-schedule-20210101T060000Z
- named-schedule-20210101T180000Z
- named-schedule-20210102T060000Z
- named-schedule-20210102T180000Z, and so on

:::image type="content" source="media/how-to-schedule-pipeline-job/schedule-triggered-pipeline-jobs.png" alt-text="Screenshot of the jobs tab in the Azure Machine Learning studio filtering by job display name." lightbox= "media/how-to-schedule-pipeline-job/schedule-triggered-pipeline-jobs.png":::

You can also apply [Azure CLI JMESPath query](/cli/azure/query-azure-cli) to query the jobs triggered by a schedule name.

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

> [!NOTE]
> For a simpler way to find all jobs triggered by a schedule, see the *Jobs history* on the *schedule detail page* using the studio UI.


## Delete a schedule

> [!IMPORTANT]
> A schedule must be disabled to be deleted. Delete is an unrecoverable action. After a schedule is deleted, you can never access or recover it.

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
# Only disabled schedules can be deleted
ml_client.schedules.begin_disable(name=schedule_name).result()
ml_client.schedules.begin_delete(name=schedule_name).result()
```

# [studio UI](#tab/ui)

You can delete a schedule from the schedule detail page or all schedules tab.

## RBAC (Role-based-access-control) support

Since schedules are usually used for production, to reduce impact of misoperation, workspace admins may want to restrict access to creating and managing schedules within a workspace.

Currently there are three action rules related to schedules and you can configure in Azure portal. You can learn more details about [how to manage access to an Azure Machine Learning workspace.](how-to-assign-roles.md#create-custom-role)
