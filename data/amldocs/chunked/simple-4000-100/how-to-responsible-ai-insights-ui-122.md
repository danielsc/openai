Once you've created a dashboard, you can use a no-code UI in Azure Machine Learning studio to customize and generate a Responsible AI scorecard. This enables you to share key insights for responsible deployment of your model, such as fairness and feature importance, with non-technical and technical stakeholders. Similar to creating a dashboard, you can use the following steps to access the scorecard generation wizard:

- Navigate to the Models tab from the left navigation bar in Azure Machine Learning studio.
- Select the registered model you’d like to create a scorecard for and select the **Responsible AI** tab.
- From the top panel, select **Create Responsible AI insights (preview)** and then **Generate new PDF scorecard**.

The wizard will allow you to customize your PDF scorecard without having to touch code. The experience takes place entirely in the Azure Machine Learning studio to help contextualize the variety of choices of UI with a guided flow and instructional text to help you choose the components you’d like to populate your scorecard with. The wizard is divided into seven steps, with an eighth step (fairness assessment) that will only appear for models with categorical features:

1. PDF scorecard summary
2. Model performance
3. Tool selection
4. Data analysis (previously called data explorer)
5. Causal analysis
6. Interpretability
7. Experiment configuration
8. Fairness assessment (only if categorical features exist)

### Configuring your scorecard

1. First, enter a descriptive title for your scorecard. You can also enter an optional description about the model's functionality, data it was trained and evaluated on, architecture type, and more.

    :::image type="content" source="./media/how-to-responsible-ai-insights-ui/scorecard-summary.png" alt-text="Screenshot of the wizard on scorecard summary configuration." lightbox= "./media/how-to-responsible-ai-insights-ui/scorecard-summary.png":::

2. *The Model performance* section allows you to incorporate into your scorecard industry-standard model evaluation metrics, while enabling you to set desired target values for your selected metrics. Select your desired performance metrics (up to three) and target values using the dropdowns.

    :::image type="content" source="./media/how-to-responsible-ai-insights-ui/scorecard-performance.png" alt-text="Screenshot of the wizard on scorecard model performance configuration." lightbox= "./media/how-to-responsible-ai-insights-ui/scorecard-performance.png":::

3. *The Tool selection* step allows you to choose which subsequent components you would like to include in your scorecard. Check Include in scorecard to include all components, or check/uncheck each component individually. Select the info icon ("i" in a circle) next to the components to learn more about them.

    :::image type="content" source="./media/how-to-responsible-ai-insights-ui/scorecard-selection.png" alt-text="Screenshot of the wizard on scorecard tool selection configuration." lightbox= "./media/how-to-responsible-ai-insights-ui/scorecard-selection.png":::

4. *The Data analysis* section (previously called data explorer) enables cohort analysis. Here, you can identify issues of over- and under-representation explore how data is clustered in the dataset, and how model predictions impact specific data cohorts. Use checkboxes in the dropdown to select your features of interest below to identify your model performance on their underlying cohorts.

    :::image type="content" source="./media/how-to-responsible-ai-insights-ui/scorecard-explorer.png" alt-text="Screenshot of the wizard on scorecard data analysis configuration." lightbox= "./media/how-to-responsible-ai-insights-ui/scorecard-explorer.png":::

5. *The Fairness assessment* section can help with assessing which groups of people might be negatively impacted by predictions of a machine learning model. There are two fields in this section.

    - Sensitive features: identify your sensitive attribute(s) of choice (for example, age, gender) by prioritizing up to 20 subgroups you would like to explore and compare.
