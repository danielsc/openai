2. **Dashboard configuration**: Allows you to view and modify the layout of the overall dashboard in a side panel.
3. **Switch cohort**: Allows you to select a different cohort and view its statistics in a pop-up window.
4. **New cohort**: Allows you to create and add a new cohort to your dashboard.

Select **Cohort settings** to open a panel with a list of your cohorts, where you can create, edit, duplicate, or delete them.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/view-dashboard-cohort-settings.png" alt-text="Screenshot showing the cohort settings on the dashboard." lightbox ="./media/how-to-responsible-ai-dashboard/view-dashboard-cohort-settings.png":::

Select **New cohort** at the top of the dashboard or in the Cohort settings to open a new panel with options to filter on the following:

1. **Index**: Filters by the position of the data point in the full dataset.
2. **Dataset**: Filters by the value of a particular feature in the dataset.
3. **Predicted Y**: Filters by the prediction made by the model.
4. **True Y**: Filters by the actual value of the target feature.
5. **Error (regression)**: Filters by error (or **Classification Outcome (classification)**: Filters by type and accuracy of classification).
6. **Categorical Values**: Filter by a list of values that should be included.
7. **Numerical Values**: Filter by a Boolean operation over the values (for example, select data points where age < 64).

:::image type="content" source="./media/how-to-responsible-ai-dashboard/view-dashboard-cohort-panel.png" alt-text="Screenshot of making multiple new cohorts." lightbox= "./media/how-to-responsible-ai-dashboard/view-dashboard-cohort-panel.png":::

You can name your new dataset cohort, select **Add filter** to add each filter you want to use, and then do either of the following:
* Select **Save** to save the new cohort to your cohort list.
* Select **Save and switch** to save and immediately switch the global cohort of the dashboard to the newly created cohort.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/view-dashboard-new-cohort.png" alt-text="Screenshot of making a new cohort in the dashboard." lightbox= "./media/how-to-responsible-ai-dashboard/view-dashboard-new-cohort.png":::

Select **Dashboard configuration** to open a panel with a list of the components you’ve configured on your dashboard. You can hide components on your dashboard by selecting the **Trash** icon, as shown in the following image:

:::image type="content" source="./media/how-to-responsible-ai-dashboard/dashboard-configuration.png" alt-text="Screenshot showing the dashboard configuration." lightbox="./media/how-to-responsible-ai-dashboard/dashboard-configuration.png":::

You can add components back to your dashboard via the blue circular plus sign (**+**) icon in the divider between each component, as shown in the following image:

:::image type="content" source="./media/how-to-responsible-ai-dashboard/dashboard-add-component.png" alt-text="Screenshot of adding a component to the dashboard." lightbox= "./media/how-to-responsible-ai-dashboard/dashboard-add-component.png":::

### Error analysis

The next sections cover how to interpret and use error tree maps and heat maps.

#### Error tree map

The first pane of the error analysis component is a tree map, which illustrates how model failure is distributed across various cohorts with a tree visualization. Select any node to see the prediction path on your features where an error was found.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/error-analysis-tree-map-selected.png" alt-text="Screenshot of the dashboard showing an error analysis on the tree map pane." lightbox="./media/how-to-responsible-ai-dashboard/error-analysis-tree-map-selected.png":::

1. **Heat map view**: Switches to heat map visualization of error distribution.
2. **Feature list:** Allows you to modify the features used in the heat map using a side panel.
