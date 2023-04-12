|jobs|**Required**. Dictionary of the set of individual jobs to run as steps within the pipeline. These jobs are considered child jobs of the parent pipeline job. In this release, supported job types in pipeline are `command` and `sweep`
|inputs|Dictionary of inputs to the pipeline job. The key is a name for the input within the context of the job and the value is the input value. These pipeline inputs can be referenced by the inputs of an individual step job in the pipeline using the ${{ parent.inputs.<input_name> }} expression.|
|outputs|Dictionary of output configurations of the pipeline job. The key is a name for the output within the context of the job and the value is the output configuration. These pipeline outputs can be referenced by the outputs of an individual step job in the pipeline using the ${{ parents.outputs.<output_name> }} expression. |

In the *3b_pipeline_with_data* example, we've created a three steps pipeline.

- The three steps are defined under `jobs`. All three step type is command job. Each step's definition is in corresponding `component.yml` file. You can see the component YAML files under *3b_pipeline_with_data* directory. We'll explain the componentA.yml in next section.
- This pipeline has data dependency, which is common in most real world pipelines. Component_a takes data input from local folder under `./data`(line 17-20) and passes its output to componentB (line 29). Component_a's output can be referenced as `${{parent.jobs.component_a.outputs.component_a_output}}`.
- The `compute` defines the default compute for this pipeline. If a component under `jobs` defines a different compute for this component, the system will respect component specific setting.

:::image type="content" source="./media/how-to-create-component-pipelines-cli/pipeline-inputs-and-outputs.png" alt-text="Screenshot of the pipeline with data example above." lightbox ="./media/how-to-create-component-pipelines-cli/pipeline-inputs-and-outputs.png":::

### Read and write data in pipeline

One common scenario is to read and write data in your pipeline. In AzureML, we use the same schema to [read and write data](how-to-read-write-data-v2.md) for all type of jobs (pipeline job, command job, and sweep job). Below are pipeline job examples of using data for common scenarios.

- [local data](https://github.com/Azure/azureml-examples/tree/sdk-preview/cli/jobs/pipelines-with-components/basics/4a_local_data_input)
- [web file with public URL](https://github.com/Azure/azureml-examples/blob/sdk-preview/cli/jobs/pipelines-with-components/basics/4c_web_url_input/pipeline.yml)
- [AzureML datastore and path](https://github.com/Azure/azureml-examples/tree/sdk-preview/cli/jobs/pipelines-with-components/basics/4b_datastore_datapath_uri)
- [AzureML data asset](https://github.com/Azure/azureml-examples/tree/sdk-preview/cli/jobs/pipelines-with-components/basics/4d_data_input)

## Understand the component definition YAML

Now let's look at the *componentA.yml* as an example to understand component definition YAML.

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandComponent.schema.json
type: command

name: component_a
display_name: componentA
version: 1

inputs:
  component_a_input:
    type: uri_folder

outputs:
  component_a_output:
    type: uri_folder

code: ./componentA_src

environment: 
  image: python

command: >-
  python hello.py --componentA_input ${{inputs.component_a_input}} --componentA_output ${{outputs.component_a_output}}

```

The most common used schema of the component YAML is described in below table. See [full component YAML schema here](reference-yaml-component-command.md).

|key|description|
|------|------|
|name|**Required**. Name of the component. Must be unique across the AzureML workspace. Must start with lowercase letter. Allow lowercase letters, numbers and underscore(_). Maximum length is 255 characters.|
|display_name|Display name of the component in the studio UI. Can be non-unique within the workspace.|
