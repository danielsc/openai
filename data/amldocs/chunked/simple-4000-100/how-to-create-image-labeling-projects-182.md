Finally, the middle section shows a table with a queue of unassigned tasks. When ML assisted labeling is off, this section shows the number of manual tasks awaiting assignment.

When ML assisted labeling is on, this section also shows:

* Tasks containing clustered items in the queue
* Tasks containing prelabeled items in the queue

Additionally, when ML assisted labeling is enabled, you can scroll down to see the ML assisted labeling status. The Jobs sections give links for each of the machine learning runs.

* Training - trains a model to predict the labels
* Validation - determines whether item pre-labeling uses the prediction of this model
* Inference - prediction run for new items
* Featurization - clusters items (only for image classification projects)


### Data tab

On the **Data** tab, you can see your dataset, and review labeled data. Scroll through the labeled data to see the labels. If you see incorrectly labeled data, select it and choose **Reject**, to remove the labels and return the data to the unlabeled queue.

If your project uses consensus labeling, you should review those images that have no consensus:

1. Select the **Data** tab.
1. On the left, select  **Review labels**.
1. On the top right, select **All filters**.

    :::image type="content" source="media/how-to-create-labeling-projects/select-filters.png" alt-text="Screenshot: select filters to review consensus label problems." lightbox="media/how-to-create-labeling-projects/select-filters.png":::

1. Under **Labeled datapoints**, select **Consensus labels in need of review**, to show only those images where the labelers didn't come to a consensus.

    :::image type="content" source="media/how-to-create-labeling-projects/select-need-review.png" alt-text="Screenshot: Select labels in need of review.":::

1. For each image to review, select the **Consensus label** dropdown, to view the conflicting labels.

    :::image type="content" source="media/how-to-create-labeling-projects/consensus-dropdown.png" alt-text="Screenshot: Select Consensus label dropdown to review conflicting labels." lightbox="media/how-to-create-labeling-projects/consensus-dropdown.png":::

1. Although you can select an individual to see just their label(s), you can only update or reject the labels from the top choice, **Consensus label (preview)**.

### Details tab

View and change details of your project. In this tab, you can:

* View project details and input datasets
* Enable or disable **incremental refresh at regular intervals**, or request an immediate refresh
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

* Image labels can be exported as:
    * [COCO format](http://cocodataset.org/#format-data). The COCO file is created in the default blob store of the Azure Machine Learning workspace in a folder within *Labeling/export/coco*. 
    * An [Azure Machine Learning dataset with labels](v1/how-to-use-labeled-dataset.md). 

Access exported Azure Machine Learning datasets in the **Datasets** section of Machine Learning. The dataset details page also provides sample code to access your labels from Python.

![Exported dataset](./media/how-to-create-labeling-projects/exported-dataset.png)

Once you export your labeled data to an Azure Machine Learning dataset, you can use AutoML to build computer vision models trained on your labeled data. Learn more at [Set up AutoML to train computer vision models with Python](how-to-auto-train-image-models.md)
