| `desired_range` | For regression problems, identify the desired range of outcomes. | Optional list of two numbers<sup>3</sup>. |
| `permitted_range` | Dictionary with feature names as keys and the permitted range in a list as values. Defaults to the range inferred from training data. |  Optional string or list<sup>3</sup>.|
| `features_to_vary` | Either a string `all` or a list of feature names to vary. | Optional string or list<sup>3</sup>.|
| `feature_importance` | Flag to enable computation of feature importances by using `dice-ml`. |Optional Boolean. Defaults to `True`. |

<sup>3</sup> For the non-scalar parameters: Parameters that are lists or dictionaries should be passed as single JSON-encoded strings.

This component has a single output port, which can be connected to one of the `insight_[n]` input ports of the `Gather RAI Insights dashboard` component.

# [YAML](#tab/yaml)

```yml
 counterfactual_01: 
    type: command 
    component: azureml://registries/azureml/components/microsoft_azureml_rai_tabular_counterfactual/versions/<version>
    inputs: 
      rai_insights_dashboard: ${{parent.jobs.create_rai_job.outputs.rai_insights_dashboard}} 
      total_CFs: 10 
      desired_range: "[5, 10]" 
```


# [Python SDK](#tab/python)

```python
#First load the component: 
        rai_counterfactual_component = ml_client_registry.components.get(name="microsoft_azureml_rai_tabular_counterfactual", label="latest")

#Use it in a pipeline function: 
            counterfactual_job = rai_counterfactual_component( 
                rai_insights_dashboard=create_rai_job.outputs.rai_insights_dashboard, 
                total_cfs=10, 
                desired_range="[5, 10]", 
            ) 
```


### Add Error Analysis to RAI Insights dashboard 

This component generates an error analysis for the model. It has a single input port, which accepts the output of the `RAI Insights Dashboard Constructor`. It also accepts the following parameters:

| Parameter name | Description | Type |
|---|---|---|
| `max_depth` | The maximum depth of the error analysis tree. | Optional integer. Defaults to 3. |
| `num_leaves` | The maximum number of leaves in the error tree. | Optional integer. Defaults to 31. |
| `min_child_samples` | The minimum number of datapoints required to produce a leaf. | Optional integer. Defaults to 20. |
| `filter_features` | A list of one or two features to use for the matrix filter. | Optional list, to be passed as a single JSON-encoded string. |

This component has a single output port, which can be connected to one of the `insight_[n]` input ports of the `Gather RAI Insights Dashboard` component.

# [YAML](#tab/yaml)

```yml
  error_analysis_01: 
    type: command 
    component: azureml://registries/azureml/components/microsoft_azureml_rai_tabular_erroranalysis/versions/<version>
    inputs: 
      rai_insights_dashboard: ${{parent.jobs.create_rai_job.outputs.rai_insights_dashboard}} 
      filter_features: `["style", "Employer"]' 
```

# [Python SDK](#tab/python)

```python
#First load the component: 
        rai_erroranalysis_component = ml_client_registry.components.get(name="microsoft_azureml_rai_tabular_erroranalysis", label="latest")

#Use inside a pipeline: 
            erroranalysis_job = rai_erroranalysis_component( 
                rai_insights_dashboard=create_rai_job.outputs.rai_insights_dashboard, 
                filter_features='["style", "Employer"]', 
            ) 
```


### Add Explanation to RAI Insights dashboard

This component generates an explanation for the model. It has a single input port, which accepts the output of the `RAI Insights Dashboard Constructor`. It accepts a single, optional comment string as a parameter.

This component has a single output port, which can be connected to one of the `insight_[n]` input ports of the Gather RAI Insights dashboard component.


# [YAML](#tab/yaml)

```yml
  explain_01: 
    type: command 
    component: azureml://registries/azureml/components/microsoft_azureml_rai_tabular_explanation/versions/<version>
    inputs: 
      comment: My comment 
      rai_insights_dashboard: ${{parent.jobs.create_rai_job.outputs.rai_insights_dashboard}} 
```
