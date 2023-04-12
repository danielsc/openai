  - A **literal value** can be a number, a boolean value or a string. Some examples are shown here:
      ```yaml
      inputs:
        sampling_rate: 0.02 # a number
        hello_number: 42 # an integer
        hello_string: "Hello world" # a string
        hello_boolean: True # a boolean value
      ```
  - **Data** stored in a file or folder should be defined using these properties:
    - `type` - set this property to `uri_file`, or `uri_folder`, for input data contained in a file or a folder respectively.
    - `path` - the URI of the input data, such as `azureml://`, `abfss://`, or `wasbs://`.
    - `mode` - set this property to `direct`.
      This sample shows the definition of a job input, which can be referred to as `$${inputs.titanic_data}}`:
      ```YAML
      inputs:
        titanic_data:
          type: uri_file
          path: azureml://datastores/workspaceblobstore/paths/data/titanic.csv
          mode: direct
      ```
- `outputs` - this property defines the Spark job outputs. Outputs for a Spark job can be written to either a file or a folder location, which is defined using the following three properties:
  - `type` - this property can be set to `uri_file` or `uri_folder` for writing output data to a file or a folder respectively.
  - `path` - this property defines the output location URI, such as `azureml://`, `abfss://`, or `wasbs://`.
  - `mode` - set this property to `direct`.
    This sample shows the definition of a job output, which can be referred to as `${{outputs.wrangled_data}}`:
    ```YAML
    outputs:
      wrangled_data:
        type: uri_folder
        path: azureml://datastores/workspaceblobstore/paths/data/wrangled/
        mode: direct
    ```
- `identity` - this optional property defines the identity used to submit this job. It can have `user_identity` and `managed` values. If no identity is defined in the YAML specification, the default identity will be used.
 
### Standalone Spark job
This example YAML specification shows a standalone Spark job. It uses an Azure Machine Learning Managed (Automatic) Spark compute:

```yaml
$schema: http://azureml/sdk-2-0/SparkJob.json
type: spark

code: ./ 
entry:
  file: titanic.py

conf:
  spark.driver.cores: 1
  spark.driver.memory: 2g
  spark.executor.cores: 2
  spark.executor.memory: 2g
  spark.executor.instances: 2

inputs:
  titanic_data:
    type: uri_file
    path: azureml://datastores/workspaceblobstore/paths/data/titanic.csv
    mode: direct

outputs:
  wrangled_data:
    type: uri_folder
    path: azureml://datastores/workspaceblobstore/paths/data/wrangled/
    mode: direct

args: >-
  --titanic_data ${{inputs.titanic_data}}
  --wrangled_data ${{outputs.wrangled_data}}

identity:
  type: user_identity

resources:
  instance_type: standard_e4s_v3
  runtime_version: "3.2"
```

> [!NOTE]
> To use an attached Synapse Spark pool, define the `compute` property in the sample YAML specification file shown above, instead of the `resources` property.

The YAML files shown above can be used in the `az ml job create` command, with the `--file` parameter, to create a standalone Spark job as shown:

```azurecli
az ml job create --file <YAML_SPECIFICATION_FILE_NAME>.yaml --subscription <SUBSCRIPTION_ID> --resource-group <RESOURCE_GROUP> --workspace-name <AML_WORKSPACE_NAME>
```

You can execute the above command from:
- [terminal of an Azure Machine Learning compute instance](how-to-access-terminal.md#access-a-terminal). 
- terminal of [Visual Studio Code connected to an Azure Machine Learning compute instance](./how-to-set-up-vs-code-remote.md?tabs=studio).
- your local computer that has [Azure Machine Learning CLI](./how-to-configure-cli.md?tabs=public) installed.

# [Python SDK](#tab/sdk)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

### Standalone Spark job using Python SDK 
To create a standalone Spark job, use the `azure.ai.ml.spark` function, with these parameters:
- `name` - the name of the Spark job.
- `display_name` - the display name of the Spark job that should be displayed in the UI and elsewhere.
