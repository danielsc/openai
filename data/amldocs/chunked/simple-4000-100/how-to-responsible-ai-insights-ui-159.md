    - Sensitive features: identify your sensitive attribute(s) of choice (for example, age, gender) by prioritizing up to 20 subgroups you would like to explore and compare.

    - Fairness metric: select a fairness metric that is appropriate for your setting (for example, difference in accuracy, error rate ratio), and identify your desired target value(s) on your selected fairness metric(s). Your selected fairness metric (paired with your selection of difference or ratio via the toggle) will capture the difference or ratio between the extreme values across the subgroups. (max - min or max/min).

    :::image type="content" source="./media/how-to-responsible-ai-insights-ui/scorecard-fairness.png" alt-text="Screenshot of the wizard on scorecard fairness assessment configuration." lightbox= "./media/how-to-responsible-ai-insights-ui/scorecard-fairness.png":::

    > [!NOTE]
    > The Fairness assessment is currently only available for categorical sensitive attributes such as gender.

6. *The Causal analysis* section answers real-world “what if” questions about how changes of treatments would impact a real-world outcome. If the causal component is activated in the Responsible AI dashboard for which you're generating a scorecard, no more configuration is needed.

    :::image type="content" source="./media/how-to-responsible-ai-insights-ui/scorecard-causal.png" alt-text="Screenshot of the wizard on scorecard causal analysis configuration." lightbox= "./media/how-to-responsible-ai-insights-ui/scorecard-causal.png":::

7. *The Interpretability* section generates human-understandable descriptions for predictions made by of your machine learning model. Using model explanations, you can understand the reasoning behind decisions made by your model. Select a number (K) below to see the top K important features impacting your overall model predictions. The default value for K is 10.

    :::image type="content" source="./media/how-to-responsible-ai-insights-ui/scorecard-interpretability.png" alt-text="Screenshot of the wizard on scorecard feature importance configuration." lightbox= "./media/how-to-responsible-ai-insights-ui/scorecard-interpretability.png":::

8. Lastly, configure your experiment to kick off a job to generate your scorecard. These configurations are the same as the ones for your Responsible AI dashboard.

    :::image type="content" source="./media/how-to-responsible-ai-insights-ui/scorecard-experiment.png" alt-text="Screenshot of the wizard on scorecard experiment configuration." lightbox= "./media/how-to-responsible-ai-insights-ui/scorecard-experiment.png":::

9. Finally, review your configurations and select **Create** to start your job!

    :::image type="content" source="./media/how-to-responsible-ai-insights-ui/scorecard-review.png" alt-text="Screenshot of the wizard on scorecard configuration review." lightbox= "./media/how-to-responsible-ai-insights-ui/scorecard-review.png":::

    You'll be redirected to the experiment page to track the progress of your job once you've started it. To learn how to view and use your Responsible AI scorecard, see [Use Responsible AI scorecard (preview)](how-to-responsible-ai-scorecard.md).

## Next steps

- After you've generated your Responsible AI dashboard, [view how to access and use it in Azure Machine Learning studio](how-to-responsible-ai-dashboard.md).
- Learn more about the  [concepts and techniques behind the Responsible AI dashboard](concept-responsible-ai-dashboard.md).
- Learn more about how to [collect data responsibly](concept-sourcing-human-data.md).
- Learn more about how to use the Responsible AI dashboard and scorecard to debug data and models and inform better decision-making in this [tech community blog post](https://www.microsoft.com/ai/ai-lab-responsible-ai-dashboard).
- Learn about how the Responsible AI dashboard and scorecard were used by the UK National Health Service (NHS) in a [real life customer story](https://aka.ms/NHSCustomerStory).
- Explore the features of the Responsible AI dashboard through this [interactive AI Lab web demo](https://www.microsoft.com/ai/ai-lab-responsible-ai-dashboard).
