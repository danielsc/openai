> [!IMPORTANT]
> If your subscription does not have enough quota for these services, a failure will occur.

> [!WARNING]
> __Don't delete the resource group__ that contains this Azure Cosmos DB instance, or any of the resources automatically created in this group. If you need to delete the resource group or Microsoft-managed services in it, you must delete the Azure Machine Learning workspace that uses it. The resource group resources are deleted when the associated workspace is deleted.

For more information on customer-managed keys with Azure Cosmos DB, see [Configure customer-managed keys for your Azure Cosmos DB account](../cosmos-db/how-to-setup-cmk.md).

### Azure Container Instance

> [!IMPORTANT]
> Deploying to Azure Container Instances is not available in SDK or CLI v2. Only through SDK & CLI v1.

When __deploying__ a trained model to an Azure Container instance (ACI), you can encrypt the deployed resource using a customer-managed key. For information on generating a key, see [Encrypt data with a customer-managed key](../container-instances/container-instances-encrypt-data.md#generate-a-new-key).

To use the key when deploying a model to Azure Container Instance, create a new deployment configuration using `AciWebservice.deploy_configuration()`. Provide the key information using the following parameters:

* `cmk_vault_base_url`: The URL of the key vault that contains the key.
* `cmk_key_name`: The name of the key.
* `cmk_key_version`: The version of the key.

For more information on creating and using a deployment configuration, see the following articles:

* [AciWebservice.deploy_configuration()](/python/api/azureml-core/azureml.core.webservice.aci.aciwebservice#deploy-configuration-cpu-cores-none--memory-gb-none--tags-none--properties-none--description-none--location-none--auth-enabled-none--ssl-enabled-none--enable-app-insights-none--ssl-cert-pem-file-none--ssl-key-pem-file-none--ssl-cname-none--dns-name-label-none--primary-key-none--secondary-key-none--collect-model-data-none--cmk-vault-base-url-none--cmk-key-name-none--cmk-key-version-none-) reference
* [Where and how to deploy](how-to-deploy-online-endpoints.md)
* [Deploy a model to Azure Container Instances (SDK/CLI v1)](v1/how-to-deploy-azure-container-instance.md)

    For more information on using a customer-managed key with ACI, see [Encrypt deployment data](../container-instances/container-instances-encrypt-data.md).

### Azure Kubernetes Service

You may encrypt a deployed Azure Kubernetes Service resource using customer-managed keys at any time. For more information, see [Bring your own keys with Azure Kubernetes Service](../aks/azure-disk-customer-managed-keys.md). 

This process allows you to encrypt both the Data and the OS Disk of the deployed virtual machines in the Kubernetes cluster.

> [!IMPORTANT]
> This process only works with AKS K8s version 1.17 or higher.

## Next steps

* [Customer-managed keys with Azure Machine Learning](concept-customer-managed-keys.md)
* [Create a workspace with Azure CLI](how-to-manage-workspace-cli.md#customer-managed-key-and-high-business-impact-workspace) |
* [Create and manage a workspace](how-to-manage-workspace.md#use-your-own-data-encryption-key) |
* [Create a workspace with a template](how-to-create-workspace-template.md#deploy-an-encrypted-workspace) |
* [Create, run, and delete Azure ML resources with REST](how-to-manage-rest.md#create-a-workspace-using-customer-managed-encryption-keys) |
