| [TruncatedSVDWrapper](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html) |This transformer performs linear dimensionality reduction by means of truncated singular value decomposition (SVD). Contrary to PCA, this estimator does not center the data before computing the singular value decomposition, which means it can work with scipy.sparse matrices efficiently |
| [SparseNormalizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html) | Each sample (that is, each row of the data matrix) with at least one non-zero component is rescaled independently of other samples so that its norm (l1 or l2) equals one |

## Data guardrails

*Data guardrails* help you identify potential issues with your data (for example, missing values or [class imbalance](concept-manage-ml-pitfalls.md#identify-models-with-imbalanced-data)). They also help you take corrective actions for improved results.

Data guardrails are applied:

- **For SDK experiments**: When the parameters `"featurization": 'auto'` or `validation=auto` are specified in your `AutoMLConfig` object.
- **For studio experiments**: When automatic featurization is enabled.

You can review the data guardrails for your experiment:

- By setting `show_output=True` when you submit an experiment by using the SDK.

- In the studio, on the **Data guardrails** tab of your automated ML run.

### Data guardrail states

Data guardrails display one of three states:

|State| Description |
|----|---- |
|**Passed**| No data problems were detected and no action is required by you. |
|**Done**| Changes were applied to your data. We encourage you to review the corrective actions that AutoML took, to ensure that the changes align with the expected results. |
|**Alerted**| A data issue was detected but couldn't be remedied. We encourage you to revise and fix the issue.|

### Supported data guardrails

The following table describes the data guardrails that are currently supported and the associated statuses that you might see when you submit your experiment:

Guardrail|Status|Condition&nbsp;for&nbsp;trigger
---|---|---
**Missing feature values imputation** |Passed <br><br><br> Done| No missing feature values were detected in your training data. Learn more about [missing-value imputation.](./how-to-use-automated-ml-for-ml-models.md#customize-featurization) <br><br> Missing feature values were detected in your training data and were imputed.
**High cardinality feature detection** |Passed <br><br><br> Done| Your inputs were analyzed, and no high-cardinality features were detected. <br><br> High-cardinality features were detected in your inputs and were handled.
**Validation split handling** |Done| The validation configuration was set to `'auto'` and the training data contained *fewer than 20,000 rows*. <br> Each iteration of the trained model was validated by using cross-validation. Learn more about [validation data](./how-to-configure-auto-train.md#training-validation-and-test-data). <br><br> The validation configuration was set to `'auto'`, and the training data contained *more than 20,000 rows*. <br> The input data has been split into a training dataset and a validation dataset for validation of the model.
**Class balancing detection** |Passed <br><br><br><br>Alerted <br><br><br>Done | Your inputs were analyzed, and all classes are balanced in your training data. A dataset is considered to be balanced if each class has good representation in the dataset, as measured by number and ratio of samples. <br><br> Imbalanced classes were detected in your inputs. To fix model bias, fix the balancing problem. Learn more about [imbalanced data](./concept-manage-ml-pitfalls.md#identify-models-with-imbalanced-data).<br><br> Imbalanced classes were detected in your inputs and the sweeping logic has determined to apply balancing.
**Memory issues detection** |Passed <br><br><br><br> Done |<br> The selected values (horizon, lag, rolling window) were analyzed, and no potential out-of-memory issues were detected. Learn more about time-series [forecasting configurations](./how-to-auto-train-forecast.md#configuration-settings). <br><br><br>The selected values (horizon, lag, rolling window) were analyzed and will potentially cause your experiment to run out of memory. The lag or rolling-window configurations have been turned off.
