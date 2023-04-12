Before you can submit your automated ML job, you need to determine the kind of machine learning problem you're solving. This problem determines which function your automated ML job uses and what model algorithms it applies.

Automated ML supports tabular data based tasks (classification, regression, forecasting), computer vision tasks (such as Image Classification and Object Detection), and natural language processing tasks (such as Text classification and Entity Recognition tasks). Learn more about [task types](concept-automated-ml.md#when-to-use-automl-classification-regression-forecasting-computer-vision--nlp).


### Supported algorithms

Automated machine learning tries different models and algorithms during the automation and tuning process. As a user, there's no need for you to specify the algorithm. 

The task method determines the list of algorithms/models, to apply. Use the `allowed_training_algorithms` or `blocked_training_algorithms` parameters in the `set_training()` setter function to further modify iterations with the available models to include or exclude. 

In the following list of links you can explore the supported algorithms per machine learning task listed below.

Classification | Regression | Time Series Forecasting
|-- |-- |--
[Logistic Regression](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.classification#logisticregression----logisticregression-)* | [Elastic Net](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.regression#elasticnet----elasticnet-)* | [AutoARIMA](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.forecasting#autoarima----autoarima-)
[Light GBM](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.classification#lightgbmclassifier----lightgbm-)* | [Light GBM](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.regression#lightgbmregressor----lightgbm-)* | [Prophet](/python/api/azureml-automl-core/azureml.automl.core.shared.constants.supportedmodels.forecasting#prophet----prophet-)
[Gradient Boosting](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.classification#gradientboosting----gradientboosting-)* | [Gradient Boosting](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.regression#gradientboostingregressor----gradientboosting-)* | [Elastic Net](https://scikit-learn.org/stable/modules/linear_model.html#elastic-net)
[Decision Tree](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.classification#decisiontree----decisiontree-)* |[Decision Tree](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.regression#decisiontreeregressor----decisiontree-)* |[Light GBM](https://lightgbm.readthedocs.io/en/latest/index.html)
[K Nearest Neighbors](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.classification#knearestneighborsclassifier----knn-)* |[K Nearest Neighbors](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.regression#knearestneighborsregressor----knn-)* | K Nearest Neighbors
[Linear SVC](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.classification#linearsupportvectormachine----linearsvm-)* |[LARS Lasso](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.regression#lassolars----lassolars-)* | [Decision Tree](https://scikit-learn.org/stable/modules/tree.html#regression)
[Support Vector Classification (SVC)](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.classification#supportvectormachine----svm-)* |[Stochastic Gradient Descent (SGD)](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.regression#sgdregressor----sgd-)* | [Arimax](/python/api/azureml-automl-core/azureml.automl.core.shared.constants.supportedmodels.forecasting#arimax----arimax-)
