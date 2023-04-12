| ML assisted labeling (Image classification and object detection)           | Preview   | YES       | N/A        |
| **Responsible AI** |    | | |
| Explainability in UI                                                       | Preview   | NO        | N/A        |
| Differential privacy SmartNoise toolkit                                    | OSS              | NO        | N/A        |
| custom tags in Azure Machine Learning to implement datasheets              | GA               | YES        | N/A        |
| Fairness AzureML Integration                                               | Preview   | NO        | N/A        |
| Interpretability  SDK                                                      | GA               | YES       | N/A        |
| **Training** |    | | |
| Experimentation log streaming                                              | GA               | YES       | N/A        |
| Reinforcement Learning                                                     | Deprecating       | Deprecating            | N/A        |
| Experimentation UI                                                         | GA               | YES       | N/A        |
| .NET integration ML.NET 1.0                                                | GA               | YES       | N/A        |
| **Inference** |   | | |
| Managed online endpoints | GA | YES | N/A |
| Batch inferencing                                                          | GA               | YES       | N/A        |
| Azure Stack Edge with FPGA                                                    | Deprecating       | Deprecating            | N/A        |
| **Other** |    | | |
| Open Datasets                                                              | Preview   | YES       | N/A        |
| Custom Cognitive Search                                                    | Preview   | YES       | N/A        |



### Other Azure China limitations

* Azure China has limited VM SKU, especially for GPU SKU. It only has NCv3 family (V100).
* REST API Endpoints are different from global Azure. Use the following table to find the REST API endpoint for Azure China regions:

    | REST endpoint                 | Global Azure                                 | China-Government                           |
    |------------------|--------------------------------------------|--------------------------------------------|
    | Management plane | `https://management.azure.com/`              | `https://management.chinacloudapi.cn/`       |
    | Data plane       | `https://{location}.experiments.azureml.net` | `https://{location}.experiments.ml.azure.cn` |
    | Azure Active Directory              | `https://login.microsoftonline.com`          | `https://login.chinacloudapi.cn`             |

* Sample notebook may not work, if it needs access to public data.
* IP address ranges: The CLI command used in the [required public internet access](how-to-secure-training-vnet.md#required-public-internet-access-to-train-models) instructions does not return IP ranges. Use the [Azure IP ranges and service tags for Azure China](https://www.microsoft.com//download/details.aspx?id=57062) instead.
* Azure Machine Learning compute instances preview is not supported in a workspace where Private Endpoint is enabled for now, but CI will be supported in the next deployment for the service expansion to all AzureML regions.
* Searching for assets in the web UI with Chinese characters will not work correctly.

## Next steps

To learn more about the regions that Azure Machine learning is available in, see [Products by region](https://azure.microsoft.com/global-infrastructure/services/).
