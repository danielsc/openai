   
   Then, create the deployment with the following command:
   
   ```azurecli
   DEPLOYMENT_NAME="classifier-xgboost-mlflow"
   az ml batch-deployment create -n $DEPLOYMENT_NAME -f endpoint.yml
   ```
   
   # [Python](#tab/sdk)
   
   To create a new deployment under the created endpoint, first define the deployment:
   
   ```python
   deployment = BatchDeployment(
       name="classifier-xgboost-mlflow",
       description="A heart condition classifier based on XGBoost",
       endpoint_name=endpoint.name,
       model=model,
       compute=compute_name,
       instance_count=2,
       max_concurrency_per_instance=2,
       mini_batch_size=2,
       output_action=BatchDeploymentOutputAction.APPEND_ROW,
       output_file_name="predictions.csv",
       retry_settings=BatchRetrySettings(max_retries=3, timeout=300),
       logging_level="info",
   )
   ```
   
   Then, create the deployment with the following command:
   
   ```python
   ml_client.batch_deployments.begin_create_or_update(deployment)
   ```
   
   > [!NOTE]
   > Batch deployments only support deploying MLflow models with a `pyfunc` flavor. To use a different flavor, see [Customizing MLflow models deployments with a scoring script](#customizing-mlflow-models-deployments-with-a-scoring-script)..

6. Although you can invoke a specific deployment inside of an endpoint, you will usually want to invoke the endpoint itself and let the endpoint decide which deployment to use. Such deployment is named the "default" deployment. This gives you the possibility of changing the default deployment and hence changing the model serving the deployment without changing the contract with the user invoking the endpoint. Use the following instruction to update the default deployment:

   # [Azure CLI](#tab/cli)
   
   ```azurecli
   az ml batch-endpoint update --name $ENDPOINT_NAME --set defaults.deployment_name=$DEPLOYMENT_NAME
   ```
   
   # [Python](#tab/sdk)
   
   ```python
   endpoint = ml_client.batch_endpoints.get(endpoint.name)
   endpoint.defaults.deployment_name = deployment.name
   ml_client.batch_endpoints.begin_create_or_update(endpoint)
   ```

7. At this point, our batch endpoint is ready to be used. 

## Testing out the deployment

For testing our endpoint, we are going to use a sample of unlabeled data located in this repository and that can be used with the model. Batch endpoints can only process data that is located in the cloud and that is accessible from the Azure Machine Learning workspace. In this example, we are going to upload it to an Azure Machine Learning data store. Particularly, we are going to create a data asset that can be used to invoke the endpoint for scoring. However, notice that batch endpoints accept data that can be placed in multiple type of locations.

1. Let's create the data asset first. This data asset consists of a folder with multiple CSV files that we want to process in parallel using batch endpoints. You can skip this step is your data is already registered as a data asset or you want to use a different input type.

   # [Azure CLI](#tab/cli)
   
   a. Create a data asset definition in `YAML`:
   
   __heart-dataset-unlabeled.yml__
   ```yaml
   $schema: https://azuremlschemas.azureedge.net/latest/data.schema.json
   name: heart-dataset-unlabeled
   description: An unlabeled dataset for heart classification.
   type: uri_folder
   path: heart-classifier-mlflow/data
   ```
   
   b. Create the data asset:
   
   ```azurecli
   az ml data create -f heart-dataset-unlabeled.yml
   ```
   
   # [Python](#tab/sdk)
   
   a. Create a data asset definition:
   
   ```python
   data_path = "heart-classifier-mlflow/data"
   dataset_name = "heart-dataset-unlabeled"

   heart_dataset_unlabeled = Data(
       path=data_path,
       type=AssetTypes.URI_FOLDER,
       description="An unlabeled dataset for heart classification",
       name=dataset_name,
   )
   ```
   
   b. Create the data asset:
   
   ```python
   ml_client.data.create_or_update(heart_dataset_unlabeled)
   ```
