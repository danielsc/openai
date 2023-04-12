

# [Python SDK](#tab/python)

```python
#First load the component: 
        rai_explanation_component = ml_client_registry.components.get(name="microsoft_azureml_rai_tabular_explanation", label="latest"

#Use inside a pipeline: 
            explain_job = rai_explanation_component( 
                comment="My comment", 
                rai_insights_dashboard=create_rai_job.outputs.rai_insights_dashboard, 
            ) 
```

### Gather RAI Insights dashboard

This component assembles the generated insights into a single Responsible AI dashboard. It has five input ports: 

- The `constructor` port that must be connected to the RAI Insights dashboard constructor component.
- Four `insight_[n]` ports that can be connected to the output of the tool components. At least one of these ports must be connected.

There are two output ports: 
- The `dashboard` port contains the completed `RAIInsights` object.
- The `ux_json` port contains the data required to display a minimal dashboard.


# [YAML](#tab/yaml)

```yml
  gather_01: 
    type: command 
    component: azureml://registries/azureml/components/microsoft_azureml_rai_tabular_insight_gather/versions/<version>
    inputs: 
      constructor: ${{parent.jobs.create_rai_job.outputs.rai_insights_dashboard}} 
      insight_1: ${{parent.jobs.causal_01.outputs.causal}} 
      insight_2: ${{parent.jobs.counterfactual_01.outputs.counterfactual}} 
      insight_3: ${{parent.jobs.error_analysis_01.outputs.error_analysis}} 
      insight_4: ${{parent.jobs.explain_01.outputs.explanation}} 
```


# [Python SDK](#tab/python)

```python
#First load the component: 
        rai_gather_component = ml_client_registry.components.get(name="microsoft_azureml_rai_tabular_insight_gather", label="latest")
#Use in a pipeline: 
            rai_gather_job = rai_gather_component( 
                constructor=create_rai_job.outputs.rai_insights_dashboard, 
                insight_1=explain_job.outputs.explanation, 
                insight_2=causal_job.outputs.causal, 
                insight_3=counterfactual_job.outputs.counterfactual, 
                insight_4=erroranalysis_job.outputs.error_analysis, 
            ) 
```



## How to generate a Responsible AI scorecard (preview)

The configuration stage requires you to use your domain expertise around the problem to set your desired target values on model performance and fairness metrics. 

Like other Responsible AI dashboard components configured in the YAML pipeline, you can add a component to generate the scorecard in the YAML pipeline:

```yml
scorecard_01: 

   type: command 
   component: azureml:rai_score_card@latest 
   inputs: 
     dashboard: ${{parent.jobs.gather_01.outputs.dashboard}} 
     pdf_generation_config: 
       type: uri_file 
       path: ./pdf_gen.json 
       mode: download 

     predefined_cohorts_json: 
       type: uri_file 
       path: ./cohorts.json 
       mode: download 

```

Where pdf_gen.json is the score card generation configuration json file, and *predifined_cohorts_json* ID the prebuilt cohorts definition json file. 

Here's a sample JSON file for cohorts definition and scorecard-generation configuration:


Cohorts definition:
```yml
[ 
  { 
    "name": "High Yoe", 
    "cohort_filter_list": [ 
      { 
        "method": "greater", 
        "arg": [ 
          5 
        ], 
        "column": "YOE" 
      } 
    ] 
  }, 
  { 
    "name": "Low Yoe", 
    "cohort_filter_list": [ 
      { 
        "method": "less", 
        "arg": [ 
          6.5 
        ], 
        "column": "YOE" 
      } 
    ] 
  } 
] 
```

Here's a scorecard-generation configuration file as a regression example:

```yml
{ 
  "Model": { 
    "ModelName": "GPT-2 Access", 
    "ModelType": "Regression", 
    "ModelSummary": "This is a regression model to analyze how likely a programmer is given access to GPT-2" 
  }, 
  "Metrics": { 
    "mean_absolute_error": { 
      "threshold": "<=20" 
    }, 
    "mean_squared_error": {} 
  }, 
  "FeatureImportance": { 
    "top_n": 6 
  }, 
  "DataExplorer": { 
    "features": [ 
      "YOE", 
      "age" 
    ] 
  }, 
  "Fairness": {
    "metric": ["mean_squared_error"],
    "sensitive_features": ["YOUR SENSITIVE ATTRIBUTE"],
    "fairness_evaluation_kind": "difference OR ratio"
  },
  "Cohorts": [ 
    "High Yoe", 
    "Low Yoe" 
  ]  
} 
```
