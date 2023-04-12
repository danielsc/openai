| `ThresholdOptimizer` | Postprocessing algorithm based on the paper [Equality of Opportunity in Supervised Learning](https://arxiv.org/abs/1610.02413). This technique takes as input an existing classifier and a sensitive feature. Then, it derives a monotone transformation of the classifier's prediction to enforce the specified parity constraints. | Binary classification | Categorical | Demographic parity, equalized odds| Post-processing |

## Next steps

- Learn how to generate the Responsible AI dashboard via [CLI and SDK](how-to-responsible-ai-insights-sdk-cli.md) or [Azure Machine Learning studio UI](how-to-responsible-ai-insights-ui.md).
- Explore the [supported model overview and fairness assessment visualizations](how-to-responsible-ai-dashboard.md#model-overview-and-fairness-metrics) of the Responsible AI dashboard.
- Learn how to generate a [Responsible AI scorecard](how-to-responsible-ai-scorecard.md) based on the insights observed in the Responsible AI dashboard.
- Learn how to use the components by checking out Fairlearn's [GitHub repository](https://github.com/fairlearn/fairlearn/), [user guide](https://fairlearn.github.io/main/user_guide/index.html), [examples](https://fairlearn.github.io/main/auto_examples/index.html), and [sample notebooks](https://github.com/fairlearn/fairlearn/tree/master/notebooks).
