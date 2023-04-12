| `accuracy_score` | difference | The maximum difference in accuracy score between any two groups. | Classification |
| `accuracy_score` | ratio | The minimum ratio in accuracy score between any two groups. | Classification |
| `precision_score` | difference | The maximum difference in precision score between any two groups. | Classification |
| `precision_score` | ratio | The maximum ratio in precision score between any two groups. | Classification |
| `recall_score` | difference | The maximum difference in recall score between any two groups. | Classification |
| `recall_score` | ratio | The maximum ratio in recall score between any two groups. | Classification |
| `f1_score` | difference | The maximum difference in f1 score between any two groups. | Classification |
| `f1_score` | ratio | The maximum ratio in f1 score between any two groups. | Classification |
| `error_rate` | difference | The maximum difference in error rate between any two groups. | Classification |
| `error_rate` | ratio | The maximum ratio in error rate between any two groups.|Classification|
| `Selection_rate` | difference | The maximum difference in selection rate between any two groups. | Classification |
| `Selection_rate` | ratio | The maximum ratio in selection rate between any two groups. | Classification |
| `mean_absolute_error` | difference | The maximum difference in mean absolute error between any two groups. | Regression |
| `mean_absolute_error` | ratio | The maximum ratio in mean absolute error between any two groups. | Regression |
| `mean_squared_error` | difference | The maximum difference in mean squared error between any two groups. | Regression |
| `mean_squared_error` | ratio | The maximum ratio in mean squared error between any two groups. | Regression |
| `median_absolute_error` | difference | The maximum difference in median absolute error between any two groups. | Regression |
| `median_absolute_error` | ratio | The maximum ratio in median absolute error between any two groups. | Regression |
| `r2_score` | difference | The maximum difference in R<sup>2</sup> score between any two groups. | Regression |
| `r2_Score` | ratio | The maximum ratio in R<sup>2</sup> score between any two groups. | Regression |

## Input constraints

### What model formats and flavors are supported?

The model must be in the MLflow directory with a sklearn flavor available. Additionally, the model needs to be loadable in the environment that's used by the Responsible AI components.

### What data formats are supported?

The supplied datasets should be `mltable` with tabular data.

## Next steps

- After you've generated your Responsible AI dashboard, [view how to access and use it in Azure Machine Learning studio](how-to-responsible-ai-dashboard.md).
- Summarize and share your Responsible AI insights with the [Responsible AI scorecard as a PDF export](how-to-responsible-ai-scorecard.md).
- Learn more about the [concepts and techniques behind the Responsible AI dashboard](concept-responsible-ai-dashboard.md).
- Learn more about how to [collect data responsibly](concept-sourcing-human-data.md).
- View [sample YAML and Python notebooks](https://aka.ms/RAIsamples) to generate the Responsible AI dashboard with YAML or Python.
- Learn more about how to use the Responsible AI dashboard and scorecard to debug data and models and inform better decision-making in this [tech community blog post](https://www.microsoft.com/ai/ai-lab-responsible-ai-dashboard).
- Learn about how the Responsible AI dashboard and scorecard were used by the UK National Health Service (NHS) in a [real life customer story](https://aka.ms/NHSCustomerStory).
- Explore the features of the Responsible AI dashboard through this [interactive AI lab web demo](https://www.microsoft.com/ai/ai-lab-responsible-ai-dashboard).
