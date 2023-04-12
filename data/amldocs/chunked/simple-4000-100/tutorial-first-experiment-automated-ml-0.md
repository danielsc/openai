
# Tutorial: Train a classification model with no-code AutoML in the Azure Machine Learning studio

Learn how to train a classification model with no-code AutoML using Azure Machine Learning automated ML in the Azure Machine Learning studio. This classification model predicts if a client will subscribe to a fixed term deposit with a financial institution.

With automated ML, you can automate away time intensive tasks. Automated machine learning rapidly iterates over many combinations of algorithms and hyperparameters to help you find the best model based on a success metric of your choosing.

You won't write any code in this tutorial, you'll use the studio interface to perform training.  You'll learn how to do the following tasks:

> [!div class="checklist"]
> * Create an Azure Machine Learning workspace.
> * Run an automated machine learning experiment.
> * Explore model details.
> * Deploy the recommended model.

Also try automated machine learning for these other model types:

* For a no-code example of forecasting, see [Tutorial: Demand forecasting & AutoML](tutorial-automated-ml-forecast.md).
* For a code first example of an object detection model, see the [Tutorial: Train an object detection model with AutoML and Python](tutorial-auto-train-image-models.md),

## Prerequisites

* An Azure subscription. If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/).

* Download the [**bankmarketing_train.csv**](https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv) data file. The **y** column indicates if a customer subscribed to a fixed term deposit, which is later identified as the target column for predictions in this tutorial. 

## Create a workspace

An Azure Machine Learning workspace is a foundational resource in the cloud that you use to experiment, train, and deploy machine learning models. It ties your Azure subscription and resource group to an easily consumed object in the service. 

There are many [ways to create a workspace](how-to-manage-workspace.md). In this tutorial, you create a workspace via the Azure portal, a web-based console for managing your Azure resources.

[!INCLUDE [aml-create-portal](../../includes/aml-create-in-portal.md)]

>[!IMPORTANT] 
> Take note of your **workspace** and **subscription**. You'll need these to ensure you create your experiment in the right place. 

## Sign in to the studio

You complete the following experiment set-up and run steps  via the Azure Machine Learning studio at https://ml.azure.com, a consolidated web interface that includes machine learning tools to perform data science scenarios for data science practitioners of all skill levels. The studio is not supported on Internet Explorer browsers.

1. Sign in to [Azure Machine Learning studio](https://ml.azure.com).

1. Select your subscription and the workspace you created.

1. Select **Get started**.

1. In the left pane, select **Automated ML** under the **Author** section.

   Since this is your first automated ML experiment, you'll see an empty list and links to documentation.

   ![Get started page](./media/tutorial-first-experiment-automated-ml/get-started.png)

1. Select **+New automated ML job**. 

## Create and load dataset

Before you configure your experiment, upload your data file to your workspace in the form of an Azure Machine Learning dataset. Doing so, allows you to ensure that your data is formatted appropriately for your experiment.

1. Create a new dataset by selecting **From local files** from the  **+Create dataset** drop-down. 

    1. On the **Basic info** form, give your dataset a name and provide an optional description. The automated ML interface currently only supports TabularDatasets, so the dataset type should default to *Tabular*.

    1. Select **Next** on the bottom left

    1. On the **Datastore and file selection** form, select the default datastore that was automatically set up during your workspace creation, **workspaceblobstore (Azure Blob Storage)**. This is where you'll upload your data file to make it available to your workspace.
