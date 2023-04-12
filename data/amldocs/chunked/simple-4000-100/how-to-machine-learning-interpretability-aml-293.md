When attempting to interpret a model with respect to the original dataset, it’s recommended to use raw explanations as each feature importance will correspond to a column from the original dataset. One scenario where engineered explanations might be useful is when examining the impact of individual categories from a categorical feature. If a one-hot encoding is applied to a categorical feature, then the resulting engineered explanations will include a different importance value per category, one per one-hot engineered feature. This encoding can be useful when narrowing down which part of the dataset is most informative to the model.

> [!NOTE]
> Engineered and raw explanations are computed sequentially. First an engineered explanation is created based on the model and featurization pipeline. Then the raw explanation is created based on that engineered explanation by aggregating the importance of engineered features that came from the same raw feature.

### Create, edit, and view dataset cohorts

The top ribbon shows the overall statistics on your model and data. You can slice and dice your data into dataset cohorts, or subgroups, to investigate or compare your model’s performance and explanations across these defined subgroups. By comparing your dataset statistics and explanations across those subgroups, you can get a sense of why possible errors are happening in one group versus another.

[![Creating, editing, and viewing dataset cohorts](./media/how-to-machine-learning-interpretability-aml/dataset-cohorts.gif)](./media/how-to-machine-learning-interpretability-aml/dataset-cohorts.gif#lightbox)

### Understand entire model behavior (global explanation) 

The first three tabs of the explanation dashboard provide an overall analysis of the trained model along with its predictions and explanations.

#### Model performance
Evaluate the performance of your model by exploring the distribution of your prediction values and the values of your model performance metrics. You can further investigate your model by looking at a comparative analysis of its performance across different cohorts or subgroups of your dataset. Select filters along y-value and x-value to cut across different dimensions. View metrics such as accuracy, precision, recall, false positive rate (FPR), and false negative rate (FNR).

[![Model performance tab in the explanation visualization](./media/how-to-machine-learning-interpretability-aml/model-performance.gif)](./media/how-to-machine-learning-interpretability-aml/model-performance.gif#lightbox)

#### Dataset explorer
Explore your dataset statistics by selecting different filters along the X, Y, and color axes to slice your data along different dimensions. Create dataset cohorts above to analyze dataset statistics with filters such as predicted outcome, dataset features and error groups. Use the gear icon in the upper right-hand corner of the graph to change graph types.

[![Dataset explorer tab in the explanation visualization](./media/how-to-machine-learning-interpretability-aml/dataset-explorer.gif)](./media/how-to-machine-learning-interpretability-aml/dataset-explorer.gif#lightbox)

#### Aggregate feature importance
Explore the top-k important features that impact your overall model predictions (also known as global explanation). Use the slider to show descending feature importance values. Select up to three cohorts to see their feature importance values side by side. Select any of the feature bars in the graph to see how values of the selected feature impact model prediction in the dependence plot below.

[![Aggregate feature importance tab in the explanation visualization](./media/how-to-machine-learning-interpretability-aml/aggregate-feature-importance.gif)](./media/how-to-machine-learning-interpretability-aml/aggregate-feature-importance.gif#lightbox)

### Understand individual predictions (local explanation) 

The fourth tab of the explanation tab lets you drill into an individual datapoint and their individual feature importances. You can load the individual feature importance plot for any data point by clicking on any of the individual data points in the main scatter plot or selecting a specific datapoint in the panel wizard on the right.
