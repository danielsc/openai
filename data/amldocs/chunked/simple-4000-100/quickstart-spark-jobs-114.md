>  - Please ensure that `titanic.py` file is uploaded to a folder named `src`. The `src` folder should be located in the same directory where you have created the Python script/notebook or the YAML specification file defining the standalone Spark job.

That script takes two arguments: `--titanic_data` and `--wrangled_data`. These arguments pass the input data path, and the output folder, respectively. The script uses the `titanic.csv` file, [available here](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/spark/data/titanic.csv). Upload this file to a container created in the Azure Data Lake Storage (ADLS) Gen 2 storage account.

## Submit a standalone Spark job

# [CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

> [!TIP]
> You can submit a Spark job from:
>  - [terminal of an Azure Machine Learning compute instance](./how-to-access-terminal.md#access-a-terminal). 
>  - terminal of [Visual Studio Code connected to an Azure Machine Learning compute instance](./how-to-set-up-vs-code-remote.md?tabs=studio).
>  - your local computer that has [the Azure Machine Learning CLI](./how-to-configure-cli.md?tabs=public) installed.

This example YAML specification shows a standalone Spark job. It uses an Azure Machine Learning Managed (Automatic) Spark compute, user identity passthrough, and input/output data URI in the `abfss://<FILE_SYSTEM_NAME>@<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net/<PATH_TO_DATA>` format. Here, `<FILE_SYSTEM_NAME>` matches the container name.

```yaml
$schema: http://azureml/sdk-2-0/SparkJob.json
type: spark

code: ./src 
entry:
  file: titanic.py

conf:
  spark.driver.cores: 1
  spark.driver.memory: 2g
  spark.executor.cores: 2
  spark.executor.memory: 2g
  spark.executor.instances: 2

inputs:
  titanic_data:
    type: uri_file
    path: abfss://<FILE_SYSTEM_NAME>@<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net/data/titanic.csv
    mode: direct

outputs:
  wrangled_data:
    type: uri_folder
    path: abfss://<FILE_SYSTEM_NAME>@<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net/data/wrangled/
    mode: direct

args: >-
  --titanic_data ${{inputs.titanic_data}}
  --wrangled_data ${{outputs.wrangled_data}}

identity:
  type: user_identity

resources:
  instance_type: standard_e4s_v3
  runtime_version: "3.2"
```

In the above YAML specification file:
- `code` property defines relative path of the folder containing parameterized `titanic.py` file.
- `resource` property defines `instance_type` and Apache Spark `runtime_version` used by Managed (Automatic) Spark compute. The following instance types are currently supported:
    - `standard_e4s_v3`
    - `standard_e8s_v3`
    - `standard_e16s_v3`
    - `standard_e32s_v3`
    - `standard_e64s_v3`

The YAML file shown can be used in the `az ml job create` command, with the `--file` parameter, to create a standalone Spark job as shown:

```azurecli
az ml job create --file <YAML_SPECIFICATION_FILE_NAME>.yaml --subscription <SUBSCRIPTION_ID> --resource-group <RESOURCE_GROUP> --workspace-name <AML_WORKSPACE_NAME>
```

# [Python SDK](#tab/sdk)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

> [!TIP]
> You can submit a Spark job from:
>  - an Azure Machine Learning Notebook connected to an Azure Machine Learning compute instance. 
>  - [Visual Studio Code connected to an Azure Machine Learning compute instance](./how-to-set-up-vs-code-remote.md?tabs=studio).
>  - your local computer that has [the Azure Machine Learning SDK for Python](/python/api/overview/azure/ai-ml-readme) installed.

This Python code snippet shows a standalone Spark job creation, with an Azure Machine Learning Managed (Automatic) Spark compute, user identity passthrough, and input/output data URI in the `abfss://<FILE_SYSTEM_NAME>@<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net/<PATH_TO_DATA>`format. Here, the `<FILE_SYSTEM_NAME>` matches the container name.

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
            path="abfss://<FILE_SYSTEM_NAME>@<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net/data/titanic.csv",
            mode="direct",
        ),
    },
    outputs={
        "wrangled_data": Output(
            type="uri_folder",
            path="abfss://<FILE_SYSTEM_NAME>@<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net/data/wrangled/",
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
