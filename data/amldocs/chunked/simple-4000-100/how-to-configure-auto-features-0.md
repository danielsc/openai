
# Data featurization in automated machine learning

[!INCLUDE [sdk v1](../../includes/machine-learning-sdk-v1.md)]

Learn about the data featurization settings in Azure Machine Learning, and how to customize those features for [automated machine learning experiments](concept-automated-ml.md).

## Feature engineering and featurization

Training data consists of rows and columns. Each row is an observation or record, and the columns of each row are the features that describe each record. Typically, the features that best characterize the patterns in the data are selected to create predictive models.

Although many of the raw data fields can be used directly to train a model, it's often necessary to create additional (engineered) features that provide information that  better differentiates patterns in the data. This process is called **feature engineering**, where the use of domain knowledge of the data is leveraged to create features that, in turn, help machine learning algorithms to learn better. 

In Azure Machine Learning, data-scaling and normalization techniques are applied to make feature engineering easier. Collectively, these techniques and this feature engineering are called **featurization** in automated ML experiments.

## Prerequisites

This article assumes that you already know how to configure an automated ML experiment. 

[!INCLUDE [automl-sdk-version](../../includes/machine-learning-automl-sdk-version.md)]

For information about configuration, see the following articles:

- For a code-first experience: [Configure automated ML experiments by using the Azure Machine Learning SDK for Python](how-to-configure-auto-train.md).
- For a low-code or no-code experience: [Create, review, and deploy automated machine learning models by using the Azure Machine Learning studio](how-to-use-automated-ml-for-ml-models.md).

## Configure featurization

In every automated machine learning experiment, [automatic scaling and normalization techniques](#featurization) are applied to your data by default. These techniques are types of featurization that help *certain* algorithms that are sensitive to features on different scales. You can enable more featurization, such as *missing-values imputation*, *encoding*, and *transforms*.

> [!NOTE]
> Steps for automated machine learning featurization (such as feature normalization, handling missing data,
> or converting text to numeric) become part of the underlying model. When you use the model for
> predictions, the same featurization steps that are applied during training are applied to
> your input data automatically.

For experiments that you configure with the Python SDK, you can enable or disable the featurization setting and further specify the featurization steps to be used for your experiment. If you're using the Azure Machine Learning studio, see the [steps to enable featurization](how-to-use-automated-ml-for-ml-models.md#customize-featurization).

The following table shows the accepted settings for `featurization` in the [AutoMLConfig class](/python/api/azureml-train-automl-client/azureml.train.automl.automlconfig.automlconfig):

|Featurization configuration | Description|
------------- | ------------- |
|`"featurization": 'auto'`| Specifies that, as part of preprocessing, [data guardrails](#data-guardrails) and [featurization steps](#featurization) are to be done automatically. This setting is the default.|
|`"featurization": 'off'`| Specifies that featurization steps are not to be done automatically.|
|`"featurization":`&nbsp;`'FeaturizationConfig'`| Specifies that customized featurization steps are to be used. [Learn how to customize featurization](#customize-featurization).|

<a name="featurization"></a>

## Automatic featurization

The following table summarizes techniques that are automatically applied to your data. These techniques are applied for experiments that are configured by using the SDK or the studio UI. To disable this behavior, set `"featurization": 'off'` in your `AutoMLConfig` object.
