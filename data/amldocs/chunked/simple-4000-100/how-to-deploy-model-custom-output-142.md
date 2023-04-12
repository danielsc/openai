   > This example assumes you have an endpoint created with the name `heart-classifier-batch` and a compute cluster with name `cpu-cluster`. If you don't, please follow the steps in the doc [Use batch endpoints for batch scoring](how-to-use-batch-endpoint.md).

   # [Azure CLI](#tab/cli)
   
   To create a new deployment under the created endpoint, create a `YAML` configuration like the following:
   
   ```yaml
   $schema: https://azuremlschemas.azureedge.net/latest/batchDeployment.schema.json
   endpoint_name: heart-classifier-batch
   name: classifier-xgboost-parquet
   description: A heart condition classifier based on XGBoost
   model: azureml:heart-classifier@latest
   environment:
      image: mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:latest
      conda_file: ./heart-classifier-mlflow/environment/conda.yaml
   code_configuration:
     code: ./heart-classifier-custom/code/
     scoring_script: batch_driver_parquet.py
   compute: azureml:cpu-cluster
   resources:
     instance_count: 2
   max_concurrency_per_instance: 2
   mini_batch_size: 2
   output_action: summary_only
   retry_settings:
     max_retries: 3
     timeout: 300
   error_threshold: -1
   logging_level: info
   ```
   
   Then, create the deployment with the following command:
   
   ```azurecli
   DEPLOYMENT_NAME="classifier-xgboost-parquet"
   az ml batch-deployment create -f endpoint.yml
   ```
   
   # [Python](#tab/sdk)
   
   To create a new deployment under the created endpoint, use the following script:
   
   ```python
   deployment = BatchDeployment(
       name="classifier-xgboost-parquet",
       description="A heart condition classifier based on XGBoost",
       endpoint_name=endpoint.name,
       model=model,
       environment=environment,
       code_configuration=CodeConfiguration(
           code="./heart-classifier-mlflow/code/",
           scoring_script="batch_driver_parquet.py",
       ),
       compute=compute_name,
       instance_count=2,
       max_concurrency_per_instance=2,
       mini_batch_size=2,
       output_action=BatchDeploymentOutputAction.SUMMARY_ONLY,
       retry_settings=BatchRetrySettings(max_retries=3, timeout=300),
       logging_level="info",
   )
   ```
   
   Then, create the deployment with the following command:
   
   ```python
   ml_client.batch_deployments.begin_create_or_update(deployment)
   ```
   
   > [!IMPORTANT]
   > Notice that now `output_action` is set to `SUMMARY_ONLY`.

3. At this point, our batch endpoint is ready to be used. 

## Testing out the deployment

For testing our endpoint, we are going to use a sample of unlabeled data located in this repository and that can be used with the model. Batch endpoints can only process data that is located in the cloud and that is accessible from the Azure Machine Learning workspace. In this example, we are going to upload it to an Azure Machine Learning data store. Particularly, we are going to create a data asset that can be used to invoke the endpoint for scoring. However, notice that batch endpoints accept data that can be placed in multiple type of locations.

1. Let's create the data asset first. This data asset consists of a folder with multiple CSV files that we want to process in parallel using batch endpoints. You can skip this step is your data is already registered as a data asset or you want to use a different input type.

   # [Azure CLI](#tab/cli)
   
   Create a data asset definition in `YAML`:
   
   __heart-dataset-unlabeled.yml__
   
   ```yaml
   $schema: https://azuremlschemas.azureedge.net/latest/data.schema.json
   name: heart-dataset-unlabeled
   description: An unlabeled dataset for heart classification.
   type: uri_folder
   path: heart-dataset
   ```
   
   Then, create the data asset:
   
   ```azurecli
   az ml data create -f heart-dataset-unlabeled.yml
   ```
   
   # [Python](#tab/sdk)
   
   ```python
   data_path = "resources/heart-dataset/"
   dataset_name = "heart-dataset-unlabeled"

   heart_dataset_unlabeled = Data(
       path=data_path,
       type=AssetTypes.URI_FOLDER,
       description="An unlabeled dataset for heart classification",
       name=dataset_name,
   )
   ```
