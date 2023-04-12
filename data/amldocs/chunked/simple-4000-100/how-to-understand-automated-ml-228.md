For forecasting experiments, the forecast horizon chart plots the relationship between the models predicted value and the actual values mapped over time per cross validation fold, up to 5 folds. The x axis maps time based on the frequency you provided during training setup. The vertical line in the chart marks the forecast horizon point also referred to as the horizon line, which is the time period at which you would want to start generating predictions. To the left of the forecast horizon line, you can view historic training data to better visualize past trends. To the right of the forecast horizon, you can visualize the predictions (the purple line) against the actuals (the blue line) for the different cross validation folds and time series identifiers. The shaded purple area indicates the confidence intervals or variance of predictions around that mean. 

You can choose which cross validation fold and time series identifier combinations to display by clicking the edit pencil icon on the top right corner of the chart. Select from the first 5 cross validation folds and up to 20 different time series identifiers to visualize the chart for your various time series.  

> [!IMPORTANT]
> This chart is only available for models generated from training and validation data. We allow up to 20 data points before and up to 80 data points after the forecast origin. Visuals for models based on test data are not supported at this time. 

![Forecast horizon chart](./media/how-to-understand-automated-ml/forecast-horizon.png)

## Metrics for image models (preview)

Automated ML uses the images from the validation dataset for evaluating the performance of the model. The performance of the model is measured at an **epoch-level** to understand how the training progresses. An epoch elapses when an entire dataset is passed forward and backward through the neural network exactly once. 

### Image classification metrics

The primary metric for evaluation is **accuracy** for binary and multi-class classification models and **IoU** ([Intersection over Union](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score)) for multilabel classification models.
The classification metrics for image classification models are same as those defined in the [classification metrics](#classification-metrics) section. The loss values associated with an epoch are also logged which can help monitor how the training progresses and determine if the model is over-fitting or under-fitting.

Every prediction from a classification model is associated with a confidence score, which indicates the level of confidence with which the prediction was made. Multilabel image classification models are by default evaluated with a score threshold of 0.5 which means only predictions with at least this level of confidence will be considered as a positive prediction for the associated class. Multiclass classification does not use a score threshold but instead, the class with the maximum confidence score is considered as the prediction. 

#### Epoch-level metrics for image classification
Unlike the classification metrics for tabular datasets, image classification models log all the classification metrics at an epoch-level as shown below.

![Epoch-level charts for image classification](./media/how-to-understand-automated-ml/image-classification-accuracy.png)

#### Summary metrics for image classification

Apart from the scalar metrics that are logged at the epoch level, image classification model also log summary metrics like [confusion matrix](#confusion-matrix), [classification charts](#roc-curve) including ROC curve, precision-recall curve and classification report for the model from the best epoch at which we get the highest primary metric (accuracy) score.

Classification report provides the class-level values for metrics like precision, recall, f1-score, support, auc and average_precision with  various level of averaging - micro, macro and weighted as shown below.
