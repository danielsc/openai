1. **Heat map view**: Switches to heat map visualization of error distribution.
2. **Feature list:** Allows you to modify the features used in the heat map using a side panel.
3. **Error coverage**: Displays the percentage of all error in the dataset concentrated in the selected node.
4. **Error (regression) or Error rate (classification)**: Displays the error or percentage of failures of all the data points in the selected node.
5. **Node**: Represents a cohort of the dataset, potentially with filters applied, and the number of errors out of the total number of data points in the cohort.
6. **Fill line**: Visualizes the distribution of data points into child cohorts based on filters, with the number of data points represented through line thickness.
7. **Selection information**: Contains information about the selected node in a side panel.
8. **Save as a new cohort:** Creates a new cohort with the specified filters.
9. **Instances in the base cohort**: Displays the total number of points in the entire dataset and the number of correctly and incorrectly predicted points.
10. **Instances in the selected cohort**: Displays the total number of points in the selected node and the number of correctly and incorrectly predicted points.
11. **Prediction path (filters)**: Lists the filters placed over the full dataset to create this smaller cohort.

Select the **Feature list** button to open a side panel, from which you can retrain the error tree on specific features.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/error-analysis-feature-selection.png" alt-text="Screenshot of the dashboard side panel, which lists selectable features of an error analysis tree map." lightbox= "./media/how-to-responsible-ai-dashboard/error-analysis-feature-selection.png":::

1. **Search features**: Allows you to find specific features in the dataset.
2. **Features**: Lists the name of the feature in the dataset.
3. **Importances**: A guideline for how related the feature might be to the error. Calculated via mutual information score between the feature and the error on the labels. You can use this score to help you decide which features to choose in the error analysis.
4. **Check mark**: Allows you to add or remove the feature from the tree map.
5. **Maximum depth**: The maximum depth of the surrogate tree trained on errors.
6. **Number of leaves**: The number of leaves of the surrogate tree trained on errors.
7. **Minimum number of samples in one leaf**: The minimum amount of data required to create one leaf.

#### Error heat map

Select the **Heat map** tab to switch to a different view of the error in the dataset. You can select one or many heat map cells and create new cohorts. You can choose up to two features to create a heat map.

:::image type="content" source="./media/how-to-responsible-ai-dashboard/error-analysis-heat-map.png" alt-text="Screenshot of the dashboard, showing an error analysis heat map and list of features to compare." lightbox= "./media/how-to-responsible-ai-dashboard/error-analysis-heat-map.png":::

1. **Cells**: Displays the number of cells selected.
2. **Error coverage**: Displays the percentage of all errors concentrated in the selected cell(s).
3. **Error rate**: Displays the percentage of failures of all data points in the selected cell(s).
4. **Axis features**: Selects the intersection of features to display in the heat map.
5. **Cells**: Represents a cohort of the dataset, with filters applied, and the percentage of errors out of the total number of data points in the cohort. A blue outline indicates selected cells, and the darkness of red represents the concentration of failures.
6. **Prediction path (filters)**: Lists the filters placed over the full dataset for each selected cohort.

### Model overview and fairness metrics

The model overview component provides a comprehensive set of performance and fairness metrics for evaluating your model, along with key performance disparity metrics along specified features and dataset cohorts.  
