
# Create an image labeling project and export labels

Learn how to create and run data labeling projects to label images in Azure Machine Learning. Use machine-learning-assisted data labeling, or human-in-the-loop labeling, to aid with the task.

Set up labels for classification, object detection (bounding box), or instance segmentation (polygon).

You can also use the data labeling tool to [create a text labeling project](how-to-create-text-labeling-projects.md).

## Image labeling capabilities

Azure Machine Learning data labeling is a tool to create, manage, and monitor data labeling projects:

- Coordinate data, labels, and team members to efficiently manage labeling tasks.
- Track progress and maintain the queue of incomplete labeling tasks.
- Start and stop the project, and control the labeling progress.
- Review and export the labeled data as an Azure Machine Learning dataset.

> [!Important]
> Data images must be files available in an Azure blob datastore. (If you do not have an existing datastore, you can upload files during project creation.)

Image data can be files with any of these types: ".jpg", ".jpeg", ".png", ".jpe", ".jfif", ".bmp", ".tif", ".tiff", ".dcm", ".dicom". Each file is an item to be labeled.

## Prerequisites

[!INCLUDE [prerequisites](../../includes/machine-learning-data-labeling-prerequisites.md)]

## Create an image labeling project

[!INCLUDE [start](../../includes/machine-learning-data-labeling-start.md)]

1. To create a project, select **Add project**. Give the project an appropriate name. You can't reuse the project name, even if the project is deleted in future.

1. Select **Image** to create an image labeling project.

    :::image type="content" source="media/how-to-create-labeling-projects/labeling-creation-wizard.png" alt-text="Labeling project creation for mage labeling":::

    * Choose **Image Classification Multi-class** for those projects that involve the application of only a *single label*, from a set of labels, to an image.
    * Choose **Image Classification Multi-label** for projects that involve the application of *one or more* labels, from a set of labels, to an image. For example, a photo of a dog might be labeled with both *dog* and *daytime*.
    * Choose **Object Identification (Bounding Box)** for projects that involve the assignment of a label, and a bounding box, to each object within an image.
    * Choose **Instance Segmentation (Polygon)** for projects that involve both the assignment of a label to, and a drawn polygon around, each object within an image.

1. Select **Next** when you want to continue.

## Add workforce (optional)

[!INCLUDE [outsource](../../includes/machine-learning-data-labeling-outsource.md)]

## Specify the data to label

If you already created a dataset that contains your data, select it from the **Select an existing dataset** drop-down list. You can also select **Create a dataset** to use an existing Azure datastore, or to upload local files.

> [!NOTE]
> A project cannot contain more than 500,000 files. If your dataset exceeds this file count, only the first 500,000 files will be loaded.

### Create a dataset from an Azure datastore

In many cases, you can upload local files. However, [Azure Storage Explorer](https://azure.microsoft.com/features/storage-explorer/) provides a faster and more robust way to transfer a large amount of data. We recommend Storage Explorer as the default way to move files.

To create a dataset from data that you've already stored in Azure Blob storage:

1. Select **+ Create** .
1. Assign a **Name** to your dataset, and optionally a description.
1. **Dataset type** is set to file; only file dataset types are supported for images.
1. Select **Next**.
1. Select **From Azure storage**, then select **Next**.
1. Select the datastore, then select **Next**.
1. If your data is in a subfolder within your blob storage, choose **Browse** to select the path.
    * Append "/**" to the path, to include all the files in the subfolders of the selected path.
