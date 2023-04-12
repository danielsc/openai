[Support Vector Classification (SVC)](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.classification#supportvectormachine----svm-)* |[Stochastic Gradient Descent (SGD)](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.regression#sgdregressor----sgd-)* | [Arimax](/python/api/azureml-automl-core/azureml.automl.core.shared.constants.supportedmodels.forecasting#arimax----arimax-)
[Random Forest](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.classification#randomforest----randomforest-)* | [Random Forest](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.regression#randomforestregressor----randomforest-) | [LARS Lasso](https://scikit-learn.org/stable/modules/linear_model.html#lars-lasso)
[Extremely Randomized Trees](https://scikit-learn.org/stable/modules/ensemble.html#extremely-randomized-trees)* | [Extremely Randomized Trees](https://scikit-learn.org/stable/modules/ensemble.html#extremely-randomized-trees)* | [Extremely Randomized Trees](https://scikit-learn.org/stable/modules/ensemble.html#extremely-randomized-trees)*
[Xgboost](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.classification#xgboostclassifier----xgboostclassifier-)* |[Xgboost](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.regression#xgboostregressor----xgboostregressor-)* | [Random Forest](https://scikit-learn.org/stable/modules/ensemble.html#random-forests)
[Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html#bernoulli-naive-bayes)* | [Xgboost](https://xgboost.readthedocs.io/en/latest/parameter.html)  | [ForecastTCN](/python/api/azureml-automl-core/azureml.automl.core.shared.constants.supportedmodels.forecasting#tcnforecaster----tcnforecaster-)
[Stochastic Gradient Descent (SGD)](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.classification#sgdclassifier----sgd-)* |[Stochastic Gradient Descent (SGD)](https://scikit-learn.org/stable/modules/sgd.html#regression) | [Gradient Boosting](https://scikit-learn.org/stable/modules/ensemble.html#regression)
||| [ExponentialSmoothing](/python/api/azureml-automl-core/azureml.automl.core.shared.constants.supportedmodels.forecasting#exponentialsmoothing----exponentialsmoothing-)
||| SeasonalNaive
||| Average
||| Naive
||| SeasonalAverage


With additional algorithms below.

* [Image Classification Multi-class Algorithms](how-to-auto-train-image-models.md#supported-model-architectures)
* [Image Classification Multi-label Algorithms](how-to-auto-train-image-models.md#supported-model-architectures)
* [Image Object Detection Algorithms](how-to-auto-train-image-models.md#supported-model-architectures)
* [NLP Text Classification Multi-label Algorithms](how-to-auto-train-nlp-models.md#language-settings)
* [NLP Text Named Entity Recognition (NER) Algorithms](how-to-auto-train-nlp-models.md#language-settings)

Follow [this link](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs) for example notebooks of each task type.

### Primary metric

The `primary_metric` parameter determines the metric to be used during model training for optimization. The available metrics you can select is determined by the task type you choose.

Choosing a primary metric for automated ML to optimize depends on many factors. We recommend your primary consideration be to choose a metric that best represents your business needs. Then consider if the metric is suitable for your dataset profile (data size, range, class distribution, etc.). The following sections summarize the recommended primary metrics based on task type and business scenario. 

Learn about the specific definitions of these metrics in [Understand automated machine learning results](how-to-understand-automated-ml.md).

#### Metrics for classification multi-class scenarios 
