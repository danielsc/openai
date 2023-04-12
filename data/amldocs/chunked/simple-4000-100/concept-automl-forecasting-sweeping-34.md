AutoML has two validation configurations - cross-validation and explicit validation data. In the cross-validation case, AutoML uses the input configuration to create data splits into training and validation folds. Time order must be preserved in these splits, so AutoML uses so-called **Rolling Origin Cross Validation** which divides the series into training and validation data using an origin time point. Sliding the origin in time generates the cross-validation folds. Each validation fold contains the next horizon of observations immediately following the position of the origin for the given fold. This strategy preserves the time series data integrity and mitigates the risk of information leakage.  

:::image type="content" source="media/how-to-auto-train-forecast/rolling-origin-cross-validation.png" alt-text="Diagram showing cross validation folds separating the training and validation sets based on the cross validation step size.":::

AutoML follows the usual cross-validation procedure, training a separate model on each fold and averaging validation metrics from all folds. 

Cross-validation for forecasting jobs is configured by setting the number of cross-validation folds and, optionally, the number of time periods between two consecutive cross-validation folds. See the [custom cross-validation settings](./how-to-auto-train-forecast.md#custom-cross-validation-settings) guide for more information and an example of configuring cross-validation for forecasting.

You can also bring your own validation data. Learn more in the [configure data splits and cross-validation in AutoML](how-to-configure-cross-validation-data-splits.md#provide-validation-data) article.

## Next steps
* Learn more about [how to set up AutoML to train a time-series forecasting model](./how-to-auto-train-forecast.md).
* Browse [AutoML Forecasting Frequently Asked Questions](./how-to-automl-forecasting-faq.md).
* Learn about [calendar features for time series forecasting in AutoML](./concept-automl-forecasting-calendar-features.md).
* Learn about [how AutoML uses machine learning to build forecasting models](./concept-automl-forecasting-methods.md).
