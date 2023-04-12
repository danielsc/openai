
# Schedule machine learning pipeline jobs

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

In this article, you'll learn how to programmatically schedule a pipeline to run on Azure and use the schedule UI to do the same. You can create a schedule based on elapsed time. Time-based schedules can be used to take care of routine tasks, such as retrain models or do batch predictions regularly to keep them up-to-date. After learning how to create schedules, you'll learn how to retrieve, update and deactivate them via CLI, SDK, and studio UI.

## Prerequisites

- You must have an Azure subscription to use Azure Machine Learning. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/) today.

# [Azure CLI](#tab/cliv2)

- Install the Azure CLI and the `ml` extension. Follow the installation steps in [Install, set up, and use the CLI (v2)](how-to-configure-cli.md).

- Create an Azure Machine Learning workspace if you don't have one. For workspace creation, see [Install, set up, and use the CLI (v2)](how-to-configure-cli.md).

# [Python SDK](#tab/python)

- Create an Azure Machine Learning workspace if you don't have one.
- The [Azure Machine Learning SDK v2 for Python](/python/api/overview/azure/ai-ml-readme).

# [studio UI](#tab/ui)

- An Azure Machine Learning workspace. See [Create workspace resources](quickstart-create-resources.md).
- Understanding of Azure Machine Learning pipelines. See [what are machine learning pipelines](concept-ml-pipelines.md), and how to create pipeline job in [CLI v2](how-to-create-component-pipelines-cli.md) or [SDK v2](how-to-create-component-pipeline-python.md).
- To enable this feature:
  1. Navigate to Azure Machine Learning studio UI.
  2. Select **Manage preview features** (megaphone icon) among the icons on the top right side of the screen.
  3. In **Managed preview feature** panel, toggle on **Create and manage your pipeline schedule** feature.
    :::image type="content" source="./media/how-to-schedule-pipeline-job/manage-preview-features.png" alt-text="Screenshot of manage preview features toggled on." lightbox= "./media/how-to-schedule-pipeline-job/manage-preview-features.png":::


## Schedule a pipeline job

To run a pipeline job on a recurring basis, you'll need to create a schedule. A `Schedule` associates a job, and a trigger. The trigger can either be `cron` that use cron expression to describe the wait between runs or `recurrence` that specify using what frequency to trigger job. In each case, you need to define a pipeline job first, it can be existing pipeline jobs or a pipeline job define inline, refer to [Create a pipeline job in CLI](how-to-create-component-pipelines-cli.md) and [Create a pipeline job in SDK](how-to-create-component-pipeline-python.md).

You can schedule a pipeline job yaml in local or an existing pipeline job in workspace.

## Create a schedule

### Create a time-based schedule with recurrence pattern

# [Azure CLI](#tab/cliv2)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/schedule.schema.json
name: simple_recurrence_job_schedule
display_name: Simple recurrence job schedule
description: a simple hourly recurrence job schedule

trigger:
  type: recurrence
  frequency: day #can be minute, hour, day, week, month
  interval: 1 #every day
  schedule:
    hours: [4,5,10,11,12]
    minutes: [0,30]
  start_time: "2022-07-10T10:00:00" # optional - default will be schedule creation time
  time_zone: "Pacific Standard Time" # optional - default will be UTC

create_job: ./simple-pipeline-job.yml
# create_job: azureml:simple-pipeline-job

```

`trigger` contains the following properties:

- **(Required)**  `type` specifies the schedule type is `recurrence`. It can also be `cron`, see details in the next section.

List continues below.

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
