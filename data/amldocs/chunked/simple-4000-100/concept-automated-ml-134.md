> Testing your models with a test dataset to evaluate generated models is a preview feature. This capability is an [experimental](/python/api/overview/azure/ml/#stable-vs-experimental) preview feature, and may change at any time.

Learn how to [configure AutoML experiments to use test data (preview) with the SDK](how-to-configure-auto-train.md#training-validation-and-test-data) or with the [Azure Machine Learning studio](how-to-use-automated-ml-for-ml-models.md#create-and-run-experiment).


## Feature engineering

Feature engineering is the process of using domain knowledge of the data to create features that help ML algorithms learn better. In Azure Machine Learning, scaling and normalization techniques are applied to facilitate feature engineering. Collectively, these techniques and feature engineering are referred to as featurization.

For automated machine learning experiments, featurization is applied automatically, but can also be customized based on your data. [Learn more about what featurization is included](how-to-configure-auto-features.md#featurization) and how AutoML helps [prevent over-fitting and imbalanced data](concept-manage-ml-pitfalls.md) in your models.  

> [!NOTE]
> Automated machine learning featurization steps (feature normalization, handling missing data,
> converting text to numeric, etc.) become part of the underlying model. When using the model for
> predictions, the same featurization steps applied during training are applied to
> your input data automatically.

### Customize featurization

Additional feature engineering techniques such as, encoding and transforms are also available. 

Enable this setting with:

+ Azure Machine Learning studio: Enable **Automatic featurization** in the **View additional configuration** section [with these steps](how-to-use-automated-ml-for-ml-models.md#customize-featurization).

+ Python SDK: Specify featurization in your [AutoML Job](/python/api/azure-ai-ml/azure.ai.ml.automl) object. Learn more about [enabling featurization](how-to-configure-auto-train.md#data-featurization). 

## <a name="ensemble"></a> Ensemble models

Automated machine learning supports ensemble models, which are enabled by default. Ensemble learning improves machine learning results and predictive performance by combining multiple models as opposed to using single models. The ensemble iterations appear as the final iterations of your job. Automated machine learning uses both voting and stacking ensemble methods for combining models:

* **Voting**: predicts based on the weighted average of predicted class probabilities (for classification tasks) or predicted regression targets (for regression tasks).
* **Stacking**: stacking combines heterogenous models and trains a meta-model based on the output from the individual models. The current default meta-models are LogisticRegression for classification tasks and ElasticNet for regression/forecasting tasks.

The [Caruana ensemble selection algorithm](http://www.niculescu-mizil.org/papers/shotgun.icml04.revised.rev2.pdf) with sorted ensemble initialization is used to decide which models to use within the ensemble. At a high level, this algorithm initializes the ensemble with up to five models with the best individual scores, and verifies that these models are within 5% threshold of the best score to avoid a poor initial ensemble. Then for each ensemble iteration, a new model is added to the existing ensemble and the resulting score is calculated. If a new model improved the existing ensemble score, the ensemble is updated to include the new model.

See the [AutoML package](/python/api/azure-ai-ml/azure.ai.ml.automl) for changing default ensemble settings in automated machine learning.

<a name="use-with-onnx"></a>

## AutoML & ONNX

With Azure Machine Learning, you can use automated ML to build a Python model and have it converted to the ONNX format. Once the models are in the ONNX format, they can be run on a variety of platforms and devices. Learn more about [accelerating ML models with ONNX](concept-onnx.md).
