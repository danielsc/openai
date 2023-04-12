| `treatment_cost` | The cost of the treatments. If 0, all treatments will have zero cost. If a list is passed, each element is applied to one of the `treatment_features`.<br><br>Each element can be a scalar value to indicate a constant cost of applying that treatment or an array indicating the cost for each sample. If the treatment is a discrete treatment, the array for that feature should be two dimensional, with the first dimension representing samples and the second representing the difference in cost between the non-default values and the default value. | Optional integer or list<sup>2</sup>.|
| `min_tree_leaf_samples` | The minimum number of samples per leaf in the policy tree. | Optional integer, defaults to 2. |
| `max_tree_depth` | The maximum depth of the policy tree. | Optional integer, defaults to 2. | 
| `skip_cat_limit_checks` | By default, categorical features need to have several instances of each category in order for a model to be fit robustly. Setting this to `True` will skip these checks. |Optional Boolean, defaults to `False`. |
| `categories` | The categories to use for the categorical columns. If `auto`, the categories will be inferred for all categorical columns. Otherwise, this argument should have as many entries as there are categorical columns.<br><br>Each entry should be either `auto` to infer the values for that column or the list of values for the column.  If explicit values are provided, the first value is treated as the "control" value for that column against which other values are compared. | Optional, `auto` or list<sup>2</sup>. |
| `n_jobs` | The degree of parallelism to use. | Optional integer, defaults to 1. |
| `verbose` | Expresses whether to provide detailed output during the computation. | Optional integer, defaults to 1. |
| `random_state` | Seed for the pseudorandom number generator (PRNG). | Optional integer. |

<sup>2</sup> For the `list` parameters: Several of the parameters accept lists of other types (strings, numbers, even other lists). To pass these into the component, they must first be JSON-encoded into a single string.

This component has a single output port, which can be connected to one of the `insight_[n]` input ports of the `Gather RAI Insights Dashboard` component.

# [YAML](#tab/yaml)

```yml
  causal_01: 
    type: command 
    component: azureml://registries/azureml/components/microsoft_azureml_rai_tabular_causal/versions/<version>
    inputs: 
      rai_insights_dashboard: ${{parent.jobs.create_rai_job.outputs.rai_insights_dashboard}} 
      treatment_features: `["Number of GitHub repos contributed to", "YOE"]' 
```

# [Python SDK](#tab/python)

```python
#First load the component: 

        rai_causal_component = ml_client_registry.components.get(name="microsoft_azureml_rai_tabular_causal", label="latest")

#Use it inside a pipeline definition: 
            causal_job = rai_causal_component( 
                rai_insights_dashboard=construct_job.outputs.rai_insights_dashboard, 
                treatment_features='`["Number of GitHub repos contributed to", "YOE"]', 
            ) 
```


### Add Counterfactuals to RAI Insights dashboard

This component generates counterfactual points for the supplied test dataset. It has a single input port, which accepts the output of the RAI Insights dashboard constructor. It also accepts the following parameters: 

| Parameter name | Description | Type |
|---|---|---|
| `total_CFs` | The number of counterfactual points to generate for each row in the test dataset. | Optional integer, defaults to 10. |
| `method` | The `dice-ml` explainer to use. | Optional string. Either `random`, `genetic`, or `kdtree`. Defaults to `random`. |
| `desired_class` | Index identifying the desired counterfactual class. For binary classification, this should be set to `opposite`. | Optional string or integer. Defaults to 0. |
| `desired_range` | For regression problems, identify the desired range of outcomes. | Optional list of two numbers<sup>3</sup>. |
