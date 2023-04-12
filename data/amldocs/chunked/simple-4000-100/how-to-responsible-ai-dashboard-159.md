The model overview component provides a comprehensive set of performance and fairness metrics for evaluating your model, along with key performance disparity metrics along specified features and dataset cohorts.  

#### Dataset cohorts

On the **Dataset cohorts** pane, you can investigate your model by comparing the model performance of various user-specified dataset cohorts (accessible via the **Cohort settings** icon at the top right of the dashboard).

:::image type="content" source="./media/how-to-responsible-ai-dashboard/model-overview-dataset-cohorts.png" alt-text="Screenshot of the 'Model overview' pane, showing the 'Dataset cohorts' tab." lightbox= "./media/how-to-responsible-ai-dashboard/model-overview-dataset-cohorts.png":::

1. **Help me choose metrics**: Select this icon to open a panel with more information about what model performance metrics are available to be shown in the table. Easily adjust which metrics to view by using the multi-select dropdown list to select and deselect performance metrics. 
2. **Show heat map**: Toggle on and off to show or hide heat map visualization in the table. The gradient of the heat map corresponds to the range normalized between the lowest value and the highest value in each column.  
3. **Table of metrics for each dataset cohort**: View columns of dataset cohorts, the sample size of each cohort, and the selected model performance metrics for each cohort.
4. **Bar chart visualizing individual metric**: View mean absolute error across the cohorts for easy comparison. 
5. **Choose metric (x-axis)**: Select this button to choose which metrics to view in the bar chart. 
6. **Choose cohorts (y-axis)**: Select this button to choose which cohorts to view in the bar chart. **Feature cohort** selection might be disabled unless you first specify the features you want on the **Feature cohort tab** of the component. 

Select **Help me choose metrics** to open a panel with a list of model performance metrics and their definitions, which can help you select the right metrics to view.

| Machine learning scenario | Metrics |
|---|---|
| Regression | Mean absolute error, Mean squared error, R-squared, Mean prediction. |
| Classification | Accuracy, Precision, Recall, F1 score, False positive rate, False negative rate, Selection rate. |

#### Feature cohorts

On the **Feature cohorts** pane, you can investigate your model by comparing model performance across user-specified sensitive and non-sensitive features (for example, performance across various gender, race, and income level cohorts).

:::image type="content" source="./media/how-to-responsible-ai-dashboard/model-overview-feature-cohorts.png" alt-text="Screenshot of the dashboard 'Model overview' pane, showing the 'Feature cohorts' tab." lightbox= "./media/how-to-responsible-ai-dashboard/model-overview-feature-cohorts.png":::

1. **Help me choose metrics**: Select this icon to open a panel with more information about what metrics are available to be shown in the table. Easily adjust which metrics to view by using the multi-select dropdown to select and deselect performance metrics.
2. **Help me choose features**: Select this icon to open a panel with more information about what features are available to be shown in the table, with descriptors of each feature and their binning capability (see below). Easily adjust which features to view by using the multi-select dropdown to select and deselect them.

    :::image type="content" source="./media/how-to-responsible-ai-dashboard/model-overview-choose-features.png" alt-text="Screenshot of the dashboard 'Model overview' pane, showing how to choose features." lightbox= "./media/how-to-responsible-ai-dashboard/model-overview-choose-features.png":::
3. **Show heat map**: Toggle on and off to see a heat map visualization. The gradient of the heat map corresponds to the range that's normalized between the lowest value and the highest value in each column.
4. **Table of metrics for each feature cohort**: A table with columns for feature cohorts (sub-cohort of your selected feature), sample size of each cohort, and the selected model performance metrics for each feature cohort.
