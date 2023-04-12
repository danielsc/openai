
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
