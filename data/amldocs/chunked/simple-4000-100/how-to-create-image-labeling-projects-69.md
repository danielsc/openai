1. If your data is in a subfolder within your blob storage, choose **Browse** to select the path.
    * Append "/**" to the path, to include all the files in the subfolders of the selected path.
    * Append "**/*.*" to include all the data in the current container and its subfolders.
1. Select **Create**.
1. Select the data asset you created.

### Create a dataset from uploaded data

To directly upload your data:

1. Select **+ Create**.
1. Assign a **Name** to your dataset, and optionally a description.
1. **Dataset type** is set to file; only file dataset types are supported for images.
1. Select **Next**.
1. Select **From local files**, then select **Next**.
1. (Optional) Select a datastore. You can also keep the default to upload to the default blob store ("workspaceblobstore") of your Machine Learning workspace.
1. Select **Next**.
1. Select **Upload > Upload files** or **Upload > Upload folder** to select the local files or folder(s) to upload.
1. In the browser window, find your files or folder, then select **Open**.
1. Continue using **Upload** until you specify all your files/folders.
1. If you want, check the box **Overwrite if already exists**. Verify the list of files/folders.
1. Select **Next**.
1. Confirm the details. Select **Back** to modify the settings or **Create** to create the dataset.
1. Finally, select the data asset you created.

## Configure incremental refresh

[!INCLUDE [refresh](../../includes/machine-learning-data-labeling-refresh.md)]

## Specify label classes

[!INCLUDE [classes](../../includes/machine-learning-data-labeling-classes.md)]

## Describe the image labeling task

[!INCLUDE [describe](../../includes/machine-learning-data-labeling-describe.md)]

For bounding boxes, important questions include:

* How is the bounding box defined for this task? Should it stay entirely on the interior of the object, or should it be on the exterior? Should it be cropped as closely as possible, or is some clearance acceptable?
* What level of care and consistency do you expect the labelers to apply in defining bounding boxes?
* What is the visual definition of each label class? Can you provide a list of normal, edge, and counter cases for each class?
* What should the labelers do if the object is tiny? Should it be labeled as an object, or should they ignore that object as background?
* How should labelers handle an object only partially shown in the image?
* How should labelers handle an object partially covered by other object?
* How should labelers handle an object with no clear boundary?
* How should labelers handle an object that isn't the object class of interest, but has visual similarities to a relevant object type?

> [!NOTE]
> Labelers can select the first 9 labels with number keys 1-9.

## Quality control (preview)

[!INCLUDE [describe](../../includes/machine-learning-data-labeling-quality-control.md)]

> [!NOTE]
> **Instance Segmentation** projects cannot use consensus labeling.

## Use ML-assisted data labeling

To accelerate labeling tasks, the **ML-assisted labeling** page lets you trigger automatic machine learning models. Medical images (".dcm") aren't included in assisted labeling.

At the start of your labeling project, the items are shuffled into a random order to reduce potential bias. However, the trained model reflects any biases present in the dataset. For example, if 80% of your items are of a single class, then approximately 80% of the data used to train the model lands in that class.

Select *Enable ML assisted labeling*, and specify a GPU to enable assisted labeling. If you don't have a GPU in your workspace, a GPU cluster is created for you and added to your workspace. The cluster is created with a minimum of zero nodes, which means it costs nothing when not in use.

ML-assisted labeling consists of two phases:

* Clustering
* Prelabeling

The exact labeled data item count necessary to start assisted labeling isn't a fixed number. This number can vary significantly from one labeling project to another. For some projects, is sometimes possible to see pre-label or cluster tasks after 300 items have been manually labeled. ML Assisted Labeling uses a technique called *Transfer Learning*, which uses a pre-trained model to jump-start the training process. If the classes of your dataset resemble the classes in the pre-trained model, pre-labels may become available after only a few hundred manually labeled items. If your dataset significantly differs from the data used to pre-train the model, the process may take more time.
