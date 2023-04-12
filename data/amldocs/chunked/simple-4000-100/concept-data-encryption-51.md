Azure Database for MySQL is a relational database service in the Microsoft cloud based on the MySQL Community Edition database engine. The Azure Database for MySQL service uses the FIPS 140-2 validated cryptographic module for storage encryption of data at-rest. 

To encrypt data using customer managed keys, see [Azure Database for MySQL data encryption with a customer-managed key](../mysql/single-server/concepts-data-encryption-mysql.md) .


### Azure Cosmos DB

Azure Machine Learning stores metadata in an Azure Cosmos DB instance. This instance is associated with a Microsoft subscription managed by Azure Machine Learning. All the data stored in Azure Cosmos DB is encrypted at rest with Microsoft-managed keys.

When using your own (customer-managed) keys to encrypt the Azure Cosmos DB instance, a Microsoft managed Azure Cosmos DB instance is created in your subscription. This instance is created in a Microsoft-managed resource group, which is different than the resource group for your workspace. For more information, see [Customer-managed keys](concept-customer-managed-keys.md).

### Azure Container Registry

All container images in your registry (Azure Container Registry) are encrypted at rest. Azure automatically encrypts an image before storing it and decrypts it when Azure Machine Learning pulls the image.

To use customer-managed keys to encrypt your Azure Container Registry, you need to create your own ACR and attach it while provisioning the workspace. You can encrypt the default instance that gets created at the time of workspace provisioning.

> [!IMPORTANT]
> Azure Machine Learning requires the admin account be enabled on your Azure Container Registry. By default, this setting is disabled when you create a container registry. For information on enabling the admin account, see [Admin account](../container-registry/container-registry-authentication.md#admin-account).
>
> Once an Azure Container Registry has been created for a workspace, do not delete it. Doing so will break your Azure Machine Learning workspace.

For an example of creating a workspace using an existing Azure Container Registry, see the following articles:

* [Create a workspace for Azure Machine Learning with Azure CLI](how-to-manage-workspace-cli.md).
* [Create a workspace with Python SDK](how-to-manage-workspace.md?tabs=python#create-a-workspace).
* [Use an Azure Resource Manager template to create a workspace for Azure Machine Learning](how-to-create-workspace-template.md)

### Azure Container Instance

> [!IMPORTANT]
> Deployments to ACI rely on the Azure Machine Learning Python SDK and CLI v1.

You may encrypt a deployed Azure Container Instance (ACI) resource using customer-managed keys. The customer-managed key used for ACI can be stored in the Azure Key Vault for your workspace. For information on generating a key, see [Encrypt data with a customer-managed key](../container-instances/container-instances-encrypt-data.md#generate-a-new-key).

[!INCLUDE [sdk v1](../../includes/machine-learning-sdk-v1.md)]

To use the key when deploying a model to Azure Container Instance, create a new deployment configuration using `AciWebservice.deploy_configuration()`. Provide the key information using the following parameters:

* `cmk_vault_base_url`: The URL of the key vault that contains the key.
* `cmk_key_name`: The name of the key.
* `cmk_key_version`: The version of the key.

For more information on creating and using a deployment configuration, see the following articles:

* [AciWebservice.deploy_configuration()](/python/api/azureml-core/azureml.core.webservice.aci.aciwebservice#deploy-configuration-cpu-cores-none--memory-gb-none--tags-none--properties-none--description-none--location-none--auth-enabled-none--ssl-enabled-none--enable-app-insights-none--ssl-cert-pem-file-none--ssl-key-pem-file-none--ssl-cname-none--dns-name-label-none--primary-key-none--secondary-key-none--collect-model-data-none--cmk-vault-base-url-none--cmk-key-name-none--cmk-key-version-none-) reference
