| Labeler Portal                                                            | GA                   | YES                | YES         |
| Labeling using private workforce                                          | GA                   | YES                | YES         |
| ML assisted labeling (Image classification and object detection)           | Public Preview       | YES                | YES         |
| **[Responsible ML](concept-responsible-ml.md)** |   | | |
| Explainability in UI                                                       | Public Preview       | NO                 | NO          |
| Differential privacy SmartNoise toolkit                                    | OSS                  | NO                 | NO          |
| Custom tags in Azure Machine Learning to implement datasheets              | GA                   | NO                 | NO          |
| Fairness AzureML Integration                                               | Public Preview       | NO                 | NO          |
| Interpretability  SDK                                                      | GA                   | YES                | YES         |
| **Training** |   | | |
| [Experimentation log streaming](how-to-track-monitor-analyze-runs.md)                                              | GA                   | YES                | YES         |
| [Reinforcement Learning (SDK/CLI v1)](./v1/how-to-use-reinforcement-learning.md)                                                     | Public Preview       | NO                 | NO          |
| [Experimentation UI](how-to-track-monitor-analyze-runs.md)                                                         | Public Preview                   | YES                | YES         |
| [.NET integration ML.NET 1.0](/dotnet/machine-learning/tutorials/object-detection-model-builder)                                                | GA                   | YES                | YES         |
| **Inference** |   | | |
| Managed online endpoints | GA | YES | YES |
| [Batch inferencing](tutorial-pipeline-batch-scoring-classification.md)                                                          | GA                   | YES                | YES         |
| [Azure Stack Edge with FPGA (SDK/CLI v1)](./v1/how-to-deploy-fpga-web-service.md#deploy-to-a-local-edge-server)                                                    | Public Preview       | NO                 | NO          |
| **Other** |   | | |
| [Open Datasets](../open-datasets/samples.md)                                                              | Public Preview       | YES                | YES         |
| [Custom Cognitive Search](how-to-deploy-model-cognitive-search.md)                                                    | Public Preview       | YES                | YES         |


### Azure Government scenarios

| Scenario                                                    | US-Virginia | US-Arizona| Limitations  |
|----------------------------------------------------------------------------|:----------------------:|:--------------------:|-------------|
| **General security setup** |   | | |
| Disable/control internet access (inbound and outbound) and specific VNet | PARTIAL| PARTIAL	|  | 
| Placement for all associated resources/services  | YES | YES |  |
| Encryption at-rest and in-transit.                                                 | YES | YES |  |
| Root and SSH access to compute resources.                                          | YES | YES |  |
| Maintain the security of deployed systems (instances, endpoints, etc.), including endpoint protection, patching, and logging |  PARTIAL|	PARTIAL	|ACI behind VNet currently not available |                                  
| Control (disable/limit/restrict) the use of ACI/AKS integration                    | PARTIAL|	PARTIAL	|ACI behind VNet currently not available|
| Azure role-based access control (Azure RBAC) - Custom Role Creations                           | YES | YES |  |
| Control access to ACR images used by ML Service (Azure provided/maintained versus custom)  |PARTIAL|	PARTIAL	|  |
