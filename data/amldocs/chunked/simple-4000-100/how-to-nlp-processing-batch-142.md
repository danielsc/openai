   > This example assumes you have an endpoint created with the name `text-summarization-batch` and a compute cluster with name `cpu-cluster`. If you don't, please follow the steps in the doc [Use batch endpoints for batch scoring](how-to-use-batch-endpoint.md).

   # [Azure CLI](#tab/cli)
   
   To create a new deployment under the created endpoint, create a `YAML` configuration like the following:
   
   ```yaml
   $schema: https://azuremlschemas.azureedge.net/latest/batchDeployment.schema.json
   endpoint_name: text-summarization-batch
   name: text-summarization-hfbart
   description: A text summarization deployment implemented with HuggingFace and BART architecture
   model: azureml:bart-text-summarization@latest
   compute: azureml:cpu-cluster
   environment:
      image: mcr.microsoft.com/azureml/tensorflow-2.4-ubuntu18.04-py37-cpu-inference:latest
      conda_file: ./bart-text-summarization/environment/conda.yml
   code_configuration:
     code: ./bart-text-summarization/code/
     scoring_script: transformer_scorer.py
   resources:
     instance_count: 2
   max_concurrency_per_instance: 1
   mini_batch_size: 1
   output_action: append_row
   output_file_name: predictions.csv
   retry_settings:
     max_retries: 3
     timeout: 3000
   error_threshold: -1
   logging_level: info
   ```
  
   Then, create the deployment with the following command:
   
   ```azurecli
   DEPLOYMENT_NAME="text-summarization-hfbart"
   az ml batch-deployment create -f endpoint.yml
   ```
   
   # [Python](#tab/sdk)
   
   To create a new deployment with the indicated environment and scoring script use the following code:
   
   ```python
   deployment = BatchDeployment(
       name="text-summarization-hfbart",
       description="A text summarization deployment implemented with HuggingFace and BART architecture",
       endpoint_name=endpoint.name,
       model=model,
       environment=environment,
       code_configuration=CodeConfiguration(
           code="./bart-text-summarization/code/",
           scoring_script="imagenet_scorer.py",
       ),
       compute=compute_name,
       instance_count=2,
       max_concurrency_per_instance=1,
       mini_batch_size=1,
       output_action=BatchDeploymentOutputAction.APPEND_ROW,
       output_file_name="predictions.csv",
       retry_settings=BatchRetrySettings(max_retries=3, timeout=3000),
       logging_level="info",
   )
   ```
   
   Then, create the deployment with the following command:
   
   ```python
   ml_client.batch_deployments.begin_create_or_update(deployment)
   ```
   
   > [!IMPORTANT]
   > You will notice in this deployment a high value in `timeout` in the parameter `retry_settings`. The reason for it is due to the nature of the model we are running. This is a very expensive model and inference on a single row may take up to 60 seconds. The `timeout` parameters controls how much time the Batch Deployment should wait for the scoring script to finish processing each mini-batch. Since our model runs predictions row by row, processing a long file may take time. Also notice that the number of files per batch is set to 1 (`mini_batch_size=1`). This is again related to the nature of the work we are doing. Processing one file at a time per batch is expensive enough to justify it. You will notice this being a pattern in NLP processing.

3. Although you can invoke a specific deployment inside of an endpoint, you will usually want to invoke the endpoint itself and let the endpoint decide which deployment to use. Such deployment is named the "default" deployment. This gives you the possibility of changing the default deployment and hence changing the model serving the deployment without changing the contract with the user invoking the endpoint. Use the following instruction to update the default deployment:

   # [Azure CLI](#tab/cli)
   
   ```azurecli
   az ml batch-endpoint update --name $ENDPOINT_NAME --set defaults.deployment_name=$DEPLOYMENT_NAME
   ```
   
   # [Python](#tab/sdk)
