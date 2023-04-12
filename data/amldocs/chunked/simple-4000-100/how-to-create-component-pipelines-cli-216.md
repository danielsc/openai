- [AzureML registered environment asset](https://github.com/Azure/azureml-examples/tree/sdk-preview/cli/jobs/pipelines-with-components/basics/5b_env_registered). It's referenced in component following `azureml:<environment-name>:<environment-version>` syntax.
- [public docker image](https://github.com/Azure/azureml-examples/tree/sdk-preview/cli/jobs/pipelines-with-components/basics/5a_env_public_docker_image)
- [conda file](https://github.com/Azure/azureml-examples/tree/sdk-preview/cli/jobs/pipelines-with-components/basics/5c_env_conda_file) Conda file needs to be used together with a base image.

## Register component for reuse and sharing

While some components will be specific to a particular pipeline, the real benefit of components comes from reuse and sharing. Register a component in your Machine Learning workspace to make it available for reuse. Registered components support automatic versioning so you can update the component but assure that pipelines that require an older version will continue to work.  

In the azureml-examples repository, navigate to the `cli/jobs/pipelines-with-components/basics/1b_e2e_registered_components` directory. 

To register a component, use the `az ml component create` command:

```azurecli
az ml component create --file train.yml
az ml component create --file score.yml
az ml component create --file eval.yml
```

After these commands run to completion, you can see the components in Studio, under Asset -> Components:

:::image type="content" source="./media/how-to-create-component-pipelines-cli/registered-components.png" alt-text="Screenshot of Studio showing the components that were just registered." lightbox ="./media/how-to-create-component-pipelines-cli/registered-components.png":::

Select a component. You'll see detailed information for each version of the component.

Under **Details** tab, you'll see basic information of the component like name, created by, version etc. You'll see editable fields for Tags and Description. The tags can be used for adding rapidly searched keywords. The description field supports Markdown formatting and should be used to describe your component's functionality and basic use.

Under **Jobs** tab, you'll see the history of all jobs that use this component.

:::image type="content" source="./media/how-to-create-component-pipelines-cli/registered-components.png" alt-text="Screenshot of the component tab showing 3 components." lightbox ="./media/how-to-create-component-pipelines-cli/registered-components.png":::

### Use registered components in a pipeline job YAML file

Let's use `1b_e2e_registered_components` to demo how to use registered component in pipeline YAML. Navigate to `1b_e2e_registered_components` directory, open the `pipeline.yml` file. The keys and values in the `inputs` and `outputs` fields are similar to those already discussed. The only significant difference is the value of the `component` field in the `jobs.<JOB_NAME>.component` entries. The `component` value is of the form `azureml:<COMPONENT_NAME>:<COMPONENT_VERSION>`. The `train-job` definition, for instance, specifies the latest version of the registered component `my_train` should be used:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json
type: pipeline
display_name: 1b_e2e_registered_components
description: E2E dummy train-score-eval pipeline with registered components

inputs:
  pipeline_job_training_max_epocs: 20
  pipeline_job_training_learning_rate: 1.8
  pipeline_job_learning_rate_schedule: 'time-based'

outputs: 
  pipeline_job_trained_model:
    mode: upload
  pipeline_job_scored_data:
    mode: upload
  pipeline_job_evaluation_report:
    mode: upload

settings:
 default_compute: azureml:cpu-cluster

jobs:
  train_job:
    type: command
    component: azureml:my_train@latest
    inputs:
      training_data: 
        type: uri_folder 
        path: ./data      
      max_epocs: ${{parent.inputs.pipeline_job_training_max_epocs}}
      learning_rate: ${{parent.inputs.pipeline_job_training_learning_rate}}
      learning_rate_schedule: ${{parent.inputs.pipeline_job_learning_rate_schedule}}
    outputs:
      model_output: ${{parent.outputs.pipeline_job_trained_model}}
    services: 
      my_vscode: 
        job_service_type: vs_code
      my_jupyter_lab: 
        job_service_type: jupyter_lab
      my_tensorboard:
        job_service_type: tensor_board
        properties:
          logDir: "outputs/tblogs"
    #  my_ssh:
    #    job_service_type: tensor_board
    #    properties:
    #      sshPublicKeys: <paste the entire pub key content>
    #    nodes: all # Use the `nodes` property to pick which node you want to enable interactive services on. If `nodes` are not selected, by default, interactive applications are only enabled on the head node.
  
  score_job:
    type: command
    component: azureml:my_score@latest
    inputs:
      model_input: ${{parent.jobs.train_job.outputs.model_output}}
      test_data: 
        type: uri_folder 
        path: ./data
    outputs:
      score_output: ${{parent.outputs.pipeline_job_scored_data}}

  evaluate_job:
    type: command
    component: azureml:my_eval@latest
    inputs:
      scoring_result: ${{parent.jobs.score_job.outputs.score_output}}
    outputs:
      eval_output: ${{parent.outputs.pipeline_job_evaluation_report}}
```
