  - a corresponding value is an object of class `azure.ai.ml.Output`, with the following parameters:
      - `type` - set this parameter to `uri_file` or `uri_folder`, for an output data file or a folder respectively.
      - `path` - the URI of the output data, such as `azureml://`, `abfss://`, or `wasbs://`.
      - `mode` - set this parameter to `direct`.
- `identity` - an optional parameter that defines the identity used for submission of this job. Allowed values are an object of class 
  - `azure.ai.ml.entities.UserIdentityConfiguration`
  or
  - `azure.ai.ml.entities.ManagedIdentityConfiguration`
  for user identity and managed identity respectively. If no identity is defined, the default identity will be used.

You can submit a standalone Spark job from:
- an Azure Machine Learning Notebook connected to an Azure Machine Learning compute instance. 
- [Visual Studio Code connected to an Azure Machine Learning compute instance](./how-to-set-up-vs-code-remote.md?tabs=studio).
- your local computer that has [the Azure Machine Learning SDK for Python](/python/api/overview/azure/ai-ml-readme) installed.

This Python code snippet shows the creation of a standalone Spark job, with an Azure Machine Learning Managed (Automatic) Spark compute, using user identity.

```python
from azure.ai.ml import MLClient, spark, Input, Output
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import UserIdentityConfiguration

subscription_id = "<SUBSCRIPTION_ID>"
resource_group = "<RESOURCE_GROUP>"
workspace_name = "<AML_WORKSPACE_NAME>"
ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace_name
)

spark_job = spark(
    display_name="Titanic-Spark-Job-SDK",
    code="./src",
    entry={"file": "titanic.py"},
    driver_cores=1,
    driver_memory="2g",
    executor_cores=2,
    executor_memory="2g",
    executor_instances=2,
    resources={
        "instance_type": "Standard_E8S_V3",
        "runtime_version": "3.2.0",
    },
    inputs={
        "titanic_data": Input(
            type="uri_file",
            path="azureml://datastores/workspaceblobstore/paths/data/titanic.csv",
            mode="direct",
        ),
    },
    outputs={
        "wrangled_data": Output(
            type="uri_folder",
            path="azureml://datastores/workspaceblobstore/paths/data/wrangled/",
            mode="direct",
        ),
    },
    identity=UserIdentityConfiguration(),
    args="--titanic_data ${{inputs.titanic_data}} --wrangled_data ${{outputs.wrangled_data}}",
)

returned_spark_job = ml_client.jobs.create_or_update(spark_job)

# Wait until the job completes
ml_client.jobs.stream(returned_spark_job.name)
```

> [!NOTE]
> To use an attached Synapse Spark pool, define the `compute` parameter in the `azure.ai.ml.spark` function, instead of `resources`.

# [Studio UI](#tab/ui)

### Submit a standalone Spark job from Azure Machine Learning Studio UI
To submit a standalone Spark job using the Azure Machine Learning Studio UI:

:::image type="content" source="media/how-to-submit-spark-jobs/create_standalone_spark_job.png" alt-text="Screenshot showing creation of a new Spark job in Azure Machine Learning Studio UI.":::

- In the left pane, select **+ New**.
- Select **Spark job (preview)**.
- On the **Compute** screen:
 
:::image type="content" source="media/how-to-submit-spark-jobs/create_standalone_spark_job_compute.png" alt-text="Screenshot showing compute selection screen for a new Spark job in Azure Machine Learning Studio UI.":::

1. Under **Select compute type**, select **Spark automatic compute (Preview)** for Managed (Automatic) Spark compute, or **Attached compute** for an attached Synapse Spark pool.
1. If you selected **Spark automatic compute (Preview)**:
    1. Select **Virtual machine size**.
    1. Select **Spark runtime version**.
1. If you selected **Attached compute**:
    1. Select an attached Synapse Spark pool from the **Select Azure ML attached compute** menu.
1. Select **Next**.
