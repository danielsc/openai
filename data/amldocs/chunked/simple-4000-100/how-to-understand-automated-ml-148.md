The baseline lift curve is the `y = 1` line where the model performance is consistent with that of a random model. In general, the lift curve for a good model will be higher on that chart and farther from the x-axis, showing that when the model is most confident in its predictions it performs many times better than random guessing.

> [!TIP]
> For classification experiments, each of the line charts produced for automated ML models can be used to evaluate the model per-class or averaged over all classes. You can switch between these different views by clicking on class labels in the legend to the right of the chart.
### Lift curve for a good model
![Lift curve for a good model](./media/how-to-understand-automated-ml/chart-lift-curve-good.png)
 
### Lift curve for a bad model
![Lift curve for a bad model](./media/how-to-understand-automated-ml/chart-lift-curve-bad.png)

## Calibration curve

The calibration curve plots a model's confidence in its predictions against the proportion of positive samples at each confidence level. A well-calibrated model will correctly classify 100% of the predictions to which it assigns 100% confidence, 50% of the predictions it assigns 50% confidence, 20% of the predictions it assigns a 20% confidence, and so on. A perfectly calibrated model will have a calibration curve following the `y = x` line where the model perfectly predicts the probability that samples belong to each class.

An over-confident model will over-predict probabilities close to zero and one, rarely being uncertain about the class of each sample and the calibration curve will look similar to backward "S". An under-confident model will assign a lower probability on average to the class it predicts and the associated calibration curve will look similar to an "S". The calibration curve does not depict a model's ability to classify correctly, but instead its ability to correctly assign confidence to its predictions. A bad model can still have a good calibration curve if the model correctly assigns low confidence and high uncertainty.

> [!NOTE]
> The calibration curve is sensitive to the number of samples, so a small validation set can produce noisy results that can be hard to interpret. This does not necessarily mean that the model is not well-calibrated.

### Calibration curve for a good model
![Calibration curve for a good model](./media/how-to-understand-automated-ml/chart-calibration-curve-good.png)

### Calibration curve for a bad model
![Calibration curve for a bad model](./media/how-to-understand-automated-ml/chart-calibration-curve-bad.png)

## Regression/forecasting metrics

Automated ML calculates the same performance metrics for each  model generated, regardless if it is a regression or forecasting experiment. These metrics also undergo normalization to enable comparison between models trained on data with different ranges. To learn more, see [metric normalization](#metric-normalization).  

The following table summarizes the model performance metrics generated for regression and forecasting experiments. Like classification metrics, these metrics are also based on the scikit learn implementations. The appropriate scikit learn documentation is linked accordingly, in the **Calculation** field.

|Metric|Description|Calculation|
--|--|--|
explained_variance|Explained variance measures the extent to which a model accounts for the variation in the target variable. It is the percent decrease in variance of the original data to the variance of the errors. When the mean of the errors is 0, it is equal to the coefficient of determination (see r2_score below). <br> <br> **Objective:** Closer to 1 the better <br> **Range:** (-inf, 1]|[Calculation](https://scikit-learn.org/0.22/modules/generated/sklearn.metrics.explained_variance_score.html)|
mean_absolute_error|Mean absolute error is the expected value of absolute value of difference between the target and the prediction.<br><br> **Objective:** Closer to 0 the better <br> **Range:** [0, inf) <br><br> Types: <br>`mean_absolute_error` <br>  `normalized_mean_absolute_error`,  the mean_absolute_error divided by the range of the data. | [Calculation](https://scikit-learn.org/0.22/modules/generated/sklearn.metrics.mean_absolute_error.html)|
