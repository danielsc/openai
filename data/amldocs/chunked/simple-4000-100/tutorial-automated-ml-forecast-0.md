
# Tutorial: Forecast demand with no-code automated machine learning in the Azure Machine Learning studio

Learn how to create a [time-series forecasting model](concept-automated-ml.md#time-series-forecasting) without writing a single line of code using automated machine learning in the Azure Machine Learning studio. This model will predict rental demand for a bike sharing service.  

You won't write any code in this tutorial, you'll use the studio interface to perform training.  You'll learn how to do the following tasks:

> [!div class="checklist"]
> * Create and load a dataset.
> * Configure and run an automated ML experiment.
> * Specify forecasting settings.
> * Explore the experiment results.
> * Deploy the best model.

Also try automated machine learning for these other model types:

* For a no-code example of a classification model, see [Tutorial: Create a classification model with automated ML in Azure Machine Learning](tutorial-first-experiment-automated-ml.md).
* For a code first example of an object detection model, see the [Tutorial: Train an object detection model with AutoML and Python](tutorial-auto-train-image-models.md).

## Prerequisites

* An Azure Machine Learning workspace. See [Create workspace resources](quickstart-create-resources.md). 

* Download the [bike-no.csv](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-bike-share/bike-no.csv) data file

## Sign in to the studio

For this tutorial, you create your automated ML experiment run in Azure Machine Learning studio, a consolidated web interface that includes machine learning tools to perform data science scenarios for data science practitioners of all skill levels. The studio is not supported on Internet Explorer browsers.

1. Sign in to [Azure Machine Learning studio](https://ml.azure.com).

1. Select your subscription and the workspace you created.

1. Select **Get started**.

1. In the left pane, select **Automated ML** under the **Author** section.

1. Select **+New automated ML job**. 

## Create and load dataset

Before you configure your experiment, upload your data file to your workspace in the form of an Azure Machine Learning dataset. Doing so, allows you to ensure that your data is formatted appropriately for your experiment.

1. On the **Select dataset** form, select **From local files** from the  **+Create dataset** drop-down. 

    1. On the **Basic info** form, give your dataset a name and provide an optional description. The dataset type  should default to **Tabular**, since automated ML in Azure Machine Learning studio currently only supports tabular datasets.
    
    1. Select **Next** on the bottom left

    1. On the **Datastore and file selection** form, select the default datastore that was automatically set up during your workspace creation, **workspaceblobstore (Azure Blob Storage)**. This is the storage location where you'll upload your data file. 

    1. Select **Upload files** from the **Upload** drop-down.. 
    
    1. Choose the **bike-no.csv** file on your local computer. This is the file you downloaded as a [prerequisite](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-bike-share/bike-no.csv).

    1. Select **Next**

       When the upload is complete, the Settings and preview form is pre-populated based on the file type. 
       
    1. Verify that the **Settings and preview** form is populated as follows and select **Next**.
        
        Field|Description| Value for tutorial
        ---|---|---
        File format|Defines the layout and type of data stored in a file.| Delimited
        Delimiter|One or more characters for specifying the boundary between&nbsp; separate, independent regions in plain text or other data streams. |Comma
        Encoding|Identifies what bit to character schema table to use to read your dataset.| UTF-8
        Column headers| Indicates how the headers of the dataset, if any, will be treated.| Only first file has headers
