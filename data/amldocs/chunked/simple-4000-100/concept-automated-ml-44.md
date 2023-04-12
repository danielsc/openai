ML professionals and developers across industries can use automated ML to:
+ Implement ML solutions without extensive programming knowledge
+ Save time and resources
+ Leverage data science best practices
+ Provide agile problem-solving

### Classification

Classification is a type of supervised learning in which models learn using training data, and apply those learnings to new data. Azure Machine Learning offers featurizations specifically for these tasks, such as deep neural network text featurizers for classification. Learn more about [featurization options](how-to-configure-auto-train.md#data-featurization). You can also find the list of algorithms supported by AutoML [here](how-to-configure-auto-train.md#supported-algorithms). 

The main goal of classification models is to predict which categories new data will fall into based on learnings from its training data. Common classification examples include fraud detection, handwriting recognition, and object detection. 

See an example of classification and automated machine learning in this Python notebook: [Bank Marketing](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs/automl-classification-task-bankmarketing/automl-classification-task-bankmarketing.ipynb).

### Regression

Similar to classification, regression tasks are also a common supervised learning task. AzureML offers featurization specific to regression problems. Learn more about [featurization options](how-to-configure-auto-train.md#data-featurization). You can also find the list of algorithms supported by AutoML [here](how-to-configure-auto-train.md#supported-algorithms). 

Different from classification where predicted output values are categorical, regression models predict numerical output values based on independent predictors. In regression, the objective is to help establish the relationship among those independent predictor variables by estimating how one variable impacts the others. For example, automobile price based on features like, gas mileage, safety rating, etc. 

See an example of regression and automated machine learning for predictions in these Python notebooks: [Hardware Performance](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs/automl-regression-task-hardware-performance/automl-regression-task-hardware-performance.ipynb).


### Time-series forecasting

Building forecasts is an integral part of any business, whether it's revenue, inventory, sales, or customer demand. You can use automated ML to combine techniques and approaches and get a recommended, high-quality time-series forecast. You can find the list of algorithms supported by AutoML [here](how-to-configure-auto-train.md#supported-algorithms). 

An automated time-series experiment is treated as a multivariate regression problem. Past time-series values are "pivoted" to become additional dimensions for the regressor together with other predictors. This approach, unlike classical time series methods, has an advantage of naturally incorporating multiple contextual variables and their relationship to one another during training. Automated ML learns a single, but often internally branched model for all items in the dataset and prediction horizons. More data is thus available to estimate model parameters and generalization to unseen series becomes possible.

Advanced forecasting configuration includes:
* holiday detection and featurization
* time-series and DNN learners (Auto-ARIMA, Prophet, ForecastTCN)
* many models support through grouping
* rolling-origin cross validation
* configurable lags
* rolling window aggregate features

See an example of forecasting and automated machine learning in this Python notebook: [Energy Demand](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs/automl-forecasting-task-energy-demand/automl-forecasting-task-energy-demand-advanced.ipynb).

### Computer vision

Support for computer vision tasks allows you to easily generate models trained on image data for scenarios like image classification and object detection. 
