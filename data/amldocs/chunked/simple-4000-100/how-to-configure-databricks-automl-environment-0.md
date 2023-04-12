
# Set up a development environment with Azure Databricks and AutoML in Azure Machine Learning 

Learn how to configure a development environment in Azure Machine Learning that uses Azure Databricks and automated ML.

Azure Databricks is ideal for running large-scale intensive machine learning workflows on the scalable Apache Spark platform in the Azure cloud. It provides a collaborative Notebook-based environment with a CPU or GPU-based compute cluster.

For information on other machine learning development environments, see [Set up Python development environment](how-to-configure-environment.md).


## Prerequisite

Azure Machine Learning workspace. To create one, use the steps in the [Create workspace resources](quickstart-create-resources.md) article.


## Azure Databricks with Azure Machine Learning and AutoML

Azure Databricks integrates with Azure Machine Learning and its AutoML capabilities. 

You can use Azure Databricks:

+ To train a model using Spark MLlib and deploy the model to ACI/AKS.
+ With [automated machine learning](concept-automated-ml.md) capabilities using an Azure ML SDK.
+ As a compute target from an [Azure Machine Learning pipeline](concept-ml-pipelines.md).

## Set up a Databricks cluster

Create a [Databricks cluster](/azure/databricks/scenarios/quickstart-create-databricks-workspace-portal). Some settings apply only if you install the SDK for automated machine learning on Databricks.

**It takes few minutes to create the cluster.**

Use these settings:

| Setting |Applies to| Value |
|----|---|---|
| Cluster Name |always| yourclustername |
| Databricks Runtime Version |always| 9.1 LTS|
| Python version |always| 3 |
| Worker Type <br>(determines max # of concurrent iterations) |Automated ML<br>only| Memory optimized VM preferred |
| Workers |always| 2 or higher |
| Enable Autoscaling |Automated ML<br>only| Uncheck |

Wait until the cluster is running before proceeding further.

## Add the Azure ML SDK to Databricks

Once the cluster is running, [create a library](https://docs.databricks.com/user-guide/libraries.html#create-a-library) to attach the appropriate Azure Machine Learning SDK package to your cluster. 

To use automated ML, skip to [Add the Azure ML SDK with AutoML](#add-the-azure-ml-sdk-with-automl-to-databricks).


1. Right-click the current Workspace folder where you want to store the library. Select **Create** > **Library**.
    
    > [!TIP]
    > If you have an old SDK version, deselect it from cluster's installed libraries and move to trash. Install the new SDK version and restart the cluster. If there is an issue after the restart, detach and reattach your cluster.

1. Choose the following option (no other SDK installations are supported)

   |SDK&nbsp;package&nbsp;extras|Source|PyPi&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
   |----|---|---|
   |For Databricks| Upload Python Egg or PyPI | azureml-sdk[databricks]|

   > [!WARNING]
   > No other SDK extras can be installed. Choose only the [`databricks`] option .

   * Do not select **Attach automatically to all clusters**.
   * Select  **Attach** next to your cluster name.

1. Monitor for errors until status changes to **Attached**, which may take several minutes.  If this step fails:

   Try restarting your cluster by:
   1. In the left pane, select **Clusters**.
   1. In the table, select your cluster name.
   1. On the **Libraries** tab, select **Restart**.

   A successful install looks like the following: 

  ![Azure Machine Learning SDK for Databricks](./media/how-to-configure-environment/amlsdk-withoutautoml.jpg) 

## Add the Azure ML SDK with AutoML to Databricks
If the cluster was created with Databricks Runtime 7.3 LTS (*not* ML), run the following command in the first cell of your notebook to install the AzureML SDK.

```
%pip install --upgrade --force-reinstall -r https://aka.ms/automl_linux_requirements.txt
```

### AutoML config settings

In AutoML config, when using Azure Databricks add the following parameters:

