   > This example assumes you have an endpoint created with the name `imagenet-classifier-batch` and a compute cluster with name `cpu-cluster`. If you don't, please follow the steps in the doc [Use batch endpoints for batch scoring](how-to-use-batch-endpoint.md).

   # [Azure CLI](#tab/cli)
   
   To create a new deployment under the created endpoint, create a `YAML` configuration like the following:
   
   ```yaml
   $schema: https://azuremlschemas.azureedge.net/latest/batchDeployment.schema.json
   endpoint_name: imagenet-classifier-batch
   name: imagenet-classifier-resnetv2
   description: A ResNetV2 model architecture for performing ImageNet classification in batch
   model: azureml:imagenet-classifier@latest
   compute: azureml:cpu-cluster
   environment:
      image: mcr.microsoft.com/azureml/tensorflow-2.4-ubuntu18.04-py37-cpu-inference:latest
      conda_file: ./imagenet-classifier/environment/conda.yml
   code_configuration:
     code: ./imagenet-classifier/code/
     scoring_script: imagenet_scorer.py
   resources:
     instance_count: 2
   max_concurrency_per_instance: 1
   mini_batch_size: 5
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
   DEPLOYMENT_NAME="imagenet-classifier-resnetv2"
   az ml batch-deployment create -f deployment.yml
   ```
   
   # [Python](#tab/sdk)
   
   To create a new deployment with the indicated environment and scoring script use the following code:
   
   ```python
   deployment = BatchDeployment(
       name="imagenet-classifier-resnetv2",
       description="A ResNetV2 model architecture for performing ImageNet classification in batch",
       endpoint_name=endpoint.name,
       model=model,
       environment=environment,
       code_configuration=CodeConfiguration(
           code="./imagenet-classifier/code/",
           scoring_script="imagenet_scorer.py",
       ),
       compute=compute_name,
       instance_count=2,
       max_concurrency_per_instance=1,
       mini_batch_size=10,
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

1. Although you can invoke a specific deployment inside of an endpoint, you will usually want to invoke the endpoint itself, and let the endpoint decide which deployment to use. Such deployment is named the "default" deployment. This gives you the possibility of changing the default deployment - and hence changing the model serving the deployment - without changing the contract with the user invoking the endpoint. Use the following instruction to update the default deployment:

   # [Azure ML CLI](#tab/cli)
   
   ```bash
   az ml batch-endpoint update --name $ENDPOINT_NAME --set defaults.deployment_name=$DEPLOYMENT_NAME
   ```
   
   # [Azure ML SDK for Python](#tab/sdk)
   
   ```python
   endpoint.defaults.deployment_name = deployment.name
   ml_client.batch_endpoints.begin_create_or_update(endpoint)
   ```

1. At this point, our batch endpoint is ready to be used.  

## Testing out the deployment

For testing our endpoint, we are going to use a sample of 1000 images from the original ImageNet dataset. Batch endpoints can only process data that is located in the cloud and that is accessible from the Azure Machine Learning workspace. In this example, we are going to upload it to an Azure Machine Learning data store. Particularly, we are going to create a data asset that can be used to invoke the endpoint for scoring. However, notice that batch endpoints accept data that can be placed in multiple type of locations.

1. Let's download the associated sample data:
