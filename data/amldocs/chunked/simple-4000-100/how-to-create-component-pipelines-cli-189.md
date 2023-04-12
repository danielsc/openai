|display_name|Display name of the component in the studio UI. Can be non-unique within the workspace.|
|command|**Required** the command to execute|
|code|Local path to the source code directory to be uploaded and used for the component.|
|environment|**Required**. The environment that will be used to execute the component.|
|inputs|Dictionary of component inputs. The key is a name for the input within the context of the component and the value is the component input definition. Inputs can be referenced in the command using the ${{ inputs.<input_name> }} expression.|
|outputs|Dictionary of component outputs. The key is a name for the output within the context of the component and the value is the component output definition. Outputs can be referenced in the command using the ${{ outputs.<output_name> }} expression.|
|is_deterministic|Whether to reuse the previous job's result if the component inputs did not change. Default value is `true`, also known as reuse by default. The common scenario when set as `false` is to force reload data from a cloud storage or URL.|

For the example in *3b_pipeline_with_data/componentA.yml*, componentA has one data input and one data output, which can be connected to other steps in the parent pipeline. All the files under `code` section in component YAML will be uploaded to AzureML when submitting the pipeline job. In this example, files under `./componentA_src` will be uploaded (line 16 in *componentA.yml*). You can see the uploaded source code in Studio UI: double select the ComponentA step and navigate to Snapshot tab, as shown in below screenshot. We can see it's a hello-world script just doing some simple printing, and write current datetime to the `componentA_output` path. The component takes input and output through command line argument, and it's handled in the *hello.py* using `argparse`.
  
:::image type="content" source="./media/how-to-create-component-pipelines-cli/component-snapshot.png" alt-text="Screenshot of pipeline with data example above showing componentA." lightbox="./media/how-to-create-component-pipelines-cli/component-snapshot.png":::

### Input and output
Input and output define the interface of a component. Input and output could be either of a literal value(of type `string`,`number`,`integer`, or `boolean`) or an object containing input schema.

**Object input** (of type `uri_file`, `uri_folder`,`mltable`,`mlflow_model`,`custom_model`) can connect to other steps in the parent pipeline job and hence pass data/model to other steps. In pipeline graph, the object type input will render as a connection dot.

**Literal value inputs** (`string`,`number`,`integer`,`boolean`) are the parameters you can pass to the component at run time. You can add default value of literal inputs under `default` field. For `number` and `integer` type, you can also add minimum and maximum value of the accepted value using `min` and `max` fields. If the input value exceeds the min and max, pipeline will fail at validation. Validation happens before you submit a pipeline job to save your time. Validation works for CLI, Python SDK and designer UI. Below screenshot shows a validation example in designer UI. Similarly, you can define allowed values in `enum` field.

:::image type="content" source="./media/how-to-create-component-pipelines-cli/component-input-output.png" alt-text="Screenshot of the input and output of the train linear regression model component." lightbox= "./media/how-to-create-component-pipelines-cli/component-input-output.png":::

If you want to add an input to a component, remember to edit three places:  1)`inputs` field in component YAML 2) `command` field in component YAML. 3) component source code to handle the command line input. It's marked in green box in above screenshot.  

### Environment

Environment defines the environment to execute the component. It could be an AzureML environment(curated or custom registered), docker image or conda environment. See examples below.

- [AzureML registered environment asset](https://github.com/Azure/azureml-examples/tree/sdk-preview/cli/jobs/pipelines-with-components/basics/5b_env_registered). It's referenced in component following `azureml:<environment-name>:<environment-version>` syntax.
