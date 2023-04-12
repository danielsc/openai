:::image type="content" source="media/how-to-track-monitor-analyze-runs/run-description-2.gif" alt-text="Screenshot of how to create a job description."::: 


## Tag and find jobs

In Azure Machine Learning, you can use properties and tags to help organize and query your jobs for important information.

* Edit tags

    You can add, edit, or delete job tags from the studio. Navigate to the **Job Details** page for your job and select the edit, or pencil icon to add, edit, or delete tags for your jobs. You can also search and filter on these tags from the jobs list page.
    
    :::image type="content" source="media/how-to-track-monitor-analyze-runs/run-tags.gif" alt-text="Screenshot of how to add, edit, or delete job tags.":::
    

* Query properties and tags

    You can query jobs within an experiment to return a list of jobs that match specific properties and tags.
    
    To search for specific jobs, navigate to the  **All jobs** list. From there you have two options:
    
    1. Use the **Add filter** button and select filter on tags to filter your jobs by tag that was assigned to the job(s). <br><br>
    OR
    
    1. Use the search bar to quickly find jobs by searching on the job metadata like the job status, descriptions, experiment names, and submitter name. 

## Cancel or fail jobs

If you notice a mistake or if your job is taking too long to finish, you can cancel the job.

To cancel a job in the studio, using the following steps:

1. Go to the running pipeline in either the **Jobs** or **Pipelines** section. 

1. Select the pipeline job number you want to cancel.

1. In the toolbar, select **Cancel**.

## Monitor the job status by email notification

1. In the [Azure portal](https://portal.azure.com/), in the left navigation bar, select the **Monitor** tab. 

1. Select **Diagnostic settings** and then select **+ Add diagnostic setting**.

    ![Screenshot of diagnostic settings for email notification](./media/how-to-track-monitor-analyze-runs/diagnostic-setting.png)

1. In the Diagnostic Setting, 
    1. under the **Category details**, select the **AmlRunStatusChangedEvent**. 
    1. In the **Destination details**, select the **Send to Log Analytics workspace**  and specify the **Subscription** and **Log Analytics workspace**. 

    > [!NOTE]
    > The **Azure Log Analytics Workspace** is a different type of Azure Resource than the **Azure Machine Learning service Workspace**. If there are no options in that list, you can [create a Log Analytics Workspace](../azure-monitor/logs/quick-create-workspace.md). 
    
    ![Where to save email notification](./media/how-to-track-monitor-analyze-runs/log-location.png)

1. In the **Logs** tab, add a **New alert rule**. 

    ![New alert rule](./media/how-to-track-monitor-analyze-runs/new-alert-rule.png)

1. See [how to create and manage log alerts using Azure Monitor](../azure-monitor/alerts/alerts-log.md).

## Monitor your job resources (preview)

Navigate to your job in the studio and select the Monitoring tab. This view provides insights on your job's resources on a 30 day rolling basis. 

:::image type="content" source="media/how-to-track-monitor-analyze-runs/monitoring-tab.png" alt-text="Screenshot of Monitoring tab showing resources the selected job has used.":::

>[!NOTE] 
>This view supports only compute that is managed by AzureML.
>Jobs with a runtime of less than 5 minutes will not have enough data to populate this view.


## Next steps

* To learn how to log metrics for your experiments, see [Log metrics during training jobs](how-to-log-view-metrics.md).
* To learn how to monitor resources and logs from Azure Machine Learning, see [Monitoring Azure Machine Learning](monitor-azure-machine-learning.md).
