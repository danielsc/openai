The fourth tab of the explanation tab lets you drill into an individual datapoint and their individual feature importances. You can load the individual feature importance plot for any data point by clicking on any of the individual data points in the main scatter plot or selecting a specific datapoint in the panel wizard on the right.

|Plot|Description|
|----|-----------|
|Individual feature importance|Shows the top-k important features for an individual prediction. Helps illustrate the local behavior of the underlying model on a specific data point.|
|What-If analysis|Allows changes to feature values of the selected real data point and observe resulting changes to prediction value by generating a hypothetical datapoint with the new feature values.|
|Individual Conditional Expectation (ICE)|Allows feature value changes from a minimum value to a maximum value. Helps illustrate how the data point's prediction changes when a feature changes.|

[![Individual feature importance and What-if tab in explanation dashboard](./media/how-to-machine-learning-interpretability-aml/individual-tab.gif)](./media/how-to-machine-learning-interpretability-aml/individual-tab.gif#lightbox)

> [!NOTE]
> These are explanations based on many approximations and are not the "cause" of predictions. Without strict mathematical robustness of causal inference, we do not advise users to make real-life decisions based on the feature perturbations of the What-If tool. This tool is primarily for understanding your model and debugging.

### Visualization in Azure Machine Learning studio

If you complete the [remote interpretability](how-to-machine-learning-interpretability-aml.md#generate-feature-importance-values-via-remote-runs) steps (uploading generated explanations to Azure Machine Learning Run History), you can view the visualizations on the explanations dashboard in [Azure Machine Learning studio](https://ml.azure.com). This dashboard is a simpler version of the dashboard widget that's generated within your Jupyter Notebook. What-If datapoint generation and ICE plots are disabled as there’s no active compute in Azure Machine Learning studio that can perform their real-time computations.

If the dataset, global, and local explanations are available, data populates all of the tabs. However, if only a global explanation is available, the Individual feature importance tab will be disabled.

Follow one of these paths to access the explanations dashboard in Azure Machine Learning studio:

* **Experiments** pane (Preview)
  1. Select **Experiments** in the left pane to see a list of experiments that you've run on Azure Machine Learning.
  1. Select a particular experiment to view all the runs in that experiment.
  1. Select a run, and then the **Explanations** tab to the explanation visualization dashboard.

   [![Visualization Dashboard with Aggregate Feature Importance in AzureML studio in experiments](./media/how-to-machine-learning-interpretability-aml/model-explanation-dashboard-aml-studio.png)](./media/how-to-machine-learning-interpretability-aml/model-explanation-dashboard-aml-studio.png#lightbox)

* **Models** pane

  1. If you registered your original model by following the steps in [Deploy models with Azure Machine Learning](./how-to-deploy-online-endpoints.md), you can select **Models** in the left pane to view it.
  1. Select a model, and then the **Explanations** tab to view the explanations dashboard.

## Interpretability at inference time

You can deploy the explainer along with the original model and use it at inference time to provide the individual feature importance values (local explanation) for any new datapoint. We also offer lighter-weight scoring explainers to improve interpretability performance at inference time, which is currently supported only in Azure Machine Learning SDK. The process of deploying a lighter-weight scoring explainer is similar to deploying a model and includes the following steps:

1. Create an explanation object. For example, you can use `TabularExplainer`:
