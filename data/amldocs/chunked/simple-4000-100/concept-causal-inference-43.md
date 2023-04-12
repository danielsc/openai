  By itself, this approach can provide insights into the data. It enables the calculation of metrics such as individual treatment effect (ITE), average treatment effect (ATE), and conditional average treatment effect (CATE). You can then use these calculations to make optimal decisions. 

  The framework is scalable for large data, in terms of both the number of variables and the number of data points. It can also handle missing data entries with mixed statistical types.

- [EconML](https://www.microsoft.com/research/project/econml/) powers the back end of the Responsible AI dashboard's causal inference component. It's a Python package that applies machine learning techniques to estimate individualized causal responses from observational or experimental data. 

  The suite of estimation methods in EconML represents the latest advances in causal machine learning. By incorporating individual machine learning steps into interpretable causal models, these methods improve the reliability of what-if predictions and make causal analysis quicker and easier for a broad set of users.

- [DoWhy](https://py-why.github.io/dowhy/) is a Python library that aims to spark causal thinking and analysis. DoWhy provides a principled four-step interface for causal inference that focuses on explicitly modeling causal assumptions and validating them as much as possible. 

  The key feature of DoWhy is its state-of-the-art refutation API that can automatically test causal assumptions for any estimation method. It makes inference more robust and accessible to non-experts. 

  DoWhy supports estimation of the average causal effect for back-door, front-door, instrumental variable, and other identification methods. It also supports estimation of the CATE through an integration with the EconML library.

## Next steps

- Learn how to generate the Responsible AI dashboard via [CLI and SDK](how-to-responsible-ai-dashboard-sdk-cli.md) or [Azure Machine Learning studio UI](how-to-responsible-ai-dashboard-ui.md).
- Explore the [supported causal inference visualizations](how-to-responsible-ai-dashboard.md#causal-analysis) of the Responsible AI dashboard.
- Learn how to generate a [Responsible AI scorecard](how-to-responsible-ai-scorecard.md) based on the insights observed in the Responsible AI dashboard.
