1. **Generate explanations**: Toggle on and off to generate a model explanation component for your Responsible AI dashboard. No configuration is necessary, because a default opaque box mimic explainer will be used to generate feature importances.

Alternatively, if you select the **Real-life interventions** profile, you’ll see the following screen generate a causal analysis. This will help you understand the causal effects of features you want to “treat” on a certain outcome you want to optimize.

:::image type="content" source="./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard-ui-component-parameter-real-life-intervention.png" alt-text="Screenshot of the wizard, showing the 'Component parameters for real-life interventions' pane." lightbox = "./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard-ui-component-parameter-real-life-intervention.png":::

Component parameters for real-life interventions use causal analysis. Do the following:

1. **Target feature (required)**: Choose the outcome you want the causal effects to be calculated for.
1. **Treatment features (required)**: Choose one or more features that you’re interested in changing (“treating”) to optimize the target outcome.
1. **Categorical features**: Indicate which features are categorical to properly render them as categorical values in the dashboard UI. This field is pre-loaded for you based on your dataset metadata.
1. **Advanced settings**: Specify additional parameters for your causal analysis, such as heterogenous features (that is, additional features to understand causal segmentation in your analysis, in addition to your treatment features) and which causal model you want to be used.

## Configure your experiment

Finally, configure your experiment to kick off a job to generate your Responsible AI dashboard.

:::image type="content" source="./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard-ui-experiment-config.png" alt-text="Screenshot of the Experiment configuration tab, showing the 'Training job or experiment configuration' pane." lightbox= "./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard-ui-experiment-config.png":::

On the **Training job** or **Experiment configuration** pane, do the following:

1. **Name**: Give your dashboard a unique name so that you can differentiate it when you’re viewing the list of dashboards for a given model.
1. **Experiment name**: Select an existing experiment to run the job in, or create a new experiment.
1. **Existing experiment**: In the dropdown list, select an existing experiment.
1. **Select compute type**: Specify which compute type you want to use to execute your job.
1. **Select compute**: In the dropdown list, select the compute you want to use. If there are no existing compute resources, select the plus sign (**+**), create a new compute resource, and then refresh the list.
1. **Description**: Add a longer description of your Responsible AI dashboard.
1. **Tags**: Add any tags to this Responsible AI dashboard.

After you’ve finished configuring your experiment, select **Create** to start generating your Responsible AI dashboard. You'll be redirected to the experiment page to track the progress of your job with a link to the resulting Responsible AI dashboard from the job page when it's completed.

To learn how to view and use your Responsible AI dashboard see, [Use the Responsible AI dashboard in Azure Machine Learning studio](how-to-responsible-ai-dashboard.md).

## How to generate Responsible AI scorecard (preview)

Once you've created a dashboard, you can use a no-code UI in Azure Machine Learning studio to customize and generate a Responsible AI scorecard. This enables you to share key insights for responsible deployment of your model, such as fairness and feature importance, with non-technical and technical stakeholders. Similar to creating a dashboard, you can use the following steps to access the scorecard generation wizard:
