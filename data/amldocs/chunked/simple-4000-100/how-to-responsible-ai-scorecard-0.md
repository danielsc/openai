
# Use Responsible AI scorecard (preview) in Azure Machine Learning

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

An Azure Machine Learning Responsible AI scorecard is a PDF report that's generated based on Responsible AI dashboard insights and customizations to accompany your machine learning models. You can easily configure, download, and share your PDF scorecard with your technical and non-technical stakeholders to educate them about your data and model health and compliance, and to help build trust. You can also use the scorecard in audit reviews to inform the stakeholders about the characteristics of your model.

## Where to find your Responsible AI scorecard

 Responsible AI scorecards are linked to your Responsible AI dashboards. To view your Responsible AI scorecard, go into your model registry by selecting the **Model** in Azure Machine Learning studio. Then select the registered model that you've generated a Responsible AI dashboard and scorecard for. After you've selected your model, select the **Responsible AI** tab to view a list of generated dashboards. Select which dashboard you want to export a Responsible AI scorecard PDF for by selecting **Responsible AI Insights** then **View all PDF scorecards.

:::image type="content" source="./media/how-to-responsible-ai-scorecard/scorecard-studio.png" alt-text="Screenshot of the 'Responsible AI (preview)' pane in Azure Machine Learning studio, with the 'Responsible AI scorecard (preview)' tab highlighted." lightbox = "./media/how-to-responsible-ai-scorecard/scorecard-studio.png":::

1. Select **Responsible AI scorecard (preview)** to display a list of all Responsible AI scorecards that are generated for this dashboard.

   :::image type="content" source="./media/how-to-responsible-ai-scorecard/scorecard-studio-dropdown.png" alt-text="Screenshot of Responsible AI scorecard dropdown." lightbox ="./media/how-to-responsible-ai-scorecard/scorecard-studio-dropdown.png":::

1. In the list, select the scorecard you want to download, and then select **Download** to download the PDF to your machine.

   :::image type="content" source="./media/how-to-responsible-ai-scorecard/studio-select-scorecard.png" alt-text="Screenshot of the 'Responsible AI scorecards' pane for selecting a scorecard to download." lightbox= "./media/how-to-responsible-ai-scorecard/studio-select-scorecard.png":::

## How to read your Responsible AI scorecard

The Responsible AI scorecard is a PDF summary of key insights from your Responsible AI dashboard. The first summary segment of the scorecard gives you an overview of the machine learning model and the key target values you've set to help your stakeholders determine whether the model is ready to be deployed:

:::image type="content" source="./media/how-to-responsible-ai-scorecard/scorecard-summary.png" alt-text="Screenshot of the model summary on the Responsible AI scorecard PDF.":::

The data analysis segment shows you characteristics of your data, because any model story is incomplete without a correct understanding of your data:

:::image type="content" source="./media/how-to-responsible-ai-scorecard/scorecard-data-explorer.png" alt-text="Screenshot of the data analysis on the Responsible AI scorecard PDF.":::

The model performance segment displays your model's most important metrics and characteristics of your predictions and how well they satisfy your desired target values:

:::image type="content" source="./media/how-to-responsible-ai-scorecard/scorecard-model-performance.png" alt-text="Screenshot of the model performance on the Responsible AI scorecard PDF.":::

Next, you can also view the top performing and worst performing data cohorts and subgroups that are automatically extracted for you to see the blind spots of your model:

:::image type="content" source="./media/how-to-responsible-ai-scorecard/scorecard-cohorts.png" alt-text="Screenshot of data cohorts and subgroups on the Responsible AI scorecard PDF.":::

You can see the top important factors that affect your model predictions, which is a requirement to build trust with how your model is performing its task:
