Automated ML normalizes regression and forecasting metrics which enable comparison between models trained on data with different ranges. A model trained on a data with a larger range has higher error than the same model trained on data with a smaller range, unless that error is normalized.

While there is no standard method of normalizing error metrics, automated ML takes the common approach of dividing the error by the range of the data: `normalized_error = error / (y_max - y_min)`

>[!Note]
>The range of data is not saved with the model. If you do inference with the same model on a holdout test set, `y_min` and `y_max` may change according to the test data and the normalized metrics may not be directly used to compare the model's performance on training and test sets. You can pass in the value of `y_min` and `y_max` from your training set to make the comparison fair.

When evaluating a forecasting model on time series data, automated ML takes extra steps to ensure that normalization happens per time series ID (grain), because each time series likely has a different distribution of target values.
## Residuals

The residuals chart is a histogram of the prediction errors (residuals) generated for regression and forecasting experiments. Residuals are calculated as `y_predicted - y_true` for all samples and then displayed as a histogram to show model bias.

In this example, note that both models are slightly biased to predict lower than the actual value. This is not uncommon for a dataset with a skewed distribution of actual targets, but indicates worse model performance. A good model will have a residuals distribution that peaks at zero with few residuals at the extremes. A worse model will have a spread out residuals distribution with fewer samples around zero.

### Residuals chart for a good model
![Residuals chart for a good model](./media/how-to-understand-automated-ml/chart-residuals-good.png)

### Residuals chart for a bad model
![Residuals chart for a bad model](./media/how-to-understand-automated-ml/chart-residuals-bad.png)

## Predicted vs. true

For regression and forecasting experiment the predicted vs. true chart plots the relationship between the target feature (true/actual values) and the model's predictions. The true values are binned along the x-axis and for each bin the mean predicted value is plotted with error bars. This allows you to see if a model is biased toward predicting certain values. The line displays the average prediction and the shaded area indicates the variance of predictions around that mean.

Often, the most common true value will have the most accurate predictions with the lowest variance. The distance of the trend line from the ideal `y = x` line where there are few true values is a good measure of model performance on outliers. You can use the histogram at the bottom of the chart to reason about the actual data distribution. Including more data samples where the distribution is sparse can improve model performance on unseen data.

In this example, note that the better model has a predicted vs. true line that is closer to the ideal `y = x` line.

### Predicted vs. true chart for a good model
![Predicted vs. true chart for a good model](./media/how-to-understand-automated-ml/chart-predicted-true-good.png)

### Predicted vs. true chart for a bad model
![Predicted vs. true chart for a bad model](./media/how-to-understand-automated-ml/chart-predicted-true-bad.png)

## Forecast horizon (preview)

For forecasting experiments, the forecast horizon chart plots the relationship between the models predicted value and the actual values mapped over time per cross validation fold, up to 5 folds. The x axis maps time based on the frequency you provided during training setup. The vertical line in the chart marks the forecast horizon point also referred to as the horizon line, which is the time period at which you would want to start generating predictions. To the left of the forecast horizon line, you can view historic training data to better visualize past trends. To the right of the forecast horizon, you can visualize the predictions (the purple line) against the actuals (the blue line) for the different cross validation folds and time series identifiers. The shaded purple area indicates the confidence intervals or variance of predictions around that mean. 
