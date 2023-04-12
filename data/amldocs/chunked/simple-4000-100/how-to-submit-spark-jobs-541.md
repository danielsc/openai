
The Spark component defined in the above YAML specification file can be used in an Azure Machine Learning pipeline job. See [pipeline job YAML schema](./reference-yaml-job-pipeline.md) to learn more about the YAML syntax that defines a pipeline job. This example shows a YAML specification file for a pipeline job, with a Spark component, and an Azure Machine Learning Managed (Automatic) Spark compute:

```yaml
$schema: http://azureml/sdk-2-0/PipelineJob.json
type: pipeline
display_name: Titanic-Spark-CLI-Pipeline
description: Spark component for Titanic data in Pipeline

jobs:
  spark_job:
    type: spark
    component: ./spark-job-component.yaml
    inputs:
      titanic_data: 
        type: uri_file
        path: azureml://datastores/workspaceblobstore/paths/data/titanic.csv
        mode: direct

    outputs:
      wrangled_data:
        type: uri_folder
        path: azureml://datastores/workspaceblobstore/paths/data/wrangled/
        mode: direct

    identity:
      type: managed

    resources:
      instance_type: standard_e8s_v3
      runtime_version: "3.2"
```
> [!NOTE]
> To use an attached Synapse Spark pool, define the `compute` property in the sample YAML specification file shown above, instead of `resources` property.

The above YAML specification file can be used in `az ml job create` command, using the `--file` parameter, to create a pipeline job as shown:

```azurecli
az ml job create --file <YAML_SPECIFICATION_FILE_NAME>.yaml --subscription <SUBSCRIPTION_ID> --resource-group <RESOURCE_GROUP> --workspace-name <AML_WORKSPACE_NAME>
```

You can execute the above command from:
- [terminal of an Azure Machine Learning compute instance](how-to-access-terminal.md#access-a-terminal). 
- terminal of [Visual Studio Code connected to an Azure Machine Learning compute instance](./how-to-set-up-vs-code-remote.md?tabs=studio).
- your local computer that has [Azure Machine Learning CLI](./how-to-configure-cli.md?tabs=public) installed.

# [Python SDK](#tab/sdk)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

To create an Azure Machine Learning pipeline with a Spark component, you should have familiarity with creation of [Azure Machine Learning pipelines from components, using Python SDK](./tutorial-pipeline-python-sdk.md#create-the-pipeline-from-components). A Spark component is created using `azure.ai.ml.spark` function. The function parameters are defined almost the same way as for the [standalone Spark job](#standalone-spark-job-using-python-sdk). These parameters are defined differently for the Spark component:

- `name` - the name of the Spark component.
- `display_name` - the name of the Spark component that will display in the UI and elsewhere.
- `inputs` - this parameter is similar to `inputs` parameter described for the [standalone Spark job](#standalone-spark-job-using-python-sdk), except that the `azure.ai.ml.Input` class is instantiated without the `path` parameter.
- `outputs` - this parameter is similar to `outputs` parameter described for the [standalone Spark job](#standalone-spark-job-using-python-sdk), except that the `azure.ai.ml.Output` class is instantiated without the `path` parameter.

> [!NOTE]
> A Spark component created using `azure.ai.ml.spark` function does not define `identity`,  `compute` or `resources` parameters. The Azure Machine Learning pipeline defines these parameters.

You can submit a pipeline job with a Spark component from:
- an Azure Machine Learning Notebook connected to an Azure Machine Learning compute instance. 
- [Visual Studio Code connected to an Azure Machine Learning compute instance](./how-to-set-up-vs-code-remote.md?tabs=studio).
- your local computer that has [the Azure Machine Learning SDK for Python](/python/api/overview/azure/ai-ml-readme) installed.

This Python code snippet shows use of a managed identity, together with the creation of an Azure Machine Learning pipeline job. Additionally, it shows use of a Spark component and an Azure Machine Learning Managed (Automatic) Synapse compute:
