
Here's a scorecard-generation configuration file as a classification example:

```yml
{
  "Model": {
    "ModelName": "Housing Price Range Prediction",
    "ModelType": "Classification",
    "ModelSummary": "This model is a classifier that predicts whether the house will sell for more than the median price."
  },
  "Metrics" :{
    "accuracy_score": {
        "threshold": ">=0.85"
    },
  }
  "FeatureImportance": { 
    "top_n": 6 
  }, 
  "DataExplorer": { 
    "features": [ 
      "YearBuilt", 
      "OverallQual", 
      "GarageCars"
    ] 
  },
  "Fairness": {
    "metric": ["accuracy_score", "selection_rate"],
    "sensitive_features": ["YOUR SENSITIVE ATTRIBUTE"],
    "fairness_evaluation_kind": "difference OR ratio"
  }
}
```

### Definition of inputs for the Responsible AI scorecard component

This section lists and defines the parameters that are required to configure the Responsible AI scorecard component.

#### Model

| ModelName | Name of model |
|---|---|
| `ModelType` | Values in ['classification', 'regression']. |
| `ModelSummary` | Enter text that summarizes what the model is for. |

> [!NOTE]
> For multi-class classification, you should first use the One-vs-Rest strategy to choose your reference class, and then split your multi-class classification model into a binary classification problem for your selected reference class versus the rest of the classes.

#### Metrics

| Performance metric | Definition | Model type |
|---|---|---|
| `accuracy_score` | The fraction of data points that are classified correctly. | Classification |
| `precision_score` | The fraction of data points that are classified correctly among those classified as 1. | Classification |
| `recall_score` | The fraction of data points that are classified correctly among those whose true label is 1. Alternative names: true positive rate, sensitivity. | Classification |
| `f1_score` | The F1 score is the harmonic mean of precision and recall. | Classification |
| `error_rate` | The proportion of instances that are misclassified over the whole set of instances. | Classification |
| `mean_absolute_error` | The average of absolute values of errors. More robust to outliers than `mean_squared_error`. | Regression |
| `mean_squared_error` | The average of squared errors. | Regression |
| `median_absolute_error` | The median of squared errors. | Regression |
| `r2_score` | The fraction of variance in the labels explained by the model. | Regression |

Threshold: The desired threshold for the selected metric. Allowed mathematical tokens are >, <, >=, and <=m, followed by a real number. For example, >= 0.75 means that the target for the selected metric is greater than or equal to 0.75.

#### Feature importance

top_n: The number of features to show, with a maximum of 10. Positive integers up to 10 are allowed.

#### Fairness

| Metric | Definition |
|--|--|
| `metric` | The primary metric for evaluation fairness. |
| `sensitive_features` | A list of feature names from the input dataset to be designated as sensitive features for the fairness report. |
| `fairness_evaluation_kind` | Values in ['difference', 'ratio']. |
| `threshold` | The *desired target values* of the fairness evaluation. Allowed mathematical tokens are >, <, >=,  and <=, followed by a real number.<br>For example, metric="accuracy", fairness_evaluation_kind="difference".<br><= 0.05 means that the target for the difference in accuracy is less than or equal to 0.05. |

> [!NOTE]
> Your choice of `fairness_evaluation_kind` (selecting 'difference' versus 'ratio') affects the scale of your target value. In your selection, be sure to choose a meaningful target value.

You can select from the following metrics, paired with `fairness_evaluation_kind`, to configure your fairness assessment component of the scorecard:

| Metric | fairness_evaluation_kind | Definition | Model type |
|---|---|---|---|
| `accuracy_score` | difference | The maximum difference in accuracy score between any two groups. | Classification |
