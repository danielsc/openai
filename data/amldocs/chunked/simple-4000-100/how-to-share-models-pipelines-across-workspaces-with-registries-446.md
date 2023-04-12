If you're unable to download the model, you can find sample MLflow model trained by the training job in the previous section in `sdk/resources/registry/model` folder.

Create the model in the registry.

```python
mlflow_model = Model(
    path="./artifacts/model/",
    type=AssetTypes.MLFLOW_MODEL,
    name="nyc-taxi-model",
    version=str(1), # use str(int(time.time())) if you want a random model number
    description="MLflow model created from local path",
)
ml_client_registry.model.create_or_update(mlflow_model)
```


### Copy a model from workspace to registry 

In this workflow, you'll first create the model in the workspace and then copy it to the registry. This workflow is useful when you want to test the model in the workspace before sharing it. For example, deploy it to endpoints, try out inference with some test data and then copy the model to a registry if everything looks good. This workflow may also be useful when you're developing a series of models using different techniques, frameworks or parameters and want to promote just one of them to the registry as a production candidate. 

# [Azure CLI](#tab/cli)

Make sure you have the name of the pipeline job from the previous section and replace that in the command to fetch the training job name below. You'll then register the model from the output of the training job into the workspace. Note how the `--path` parameter refers to the output `train_job` output with the `azureml://jobs/$train_job_name/outputs/artifacts/paths/model` syntax. 

```azurecli
# fetch the name of the train_job by listing all child jobs of the pipeline job
train_job_name=$(az ml job list --parent-job-name <job-name> --workspace-name <workspace-name> --resource-group <workspace-resource-group> --query [0].name | sed 's/\"//g')
# create model in workspace
az ml model create --name nyc-taxi-model --version 1 --type mlflow_model --path azureml://jobs/$train_job_name/outputs/artifacts/paths/model 
```

> [!TIP]
> * Use a random number for the `version` parameter if you get an error that model name and version exists.`
> * If you have not configured the default workspace and resource group as explained in the prerequisites section, you will need to specify the `--workspace-name` and `--resource-group` parameters for the `az ml model create` to work.

Note down the model name and version. You can validate if the model is registered in the workspace by browsing it in the Studio UI or using `az ml model show --name nyc-taxi-model --version $model_version` command.  

Next, you'll now copy the model from the workspace to the registry. Note now the `--path` parameter is referring to the model with the workspace with the `azureml://subscriptions/<subscription-id-of-workspace>/resourceGroups/<resource-group-of-workspace>/workspaces/<workspace-name>/models/<model-name>/versions/<model-version>` syntax.


```azurecli
# copy model registered in workspace to registry
az ml model create --registry-name <registry-name> --path azureml://subscriptions/<subscription-id-of-workspace>/resourceGroups/<resource-group-of-workspace>/workspaces/<workspace-name>/models/nyc-taxi-model/versions/1
```

> [!TIP]
> * Make sure to use the right model name and version if you changed it in the `az ml model create` command.
> * The above command creates the model in the registry with the same name and version. You can provide a different name or version with the `--name` or `--version` parameters. 
Note down the `name` and `version` of the model from the output of the `az ml model create` command and use them with `az ml model show` commands as follows. You'll need the `name` and `version` in the next section when you deploy the model to an online endpoint for inference. 

```azurecli 
az ml model show --name <model_name> --version <model_version> --registry-name <registry-name>
```

You can also use `az ml model list --registry-name <registry-name>` to list all models in the registry or browse all components in the AzureML Studio UI. Make sure you navigate to the global UI and look for the Registries hub.
