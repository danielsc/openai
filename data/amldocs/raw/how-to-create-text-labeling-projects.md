---
title: Set up text labeling project
titleSuffix: Azure Machine Learning
description: Create a project to label text using the data labeling tool. Specify either a single label or multiple labels to apply to each piece of text.
author: kvijaykannan 
ms.author: vkann 
ms.reviewer: franksolomon
ms.service: machine-learning
ms.subservice: mldata
ms.topic: how-to
ms.date: 02/08/2023
ms.custom: data4ml, ignite-fall-2021
---

# Create a text labeling project and export labels

In Azure Machine Learning, learn how to create and run data labeling projects to label text data. Specify either a single label or multiple labels, to apply to each text item.

You can also use the data labeling tool to [create an image labeling project](how-to-create-image-labeling-projects.md).

## Text labeling capabilities

Azure Machine Learning data labeling serves as a tool to create, manage, and monitor data labeling projects:

- Coordinate data, labels, and team members to efficiently manage labeling tasks.
- Track progress and maintain the queue of incomplete labeling tasks.
- Start and stop the project, and control the labeling progress.
- Review and export the labeled data as an Azure Machine Learning dataset.

> [!Important]
> Text data must be available in an Azure blob datastore. (If you do not have an existing datastore, you can upload files during project creation.)

Data formats available for text data:

* **.txt**: each file represents one item to be labeled.
* **.csv** or **.tsv**: each row represents one item presented to the labeler. You decide which columns the labeler can see, in order to label the row.

## Prerequisites

[!INCLUDE [prerequisites](../../includes/machine-learning-data-labeling-prerequisites.md)]

## Create a text labeling project

[!INCLUDE [start](../../includes/machine-learning-data-labeling-start.md)]

1. To create a project, select **Add project**. Give the project an appropriate name. You can't reuse the project name, even if the project is deleted in future.

1. Select **Text** to create a text labeling project.

    :::image type="content" source="media/how-to-create-text-labeling-projects/text-labeling-creation-wizard.png" alt-text="Labeling project creation for text labeling":::

    * Choose **Text Classification Multi-class** for those projects that involve the application of only a *single label*, from a set of labels, to each piece of text.
    * Choose **Text Classification Multi-label** for projects that involve the application of *one or more* labels, from a set of labels, to each piece of text.
    * Choose **Text Named Entity Recognition** for projects that involve the application of labels to individual text words, or multiple text words, in each entry.

1. Select **Next** to continue.

## Add workforce (optional)

[!INCLUDE [outsource](../../includes/machine-learning-data-labeling-outsource.md)]

## Select or create a dataset

If you already created a dataset that contains your data, select it from the **Select an existing dataset** drop-down list. You can also select **Create a dataset** to use an existing Azure datastore, or to upload local files.

> [!NOTE]
> A project cannot contain more than 500,000 files. If your dataset exceeds this file count, only the first 500,000 files will be loaded.

### Create a dataset from an Azure datastore

In many cases, you can upload local files. However, [Azure Storage Explorer](https://azure.microsoft.com/features/storage-explorer/) provides a faster and more robust way to transfer a large amount of data. We recommend Storage Explorer as the default way to move files.

To create a dataset from data that you've already stored in Azure Blob storage:

1. Select **+ Create** .
1. Assign a **Name** to your dataset, and optionally a description.
1. Choose the **Dataset type**:
    * Select **Tabular** if you're using a .csv or .tsv file, where each row contains a response.
    * Select **File** if you're using separate .txt files for each response.
1. Select **Next**.
1. Select **From Azure storage**, then **Next**.
1. Select the datastore, then select **Next**.
1. If your data is in a subfolder within your blob storage, choose **Browse** to select the path.
    * Append "/**" to the path, to include all the files in the subfolders of the selected path.
    * Append "**/*.*" to include all the data in the current container and its subfolders.
1. Select **Create**.
1. Select the data asset you created.

### Create a dataset from uploaded data

To directly upload your data:

1. Select **+ Create**.
1. Assign a **Name** to your dataset, and optionally a description.
1. Choose the **Dataset type**:
    * Select **Tabular** if you use a .csv or .tsv file, where each row contains a response.
    * Select **File** if you use separate .txt files for each response.
1. Select **Next**.
1. Select **From local files**, then select **Next**.
1. (Optional) Select a datastore; the default uploads to the default blob store ("workspaceblobstore") of your Machine Learning workspace.
1. Select **Next**.
1. Select **Upload > Upload files** or **Upload > Upload folder** to select the local files or folder(s) to upload.
1. Find your files or folder in the browser window, then select **Open**.
1. Continue to use **Upload** until you specify all of your files/folders.
1. Check the **Overwrite if already exists** box if you want. Verify the list of files/folders.
1. Select **Next**.
1. Confirm the details. Select **Back** to modify the settings, or **Create** to create the dataset.
1. Finally, select the data asset you created.

## Configure incremental refresh

[!INCLUDE [refresh](../../includes/machine-learning-data-labeling-refresh.md)]

> [!NOTE]
> Projects that use tabular (.csv or .tsv) dataset input have incremental refresh available to them. However, this adds only new tabular files. The refresh will not recognize changes to existing tabular files.


## Specify label categories

[!INCLUDE [classes](../../includes/machine-learning-data-labeling-classes.md)]

## Describe the text labeling task

[!INCLUDE [describe](../../includes/machine-learning-data-labeling-describe.md)]

>[!NOTE]
> Labelers can select the first 9 labels with number keys 1-9.

## Quality control (preview)

[!INCLUDE [describe](../../includes/machine-learning-data-labeling-quality-control.md)]

## Use ML-assisted data labeling

To accelerate labeling tasks, the **ML-assisted labeling** page can trigger automatic machine learning models. ML-assisted labeling can handle both file (.txt) and tabular (.csv) text data inputs.
To use **ML-assisted labeling**:

* Select **Enable ML assisted labeling**.
* Select the **Dataset language** for the project. This list shows all languages that the [TextDNNLanguages Class](/python/api/azureml-automl-core/azureml.automl.core.constants.textdnnlanguages?view=azure-ml-py&preserve-view=true) supports.
* Specify a compute target to use. If you don't have a compute target in your workspace, this creates a compute cluster, and adds that compute cluster to your workspace. The cluster is created with a minimum of zero nodes, and it costs nothing when not in use.

### ML-assisted labeling - more information

At the start of your labeling project, the items are shuffled into a random order to reduce potential bias. However, the trained model reflects any biases present in the dataset. For example, if 80% of your items are of a single class, then approximately 80% of the data used to train the model lands in that class.

To train the text DNN model that ML-assist uses, the input text per training example is limited to approximately the first 128 words in the document. For tabular input, all text columns are first concatenated before applying this limit. This practical limit allows for the model training to complete in a reasonable amount of time. The actual text in a document (for file input) or set of text columns (for tabular input) can exceed 128 words. The limit only pertains to what the model internally uses during the training process.

The exact number of labeled items necessary to start assisted labeling isn't a fixed number. This number can vary significantly from one labeling project to another. The variance depends on many factors, including the number of label classes, and the label distribution.

When you use consensus labeling, the consensus label is used for training.

Since the final labels still rely on input from the labeler, this technology is sometimes called *human in the loop* labeling.

> [!NOTE]
> ML assisted data labeling does not support default storage accounts secured behind a [virtual network](how-to-network-security-overview.md). You must use a non-default storage account for ML assisted data labelling. The non-default storage account can be secured behind the virtual network.

### Pre-labeling

After submission of enough labels for training, the trained model is used to predict tags. The labeler now sees pages that show predicted labels already present on each item. The task then involves review of these predictions, and correction of any mis-labeled items, before page submission. 

Once you train the machine learning model on your manually labeled data, the model is evaluated on a test set of manually labeled items, to determine its accuracy at different confidence thresholds. This evaluation process is used to determine a confidence threshold, past which the model is accurate enough to show pre-labels. The model is then evaluated against unlabeled data. Pre-labeling uses items with predictions at a higher confidence level compared to this threshold.

## Initialize the text labeling project

[!INCLUDE [initialize](../../includes/machine-learning-data-labeling-initialize.md)]

## Run and monitor the project

[!INCLUDE [run](../../includes/machine-learning-data-labeling-run.md)]

### Dashboard

The **Dashboard** tab shows the labeling task progress.

:::image type="content" source="./media/how-to-create-text-labeling-projects/text-labeling-dashboard.png" alt-text="Text data labeling dashboard":::

The progress chart shows how many items have been labeled, skipped, need review, or not yet done. Hover over the chart to see the number of items in each section.

Under the chart is a distribution of the labels for completed tasks. In some project types, an item can have multiple labels. Therefore, the total number of labels can exceed the total number items.

You also see a distribution of labelers, and how many items they've labeled.

Finally, the middle section shows a table with a queue of unassigned tasks. When ML assisted labeling is off, this section shows the number of manual tasks awaiting assignment.

Additionally, when ML assisted labeling is enabled, scroll down to see the ML assisted labeling status. The Jobs sections give links for each of the machine learning runs.

### Data

On the **Data** tab, you can see your dataset and the labeled data. Scroll through the labeled data to see the labels. If you see incorrectly labeled data, select it and choose **Reject**, to remove the labels and return the data to the unlabeled queue.

If your project uses consensus labeling, you should focus on those images that have no consensus:

1. Select the **Data** tab.
1. On the left, select **Review labels**.
1. On the top right, select **All filters**.

    :::image type="content" source="media/how-to-create-text-labeling-projects/text-labeling-select-filter.png" alt-text="Screenshot: select filters to focus on consensus label problems." lightbox="media/how-to-create-text-labeling-projects/text-labeling-select-filter.png":::

1. Under **Labeled datapoints**, select **Consensus labels to review**, to show only those images where the labelers didn't come to a consensus.

    :::image type="content" source="media/how-to-create-labeling-projects/select-need-review.png" alt-text="Screenshot: Select labels that need review.":::

1. For each item that needs review, select the **Consensus label** dropdown, to view the conflicting labels.

    :::image type="content" source="media/how-to-create-text-labeling-projects/text-labeling-consensus-dropdown.png" alt-text="Screenshot: Select Consensus label dropdown to review conflicting labels." lightbox="media/how-to-create-text-labeling-projects/text-labeling-consensus-dropdown.png":::

1. Although you can select an individual to see just their label(s), you can only update or reject the labels from the top choice, **Consensus label (preview)**.

### Details tab

View and change details of your project. In this tab you can:

* View project details and input datasets
* Enable or disable **incremental refresh at regular intervals**, or request an immediate refresh.
* View details of the storage container used to store labeled outputs in your project
* Add labels to your project
* Edit instructions you give to your labels
* Change settings for ML assisted labeling, and kick off a labeling task

### Access for labelers

[!INCLUDE [access](../../includes/machine-learning-data-labeling-access.md)]

## Add new labels to a project

[!INCLUDE [add-label](../../includes/machine-learning-data-labeling-add-label.md)]

## Start an ML assisted labeling task

[!INCLUDE [start-ml-assist](../../includes/machine-learning-data-labeling-start-ml-assist.md)]

## Export the labels

Use the **Export** button on the **Project details** page of your labeling project. You can export the label data for Machine Learning experimentation at any time.

For all project types except **Text Named Entity Recognition**, you can export:
* A CSV file. The Azure Machine Learning workspace creates the CSV file, in a folder inside *Labeling/export/csv*.
* An [Azure Machine Learning dataset with labels](v1/how-to-use-labeled-dataset.md). 


For **Text Named Entity Recognition** projects, you can export:
* An [Azure Machine Learning dataset (v1) with labels](v1/how-to-use-labeled-dataset.md).
* A CoNLL file. For this export, you must assign a compute resource. The export process runs offline, and it generates the file as part of an experiment run. When the file is ready to download, a notification on the top right appears. Select that notification to see a link to the file.

    :::image type="content" source="media/how-to-create-text-labeling-projects/notification-bar.png" alt-text="Notification for file download.":::

Access exported Azure Machine Learning datasets in the **Datasets** section of Machine Learning. The dataset details page also provides sample code to access your labels from Python.

![Exported dataset](./media/how-to-create-labeling-projects/exported-dataset.png)

## Troubleshooting

[!INCLUDE [troubleshooting](../../includes/machine-learning-data-labeling-troubleshooting.md)]

## Next steps

* [How to tag text](how-to-label-data.md#label-text)