
# Assess AI systems by using the Responsible AI dashboard

Implementing Responsible AI in practice requires rigorous engineering. But rigorous engineering can be tedious, manual, and time-consuming without the right tooling and infrastructure.

The Responsible AI dashboard provides a single interface to help you implement Responsible AI in practice effectively and efficiently. It brings together several mature Responsible AI tools in the areas of:

- [Model performance and fairness assessment](http://fairlearn.org/)
- Data exploration
- [Machine learning interpretability](https://interpret.ml/)
- [Error analysis](https://erroranalysis.ai/)
- [Counterfactual analysis and perturbations](https://github.com/interpretml/DiCE)
- [Causal inference](https://github.com/microsoft/EconML)

The dashboard offers a holistic assessment and debugging of models so you can make informed data-driven decisions. Having access to all of these tools in one interface empowers you to:

- Evaluate and debug your machine learning models by identifying model errors and fairness issues, diagnosing why those errors are happening, and informing your mitigation steps.
- Boost your data-driven decision-making abilities by addressing questions such as:

   "What is the minimum change that users can apply to their features to get a different outcome from the model?"

   "What is the causal effect of reducing or increasing a feature (for example, red meat consumption) on a real-world outcome (for example, diabetes progression)?"

You can customize the dashboard to include only the subset of tools that are relevant to your use case.

The Responsible AI dashboard is accompanied by a [PDF scorecard](how-to-responsible-ai-scorecard.md). The scorecard enables you to export Responsible AI metadata and insights into your data and models. You can then share them offline with the product and compliance stakeholders.

## Responsible AI dashboard components

The Responsible AI dashboard brings together, in a comprehensive view, various new and pre-existing tools. The dashboard integrates these tools with [Azure Machine Learning CLI v2, Azure Machine Learning Python SDK v2](concept-v2.md), and [Azure Machine Learning studio](overview-what-is-azure-machine-learning.md#studio). The tools include:  

- [Data analysis](concept-data-analysis.md), to understand and explore your dataset distributions and statistics.
- [Model overview and fairness assessment](concept-fairness-ml.md), to evaluate the performance of your model and evaluate your model's group fairness issues (how your model's predictions affect diverse groups of people).
- [Error analysis](concept-error-analysis.md), to view and understand how errors are distributed in your dataset.  
- [Model interpretability](how-to-machine-learning-interpretability.md) (importance values for aggregate and individual features), to understand your model's predictions and how those overall and individual predictions are made.
- [Counterfactual what-if](concept-counterfactual-analysis.md), to observe how feature perturbations would affect your model predictions while providing the closest data points with opposing or different model predictions.
- [Causal analysis](concept-causal-inference.md), to use historical data to view the causal effects of treatment features on real-world outcomes.

Together, these tools will help you debug machine learning models, while informing your data-driven and model-driven business decisions. The following diagram shows how you can incorporate them into your AI lifecycle to improve your models and get solid data insights.

:::image type="content" source="./media/concept-responsible-ai-dashboard/dashboard.png" alt-text="Diagram of Responsible AI dashboard components for model debugging and responsible decision-making.":::

### Model debugging

Assessing and debugging machine learning models is critical for model reliability, interpretability, fairness, and compliance. It helps determine how and why AI systems behave the way they do. You can then use this knowledge to improve model performance. Conceptually, model debugging consists of three stages:
