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
