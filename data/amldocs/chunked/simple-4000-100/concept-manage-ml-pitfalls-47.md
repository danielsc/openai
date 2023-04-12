**Target leakage** is a similar issue, where you may not see overfitting between train/test sets, but rather it appears at prediction-time. Target leakage occurs when your model "cheats" during training by having access to data that it shouldn't normally have at prediction-time. For example, if your problem is to predict on Monday what a commodity price will be on Friday, but one of your features accidentally included data from Thursdays, that would be data the model won't have at prediction-time since it cannot see into the future. Target leakage is an easy mistake to miss, but is often characterized by abnormally high accuracy for your problem. If you are attempting to predict stock price and trained a model at 95% accuracy, there is likely target leakage somewhere in your features.

### Use fewer features

**Removing features** can also help with overfitting by preventing the model from having too many fields to use to memorize specific patterns, thus causing it to be more flexible. It can be difficult to measure quantitatively, but if you can remove features and retain the same accuracy, you have likely made the model more flexible and have reduced the risk of overfitting.

## Best practices automated ML implements

### Regularization and hyperparameter tuning

**Regularization** is the process of minimizing a cost function to penalize complex and overfitted models. There are different types of regularization functions, but in general they all penalize model coefficient size, variance, and complexity. Automated ML uses L1 (Lasso), L2 (Ridge), and ElasticNet (L1 and L2 simultaneously) in different combinations with different model hyperparameter settings that control overfitting. In simple terms, automated ML will vary how much a model is regulated and choose the best result.

### Model complexity limitations

Automated ML also implements explicit **model complexity limitations** to prevent overfitting. In most cases this implementation is specifically for decision tree or forest algorithms, where individual tree max-depth is limited, and the total number of trees used in forest or ensemble techniques are limited.

### Cross-validation

**Cross-validation (CV)** is the process of taking many subsets of your full training data and training a model on each subset. The idea is that a model could get "lucky" and have great accuracy with one subset, but by using many subsets the model won't achieve this high accuracy every time. When doing CV, you provide a validation holdout dataset, specify your CV folds (number of subsets) and automated ML will train your model and tune hyperparameters to minimize error on your validation set. One CV fold could be overfitted, but by using many of them it reduces the probability that your final model is overfitted. The tradeoff is that CV does result in longer training times and thus greater cost, because instead of training a model once, you train it once for each *n* CV subsets. 

> [!NOTE]
> Cross-validation is not enabled by default; it must be configured in automated ML settings. However, after cross-validation is configured and a validation data set has been provided, the process is automated for you. Learn more about [cross validation configuration in Auto ML](how-to-configure-cross-validation-data-splits.md)

<a name="imbalance"></a>

## Identify models with imbalanced data

Imbalanced data is commonly found in data for machine learning classification scenarios, and refers to data that contains a disproportionate ratio of observations in each class. This imbalance can lead to a falsely perceived positive effect of a model's accuracy, because the input data has bias towards one class, which results in the trained model to mimic that bias. 

In addition, automated ML jobs generate the following charts automatically, which can help you understand the correctness of the classifications of your model, and identify models potentially impacted by imbalanced data.

Chart| Description
---|---
[Confusion Matrix](how-to-understand-automated-ml.md#confusion-matrix)| Evaluates the correctly classified labels against the actual labels of the data. 
