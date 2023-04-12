
# Generate a Responsible AI insights in the studio UI

In this article, you create a Responsible AI dashboard and scorecard (preview) with a no-code experience in the [Azure Machine Learning studio UI](https://ml.azure.com/).

To access the dashboard generation wizard and generate a Responsible AI dashboard, do the following:
1. [Register your model](how-to-manage-models.md) in Azure Machine Learning so that you can access the no-code experience.
1. On the left pane of Azure Machine Learning studio, select the **Models** tab.
1. Select the registered model that you want to create Responsible AI insights for, and then select the **Details** tab.
1. Select **Create Responsible AI dashboard (preview)**.

    :::image type="content" source="./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard.png" alt-text="Screenshot of the wizard details pane with 'Create Responsible AI dashboard (preview)' tab highlighted." lightbox ="./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard.png":::

To learn more supported model types and limitations in the Responsible AI dashboard, see [supported scenarios and limitations](concept-responsible-ai-dashboard.md#supported-scenarios-and-limitations).

The wizard provides an interface for entering all the necessary parameters to create your Responsible AI dashboard without having to touch code. The experience takes place entirely in the Azure Machine Learning studio UI. The studio presents a guided flow and instructional text to help contextualize the variety of choices about which Responsible AI components you’d like to populate your dashboard with.

The wizard is divided into five sections:

1. Training datasets
1. Test dataset
1. Modeling task
1. Dashboard components
1. Component parameters
1. Experiment configuration

## Select your datasets

In the first two sections, you select the train and test datasets that you used when you trained your model to generate model-debugging insights. For components like causal analysis, which doesn't require a model, you use the train dataset to train the causal model to generate the causal insights.

> [!NOTE]
> Only tabular dataset formats in ML Table are supported.

1. **Select a dataset for training**: In the list of registered datasets in the Azure Machine Learning workspace, select the dataset you want to use to generate Responsible AI insights for components, such as model explanations and error analysis.  

    :::image type="content" source="./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard-ui-train-dataset.png" alt-text="Screenshot of the train dataset tab." lightbox= "./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard-ui-train-dataset.png":::

1. **Select a dataset for testing**: In the list of registered datasets, select the dataset you want to use to populate your Responsible AI dashboard visualizations.

   :::image type="content" source="./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard-ui-test-dataset.png" alt-text="Screenshot of the test dataset tab." lightbox= "./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard-ui-test-dataset.png":::

1. If the train or test dataset you want to use isn't listed, select **Create** to upload it.

## Select your modeling task

After you've picked your datasets, select your modeling task type, as shown in the following image:

:::image type="content" source="./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard-ui-modeling-task.png" alt-text="Screenshot of the modeling task tab." lightbox= "./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard-ui-modeling-task.png":::

## Select your dashboard components

The Responsible AI dashboard offers two profiles for recommended sets of tools that you can generate:

- **Model debugging**: Understand and debug erroneous data cohorts in your machine learning model by using error analysis, counterfactual what-if examples, and model explainability.
