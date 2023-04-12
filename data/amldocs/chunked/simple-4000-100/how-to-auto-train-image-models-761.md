[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=create_endpoint)]

### Configure online deployment

A deployment is a set of resources required for hosting the model that does the actual inferencing. We'll create a deployment for our endpoint using the `ManagedOnlineDeployment` class. You can use either GPU or CPU VM SKUs for your deployment cluster.


# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
name: od-fridge-items-mlflow-deploy
endpoint_name: od-fridge-items-endpoint
model: azureml:od-fridge-items-mlflow-model@latest
instance_type: Standard_DS3_v2
instance_count: 1
liveness_probe:
    failure_threshold: 30
    success_threshold: 1
    timeout: 2
    period: 10
    initial_delay: 2000
readiness_probe:
    failure_threshold: 10
    success_threshold: 1
    timeout: 10
    period: 10
    initial_delay: 2000 
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=deploy)]


### Create the deployment

Using the `MLClient` created earlier, we'll now create the deployment in the workspace. This command will start the deployment creation and return a confirmation response while the deployment creation continues.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```azurecli
az ml online-deployment create --file .\create_deployment.yml --workspace-name [YOUR_AZURE_WORKSPACE] --resource-group [YOUR_AZURE_RESOURCE_GROUP] --subscription [YOUR_AZURE_SUBSCRIPTION]
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=create_deploy)]

### update traffic:
By default the current deployment is set to receive 0% traffic. you can set the traffic percentage current deployment should receive. Sum of traffic percentages of all the deployments with one end point shouldn't exceed 100%.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```azurecli
az ml online-endpoint update --name 'od-fridge-items-endpoint' --traffic 'od-fridge-items-mlflow-deploy=100' --workspace-name [YOUR_AZURE_WORKSPACE] --resource-group [YOUR_AZURE_RESOURCE_GROUP] --subscription [YOUR_AZURE_SUBSCRIPTION]
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=update_traffic)]


Alternatively You can deploy the model from the [Azure Machine Learning studio UI](https://ml.azure.com/). 
Navigate to the model you wish to deploy in the **Models** tab of the automated ML job and select on **Deploy** and select **Deploy to real-time endpoint** .  

![Screenshot of how the Deployment page looks like after selecting the Deploy option.](./media/how-to-auto-train-image-models/deploy-end-point.png).

this is how your review page looks like. we can select instance type, instance count and set traffic percentage for the current deployment.

![Screenshot of how the top of review page looks like after selecting the options to deploy.](./media/how-to-auto-train-image-models/review-deploy-1.png).
![Screenshot of how the bottom of review page looks like after selecting the options to deploy.](./media/how-to-auto-train-image-models/review-deploy-2.png).

### Update inference settings

In the previous step, we downloaded a file `mlflow-model/artifacts/settings.json` from the best model. which can be used to update the inference settings before registering the model. Although it's recommended to use the same parameters as training for best performance.
