- The input data contains **feature columns that are derived from the target with a simple formula**. For example, a feature that is an exact multiple of the target can result in a nearly perfect training score. The model, however, will likely not generalize to out-of-sample data. We advise you to explore the data prior to model training and to drop columns that "leak" the target information.
- The training data uses **features that are not known into the future**, up to the forecast horizon. AutoML's regression models currently assume all features are known to the forecast horizon. We advise you to explore your data prior to training and remove any feature columns that are only known historically.
- There are **significant structural differences - regime changes - between the training, validation, or test portions of the data**. For example, consider the effect of the COVID-19 pandemic on demand for almost any good during 2020 and 2021; this is a classic example of a regime change. Over-fitting due to regime change is the most challenging issue to address because it's highly scenario dependent and can require deep knowledge to identify. As a first line of defense, try to reserve 10 - 20% of the total history for validation, or cross-validation, data. It isn't always possible to reserve this amount of validation data if the training history is short, but is a best practice. See our guide on [configuring validation](./how-to-auto-train-forecast.md#training-and-validation-data) for more information.


## What if my time series data doesn't have regularly spaced observations?

AutoML's forecasting models all require that training data have regularly spaced observations with respect to the calendar. This requirement includes cases like monthly or yearly observations where the number of days between observations may vary. There are two cases where time dependent data may not meet this requirement:

- The data has a well defined frequency, but **there are missing observations that create gaps in the series**. In this case, AutoML will attempt to detect the frequency, fill in new observations for the gaps, and impute missing target and feature values therein. The imputation methods can be optionally configured by the user via SDK settings or through the Web UI. See the [custom featurization](./how-to-auto-train-forecast.md#custom-featurization) 
guide for more information on configuring imputation.

- **The data doesn't have a well defined frequency**. That is, the duration between observations doesn't have a discernible pattern. Transactional data, like that from a point-of-sales system, is one example. In this case, you can set AutoML to aggregate your data to a chosen frequency. You can choose a regular frequency that best suites the data and the modeling objectives. See the [data aggregation](./how-to-auto-train-forecast.md#frequency--target-data-aggregation) section for more information.

## How do I choose the primary metric?

The primary metric is very important since its value on validation data determines the best model during [ sweeping and selection](./concept-automl-forecasting-sweeping.md). **Normalized root mean squared error (NRMSE) or normalized mean absolute error (NMAE) are usually the best choices for the primary metric** in forecasting tasks. To choose between them, note that RMSE penalizes outliers in the training data more than MAE because it uses the square of the error. The NMAE may be a better choice if you want the model to be less sensitive to outliers. See the [regression and forecasting metrics](./how-to-understand-automated-ml.md#regressionforecasting-metrics) guide for more information.

> [!NOTE]
> We do not recommend using the R2 score, or _R_<sup>2</sup>, as a primary metric for forecasting.

> [!NOTE]
> AutoML doesn't support custom, or user-provided functions for the primary metric. You must choose one of the predefined primary metrics that AutoML supports. 

## How can I improve the accuracy of my model?
