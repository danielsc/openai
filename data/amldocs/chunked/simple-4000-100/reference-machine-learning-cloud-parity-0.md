
# Azure Machine Learning feature availability across clouds regions

Learn what Azure Machine Learning features are available in the Azure Government, Azure Germany, and Azure China 21Vianet regions. 

In the list of global Azure regions, there are several regions that serve specific markets in addition to the public cloud regions. For example, the Azure Government and the Azure China 21Vianet regions. Azure Machine Learning is deployed into the following regions, in addition to public cloud regions:

* Azure Government regions **US-Arizona** and **US-Virginia**.
* Azure China 21Vianet region **China-East-2**.

Azure Machine Learning is still in development in air-gap Regions. 

The information in the rest of this document provides information on what features of Azure Machine Learning are available in these regions, along with region-specific information on using these features.
## Azure Government	

| Feature | Public cloud status  | US-Virginia | US-Arizona| 
|----------------------------------------------------------------------------|:----------------------:|:--------------------:|:-------------:|
| **[Automated machine learning](concept-automated-ml.md)** | | | |
| Create and run experiments in notebooks                                    | GA                   | YES                | YES         |
| Create and run experiments in studio web experience                        | Public Preview       | YES                | YES         |
| Industry-leading forecasting capabilities                                  | GA                   | YES                | YES         |
| Support for deep learning and other advanced learners                      | GA                   | YES                | YES         |
| Large data support (up to 100 GB)                                          | Public Preview       | YES                | YES         |
| Azure Databricks integration                                              | GA                   | NO                 | NO          |
| SQL, Azure Cosmos DB, and HDInsight integrations                                   | GA                   | YES                | YES         |
| **[Machine Learning pipelines](concept-ml-pipelines.md)** |   |  | | 
| Create, run, and publish pipelines using the Azure ML SDK                   | GA                   | YES                | YES         |
| Create pipeline endpoints using the Azure ML SDK                           | GA                   | YES                | YES         |
| Create, edit, and delete scheduled runs of pipelines using the Azure ML SDK | GA                   | YES*               | YES*        |
| View pipeline run details in studio                                        | GA                   | YES                | YES         |
| Create, run, visualize, and publish pipelines in Azure ML designer          | GA      | YES                | YES         |
| Azure Databricks Integration with ML Pipeline                             | GA                   | NO                 | NO          |
| Create pipeline endpoints in Azure ML designer                             | GA      | YES                | YES         |
| **[Integrated notebooks](how-to-run-jupyter-notebooks.md)** |   |  | | 
| Workspace notebook and file sharing                                        | GA                   | YES                | YES         |
| R and Python support                                                       | GA                   | YES                | YES         |
| Virtual Network support                                                    | GA       | YES                 | YES          |
| **[Compute instance](concept-compute-instance.md)** |   |  | | 
| Managed compute Instances for integrated Notebooks                         | GA                   | YES                | YES         |
| Jupyter, JupyterLab Integration                                            | GA                   | YES                | YES         |
| Virtual Network (VNet) support                                             | GA       | YES                | YES         |
