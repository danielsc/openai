- **component_src**: This is the source code directory for a specific component. It contains the source code that will be executed in the component. You can use your preferred language(Python, R...). The code must be executed by a shell command. The source code can take a few inputs from shell command line to control how this step is going to be executed. For example, a training step may take training data, learning rate, number of epochs to control the training process. The argument of a shell command is used to pass inputs and outputs to the code. 

 Now let's create a pipeline using the `3b_pipeline_with_data` example. We'll explain the detailed meaning of each file in following sections. 
 
 First list your available compute resources with the following command: 

```azurecli
az ml compute list
```

If you don't have it, create a cluster called `cpu-cluster` by running:

```azurecli
az ml compute create -n cpu-cluster --type amlcompute --min-instances 0 --max-instances 10
```

Now, create a pipeline job defined in the pipeline.yml file with the following command. The compute target will be referenced in the pipeline.yml file as `azureml:cpu-cluster`. If your compute target uses a different name, remember to update it in the pipeline.yml file. 

```azurecli
az ml job create --file pipeline.yml
```

You should receive a JSON dictionary with information about the pipeline job, including:

| Key                        | Description                                                           |
|----------------------------|-----------------------------------------------------------------------|
| `name`                     | The GUID-based name of the job.                                       |
| `experiment_name`          | The name under which jobs will be organized in Studio.                |
| `services.Studio.endpoint` | A URL for monitoring and reviewing the pipeline job.                  |
| `status`                   | The status of the job. This will likely be `Preparing` at this point. |

Open the `services.Studio.endpoint` URL you'll see a graph visualization of the pipeline looks like below.

:::image type="content" source="./media/how-to-create-component-pipelines-cli/pipeline-graph-dependencies.png" alt-text="Screenshot of a graph visualization of the pipeline.":::

## Understand the pipeline definition YAML

Let's take a look at the pipeline definition in the *3b_pipeline_with_data/pipeline.yml* file.  

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json
type: pipeline

display_name: 3b_pipeline_with_data
description: Pipeline with 3 component jobs with data dependencies

settings:
  default_compute: azureml:cpu-cluster

outputs:
  final_pipeline_output:
    mode: rw_mount

jobs:
  component_a:
    type: command
    component: ./componentA.yml
    inputs:
      component_a_input: 
        type: uri_folder
        path: ./data

    outputs:
      component_a_output: 
        mode: rw_mount
  component_b:
    type: command
    component: ./componentB.yml
    inputs:
      component_b_input: ${{parent.jobs.component_a.outputs.component_a_output}}
    outputs:
      component_b_output: 
        mode: rw_mount
  component_c:
    type: command
    component: ./componentC.yml
    inputs:
      component_c_input: ${{parent.jobs.component_b.outputs.component_b_output}}
    outputs:
      component_c_output: ${{parent.outputs.final_pipeline_output}}
      #  mode: upload


```

Below table describes the most common used fields of pipeline YAML schema. See [full pipeline YAML schema here](reference-yaml-job-pipeline.md).  

|key|description|
|------|------|
|type|**Required**. Job type, must be `pipeline` for pipeline jobs.|
|display_name|Display name of the pipeline job in Studio UI. Editable in Studio UI. Doesn't have to be unique across all jobs in the workspace.|
|jobs|**Required**. Dictionary of the set of individual jobs to run as steps within the pipeline. These jobs are considered child jobs of the parent pipeline job. In this release, supported job types in pipeline are `command` and `sweep`
