### ROC curve for a bad model
![ROC curve for a bad model](./media/how-to-understand-automated-ml/chart-roc-curve-bad.png)

## Precision-recall curve

The precision-recall curve plots the relationship between precision and recall as the decision threshold changes. Recall is the ability of a model to detect all positive samples and precision is the ability of a model to avoid labeling negative samples as positive. Some business problems might require higher recall and some higher precision depending on the relative importance of avoiding false negatives vs false positives.
> [!TIP]
> For classification experiments, each of the line charts produced for automated ML models can be used to evaluate the model per-class or averaged over all classes. You can switch between these different views by clicking on class labels in the legend to the right of the chart.
### Precision-recall curve for a good model
![Precision-recall curve for a good model](./media/how-to-understand-automated-ml/chart-precision-recall-curve-good.png)

### Precision-recall curve for a bad model
![Precision-recall curve for a bad model](./media/how-to-understand-automated-ml/chart-precision-recall-curve-bad.png)

## Cumulative gains curve

The cumulative gains curve plots the percent of positive samples correctly classified as a function of the percent of samples considered where we consider samples in the order of predicted probability.

To calculate gain, first sort all samples from highest to lowest probability predicted by the model. Then take `x%` of the highest confidence predictions. Divide the number of positive samples detected in that `x%` by the total number of positive samples to get the gain. Cumulative gain is the percent of positive samples we detect when considering some percent of the data that is most likely to belong to the positive class.

A perfect model will rank all positive samples above all negative samples giving a cumulative gains curve made up of two straight segments. The first is a line with slope `1 / x` from `(0, 0)` to `(x, 1)` where `x` is the fraction of samples that belong to the positive class (`1 / num_classes` if classes are balanced). The second is a horizontal line from `(x, 1)` to `(1, 1)`. In the first segment, all positive samples are classified correctly and cumulative gain goes to `100%` within the first `x%` of samples considered.

The baseline random model will have a cumulative gains curve following `y = x` where for `x%` of samples considered only about `x%` of the total positive samples were detected. A perfect model for a balanced dataset will have a micro average curve and a macro average line that has slope `num_classes` until cumulative gain is 100% and then horizontal until the data percent is 100.
> [!TIP]
> For classification experiments, each of the line charts produced for automated ML models can be used to evaluate the model per-class or averaged over all classes. You can switch between these different views by clicking on class labels in the legend to the right of the chart.
### Cumulative gains curve for a good model
![Cumulative gains curve for a good model](./media/how-to-understand-automated-ml/chart-cumulative-gains-curve-good.png)

### Cumulative gains curve for a bad model
![Cumulative gains curve for a bad model](./media/how-to-understand-automated-ml/chart-cumulative-gains-curve-bad.png)

## Lift curve

The lift curve shows how many times better a model performs compared to a random model. Lift is defined as the ratio of cumulative gain to the cumulative gain of a random model (which should always be `1`).

This relative performance takes into account the fact that classification gets harder as you increase the number of classes. (A random model incorrectly predicts a higher fraction of samples from a dataset with 10 classes compared to a dataset with two classes)

The baseline lift curve is the `y = 1` line where the model performance is consistent with that of a random model. In general, the lift curve for a good model will be higher on that chart and farther from the x-axis, showing that when the model is most confident in its predictions it performs many times better than random guessing.
