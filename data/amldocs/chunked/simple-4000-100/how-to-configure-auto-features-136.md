> The **drop columns** functionality is deprecated as of SDK version 1.19. Drop columns from your dataset as part of data cleansing, prior to consuming it in your automated ML experiment. 

Create the `FeaturizationConfig` object by using API calls:

```python
featurization_config = FeaturizationConfig()
featurization_config.blocked_transformers = ['LabelEncoder']
featurization_config.drop_columns = ['aspiration', 'stroke']
featurization_config.add_column_purpose('engine-size', 'Numeric')
featurization_config.add_column_purpose('body-style', 'CategoricalHash')
#default strategy mean, add transformer param for for 3 columns
featurization_config.add_transformer_params('Imputer', ['engine-size'], {"strategy": "median"})
featurization_config.add_transformer_params('Imputer', ['city-mpg'], {"strategy": "median"})
featurization_config.add_transformer_params('Imputer', ['bore'], {"strategy": "most_frequent"})
featurization_config.add_transformer_params('HashOneHotEncoder', [], {"number_of_bits": 3})
```

## Featurization transparency

Every AutoML model has featurization automatically applied.  Featurization includes automated feature engineering (when `"featurization": 'auto'`) and scaling and normalization, which then impacts the selected algorithm and its hyperparameter values. AutoML supports different methods to ensure you have visibility into what was applied to your model.

Consider this forecasting example:

+ There are four input features: A (Numeric), B (Numeric), C (Numeric), D (DateTime).
+ Numeric feature C is dropped because it is an ID column with all unique values.
+ Numeric features A and B have missing values and hence are imputed by the mean.
+ DateTime feature D is featurized into 11 different engineered features.

To get this information, use the `fitted_model` output from your automated ML experiment run.

```python
automl_config = AutoMLConfig(…)
automl_run = experiment.submit(automl_config …)
best_run, fitted_model = automl_run.get_output()
```
### Automated feature engineering 
The `get_engineered_feature_names()` returns a list of engineered feature names.

  >[!Note]
  >Use 'timeseriestransformer' for task='forecasting', else use 'datatransformer' for 'regression' or 'classification' task.

  ```python
  fitted_model.named_steps['timeseriestransformer']. get_engineered_feature_names ()
  ```

This list includes all engineered feature names. 

  ```
  ['A', 'B', 'A_WASNULL', 'B_WASNULL', 'year', 'half', 'quarter', 'month', 'day', 'hour', 'am_pm', 'hour12', 'wday', 'qday', 'week']
  ```

The `get_featurization_summary()` gets a featurization summary of all the input features.

  ```python
  fitted_model.named_steps['timeseriestransformer'].get_featurization_summary()
  ```

Output

  ```
  [{'RawFeatureName': 'A',
    'TypeDetected': 'Numeric',
    'Dropped': 'No',
    'EngineeredFeatureCount': 2,
    'Tranformations': ['MeanImputer', 'ImputationMarker']},
   {'RawFeatureName': 'B',
    'TypeDetected': 'Numeric',
    'Dropped': 'No',
    'EngineeredFeatureCount': 2,
    'Tranformations': ['MeanImputer', 'ImputationMarker']},
   {'RawFeatureName': 'C',
    'TypeDetected': 'Numeric',
    'Dropped': 'Yes',
    'EngineeredFeatureCount': 0,
    'Tranformations': []},
   {'RawFeatureName': 'D',
    'TypeDetected': 'DateTime',
    'Dropped': 'No',
    'EngineeredFeatureCount': 11,
    'Tranformations': ['DateTime','DateTime','DateTime','DateTime','DateTime','DateTime','DateTime','DateTime','DateTime','DateTime','DateTime']}]
  ```

   |Output|Definition|
   |----|--------|
   |RawFeatureName|Input feature/column name from the dataset provided.|
   |TypeDetected|Detected datatype of the input feature.|
   |Dropped|Indicates if the input feature was dropped or used.|
   |EngineeringFeatureCount|Number of features generated through automated feature engineering transforms.|
   |Transformations|List of transformations applied to input features to generate engineered features.|

### Scaling and normalization

To understand the scaling/normalization and the selected algorithm with its hyperparameter values, use `fitted_model.steps`. 
