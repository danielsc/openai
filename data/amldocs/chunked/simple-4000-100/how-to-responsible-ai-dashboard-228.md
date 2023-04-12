2. **Aggregate feature importance**: Visualizes the weight of each feature in influencing model decisions across all predictions.
3. **Sort by**: Allows you to select which cohort's importances to sort the aggregate feature importance graph by.
4. **Chart type**: Allows you to select between a bar plot view of average importances for each feature and a box plot of importances for all data.

    When you select one of the features in the bar plot, the dependence plot is populated, as shown in the following image. The dependence plot shows the relationship of the values of a feature to its corresponding feature importance values, which affect the model prediction.  

    :::image type="content" source="./media/how-to-responsible-ai-dashboard/aggregate-feature-importance-2.png" alt-text="Screenshot of the dashboard, showing a populated dependence plot on the 'Aggregate feature importances' pane." lightbox="./media/how-to-responsible-ai-dashboard/aggregate-feature-importance-2.png":::

5. **Feature importance of [feature] (regression) or Feature importance of [feature] on [predicted class] (classification)**: Plots the importance of a particular feature across the predictions. For regression scenarios, the importance values are in terms of the output, so positive feature importance means it contributed positively toward the output. The opposite applies to negative feature importance.  For classification scenarios, positive feature importances mean that feature value is contributing toward the predicted class denoted in the y-axis title. Negative feature importance means it's contributing against the predicted class.
6. **View dependence plot for**: Selects the feature whose importances you want to plot.
7. **Select a dataset cohort**: Selects the cohort whose importances you want to plot.

#### Individual feature importances (local explanations)

The following image illustrates how features influence the predictions that are made on specific data points. You can choose up to five data points to compare feature importances for.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/individual-feature-importance.png" alt-text="Screenshot of the dashboard, showing the 'Individual feature importances' pane." lightbox= "./media/how-to-responsible-ai-dashboard/individual-feature-importance.png":::

**Point selection table**: View your data points and select up to five points to display in the feature importance plot or the ICE plot below the table.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/individual-feature-importance-bar-plot.png" alt-text="Screenshot of the dashboard, showing a bar plot on the 'Individual feature importances' pane." lightbox="./media/how-to-responsible-ai-dashboard/individual-feature-importance-bar-plot.png":::

**Feature importance plot**: A bar plot of the importance of each feature for the model's prediction on the selected data points.

1. **Top k features**: Allows you to specify the number of features to show importances for by using a slider.
2. **Sort by**: Allows you to select the point (of those checked above) whose feature importances are displayed in descending order on the feature importance plot.
3. **View absolute values**: Toggle on to sort the bar plot by the absolute values. This allows you to see the most impactful features regardless of their positive or negative direction.
4. **Bar plot**: Displays the importance of each feature in the dataset for the model prediction of the selected data points.

**Individual conditional expectation (ICE) plot**: Switches to the ICE plot, which shows model predictions across a range of values of a particular feature.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/individual-feature-importance-ice-plot.png" alt-text="Screenshot of the dashboard, showing an ICE plot on the 'Individual feature importances' pane." lightbox="./media/how-to-responsible-ai-dashboard/individual-feature-importance-ice-plot.png":::
