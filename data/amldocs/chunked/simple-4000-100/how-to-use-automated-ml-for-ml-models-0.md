
# Set up no-code AutoML training with the studio UI 

In this article, you learn how to set up AutoML training jobs without a single line of code using Azure Machine Learning automated ML in the [Azure Machine Learning studio](overview-what-is-azure-machine-learning.md#studio).

Automated machine learning, AutoML, is a process in which the best machine learning algorithm to use for your specific data is selected for you. This process enables you to generate machine learning models quickly. [Learn more about how Azure Machine Learning implements automated machine learning](concept-automated-ml.md).
 
For an end to end example, try the [Tutorial: AutoML- train no-code classification models](tutorial-first-experiment-automated-ml.md). 

For a Python code-based experience, [configure your automated machine learning experiments](how-to-configure-auto-train.md) with the Azure Machine Learning SDK.

## Prerequisites

* An Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/) today.

* An Azure Machine Learning workspace. See [Create workspace resources](quickstart-create-resources.md). 

## Get started

1. Sign in to [Azure Machine Learning studio](https://ml.azure.com). 

1. Select your subscription and workspace. 

1. Navigate to the left pane. Select **Automated ML** under the **Author** section.

[![Azure Machine Learning studio navigation pane](media/how-to-use-automated-ml-for-ml-models/nav-pane.png)](media/how-to-use-automated-ml-for-ml-models/nav-pane-expanded.png)

 If this is your first time doing any experiments, you'll see an empty list and links to documentation. 

Otherwise, you'll see a list of your recent automated  ML experiments, including those created with the SDK. 

## Create and run experiment

1. Select **+ New automated ML job** and populate the form.

1. Select a data asset from your storage container, or create a new data asset. Data asset can be created from local files, web urls, datastores, or Azure open datasets. Learn more about [data asset creation](how-to-create-data-assets.md).  

    >[!Important]
    > Requirements for training data:
    >* Data must be in tabular form.
    >* The value you want to predict (target column) must be present in the data.

    1. To create a new dataset from a file on your local computer, select **+Create dataset** and then select **From local file**. 

    1. In the **Basic info** form, give your dataset a unique name and provide an optional description. 

    1. Select **Next** to open the **Datastore and file selection form**. On this form you select where to upload your dataset; the default storage container that's automatically created with your workspace, or choose a storage container that you want to use for the experiment. 
    
        1. If your data is behind a virtual network, you need to enable the **skip the validation** function to ensure that the workspace can access your data. For more information, see [Use Azure Machine Learning studio in an Azure virtual network](how-to-enable-studio-virtual-network.md). 
    
    1. Select **Browse** to upload the data file for your dataset. 

    1. Review the **Settings and preview** form for accuracy. The form is intelligently populated based on the file type. 

        Field| Description
        ----|----
        File format| Defines the layout and type of data stored in a file.
        Delimiter| One or more characters for specifying the boundary between separate, independent regions in plain text or other data streams.
        Encoding| Identifies what bit to character schema table to use to read your dataset.
        Column headers| Indicates how the headers of the dataset, if any, will be treated.
        Skip rows | Indicates how many, if any, rows are skipped in the dataset.
    
        Select **Next**.

    1. The **Schema** form is intelligently populated based on the selections in the **Settings and preview** form. Here configure the data type for each column, review the column names, and select which columns to **Not include** for your experiment. 
