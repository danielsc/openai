- **Model debugging**: Understand and debug erroneous data cohorts in your machine learning model by using error analysis, counterfactual what-if examples, and model explainability.
- **Real-life interventions**: Understand and debug erroneous data cohorts in your machine learning model by using causal analysis.

    > [!NOTE]
    > Multi-class classification doesn't support the real-life interventions analysis profile.

:::image type="content" source="./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard-ui-dashboard-components.png" alt-text="Screenshot of the dashboard components tab, showing the 'Model debugging' and 'Real-life interventions' profiles." lightbox ="./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard-ui-dashboard-components.png":::

1. Select the profile you want to use.
1. Select **Next**.

## Configure parameters for dashboard components

After you’ve selected a profile, the **Component parameters for model debugging** configuration pane for the corresponding components appears.

:::image type="content" source="./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard-ui-component-parameter-debugging.png" alt-text="Screenshot of the component parameter tab, showing the 'Component parameters for model debugging' configuration pane." lightbox = "./media/how-to-responsible-ai-insights-ui/create-responsible-ai-dashboard-ui-component-parameter-debugging.png":::

Component parameters for model debugging:

1. **Target feature (required)**: Specify the feature that your model was trained to predict.
1. **Categorical features**: Indicate which features are categorical to properly render them as categorical values in the dashboard UI. This field is pre-loaded for you based on your dataset metadata.
1. **Generate error tree and heat map**: Toggle on and off to generate an error analysis component for your Responsible AI dashboard.
1. **Features for error heat map**: Select up to two features that you want to pre-generate an error heatmap for. 
1. **Advanced configuration**: Specify additional parameters, such as **Maximum depth of error tree**, **Number of leaves in error tree**, and **Minimum number of samples in each leaf node**.
1. **Generate counterfactual what-if examples**: Toggle on and off to generate a counterfactual what-if component for your Responsible AI dashboard.
1. **Number of counterfactuals (required)**: Specify the number of counterfactual examples that you want generated per data point. A minimum of 10 should be generated to enable a bar chart view of the features that were most perturbed, on average, to achieve the desired prediction.
1. **Range of value predictions (required)**: Specify for regression scenarios the range that you want counterfactual examples to have prediction values in. For binary classification scenarios, the range will automatically be set to generate counterfactuals for the opposite class of each data point. For multi-classification scenarios, use the dropdown list to specify which class you want each data point to be predicted as.
1. **Specify which features to perturb**: By default, all features will be perturbed. However, if you want only specific features to be perturbed, select **Specify which features to perturb for generating counterfactual explanations** to display a pane with a list of features to select.

    When you select **Specify which features to perturb**, you can specify the range you want to allow perturbations in. For example: for the feature YOE (Years of experience), specify that counterfactuals should have feature values ranging from only 10 to 21 instead of the default values of 5 to 21.

    :::image type="content" source="./media/how-to-responsible-ai-insights-ui/model-debug-counterfactuals.png" alt-text="Screenshot of the wizard, showing a pane of features you can specify to perturb." lightbox = "./media/how-to-responsible-ai-insights-ui/model-debug-counterfactuals.png":::

1. **Generate explanations**: Toggle on and off to generate a model explanation component for your Responsible AI dashboard. No configuration is necessary, because a default opaque box mimic explainer will be used to generate feature importances.
