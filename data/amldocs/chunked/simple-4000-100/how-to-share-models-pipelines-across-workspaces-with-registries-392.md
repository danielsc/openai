In AzureML studio, select the endpoint link in the job output to view the job. Here you can analyze training metrics, verify that the job is using the component and environment from registry, and review the trained model. Note down the `name` of the job from the output or find the same information from the job overview in AzureML studio. You'll need this information to download the trained model in the next section on creating models in registry.

:::image type="content" source="./media/how-to-share-models-pipelines-across-workspaces-with-registries/job-using-component-from-registy-metrics.png" lightbox="./media/how-to-share-models-pipelines-across-workspaces-with-registries/job-using-component-from-registy-metrics.png" alt-text="Screenshot of the pipeline in AzureML studio.":::

## Create a model in registry

You'll learn how to create models in a registry in this section. Review [manage models](./how-to-manage-models.md) to learn more about model management in AzureML. We'll look at two different ways to create a model in a registry. First is from local files. Second, is to copy a model registered in the workspace to a registry. 

In both the options, you'll create model with the [MLflow format](./how-to-manage-models-mlflow.md), which will help you to [deploy this model for inference without writing any inference code](./how-to-deploy-mlflow-models-online-endpoints.md). 

### Create a model in registry from local files

# [Azure CLI](#tab/cli)

Download the model, which is available as output of the `train_job` by replacing `<job-name>` with the name from the job from the previous section. The model along with MLflow metadata files should be available in the `./artifacts/model/`.

```azurecli
# fetch the name of the train_job by listing all child jobs of the pipeline job
train_job_name=$(az ml job list --parent-job-name <job-name> --query [0].name | sed 's/\"//g')
# download the default outputs of the train_job
az ml job download --name $train_job_name 
# review the model files
ls -l ./artifacts/model/
```

> [!TIP]
> If you have not configured the default workspace and resource group as explained in the prerequisites section, you will need to specify the `--workspace-name` and `--resource-group` parameters for the `az ml model create` to work.

> [!WARNING]
> The output of `az ml job list` is passed to `sed`. This works only on Linux shells. If you are on Windows, run `az ml job list --parent-job-name <job-name> --query [0].name ` and strip any quotes you see in the train job name.

If you're unable to download the model, you can find sample MLflow model trained by the training job in the previous section in `cli/jobs/pipelines-with-components/nyc_taxi_data_regression/artifacts/model/` folder.

Create the model in the registry:

```azurecli
# create model in registry
az ml model create --name nyc-taxi-model --version 1 --type mlflow_model --path ./artifacts/model/ --registry-name <registry-name>
```

> [!TIP]
> * Use a random number for the `version` parameter if you get an error that model name and version exists.
> * The same the CLI command `az ml model create` can be used to create models in a workspace or registry. Running the command with `--workspace-name` command creates the model in a workspace whereas running the command with `--registry-name` creates the model in the registry.

# [Python SDK](#tab/python)

Make sure you use the `pipeline_job` object from the previous section or fetch the pipeline job using `ml_client_workspace.jobs.get(name="<pipeline-job-name>")` method to get the list of child jobs in the pipeline. You'll then look for the job with `display_name` as `train_job` and download the trained model from `train_job` output. The downloaded model along with MLflow metadata files should be available in the `./artifacts/model/`.

```python
jobs=ml_client_workspace.jobs.list(parent_job_name=pipeline_job.name)
for job in jobs:
    if (job.display_name == "train_job"):
        print (job.name)
        ml_client_workspace.jobs.download(job.name)
```
