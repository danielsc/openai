| `categorical_column_names` | The columns in the datasets, which represent categorical data. | Optional list of strings<sup>1</sup> |
| `classes` | The full list of class labels in the training dataset. | Optional list of strings<sup>1</sup> |

<sup>1</sup> The lists should be supplied as a single JSON-encoded string for `categorical_column_names` and `classes` inputs.

The constructor component has a single output named `rai_insights_dashboard`. This is an empty dashboard, which the individual tool components operate on. All the results are assembled by the `Gather RAI Insights dashboard` component at the end.

# [YAML](#tab/yaml)

```yml
 create_rai_job: 

    type: command 
    component: azureml://registries/azureml/components/microsoft_azureml_rai_tabular_insight_constructor/versions/<get current version>
    inputs: 
      title: From YAML snippet 
      task_type: regression
      type: mlflow_model
      path: azureml:<registered_model_name>:<registered model version> 
      train_dataset: ${{parent.inputs.my_training_data}} 
      test_dataset: ${{parent.inputs.my_test_data}} 
      target_column_name: ${{parent.inputs.target_column_name}} 
      categorical_column_names: '["location", "style", "job title", "OS", "Employer", "IDE", "Programming language"]' 
```

# [Python SDK](#tab/python)

First load the component:

```python
# First load the component:

        rai_constructor_component = ml_client_registry.components.get(name="microsoft_azureml_rai_tabular_insight_constructor", label="latest")

#Then inside the pipeline:

            construct_job = rai_constructor_component( 
                title="From Python", 
                task_type="classification", 
                model_input= model_input= Input(type=AssetTypes.MLFLOW_MODEL, path="<azureml:model_name:model_id>"),
                train_dataset=train_data, 
                test_dataset=test_data, 
                target_column_name=target_column_name, 
                categorical_column_names='["location", "style", "job title", "OS", "Employer", "IDE", "Programming language"]', 
                maximum_rows_for_test_dataset=5000, 
                classes="[]", 
            ) 
```


### Add Causal to RAI Insights dashboard

This component performs a causal analysis on the supplied datasets. It has a single input port, which accepts the output of the `RAI Insights dashboard constructor`. It also accepts the following parameters:

| Parameter name | Description | Type&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|
| `treatment_features` | A list of feature names in the datasets, which are potentially "treatable" to obtain different outcomes. | List of strings<sup>2</sup>. |
| `heterogeneity_features` | A list of feature names in the datasets, which might affect how the "treatable" features behave. By default, all features will be considered. | Optional list of strings<sup>2</sup>.|
| `nuisance_model` | The model used to estimate the outcome of changing the treatment features. | Optional string. Must be `linear` or `AutoML`, defaulting to `linear`. |
| `heterogeneity_model` | The model used to estimate the effect of the heterogeneity features on the outcome. | Optional string. Must be `linear` or `forest`, defaulting to `linear`. |
| `alpha` | Confidence level of confidence intervals. | Optional floating point number, defaults to 0.05. |
| `upper_bound_on_cat_expansion` | The maximum expansion of categorical features. | Optional integer, defaults to 50. |
| `treatment_cost` | The cost of the treatments. If 0, all treatments will have zero cost. If a list is passed, each element is applied to one of the `treatment_features`.<br><br>Each element can be a scalar value to indicate a constant cost of applying that treatment or an array indicating the cost for each sample. If the treatment is a discrete treatment, the array for that feature should be two dimensional, with the first dimension representing samples and the second representing the difference in cost between the non-default values and the default value. | Optional integer or list<sup>2</sup>.|
