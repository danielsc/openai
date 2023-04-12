            1. For **Output URI destination**, enter a storage data URI (for example, `abfss://` or `wasbs://` URI) or enter a data asset `azureml://`.
        1. Enter **Arguments** by using the names defined in the **Input name** and **Output name** fields in the earlier steps, and the names of input and output arguments used in the Python script **Entry file**. For example, if the **Input name** and **Output name** are defined as `job_input` and `job_output`, and the arguments are added in the **Entry file** as shown here

            ``` python
            import argparse

            parser = argparse.ArgumentParser()
            parser.add_argument("--input_param")
            parser.add_argument("--output_param")
            ```

    then enter **Arguments** as `--input_param ${{inputs.job_input}} --output_param ${{outputs.job_output}}`.
    1. Under the **Spark configurations** section:
        1. For **Executor size**:
            1. Enter the number of executor **Cores** and executor **Memory (GB)**, in gigabytes.
            1. For **Dynamically allocated executors**, select the **Disabled** or **Enabled** option.
        - If dynamic allocation of executors is **Disabled**, enter the number of **Executor instances**.
        - If dynamic allocation of executors is **Enabled**, use the slider to select the minimum and maximum number of executors.
        1. For **Driver size**:
            1. Enter number of driver **Cores** and driver **Memory (GB)**, in gigabytes.
            1. Enter **Name** and **Value** pairs for any **Additional configurations**, then select **Add**. Providing **Additional configurations** is optional.
    1. Select **Next**.
1. On the **Review** screen:
    1. Review the job specification before submitting it.
    1. Select **Create** to submit the standalone Spark job.


## Spark component in a pipeline job
A Spark component offers the flexibility to use the same component in multiple [Azure Machine Learning pipelines](./concept-ml-pipelines.md), as a pipeline step.

# [Azure CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

YAML syntax for a Spark component resembles the [YAML syntax for Spark job specification](#yaml-properties-in-the-spark-job-specification) in most ways. These properties are defined differently in the Spark component YAML specification:
- `name` - the name of the Spark component.
- `version` - the version of the Spark component.
- `display_name` - the name of the Spark component to display in the UI and elsewhere.
- `description` - the description of the Spark component.
- `inputs` - this property is similar to `inputs` property described in [YAML syntax for Spark job specification](#yaml-properties-in-the-spark-job-specification), except that it doesn't define the `path` property. This code snippet shows an example of the Spark component `inputs` property:

  ```yaml
  inputs:
    titanic_data:
      type: uri_file
      mode: direct
  ```

- `outputs` - this property is similar to the `outputs` property described in [YAML syntax for Spark job specification](#yaml-properties-in-the-spark-job-specification), except that it doesn't define the `path` property. This code snippet shows an example of the Spark component `outputs` property:

  ```yaml
  outputs:
    wrangled_data:
      type: uri_folder
      mode: direct
  ```

> [!NOTE]
> A Spark component does not define `identity`, `compute` or `resources` properties. The pipeline YAML specification file defines these properties.

This YAML specification file provides an example of a Spark component:

```yaml
$schema: http://azureml/sdk-2-0/SparkComponent.json
name: titanic_spark_component
type: spark
version: 1
display_name: Titanic-Spark-Component
description: Spark component for Titanic data

code: ./src
entry:
  file: titanic.py

inputs:
  titanic_data:
    type: uri_file
    mode: direct

outputs:
  wrangled_data:
    type: uri_folder
    mode: direct

args: >-
  --titanic_data ${{inputs.titanic_data}}
  --wrangled_data ${{outputs.wrangled_data}}

conf:
  spark.driver.cores: 1
  spark.driver.memory: 2g
  spark.executor.cores: 2
  spark.executor.memory: 2g
  spark.dynamicAllocation.enabled: True
  spark.dynamicAllocation.minExecutors: 1
  spark.dynamicAllocation.maxExecutors: 4
```
