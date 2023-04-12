   To create a new compute cluster with low priority VMs where to create the deployment, use the following script:
   
   ```python
   compute_name = "low-pri-cluster"
   compute_cluster = AmlCompute(
      name=compute_name, 
      description="Low priority compute cluster", 
      min_instances=0, 
      max_instances=2,
      tier='LowPriority'
   )
    
   ml_client.begin_create_or_update(compute_cluster)
   ```
   
   
Once you have the new compute created, you can create or update your deployment to use the new cluster:

   # [Azure CLI](#tab/cli)
   
   To create or update a deployment under the new compute cluster, create a `YAML` configuration like the following:
   
   ```yaml
   $schema: https://azuremlschemas.azureedge.net/latest/batchDeployment.schema.json
   endpoint_name: heart-classifier-batch
   name: classifier-xgboost
   description: A heart condition classifier based on XGBoost
   model: azureml:heart-classifier@latest
   compute: azureml:low-pri-cluster
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
   az ml batch-endpoint create -f endpoint.yml
   ```
   
   # [Python](#tab/sdk)
   
   To create or update a deployment under the new compute cluster, use the following script:
   
   ```python
   deployment = BatchDeployment(
       name="classifier-xgboost",
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
   
   ml_client.batch_deployments.begin_create_or_update(deployment)
   ```
   
## View and monitor node deallocation

New metrics are available in the [Azure portal](https://portal.azure.com) for low priority VMs to monitor low priority VMs. These metrics are:

- Preempted nodes
- Preempted cores

To view these metrics in the Azure portal

1. Navigate to your Azure Machine Learning workspace in the [Azure portal](https://portal.azure.com).
2. Select **Metrics** from the **Monitoring** section.
3. Select the metrics you desire from the **Metric** list.

:::image type="content" source="./media/how-to-use-low-priority-batch/metrics.png" alt-text="Screenshot of the metrics section in the resource monitoring blade showing the relevant metrics for low priority VMs.":::

## Limitations

- Once a deployment is associated with a low priority VMs' cluster, all the jobs produced by such deployment will use low priority VMs. Per-job configuration is not possible.
- Rescheduling is done at the mini-batch level, regardless of the progress. No checkpointing capability is provided.

> [!WARNING]
> In the cases where the entire cluster is preempted (or running on a single-node cluster), the job will be cancelled as there is no capacity available for it to run. Resubmitting will be required in this case. 


