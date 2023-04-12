1. Let's create an environment where the scoring script can be executed. Since our model is MLflow, the conda requirements are also specified in the model package (for more details about MLflow models and the files included on it see [The MLmodel format](concept-mlflow-models.md#the-mlmodel-format)). We are going then to build the environment using the conda dependencies from the file. However, __we need also to include__ the package `azureml-core` which is required for Batch Deployments.

   > [!TIP]
   > If your model is already registered in the model registry, you can download/copy the `conda.yml` file associated with your model by going to [Azure ML studio](https://ml.azure.com) > Models > Select your model from the list > Artifacts. Open the root folder in the navigation and select the `conda.yml` file listed. Click on Download or copy its content. 
   
   > [!IMPORTANT]
   > This example uses a conda environment specified at `/heart-classifier-mlflow/environment/conda.yaml`. This file was created by combining the original MLflow conda dependencies file and adding the package `azureml-core`. __You can't use the `conda.yml` file from the model directly__.

   # [Azure CLI](#tab/cli)
   
   No extra step is required for the Azure ML CLI. The environment definition will be included in the deployment file.
   
   # [Python](#tab/sdk)
   
   Let's get a reference to the environment:
   
   ```python
   environment = Environment(
       conda_file="./heart-classifier-mlflow/environment/conda.yaml",
       image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:latest",
   )
   ```
   
1. Let's create the deployment now:

   # [Azure CLI](#tab/cli)
   
   To create a new deployment under the created endpoint, create a `YAML` configuration like the following:
   
   ```yaml
   $schema: https://azuremlschemas.azureedge.net/latest/batchDeployment.schema.json
   endpoint_name: heart-classifier-batch
   name: classifier-xgboost-custom
   description: A heart condition classifier based on XGBoost
   model: azureml:heart-classifier@latest
   environment:
      image: mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:latest
      conda_file: ./heart-classifier-mlflow/environment/conda.yaml
   code_configuration:
     code: ./heart-classifier-custom/code/
     scoring_script: batch_driver.py
   compute: azureml:cpu-cluster
   resources:
     instance_count: 2
   max_concurrency_per_instance: 2
   mini_batch_size: 2
   output_action: append_row
   output_file_name: predictions.csv
   retry_settings:
     max_retries: 3
     timeout: 300
   error_threshold: -1
   logging_level: info
   ```
   
   Then, create the deployment with the following command:
   
   ```azurecli
   az ml batch-deployment create -f deployment.yml
   ```
   
   # [Python](#tab/sdk)
   
   To create a new deployment under the created endpoint, use the following script:
   
   ```python
   deployment = BatchDeployment(
       name="classifier-xgboost-custom",
       description="A heart condition classifier based on XGBoost",
       endpoint_name=endpoint.name,
       model=model,
       environment=environment,
       code_configuration=CodeConfiguration(
           code="./heart-classifier-mlflow/code/",
           scoring_script="batch_driver.py",
       ),
       compute=compute_name,
       instance_count=2,
       max_concurrency_per_instance=2,
       mini_batch_size=2,
       output_action=BatchDeploymentOutputAction.APPEND_ROW,
       output_file_name="predictions.csv",
       retry_settings=BatchRetrySettings(max_retries=3, timeout=300),
       logging_level="info",
   )
   ml_client.batch_deployments.begin_create_or_update(deployment)
   ```
   
1. At this point, our batch endpoint is ready to be used. 

## Next steps

* [Customize outputs in batch deployments](how-to-deploy-model-custom-output.md)
