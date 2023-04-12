In the last section, you'll deploy a model from registry to an online endpoint in a workspace. You can choose to deploy any workspace you have access to in your organization, provided the location of the workspace is one of the locations supported by the registry. This capability is helpful if you trained a model in a `dev` workspace and now need to deploy the model to `test` or `prod` workspace, while preserving the lineage information around the code, environment and data used to train the model.

Online endpoints let you deploy models and submit inference requests through the REST APIs. For more information, see [How to deploy and score a machine learning model by using an online endpoint](how-to-deploy-online-endpoints.md).

# [Azure CLI](#tab/cli)

Create an online endpoint. 

```azurecli
az ml online-endpoint create --name reg-ep-1234
```

Update the `model:` line `deploy.yml` available in the `cli/jobs/pipelines-with-components/nyc_taxi_data_regression` folder to refer the model name and version from the pervious step. Create an online deployment to the online endpoint. The `deploy.yml` is shown below for reference.

```YAML
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: demo
endpoint_name: reg-ep-1234
model: azureml://registries/<registry-name>/models/nyc-taxi-model/versions/1
instance_type: Standard_DS2_v2
instance_count: 1
```
Create the online deployment. The deployment takes several minutes to complete. 

```azurecli
az ml online-deployment create --file deploy.yml --all-traffic
```

Fetch the scoring URI and submit a sample scoring request. Sample data for the scoring request is available in the `scoring-data.json` in the `cli/jobs/pipelines-with-components/nyc_taxi_data_regression` folder. 

```azurecli
ENDPOINT_KEY=$(az ml online-endpoint get-credentials -n reg-ep-1234 -o tsv --query primaryKey)
SCORING_URI=$(az ml online-endpoint show -n $ep_name -o tsv --query scoring_uri)
curl --request POST "$SCORING_URI" --header "Authorization: Bearer $ENDPOINT_KEY" --header 'Content-Type: application/json' --data @./scoring-data.json
```

> [!TIP]
> * `curl` command works only on Linux.
> * If you have not configured the default workspace and resource group as explained in the prerequisites section, you will need to specify the `--workspace-name` and `--resource-group` parameters for the `az ml online-endpoint` and `az ml online-deployment` commands to work.

# [Python SDK](#tab/python)

Create an online endpoint. 

```python
online_endpoint_name = "endpoint-" + datetime.datetime.now().strftime("%m%d%H%M%f")
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="this is a sample online endpoint for mlflow model",
    auth_mode="key"
)
ml_client_workspace.begin_create_or_update(endpoint)
```

Make sure you have the `mlflow_model_from_registry` model object from the previous section or fetch the model from the registry using `ml_client_registry.models.get()` method. Pass it to the deployment configuration object and create the online deployment. The deployment takes several minutes to complete. Set all traffic to be routed to the new deployment. 

```python
demo_deployment = ManagedOnlineDeployment(
    name="demo",
    endpoint_name=online_endpoint_name,
    model=mlflow_model_from_registry,
    instance_type="Standard_F4s_v2",
    instance_count=1
)
ml_client_workspace.online_deployments.begin_create_or_update(demo_deployment)

endpoint.traffic = {"demo": 100}
ml_client_workspace.begin_create_or_update(endpoint)
```

Submit a sample scoring request using the sample data file `scoring-data.json`. This file is available in the `cli/jobs/pipelines-with-components/nyc_taxi_data_regression` folder.

```azurecli
# test the  deployment with some sample data
ml_client_workspace.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="demo",
    request_file=parent_dir + "/scoring-data.json"
)
```


## Clean up resources

If you aren't going use the deployment, you should delete it to reduce costs. The following example deletes the endpoint and all the underlying deployments:
