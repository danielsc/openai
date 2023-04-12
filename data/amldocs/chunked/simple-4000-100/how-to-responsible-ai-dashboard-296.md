The next sections cover how to read the causal analysis for your dataset on select user-specified treatments.

#### Aggregate causal effects

Select the **Aggregate causal effects** tab of the causal analysis component to display the average causal effects for pre-defined treatment features (the features that you want to treat to optimize your outcome).

> [!NOTE]
> Global cohort functionality is not supported for the causal analysis component.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/aggregate-causal-effects.png" alt-text="Screenshot of the dashboard, showing causal analysis on the 'Aggregate causal effects' pane." lightbox= "./media/how-to-responsible-ai-dashboard/aggregate-causal-effects.png":::

1. **Direct aggregate causal effect table**: Displays the causal effect of each feature aggregated on the entire dataset and associated confidence statistics.

    * **Continuous treatments**: On average in this sample, increasing this feature by one unit will cause the probability of class to increase by X units, where X is the causal effect.
    * **Binary treatments**: On average in this sample, turning on this feature will cause the probability of class to increase by X units, where X is the causal effect.

1. **Direct aggregate causal effect whisker plot**: Visualizes the causal effects and confidence intervals of the points in the table.

#### Individual causal effects and causal what-if

To get a granular view of causal effects on an individual data point, switch to the **Individual causal what-if** tab.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/individual-causal-what-if.png" alt-text="Screenshot of the dashboard showing causal analysis on the individual causal what-if tab." lightbox="./media/how-to-responsible-ai-dashboard/individual-causal-what-if.png":::

1. **X-axis**: Selects the feature to plot on the x-axis.
2. **Y-axis**: Selects the feature to plot on the y-axis.
3. **Individual causal scatter plot**: Visualizes points in the table as a scatter plot to select data points for analyzing causal what-if and viewing the individual causal effects below it.
4. **Set new treatment value**:
    * **(numerical)**: Shows a slider to change the value of the numerical feature as a real-world intervention.
    * **(categorical)**: Shows a dropdown list to select the value of the categorical feature.

#### Treatment policy

Select the **Treatment policy** tab to switch to a view to help determine real-world interventions and show treatments to apply to achieve a particular outcome.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/causal-treatment-policy.png" alt-text="Screenshot of the dashboard, showing causal analysis on the 'Treatment policy' pane." lightbox= "./media/how-to-responsible-ai-dashboard/causal-treatment-policy.png":::

1. **Set treatment feature**: Selects a feature to change as a real-world intervention.

2. **Recommended global treatment policy**: Displays recommended interventions for data cohorts to improve the target feature value. The table can be read from left to right, where the segmentation of the dataset is first in rows and then in columns. For example, for 658 individuals whose employer isn't Snapchat and whose programming language isn't JavaScript, the recommended treatment policy is to increase the number of GitHub repos contributed to.

    **Average gains of alternative policies over always applying treatment**: Plots the target feature value in a bar chart of the average gain in your outcome for the above recommended treatment policy versus always applying treatment.

    :::image type="content" source="./media/how-to-responsible-ai-dashboard/causal-treatment-policy-2.png" alt-text="Screenshot of the dashboard showing a bar chart of the average gains of alternative policies over always applying treatment on the treatment policy tab." lightbox= "./media/how-to-responsible-ai-dashboard/causal-treatment-policy-2.png":::
