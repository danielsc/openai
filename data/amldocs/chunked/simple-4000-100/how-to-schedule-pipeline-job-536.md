    :::image type="content" source="./media/how-to-schedule-pipeline-job/schedule-detail-overview.png" alt-text="Screenshot of the overview tab in the schedule detail page." lightbox= "./media/how-to-schedule-pipeline-job/schedule-detail-overview.png":::

- **Job definition**: defines the job triggered by this schedule.

  :::image type="content" source="./media/how-to-schedule-pipeline-job/schedule-detail-job-definition.png" alt-text="Screenshot of the job definition tab in the schedule detail page." lightbox= "./media/how-to-schedule-pipeline-job/schedule-detail-job-definition.png":::

- **Jobs history**: a list of all jobs triggered by this schedule.

 :::image type="content" source="./media/how-to-schedule-pipeline-job/schedule-detail-jobs-history.png" alt-text="Screenshot of the jobs history tab in the schedule detail page." lightbox= "./media/how-to-schedule-pipeline-job/schedule-detail-jobs-history.png":::


### Update a schedule

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

> [!NOTE]
> If you would like to update more than just tags/description, it is recomend to use `az ml schedule create --file update_schedule.yml`

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
job_schedule = ml_client.schedules.begin_create_or_update(
    schedule=job_schedule
).result()
print(job_schedule)
```

# [studio UI](#tab/ui)

#### Update a new version pipeline to existing schedule


Once you set up a schedule to do retraining or batch inference on production regularly, you may still work on fine tuning or optimizing the model.

When you have a new version pipeline job with optimized performance, you can update the new version pipeline to an existing schedule.

1. In the new version pipeline job detail page, select **Schedule** -> **Update to existing schedule**.

     :::image type="content" source="./media/how-to-schedule-pipeline-job/update-to-existing-schedule.png" alt-text="Screenshot of the jobs tab with schedule button selected showing update to existing schedule button." lightbox= "./media/how-to-schedule-pipeline-job/update-to-existing-schedule.png":::

2. Select an existing schedule from the table. 

    :::image type="content" source="./media/how-to-schedule-pipeline-job/update-select-schedule.png" alt-text="Screenshot of update select schedule showing the select schedule tab." lightbox= "./media/how-to-schedule-pipeline-job/update-select-schedule.png":::

> [!IMPORTANT]
> Make sure you select the correct schedule you want to update. Once you finish update, the schedule will trigger different jobs.

3. You can also modify the job inputs/outputs, and run time settings for the future jobs triggered by the schedule.

4. Select **Review + Update** to finish the update process. There will be notification when update is completed.

5. After update is completed, in the schedule detail page, you can view the new job definition.
