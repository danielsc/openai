
# Generate a Responsible AI insights with YAML and Python

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

You can generate a Responsible AI dashboard and scorecard via a pipeline job by using Responsible AI components. There are six core components for creating Responsible AI dashboards, along with a couple of helper components. Here's a sample experiment graph:

:::image type="content" source="./media/how-to-responsible-ai-insights-sdk-cli/sample-experiment-graph.png" alt-text="Screenshot of a sample experiment graph." lightbox= "./media/how-to-responsible-ai-insights-sdk-cli/sample-experiment-graph.png":::

## Responsible AI components

The core components for constructing the Responsible AI dashboard in Azure Machine Learning are:

- `RAI Insights dashboard constructor`
- The tool components:
    - `Add Explanation to RAI Insights dashboard`
    - `Add Causal to RAI Insights dashboard`
    - `Add Counterfactuals to RAI Insights dashboard`
    - `Add Error Analysis to RAI Insights dashboard`
    - `Gather RAI Insights dashboard`
    - `Gather RAI Insights score card`

The `RAI Insights dashboard constructor` and `Gather RAI Insights dashboard` components are always required, plus at least one of the tool components. However, it isn't necessary to use all the tools in every Responsible AI dashboard.  

In the following sections are specifications of the Responsible AI components and examples of code snippets in YAML and Python. To view the full code, see [sample YAML and Python notebook](https://aka.ms/RAIsamplesProgrammer).

### Limitations

The current set of components have a number of limitations on their use:

- All models must be registered in Azure Machine Learning in MLflow format with a sklearn (scikit-learn) flavor.
- The models must be loadable in the component environment.
- The models must be pickleable.
- The models must be supplied to the Responsible AI components by using the `Fetch Registered Model` component, which we provide.
- The dataset inputs must be in `mltable` format.
- A model must be supplied even if only a causal analysis of the data is performed. You can use the `DummyClassifier` and `DummyRegressor` estimators from scikit-learn for this purpose.

### RAI Insights dashboard constructor

This component has three input ports:

- The machine learning model  
- The training dataset  
- The test dataset  

To generate model-debugging insights with components such as error analysis and Model explanations, use the training and test dataset that you used when you trained your model. For components like causal analysis, which doesn't require a model, you use the training dataset to train the causal model to generate the causal insights. You use the test dataset to populate your Responsible AI dashboard visualizations.

The easiest way to supply the model is to register the input model and reference the same model in the model input port of `RAI Insight Constructor` component, which we discuss later in this article.

> [!NOTE]
> Currently, only models in MLflow format and with a `sklearn` flavor are supported.

The two datasets should be in `mltable` format. The training and test datasets provided don't have to be the same datasets that are used in training the model, but they can be the same. By default, for performance reasons, the test dataset is restricted to 5,000 rows of the visualization UI.

The constructor component also accepts the following parameters:

| Parameter name | Description | Type |
|---|---|---|
| `title` | Brief description of the dashboard. | String |
| `task_type` | Specifies whether the model is for classification or regression. | String, `classification` or `regression` |
| `target_column_name` | The name of the column in the input datasets, which the model is trying to predict. | String |
| `maximum_rows_for_test_dataset` | The maximum number of rows allowed in the test dataset, for performance reasons. | Integer, defaults to 5,000 |
| `categorical_column_names` | The columns in the datasets, which represent categorical data. | Optional list of strings<sup>1</sup> |
