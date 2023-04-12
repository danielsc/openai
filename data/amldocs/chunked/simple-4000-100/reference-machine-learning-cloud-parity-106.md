| Control access to ACR images used by ML Service (Azure provided/maintained versus custom)  |PARTIAL|	PARTIAL	|  |
| **General Machine Learning Service Usage** |  | | |
| Ability to have a development environment to build a model, train that model, host it as an endpoint, and consume it via a webapp     | YES | YES |  |
| Ability to pull data from ADLS (Data Lake Storage)                                 |YES | YES |  |
| Ability to pull data from Azure Blob Storage                                       |YES | YES |  |



### Other Azure Government limitations

* For Azure Machine Learning compute instances, the ability to refresh a token lasting more than 24 hours is not available in Azure Government.
* Model Profiling does not support 4 CPUs in the US-Arizona region.   
* Sample notebooks may not work in Azure Government if it needs access to public data.
* IP addresses: The CLI command used in the [required public internet access](how-to-secure-training-vnet.md#required-public-internet-access-to-train-models) instructions does not return IP ranges. Use the [Azure IP ranges and service tags for Azure Government](https://www.microsoft.com/download/details.aspx?id=57063) instead.
* For scheduled pipelines, we also provide a blob-based trigger mechanism. This mechanism is not supported for CMK workspaces. For enabling a blob-based trigger for CMK workspaces, you have to do extra setup. For more information, see [Trigger a run of a machine learning pipeline from a Logic App (SDK/CLI v1)](v1/how-to-trigger-published-pipeline.md).
* Firewalls: When using an Azure Government region, add the following hosts to your firewall setting:

    * For Arizona use: `usgovarizona.api.ml.azure.us`
    * For Virginia use: `usgovvirginia.api.ml.azure.us`
    * For both: `graph.windows.net` 


## Azure China 21Vianet	

| Feature                                       | Public cloud status | CH-East-2 | CH-North-3 |
|----------------------------------------------------------------------------|:------------------:|:--------------------:|:-------------:|
| **Automated machine learning** |    | | |
| Create and run experiments in notebooks                                    | GA               | YES       | N/A        |
| Create and run experiments in studio web experience                        | Preview   | YES       | N/A        |
| Industry-leading forecasting capabilities                                  | GA               | YES       | N/A        |
| Support for deep learning and other advanced learners                      | GA               | YES       | N/A        |
| Large data support (up to 100 GB)                                          |  Preview   | YES       | N/A        |
| Azure Databricks Integration                                              | GA               | YES        | N/A        |
| SQL, Azure Cosmos DB, and HDInsight integrations                                   | GA               | YES       | N/A        |
| **Machine Learning pipelines** |    | | |
| Create, run, and publish pipelines using the Azure ML SDK                   | GA               | YES       | N/A        |
| Create pipeline endpoints using the Azure ML SDK                           | GA               | YES       | N/A        |
| Create, edit, and delete scheduled runs of pipelines using the Azure ML SDK | GA               | YES       | N/A        |
| View pipeline run details in studio                                        | GA               | YES       | N/A        |
| Create, run, visualize, and publish pipelines in Azure ML designer          | GA  | YES       | N/A        |
| Azure Databricks Integration with ML Pipeline                             | GA               | YES        | N/A        |
| Create pipeline endpoints in Azure ML designer                             | GA   | YES       | N/A        |
| **Integrated notebooks** |   | | |
| Workspace notebook and file sharing                                        | GA               | YES       | N/A        |
