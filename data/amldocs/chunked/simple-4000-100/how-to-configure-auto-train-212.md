Learn about the specific definitions of these metrics in [Understand automated machine learning results](how-to-understand-automated-ml.md).

#### Metrics for classification multi-class scenarios 

These metrics apply for all classification scenarios, including tabular data, images/computer-vision and NLP-Text.

Threshold-dependent metrics, like `accuracy`, `recall_score_weighted`, `norm_macro_recall`, and `precision_score_weighted` may not optimize as well for datasets that are small, have large class skew (class imbalance), or when the expected metric value is very close to 0.0 or 1.0. In those cases, `AUC_weighted` can be a better choice for the primary metric. After automated ML completes, you can choose the winning model based on the metric best suited to your business needs.

| Metric | Example use case(s) |
| ------ | ------- |
| `accuracy` | Image classification, Sentiment analysis, Churn prediction |
| `AUC_weighted` | Fraud detection, Image classification, Anomaly detection/spam detection |
| `average_precision_score_weighted` | Sentiment analysis |
| `norm_macro_recall` | Churn prediction |
| `precision_score_weighted` |  |

#### Metrics for classification multi-label scenarios 

- For Text classification, multi-label currently 'Accuracy' is the only primary metric supported.

- For Image classification multi-label, the primary metrics supported are defined in the ClassificationMultilabelPrimaryMetrics Enum

#### Metrics for NLP Text NER (Named Entity Recognition) scenarios 

- For NLP Text NER (Named Entity Recognition) currently 'Accuracy' is the only primary metric supported.

#### Metrics for regression scenarios

`r2_score`, `normalized_mean_absolute_error` and `normalized_root_mean_squared_error` are all trying to minimize prediction errors. `r2_score` and `normalized_root_mean_squared_error` are both minimizing average squared errors while `normalized_mean_absolute_error` is minizing the average absolute value of errors. Absolute value treats errors at all magnitudes alike and squared errors will have a much larger penalty for errors with larger absolute values. Depending on whether larger errors should be punished more or not, one can choose to optimize squared error or absolute error.

The main difference between `r2_score` and `normalized_root_mean_squared_error` is the way they're normalized and their meanings. `normalized_root_mean_squared_error` is root mean squared error normalized by range and can be interpreted as the average error magnitude for prediction. `r2_score` is mean squared error normalized by an estimate of variance of data. It's the proportion of variation that can be captured by the model. 

> [!Note]
> `r2_score` and `normalized_root_mean_squared_error` also behave similarly as primary metrics. If a fixed validation set is applied, these two metrics are optimizing the same target, mean squared error, and will be optimized by the same model. When only a training set is available and cross-validation is applied, they would be slightly different as the normalizer for `normalized_root_mean_squared_error` is fixed as the range of training set, but the normalizer for `r2_score` would vary for every fold as it's the variance for each fold.

If the rank, instead of the exact value is of interest, `spearman_correlation` can be a better choice as it measures the rank correlation between real values and predictions.

However, currently no primary metrics for regression addresses relative difference. All of `r2_score`, `normalized_mean_absolute_error`, and `normalized_root_mean_squared_error` treat a $20k prediction error the same for a worker with a $30k salary as a worker making $20M, if these two data points belongs to the same dataset for regression, or the same time series specified by the time series identifier. While in reality, predicting only $20k off from a $20M salary is very close (a small 0.1% relative difference), whereas $20k off from $30k isn't close (a large 67% relative difference). To address the issue of relative difference, one can train a model with available primary metrics, and then select the model with best `mean_absolute_percentage_error` or `root_mean_squared_log_error`.
