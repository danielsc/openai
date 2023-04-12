Invoking a batch endpoint triggers an asynchronous batch inference job. Compute resources are automatically provisioned when the job starts, and automatically de-allocated as the job completes. So you only pay for compute when you use it.

You can [override compute resource settings](batch-inference/how-to-use-batch-endpoint.md#overwrite-deployment-configuration-per-each-job) (like instance count) and advanced settings (like mini batch size, error threshold, and so on) for each individual batch inference job to speed up execution and reduce cost.

### Flexible data sources and storage

You can use the following options for input data when invoking a batch endpoint:

- Cloud data: Either a path on Azure Machine Learning registered datastore, a reference to Azure Machine Learning registered V2 data asset, or a public URI. For more information, see [Data in Azure Machine Learning](concept-data.md).
- Data stored locally: The data will be automatically uploaded to the Azure ML registered datastore and passed to the batch endpoint.

> [!NOTE]
> - If you're using existing V1 FileDatasets for batch endpoints, we recommend migrating them to V2 data assets. You can then refer to the V2 data assets directly when invoking batch endpoints. Currently, only data assets of type `uri_folder` or `uri_file` are supported. Batch endpoints created with GA CLIv2 (2.4.0 and newer) or GA REST API (2022-05-01 and newer) will not support V1 Datasets.
> - You can also extract the datastores' URI or path from V1 FileDatasets. For this, you'll use the `az ml dataset show` command with the `--query` parameter and use that information for invoke.
> - While batch endpoints created with earlier APIs will continue to support V1 FileDatasets, we'll be adding more support for V2 data assets in the latest API versions for better usability and flexibility. For more information on V2 data assets, see [Work with data using SDK v2](how-to-read-write-data-v2.md). For more information on the new V2 experience, see [What is v2](concept-v2.md).

For more information on supported input options, see [Accessing data from batch endpoints jobs](batch-inference/how-to-access-data-batch-endpoints-jobs.md).

Specify the storage output location to any datastore and path. By default, batch endpoints store their output to the workspace's default blob store, organized by the Job Name (a system-generated GUID).

### Security

- Authentication: Azure Active Directory Tokens
- SSL: enabled by default for endpoint invocation
- VNET support: Batch endpoints support ingress protection. A batch endpoint with ingress protection will accept scoring requests only from hosts inside a virtual network but not from the public internet. A batch endpoint that is created in a private-link enabled workspace will have ingress protection. To create a private-link enabled workspace, see [Create a secure workspace](tutorial-create-secure-workspace.md).

> [!NOTE]
> Creating batch endpoints in a private-link enabled workspace is only supported in the following versions.
> - CLI - version 2.15.1 or higher.
> - REST API - version 2022-05-01 or higher.
> - SDK V2 - version 0.1.0b3 or higher.

## Next steps

- [How to deploy online endpoints with the Azure CLI and Python SDK](how-to-deploy-online-endpoints.md)
- [How to deploy batch endpoints with the Azure CLI and Python SDK](batch-inference/how-to-use-batch-endpoint.md)
- [How to use online endpoints with the studio](how-to-use-managed-online-endpoint-studio.md)
- [Deploy models with REST](how-to-deploy-with-rest.md)
- [How to monitor managed online endpoints](how-to-monitor-online-endpoints.md)
- [How to view managed online endpoint costs](how-to-view-online-endpoints-costs.md)
- [Manage and increase quotas for resources with Azure Machine Learning](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints)
