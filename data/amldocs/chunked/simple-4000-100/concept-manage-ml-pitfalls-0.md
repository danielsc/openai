
# Prevent overfitting and imbalanced data with automated machine learning

Overfitting and imbalanced data are common pitfalls when you build machine learning models. By default, Azure Machine Learning's automated machine learning provides charts and metrics to help you identify these risks, and implements best practices to help mitigate them. 

## Identify overfitting

Overfitting in machine learning occurs when a model fits the training data too well, and as a result can't accurately predict on unseen test data. In other words, the model has simply memorized specific patterns and noise in the training data, but is not flexible enough to make predictions on real data.

Consider the following trained models and their corresponding train and test accuracies.

| Model | Train accuracy | Test accuracy |
|-------|----------------|---------------|
| A | 99.9% | 95% |
| B | 87% | 87% |
| C | 99.9% | 45% |

Considering model **A**, there is a common misconception that if test accuracy on unseen data is lower than training accuracy, the model is overfitted. However, test accuracy should always be less than training accuracy, and the distinction for overfit vs. appropriately fit comes down to *how much* less accurate. 

When comparing models **A** and **B**, model **A** is a better model because it has higher test accuracy, and although the test accuracy is slightly lower at 95%, it is not a significant difference that suggests overfitting is present. You wouldn't choose model **B** simply because the train and test accuracies are closer together.

Model **C** represents a clear case of overfitting; the training accuracy is very high but the test accuracy isn't anywhere near as high. This distinction is subjective, but comes from knowledge of your problem and data, and what magnitudes of error are acceptable.

## Prevent overfitting

In the most egregious cases, an overfitted model assumes that the feature value combinations seen during training will always result in the exact same output for the target.

The best way to prevent overfitting is to follow ML best-practices including:

* Using more training data, and eliminating statistical bias
* Preventing target leakage
* Using fewer features
* **Regularization and hyperparameter optimization**
* **Model complexity limitations**
* **Cross-validation**

In the context of automated ML, the first three items above are **best-practices you implement**. The last three bolded items are **best-practices automated ML implements** by default to protect against overfitting. In settings other than automated ML, all six best-practices are worth following to avoid overfitting models.

## Best practices you implement

### Use more data

Using **more data** is the simplest and best possible way to prevent overfitting, and as an added bonus typically increases accuracy. When you use more data, it becomes harder for the model to memorize exact patterns, and it is forced to reach solutions that are more flexible to accommodate more conditions. It's also important to recognize **statistical bias**, to ensure your training data doesn't include isolated patterns that won't exist in live-prediction data. This scenario can be difficult to solve, because there may not be overfitting between your train and test sets, but there may be overfitting present when compared to live test data.

### Prevent target leakage

**Target leakage** is a similar issue, where you may not see overfitting between train/test sets, but rather it appears at prediction-time. Target leakage occurs when your model "cheats" during training by having access to data that it shouldn't normally have at prediction-time. For example, if your problem is to predict on Monday what a commodity price will be on Friday, but one of your features accidentally included data from Thursdays, that would be data the model won't have at prediction-time since it cannot see into the future. Target leakage is an easy mistake to miss, but is often characterized by abnormally high accuracy for your problem. If you are attempting to predict stock price and trained a model at 95% accuracy, there is likely target leakage somewhere in your features.
