# Example pipelines & datasets for Azure Machine Learning designer

Use the built-in examples in Azure Machine Learning designer to quickly get started building your own machine learning pipelines. The Azure Machine Learning designer [GitHub repository](https://github.com/Azure/MachineLearningDesigner) contains detailed documentation to help you understand some common  machine learning scenarios.

## Prerequisites

* An Azure subscription. If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/)
* An Azure Machine Learning workspace 

[!INCLUDE [machine-learning-missing-ui](../../includes/machine-learning-missing-ui.md)]

## Use sample pipelines

The designer saves a copy of the sample pipelines to your studio workspace. You can edit the pipeline to adapt it to your needs and save it as your own. Use them as a starting point to jumpstart your projects.

Here's how to use a designer sample:

1. Sign in to <a href="https://ml.azure.com?tabs=jre" target="_blank">ml.azure.com</a>, and select the workspace you want to work with.

1. Select **Designer**.

1. Select a sample pipeline under the **New pipeline** section.

    Select **Show more samples** for a complete list of samples.

1. To run a pipeline, you first have to set default compute target to run the pipeline on.

   1. In the **Settings** pane to the right of the canvas, select **Select compute target**.

   1. In the dialog that appears, select an existing compute target or create a new one. Select **Save**.

   1. Select **Submit** at the top of the canvas to submit a pipeline job.

   Depending on the sample pipeline and compute settings, jobs may take some time to complete. The default compute settings have a minimum node size of 0, which means that the designer must allocate resources after being idle. Repeated pipeline jobs will take less time since the compute resources are already allocated. Additionally, the designer uses cached results for each component to further improve efficiency.


1. After the pipeline finishes running, you can review the pipeline and view the output for each component to learn more. Use the following steps to view component outputs:

   1. Right-click the component in the canvas whose output you'd like to see.
   1. Select **Visualize**.


   Use the samples as starting points for some of the most common machine learning scenarios.

## Regression

Explore these built-in regression samples.

| Sample title | Description | 
| --- | --- |
| [Regression - Automobile Price Prediction (Basic)](https://github.com/Azure/MachineLearningDesigner/blob/master/articles/samples/regression-automobile-price-prediction-basic.md) | Predict car prices using linear regression. |
| [Regression - Automobile Price Prediction (Advanced)](https://github.com/Azure/MachineLearningDesigner/blob/master/articles/samples/regression-automobile-price-prediction-compare-algorithms.md) | Predict car prices using decision forest and boosted decision tree regressors. Compare models to find the best algorithm.

## Classification

Explore these built-in classification samples. You can learn more about the samples by opening the samples and viewing the component comments in the designer.

| Sample title | Description | 
| --- | --- |
| [Binary Classification with Feature Selection - Income Prediction](https://github.com/Azure/MachineLearningDesigner/blob/master/articles/samples/binary-classification-feature-selection-income-prediction.md) | Predict income as high or low, using a two-class boosted decision tree. Use Pearson correlation to select features.
| [Binary Classification with custom Python script - Credit Risk Prediction](https://github.com/Azure/MachineLearningDesigner/blob/master/articles/samples/binary-classification-python-credit-prediction.md) | Classify credit applications as high or low risk. Use the Execute Python Script component to weight your data.
| [Binary Classification - Customer Relationship Prediction](https://github.com/Azure/MachineLearningDesigner/blob/master/articles/samples/binary-classification-customer-relationship-prediction.md) | Predict customer churn using two-class boosted decision trees. Use SMOTE to sample biased data.
