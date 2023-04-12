
> [!NOTE]
> This Python code sample uses `pyspark.pandas`, which is only supported by Spark runtime version 3.2.

The above script takes two arguments `--titanic_data` and `--wrangled_data`, which pass the path of input data and output folder respectively.

# [Azure CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

To create a job, a standalone Spark job can be defined as a YAML specification file, which can be used in the `az ml job create` command, with the `--file` parameter. Define these properties in the YAML file as follows:

### YAML properties in the Spark job specification
- `type` - set to `spark`.
- `code` - defines the location of the folder that contains source code and scripts for this job.
- `entry` - defines the entry point for the job. It should cover one of these properties:
  - `file` - defines the name of the Python script that serves as an entry point for the job.
  - `class_name` - defines the name of the class that serves as an entry point for the job.
- `py_files` - defines a list of `.zip`, `.egg`, or `.py` files, to be placed in the `PYTHONPATH`, for successful execution of the job. This property is optional.
- `jars` - defines a list of `.jar` files to include on the Spark driver, and the executor `CLASSPATH`, for successful execution of the job. This property is optional.
- `files` - defines a list of files that should be copied to the working directory of each executor, for successful job execution. This property is optional.
- `archives` - defines a list of archives that should be extracted into the working directory of each executor, for successful job execution. This property is optional.
- `conf` - defines these Spark driver and executor properties:
  - `spark.driver.cores`: the number of cores for the Spark driver.
  - `spark.driver.memory`: allocated memory for the Spark driver, in gigabytes (GB).
  - `spark.executor.cores`: the number of cores for the Spark executor.
  - `spark.executor.memory`: the memory allocation for the Spark executor, in gigabytes (GB).
  - `spark.dynamicAllocation.enabled` - whether or not executors should be dynamically allocated, as a `True` or `False` value.
  -   If dynamic allocation of executors is enabled, define these properties:
      - `spark.dynamicAllocation.minExecutors` - the minimum number of Spark executors instances, for dynamic allocation.
      - `spark.dynamicAllocation.maxExecutors` - the maximum number of Spark executors instances, for dynamic allocation.
  -   If dynamic allocation of executors is disabled, define this property:
      - `spark.executor.instances` - the number of Spark executor instances.
- `environment` - an [Azure Machine Learning environment](./reference-yaml-environment.md) to run the job.
- `args` - the command line arguments that should be passed to the job entry point Python script or class. See the YAML specification file provided here for an example.
- `resources` - this property defines the resources to be used by an Azure Machine Learning Managed (Automatic) Spark compute. It uses the following properties:
  - `instance_type` - the compute instance type to be used for Spark pool. The following instance types are currently supported:
    - `standard_e4s_v3`
    - `standard_e8s_v3`
    - `standard_e16s_v3`
    - `standard_e32s_v3`
    - `standard_e64s_v3`
  - `runtime_version` - defines the Spark runtime version. The following Spark runtime versions are currently supported:
    - `3.1`
    - `3.2`

  An example is shown here:
  ```yaml
  resources:
    instance_type: standard_e8s_v3
    runtime_version: "3.2"
  ```
- `compute` - this property defines the name of an attached Synapse Spark pool, as shown in this example:
  ```yaml
  compute: mysparkpool
  ```
- `inputs` - this property defines inputs for the Spark job. Inputs for a Spark job can be either a literal value, or data stored in a file or folder.
  - A **literal value** can be a number, a boolean value or a string. Some examples are shown here:
