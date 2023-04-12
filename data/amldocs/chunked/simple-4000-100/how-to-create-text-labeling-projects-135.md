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
