4. **Table of metrics for each feature cohort**: A table with columns for feature cohorts (sub-cohort of your selected feature), sample size of each cohort, and the selected model performance metrics for each feature cohort.
5. **Fairness metrics/disparity metrics**: A table that corresponds to the metrics table and shows the maximum difference or maximum ratio in performance scores between any two feature cohorts.
6. **Bar chart visualizing individual metric**: View mean absolute error across the cohorts for easy comparison.
7. **Choose cohorts (y-axis)**: Select this button to choose which cohorts to view in the bar chart.

    Selecting **Choose cohorts** opens a panel with an option to either show a comparison of selected dataset cohorts or feature cohorts, depending on what you select in the multi-select dropdown list below it. Select **Confirm** to save the changes to the bar chart view.  

    :::image type="content" source="./media/how-to-responsible-ai-dashboard/model-overview-choose-cohorts.png" alt-text="Screenshot of the dashboard 'Model overview' pane, showing how to choose cohorts." lightbox= "./media/how-to-responsible-ai-dashboard/model-overview-choose-cohorts.png":::
8. **Choose metric (x-axis)**: Select this button to choose which metric to view in the bar chart.

### Data analysis

With the data analysis component, the **Table view** pane shows you a table view of your dataset for all features and rows.  

The **Chart view** panel shows you aggregate and individual plots of datapoints. You can analyze data statistics along the x-axis and y-axis by using filters such as predicted outcome, dataset features, and error groups. This view helps you understand overrepresentation and underrepresentation in your dataset.  

:::image type="content" source="./media/how-to-responsible-ai-dashboard/data-analysis-table-view.png" alt-text="Screenshot of the dashboard, showing the data analysis." lightbox= "./media/how-to-responsible-ai-dashboard/data-analysis-table-view.png":::

1. **Select a dataset cohort to explore**: Specify which dataset cohort from your list of cohorts you want to view data statistics for.
2. **X-axis**: Displays the type of value being plotted horizontally. Modify the values by selecting the button to open a side panel.
3. **Y-axis**: Displays the type of value being plotted vertically. Modify the values by selecting the button to open a side panel.
4. **Chart type**: Specifies the chart type. Choose between aggregate plots (bar charts) or individual data points (scatter plot).

   By selecting the **Individual data points** option under **Chart type**, you can shift to a disaggregated view of the data with the availability of a color axis.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/data-analysis-individual-datapoints.png" alt-text="Screenshot of the dashboard, showing the data analysis with the 'Individual data points' option selected." lightbox= "./media/how-to-responsible-ai-dashboard/data-analysis-individual-datapoints.png":::

### Feature importances (model explanations)

By using the model explanation component, you can see which features were most important in your model’s predictions. You can view what features affected your model’s prediction overall on the **Aggregate feature importance** pane or view feature importances for individual data points on the **Individual feature importance** pane.

#### Aggregate feature importances (global explanations)

:::image type="content" source="./media/how-to-responsible-ai-dashboard/aggregate-feature-importance.png" alt-text="Screenshot of the dashboard, showing aggregate feature importances on the 'Feature importances' pane." lightbox= "./media/how-to-responsible-ai-dashboard/aggregate-feature-importance.png":::

1. **Top k features**: Lists the most important global features for a prediction and allows you to change it by using a slider bar.
2. **Aggregate feature importance**: Visualizes the weight of each feature in influencing model decisions across all predictions.
