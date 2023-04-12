   

2. Batch Endpoint can only deploy registered models. In this case, we already have a local copy of the model in the repository, so we only need to publish the model to the registry in the workspace. You can skip this step if the model you are trying to deploy is already registered.
   
   # [Azure CLI](#tab/cli)
   
   ```azurecli
   MODEL_NAME='heart-classifier'
   az ml model create --name $MODEL_NAME --type "mlflow_model" --path "heart-classifier-mlflow/model"
   ```
   
   # [Python](#tab/sdk)
   
   ```python
   model_name = 'heart-classifier'
   model_local_path = "heart-classifier-mlflow/model"
   model = ml_client.models.create_or_update(
        Model(name=model_name, path=model_local_path, type=AssetTypes.MLFLOW_MODEL)
   )
   ```
   
3. Before moving any forward, we need to make sure the batch deployments we are about to create can run on some infrastructure (compute). Batch deployments can run on any Azure ML compute that already exists in the workspace. That means that multiple batch deployments can share the same compute infrastructure. In this example, we are going to work on an AzureML compute cluster called `cpu-cluster`. Let's verify the compute exists on the workspace or create it otherwise.
   
   # [Azure CLI](#tab/cli)
   
   Create a compute definition `YAML` like the following one:
   
   __cpu-cluster.yml__
   
   ```yaml
   $schema: https://azuremlschemas.azureedge.net/latest/amlCompute.schema.json 
   name: cluster-cpu
   type: amlcompute
   size: STANDARD_DS3_v2
   min_instances: 0
   max_instances: 2
   idle_time_before_scale_down: 120
   ```
   
   Create the compute using the following command:
   
   ```azurecli
   az ml compute create -f cpu-cluster.yml
   ```
   
   # [Python](#tab/sdk)
   
   To create a new compute cluster where to create the deployment, use the following script:
   
   ```python
   compute_name = "cpu-cluster"
   if not any(filter(lambda m : m.name == compute_name, ml_client.compute.list())):
       compute_cluster = AmlCompute(name=compute_name, description="amlcompute", min_instances=0, max_instances=2)
       ml_client.begin_create_or_update(compute_cluster)
   ```

4. Now it is time to create the batch endpoint and deployment. Let's start with the endpoint first. Endpoints only require a name and a description to be created:
   
   # [Azure CLI](#tab/cli)
   
   To create a new endpoint, create a `YAML` configuration like the following:
   
   ```yaml
   $schema: https://azuremlschemas.azureedge.net/latest/batchEndpoint.schema.json
   name: heart-classifier-batch
   description: A heart condition classifier for batch inference
   auth_mode: aad_token
   ```
   
   Then, create the endpoint with the following command:
   
   ```azurecli
   ENDPOINT_NAME='heart-classifier-batch'
   az ml batch-endpoint create -n $ENDPOINT_NAME -f endpoint.yml
   ```
   
   # [Python](#tab/sdk)
   
   To create a new endpoint, use the following script:
   
   ```python
   endpoint = BatchEndpoint(
      name="heart-classifier-batch", 
      description="A heart condition classifier for batch inference",
   )
   ```
   
   Then, create the endpoint with the following command:
   
   ```python
   ml_client.batch_endpoints.begin_create_or_update(endpoint)
   ```

5. Now, let create the deployment. MLflow models don't require you to indicate an environment or a scoring script when creating the deployments as it is created for you. However, you can specify them if you want to customize how the deployment does inference.

   # [Azure CLI](#tab/cli)
   
   To create a new deployment under the created endpoint, create a `YAML` configuration like the following:
   
   ```yaml
   $schema: https://azuremlschemas.azureedge.net/latest/batchDeployment.schema.json
   endpoint_name: heart-classifier-batch
   name: classifier-xgboost-mlflow
   description: A heart condition classifier based on XGBoost
   model: azureml:heart-classifier@latest
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
