
### Microsoft hosts

The hosts in the following tables are owned by Microsoft, and provide services required for the proper functioning of your workspace. The tables list hosts for the Azure public, Azure Government, and Azure China 21Vianet regions.

> [!IMPORTANT]
> Azure Machine Learning uses Azure Storage Accounts in your subscription and in Microsoft-managed subscriptions. Where applicable, the following terms are used to differentiate between them in this section:
>
> * __Your storage__: The Azure Storage Account(s) in your subscription, which is used to store your data and artifacts such as models, training data, training logs, and Python scripts.>
> * __Microsoft storage__: The Azure Machine Learning compute instance and compute clusters rely on Azure Batch, and must access storage located in a Microsoft subscription. This storage is used only for the management of the compute instances. None of your data is stored here.

__General Azure hosts__

# [Azure public](#tab/public)

| __Required for__ | __Hosts__ | __Protocol__ | __Ports__ |
| ----- | ----- | ----- | ---- | 
| Azure Active Directory | `login.microsoftonline.com` | TCP | 80, 443 |
| Azure portal | `management.azure.com` | TCP | 443 |
| Azure Resource Manager | `management.azure.com` | TCP | 443 |

# [Azure Government](#tab/gov)

| __Required for__ | __Hosts__ | __Protocol__ | __Ports__ |
| ----- | ----- | ----- | ---- |
| Azure Active Directory | `login.microsoftonline.us` | TCP | 80, 443 |
| Azure portal | `management.azure.us` | TCP | 443 |
| Azure Resource Manager | `management.usgovcloudapi.net` | TCP | 443 |

# [Azure China 21Vianet](#tab/china)

| __Required for__ | __Hosts__ | __Protocol__ | __Ports__ |
| ----- | ----- | ----- | ----- |
| Azure Active Directory | `login.chinacloudapi.cn` | TCP | 80, 443 |
| Azure portal | `management.azure.cn` | TCP | 443 |
| Azure Resource Manager | `management.chinacloudapi.cn` | TCP | 443 |


__Azure Machine Learning hosts__

> [!IMPORTANT]
> In the following table, replace `<storage>` with the name of the default storage account for your Azure Machine Learning workspace. Replace `<region>` with the region of your workspace.

# [Azure public](#tab/public)

| __Required for__ | __Hosts__ | __Protocol__ | __Ports__ |
| ----- | ----- | ----- | ----- |
| Azure Machine Learning studio | `ml.azure.com` | TCP | 443 |
| API | `*.azureml.ms` | TCP | 443 |
| API | `*.azureml.net` | TCP | 443 |
| Model management | `*.modelmanagement.azureml.net` | TCP | 443 |
| Integrated notebook | `*.notebooks.azure.net` | TCP | 443 |
| Integrated notebook | `<storage>.file.core.windows.net` | TCP | 443, 445 |
| Integrated notebook | `<storage>.dfs.core.windows.net` | TCP | 443 |
| Integrated notebook | `<storage>.blob.core.windows.net` | TCP | 443 |
| Integrated notebook | `graph.microsoft.com` | TCP | 443 |
| Integrated notebook | `*.aznbcontent.net` | TCP | 443 |
| AutoML NLP, Vision | `automlresources-prod.azureedge.net` | TCP | 443 |
| AutoML NLP, Vision | `aka.ms` | TCP | 443 |

> [!NOTE]
> AutoML NLP, Vision are currently only supported in Azure public regions.

# [Azure Government](#tab/gov)

| __Required for__ | __Hosts__ | __Protocol__ | __Ports__ |
| ----- | ----- | ----- | ----- |
| Azure Machine Learning studio | `ml.azure.us` | TCP | 443 |
| API | `*.ml.azure.us` | TCP | 443 |
| Model management | `*.modelmanagement.azureml.us` | TCP | 443 |
| Integrated notebook | `*.notebooks.usgovcloudapi.net` | TCP | 443 |
| Integrated notebook | `<storage>.file.core.usgovcloudapi.net` | TCP | 443, 445 |
| Integrated notebook | `<storage>.dfs.core.usgovcloudapi.net` | TCP | 443 |
| Integrated notebook  | `<storage>.blob.core.usgovcloudapi.net` | TCP | 443 |
| Integrated notebook | `graph.microsoft.us` | TCP | 443 |
| Integrated notebook | `*.aznbcontent.net` | TCP | 443 |

# [Azure China 21Vianet](#tab/china)

| __Required for__ | __Hosts__ | __Protocol__ | __Ports__ |
| ----- | ----- | ----- | ----- |
| Azure Machine Learning studio | `studio.ml.azure.cn` | TCP | 443 |
