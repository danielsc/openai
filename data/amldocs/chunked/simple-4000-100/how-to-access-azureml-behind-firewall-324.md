| ----- | ----- | ----- | ----- |
| Azure Machine Learning studio | `studio.ml.azure.cn` | TCP | 443 |
| API | `*.ml.azure.cn` | TCP | 443 |
| API | `*.azureml.cn` | TCP | 443 |
| Model management | `*.modelmanagement.ml.azure.cn` | TCP | 443 |
| Integrated notebook | `*.notebooks.chinacloudapi.cn` | TCP | 443 |
| Integrated notebook | `<storage>.file.core.chinacloudapi.cn` | TCP | 443, 445 |
| Integrated notebook | `<storage>.dfs.core.chinacloudapi.cn` | TCP | 443 |
| Integrated notebook | `<storage>.blob.core.chinacloudapi.cn` | TCP | 443 |
| Integrated notebook | `graph.chinacloudapi.cn` | TCP | 443 |
| Integrated notebook | `*.aznbcontent.net` | TCP | 443 |


__Azure Machine Learning compute instance and compute cluster hosts__

> [!TIP]
> * The host for __Azure Key Vault__ is only needed if your workspace was created with the [hbi_workspace](/python/api/azure-ai-ml/azure.ai.ml.entities.workspace) flag enabled.
> * Ports 8787 and 18881 for __compute instance__ are only needed when your Azure Machine workspace has a private endpoint.
> * In the following table, replace `<storage>` with the name of the default storage account for your Azure Machine Learning workspace.
> * In the following table, replace `<region>` with the Azure region that contains your Azure Machine Learning workspace.
> * Websocket communication must be allowed to the compute instance. If you block websocket traffic, Jupyter notebooks won't work correctly.

# [Azure public](#tab/public)

| __Required for__ | __Hosts__ | __Protocol__ | __Ports__ |
| ----- | ----- | ----- | ----- |
| Compute cluster/instance | `graph.windows.net` | TCP | 443 |
| Compute instance | `*.instances.azureml.net` | TCP | 443 |
| Compute instance | `*.instances.azureml.ms` | TCP | 443, 8787, 18881 |
| Compute instance | `<region>.tundra.azureml.ms` | UDP | 5831 |
| Compute instance | `*.batch.azure.com` | ANY | 443 |
| Compute instance | `*.service.batch.com` | ANY | 443 | 
| Microsoft storage access | `*.blob.core.windows.net` | TCP | 443 |
| Microsoft storage access | `*.table.core.windows.net` | TCP | 443 |
| Microsoft storage access | `*.queue.core.windows.net` | TCP | 443 |
| Your storage account | `<storage>.file.core.windows.net` | TCP | 443, 445 |
| Your storage account | `<storage>.blob.core.windows.net` | TCP | 443 |
| Azure Key Vault | \*.vault.azure.net | TCP | 443 |

# [Azure Government](#tab/gov)

| __Required for__ | __Hosts__ | __Protocol__ | __Ports__ |
| ----- | ----- | ----- | ----- |
| Compute cluster/instance | `graph.windows.net` | TCP | 443 |
| Compute instance | `*.instances.azureml.us` | TCP | 443 |
| Compute instance | `*.instances.azureml.ms` | TCP | 443, 8787, 18881 |
| Compute instance | `<region>.tundra.azureml.us` | UDP | 5831 |
| Microsoft storage access | `*.blob.core.usgovcloudapi.net` | TCP | 443 |
| Microsoft storage access | `*.table.core.usgovcloudapi.net` | TCP | 443 |
| Microsoft storage access | `*.queue.core.usgovcloudapi.net` | TCP | 443 |
| Your storage account | `<storage>.file.core.usgovcloudapi.net` | TCP | 443, 445 |
| Your storage account | `<storage>.blob.core.usgovcloudapi.net` | TCP | 443 |
| Azure Key Vault | `*.vault.usgovcloudapi.net` | TCP | 443 |

# [Azure China 21Vianet](#tab/china)

| __Required for__ | __Hosts__ | __Protocol__ | __Ports__ |
| ----- | ----- | ----- | ----- |
| Compute cluster/instance | `graph.chinacloudapi.cn` | TCP | 443 |
| Compute instance |  `*.instances.azureml.cn` | TCP | 443 |
| Compute instance | `*.instances.azureml.ms` | TCP | 443, 8787, 18881 |
| Compute instance | `<region>.tundra.azureml.cn` | UDP | 5831 |
| Microsoft storage access | `*.blob.core.chinacloudapi.cn` | TCP | 443 |
| Microsoft storage access | `*.table.core.chinacloudapi.cn` | TCP | 443 |
| Microsoft storage access | `*.queue.core.chinacloudapi.cn` | TCP | 443 |
| Your storage account | `<storage>.file.core.chinacloudapi.cn` | TCP | 443, 445 |
| Your storage account | `<storage>.blob.core.chinacloudapi.cn` | TCP | 443 |
| Azure Key Vault | `*.vault.azure.cn` | TCP | 443 |
