
# Evaluate automated machine learning experiment results

In this article, learn how to evaluate and compare models trained by your automated machine learning (automated ML) experiment. Over the course of an automated ML experiment, many jobs are created and each job creates a model. For each model, automated ML generates evaluation metrics and charts that help you measure the model's performance. 

For example, automated ML generates the following charts based on experiment type.

| Classification| Regression/forecasting |
| ----------------------------------------------------------- | --------------------------------------------------------|
| [Confusion matrix](#confusion-matrix)                       | [Residuals histogram](#residuals)                       |
| [Receiver operating characteristic (ROC) curve](#roc-curve) | [Predicted vs. true](#predicted-vs-true)                |
| [Precision-recall (PR) curve](#precision-recall-curve)      | [Forecast horizon (preview)](#forecast-horizon-preview) |
| [Lift curve](#lift-curve)                                   |                                                         |
| [Cumulative gains curve](#cumulative-gains-curve)           |                                                         |
| [Calibration curve](#calibration-curve)                     |                     


## Prerequisites

- An Azure subscription. (If you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free/) before you begin)
- An Azure Machine Learning experiment created with either:
  - The [Azure Machine Learning studio](how-to-use-automated-ml-for-ml-models.md) (no code required)
  - The [Azure Machine Learning Python SDK](how-to-configure-auto-train.md)

## View job results

After your automated ML experiment completes, a history of the jobs can be found via:
  - A browser with [Azure Machine Learning studio](https://ml.azure.com)
  - A Jupyter notebook using the [JobDetails Jupyter widget](/python/api/azureml-widgets/azureml.widgets.rundetails)

The following steps and video, show you how to view the run history and model evaluation metrics and charts in the studio:

1. [Sign into the studio](https://ml.azure.com/) and navigate to your workspace.
1. In the left menu, select **Runs**.
1. Select your experiment from the list of experiments.
1. In the table at the bottom of the page, select an automated ML job.
1. In the **Models** tab, select the **Algorithm name** for the model you want to evaluate.
1. In the **Metrics** tab, use the checkboxes on the left to view metrics and charts.

## Classification metrics

Automated ML calculates performance metrics for each classification model generated for your experiment. These metrics are based on the scikit learn implementation. 

Many classification metrics are defined for binary classification on two classes, and require averaging over classes to produce one score for multi-class classification. Scikit-learn provides several averaging methods, three of which automated ML exposes: **macro**, **micro**, and **weighted**.

- **Macro** - Calculate the metric for each class and take the unweighted average
- **Micro** - Calculate the metric globally by counting the total true positives, false negatives, and false positives (independent of classes).
- **Weighted** - Calculate the metric for each class and take the weighted average based on the number of samples per class.

While each averaging method has its benefits, one common consideration when selecting the appropriate method is class imbalance. If classes have different numbers of samples, it might be more informative to use a macro average where minority classes are given equal weighting to majority classes. Learn more about [binary vs multiclass metrics in automated ML](#binary-vs-multiclass-classification-metrics). 

The following table summarizes the model performance metrics that automated ML calculates for each classification model generated for your experiment. For more detail, see the scikit-learn documentation linked in the **Calculation** field of each metric. 
