
Update the `environment` to point to the `SKLearnEnv` environment created in the previous section and create the environment. 

```python
train_model.environment=env_from_registry
ml_client_registry.components.create_or_update(train_model)
```

> [!TIP]
> If you get an error that the name of the component already exists in the registry, you can either update the version with `train_model.version=<unique_version_number>` before creating the component. 

Note down the `name` and `version` of the component from the output and pass them to the `ml_client_registry.component.get()` method to fetch the component from registry. 

You can also use `ml_client_registry.component.list()` to list all components in the registry or browse all components in the AzureML Studio UI. Make sure you navigate to the global UI and look for the Registries hub.


You can browse all components in the AzureML studio. Make sure you navigate to the global UI and look for the __Registries__ entry.

:::image type="content" source="./media/how-to-share-models-pipelines-across-workspaces-with-registries/component-in-registry.png" lightbox="./media/how-to-share-models-pipelines-across-workspaces-with-registries/component-in-registry.png" alt-text="Screenshot of components in the registry.":::

## Run a pipeline job in a workspace using component from registry

When running a pipeline job that uses a component from a registry, the _compute_ resources and _training data_ are local to the workspace. For more information on running jobs, see the following articles:

* [Running jobs (CLI)](./how-to-train-cli.md)
* [Running jobs (SDK)](./how-to-train-sdk.md)
* [Pipeline jobs with components (CLI)](./how-to-create-component-pipelines-cli.md)
* [Pipeline jobs with components (SDK)](./how-to-create-component-pipeline-python.md)

# [Azure CLI](#tab/cli)

We'll run a pipeline job with the Scikit Learn training component created in the previous section to train a model. Check that you are in the folder `cli/jobs/pipelines-with-components/nyc_taxi_data_regression`. The training dataset is located in the `data_transformed` folder. Edit the `component` section in under the `train_job` section of the `single-job-pipeline.yml` file to refer to the training component created in the previous section.  The resulting `single-job-pipeline.yml` is shown below.

```YAML
$schema: https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json
type: pipeline
display_name: nyc_taxi_data_regression_single_job
description: Single job pipeline to train regression model based on nyc taxi dataset

jobs:
  train_job:
    type: command
    component: azureml://registries/<registry-name>/component/train_linear_regression_model/versions/1
    compute: azureml:cpu-cluster
    inputs:
      training_data: 
        type: uri_folder
        path: ./data_transformed
    outputs:
      model_output: 
        type: mlflow_model
      test_data: 
```  

The key aspect is that this pipeline is going to run in a workspace using a component that isn't in the specific workspace. The component is in a registry that can be used with any workspace in your organization. You can run this training job in any workspace you have access to without having worry about making the training code and environment available in that workspace. 

> [!WARNING]
> * Before running the pipeline job, confirm that the workspace in which you will run the job is in a Azure region that is supported by the registry in which you created the component.
> * Confirm that the workspace has a compute cluster with the name `cpu-cluster` or edit the `compute` field under `jobs.train_job.compute` with the name of your compute.

Run the pipeline job with the `az ml job create` command.

```azurecli
az ml job create --file single-job-pipeline.yml 
```

> [!TIP]
> If you have not configured the default workspace and resource group as explained in the prerequisites section, you will need to specify the `--workspace-name` and `--resource-group` parameters for the `az ml job create` to work.
