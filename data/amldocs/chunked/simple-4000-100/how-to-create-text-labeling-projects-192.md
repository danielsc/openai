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