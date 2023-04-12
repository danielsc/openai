You can also use `az ml model list --registry-name <registry-name>` to list all models in the registry or browse all components in the AzureML Studio UI. Make sure you navigate to the global UI and look for the Registries hub.

# [Python SDK](#tab/python)

Make sure you use the `pipeline_job` object from the previous section or fetch the pipeline job using `ml_client_workspace.jobs.get(name="<pipeline-job-name>")` method to get the list of child jobs in the pipeline. You'll then look for the job with `display_name` as `train_job` and use the `name` of the `train_job` to construct the path pointing to the model output, which looks like this: `azureml://jobs/<job_name>/outputs/artifacts/paths/model`.

```python
jobs=ml_client_workspace.jobs.list(parent_job_name=pipeline_job.name)
for job in jobs:
    if (job.display_name == "train_job"):
        print (job.name)
        model_path_from_job="azureml://jobs/{job_name}/outputs/artifacts/paths/model".format(job_name=job.name)

print(model_path_from_job)
```

Register the model from the output of the training job into the workspace using the path constructed above.

```python
mlflow_model = Model(
    path=model_path_from_job,
    type=AssetTypes.MLFLOW_MODEL,
    name="nyc-taxi-model",
    version=version_timestamp,
    description="MLflow model created from job output",
)
ml_client_workspace.model.create_or_update(mlflow_model)
```

> [!TIP]
> Notice that you are using MLClient object `ml_client_workspace` since you are creating the model in the workspace. 

Note down the model name and version. You can validate if the model is registered in the workspace by browsing it in the Studio UI or fetching it using `ml_client_workspace.model.get()` method.

Next, you'll now copy the model from the workspace to the registry. Construct the path to the model with the workspace using the `azureml://subscriptions/<subscription-id-of-workspace>/resourceGroups/<resource-group-of-workspace>/workspaces/<workspace-name>/models/<model-name>/versions/<model-version>` syntax.


```python
# fetch the model from workspace
model_in_workspace = ml_client_workspace.models.get(name="nyc-taxi-model", version=version)
print(model_in_workspace )
# change the format such that the registry understands the model (when you print the model_ready_to_copy object, notice the asset id 
model_ready_to_copy = ml_client_workspace.models._prepare_to_copy(model_in_workspace)
print(model_ready_to_copy)
# copy the model from registry to workspace
ml_client_registry.models.create_or_update(model_ready_to_copy)
```

> [!TIP]
> Make sure to use the right model name and version if you changed it in the `ml_client_workspace.model.create_or_update()` method used to create the model in workspace. 

Note down the `name` and `version` of the model from the output and use them with `ml_client_workspace.model.get()` commands as follows. You'll need the `name` and `version` in the next section when you deploy the model to an online endpoint for inference. 

```python 
mlflow_model_from_registry = ml_client_registry.models.get(name="nyc-taxi-model", version=str(1))
print(mlflow_model_from_registry)
```
You can also use `ml_client_registry.models.list()` to list all models in the registry or browse all components in the AzureML Studio UI. Make sure you navigate to the global UI and look for the Registries hub.


The following screenshot shows a model in a registry in AzureML studio. If you created a model from the job output and then copied the model from the workspace to registry, you'll see that the model has a link to the job that trained the model. You can use that link to navigate to the training job to review the code, environment and data used to train the model.

:::image type="content" source="./media/how-to-share-models-pipelines-across-workspaces-with-registries/model-in-registry.png" alt-text="Screenshot of the models in the registry.":::

## Deploy model from registry to online endpoint in workspace

In the last section, you'll deploy a model from registry to an online endpoint in a workspace. You can choose to deploy any workspace you have access to in your organization, provided the location of the workspace is one of the locations supported by the registry. This capability is helpful if you trained a model in a `dev` workspace and now need to deploy the model to `test` or `prod` workspace, while preserving the lineage information around the code, environment and data used to train the model.
