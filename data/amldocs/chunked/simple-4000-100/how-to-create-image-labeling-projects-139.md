The exact labeled data item count necessary to start assisted labeling isn't a fixed number. This number can vary significantly from one labeling project to another. For some projects, is sometimes possible to see pre-label or cluster tasks after 300 items have been manually labeled. ML Assisted Labeling uses a technique called *Transfer Learning*, which uses a pre-trained model to jump-start the training process. If the classes of your dataset resemble the classes in the pre-trained model, pre-labels may become available after only a few hundred manually labeled items. If your dataset significantly differs from the data used to pre-train the model, the process may take more time.

When you use consensus labeling, the consensus label is used for training.

Since the final labels still rely on input from the labeler, this technology is sometimes called *human in the loop* labeling.

> [!NOTE]
> ML assisted data labeling does not support default storage accounts secured behind a [virtual network](how-to-network-security-overview.md). You must use a non-default storage account for ML assisted data labelling. The non-default storage account can be secured behind the virtual network.

### Clustering

After submission of some labels, the classification machine learning model starts to group together similar items. These similar images are presented to the labelers on the same screen to speed up manual tagging. Clustering is especially useful when the labeler views a grid of four, six, or nine images.

Once a machine learning model has been trained on your manually labeled data, the model is truncated to its last fully connected layer. Unlabeled images are then passed through the truncated model in a process commonly known as "embedding" or "featurization." This process embeds each image in a high-dimensional space defined by this model layer. Images that are nearest neighbors in the space are used for clustering tasks.

The clustering phase doesn't appear for object detection models, or for text classification.

### Prelabeling

After submission of enough labels, a classification model is used to predict tags. Or, an object detection model is used to predict bounding boxes. The labeler now sees pages that contain predicted labels already present on each item. For object detection, predicted boxes are also shown. The task involves review of these predictions, and correction of any incorrectly labeled images, before page submission.

Once a machine learning model has been trained on your manually labeled data, the model is evaluated on a test set of manually labeled items, to determine its accuracy at different confidence thresholds. This evaluation process is used to determine a confidence threshold beyond which the model is accurate enough to show pre-labels. The model is then evaluated against unlabeled data. Items with predictions more confident than this threshold are used for pre-labeling.

## Initialize the image labeling project

[!INCLUDE [initialize](../../includes/machine-learning-data-labeling-initialize.md)]

## Run and monitor the project

[!INCLUDE [run](../../includes/machine-learning-data-labeling-run.md)]

### Dashboard

The **Dashboard** tab shows the progress of the labeling task.

:::image type="content" source="./media/how-to-create-labeling-projects/labeling-dashboard.png" alt-text="Data labeling dashboard":::

The progress charts show how many items have been labeled, skipped, need review, or not yet complete. Hover over the chart to see the number of items in each section.

Below the chart 's a distribution of the labels for completed tasks. In some project types, an item can have multiple labels. Therefore, the total number of labels can exceed the total number items.

You also see a distribution of labelers, and how many items they've labeled.

Finally, the middle section shows a table with a queue of unassigned tasks. When ML assisted labeling is off, this section shows the number of manual tasks awaiting assignment.
