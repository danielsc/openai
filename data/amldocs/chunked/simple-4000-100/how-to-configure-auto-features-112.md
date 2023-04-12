**Memory issues detection** |Passed <br><br><br><br> Done |<br> The selected values (horizon, lag, rolling window) were analyzed, and no potential out-of-memory issues were detected. Learn more about time-series [forecasting configurations](./how-to-auto-train-forecast.md#configuration-settings). <br><br><br>The selected values (horizon, lag, rolling window) were analyzed and will potentially cause your experiment to run out of memory. The lag or rolling-window configurations have been turned off.
**Frequency detection** |Passed <br><br><br><br> Done |<br> The time series was analyzed, and all data points are aligned with the detected frequency. <br> <br> The time series was analyzed, and data points that don't align with the detected frequency were detected. These data points were removed from the dataset.
**Cross validation** |Done| In order to accurately evaluate the model(s) trained by AutoML, we leverage a dataset that the model is not trained on. Hence, if the user doesn't provide an explicit validation dataset, a part of the training dataset is used to achieve this. For smaller datasets (fewer than 20,000 samples), cross-validation is leveraged, else a single hold-out set is split from the training data to serve as the validation dataset. Hence, for your input data we leverage cross-validation with 10 folds, if the number of training samples are fewer than 1000, and 3 folds in all other cases.
**Train-Test data split** |Done| In order to accurately evaluate the model(s) trained by AutoML, we leverage a dataset that the model is not trained on. Hence, if the user doesn't provide an explicit validation dataset, a part of the training dataset is used to achieve this. For smaller datasets (fewer than 20,000 samples), cross-validation is leveraged, else a single hold-out set is split from the training data to serve as the validation dataset. Hence, your input data has been split into a training dataset and a holdout validation dataset.
**Time Series ID detection** |Passed <br><br><br><br> Fixed | <br> The data set was analyzed, and no duplicate time index were detected. <br> <br> Multiple time series were found in the dataset, and the time series identifiers were automatically created for your dataset.
**Time series aggregation** |Passed <br><br><br><br> Fixed | <br> The dataset frequency is aligned with the user specified frequency. No aggregation was performed. <br> <br> The data was aggregated to comply with user provided frequency.
**Short series handling** |Passed <br><br><br><br> Fixed | <br> Automated ML detected enough data points for each series in the input data to continue with training. <br> <br> Automated ML detected that some series did not contain enough data points to train a model. To continue with training, these short series have been dropped or padded.

## Customize featurization

You can customize your featurization settings to ensure that the data and features that are used to train your ML model result in relevant predictions.

To customize featurizations, specify `"featurization": FeaturizationConfig` in your `AutoMLConfig` object. If you're using the Azure Machine Learning studio for your experiment, see the [how-to article](how-to-use-automated-ml-for-ml-models.md#customize-featurization). To customize featurization for forecastings task types, refer to the [forecasting how-to](v1/how-to-auto-train-forecast-v1.md#customize-featurization).

Supported customizations include:

|Customization|Definition|
|--|--|
|**Column purpose update**|Override the autodetected feature type for the specified column.|
|**Transformer parameter update** |Update the parameters for the specified transformer. Currently supports *Imputer* (mean, most frequent, and median) and *HashOneHotEncoder*.|
|**Drop columns** |Specifies columns to drop from being featurized.|
|**Block transformers**| Specifies block transformers to be used in the featurization process.|

>[!NOTE]
> The **drop columns** functionality is deprecated as of SDK version 1.19. Drop columns from your dataset as part of data cleansing, prior to consuming it in your automated ML experiment. 
