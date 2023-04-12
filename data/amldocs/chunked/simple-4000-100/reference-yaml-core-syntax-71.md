You can specify literal values, URI paths, and registered Azure ML data assets as inputs to a job. The `command` can then be parameterized with references to those input(s) using the `${{inputs.<input_name>}}` syntax. References to literal inputs will get resolved to the literal value at runtime, while references to data inputs will get resolved to the download path or mount path (depending on the `mode` specified).

Likewise, outputs to the job can also be referenced in the `command`. For each named output specified in the `outputs` dictionary, Azure ML will system-generate an output location on the default datastore where you can write files to. The output location for each named output is based on the following templatized path: `<default-datastore>/azureml/<job-name>/<output_name>/`. Parameterizing the `command` with the `${{outputs.<output_name>}}` syntax will resolve that reference to the system-generated path, so that your script can write files to that location from the job.

In the example below for a command job YAML file, the `command` is parameterized with two inputs, a literal input and a data input, and one output. At runtime, the `${{inputs.learning_rate}}` expression will resolve to `0.01`, and the `${{inputs.iris}}` expression will resolve to the download path of the `iris.csv` file. `${{outputs.model_dir}}` will resolve to the mount path of the system-generated output location corresponding to the `model_dir` output.

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
code: ./src
command: python train.py --lr ${{inputs.learning_rate}} --training-data ${{inputs.iris}} --model-dir ${{outputs.model_dir}}
environment: azureml:AzureML-Minimal@latest
compute: azureml:cpu-cluster
inputs:
  learning_rate: 0.01
  iris:
    type: uri_file
    path: https://azuremlexamples.blob.core.windows.net/datasets/iris.csv
    mode: download
outputs:
  model_dir:
```

### Parameterizing the `command` with the `search_space` context of a sweep job

You will also use this expression syntax when performing hyperparameter tuning via a sweep job, since the actual values of the hyperparameters are not known during job authoring time. When you run a sweep job, Azure ML will select hyperparameter values for each trial based on the `search_space`. In order to access those values in your training script, you must pass them in via the script's command-line arguments. To do so, use the `${{search_space.<hyperparameter>}}` syntax in the `trial.command`.

In the example below for a sweep job YAML file, the `${{search_space.learning_rate}}` and `${{search_space.boosting}}` references in `trial.command` will resolve to the actual hyperparameter values selected for each trial when the trial job is submitted for execution.

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/sweepJob.schema.json
type: sweep
sampling_algorithm:
  type: random
search_space:
  learning_rate:
    type: uniform
    min_value: 0.01
    max_value: 0.9
  boosting:
    type: choice
    values: ["gbdt", "dart"]
objective:
  goal: minimize
  primary_metric: test-multi_logloss
trial:
  code: ./src
  command: >-
    python train.py 
    --training-data ${{inputs.iris}}
    --lr ${{search_space.learning_rate}}
    --boosting ${{search_space.boosting}}
  environment: azureml:AzureML-Minimal@latest
inputs:
  iris:
    type: uri_file
    path: https://azuremlexamples.blob.core.windows.net/datasets/iris.csv
    mode: download
compute: azureml:cpu-cluster
```

### Binding inputs and outputs between steps in a pipeline job

Expressions are also used for binding inputs and outputs between steps in a pipeline job. For example, you can bind the input of one job (job B) in a pipeline to the output of another job (job A). This usage will signal to Azure ML the dependency flow of the pipeline graph, and job B will get executed after job A, since the output of job A is required as an input for job B.

For a pipeline job YAML file, the `inputs` and `outputs` sections of each child job are evaluated within the parent context (the top-level pipeline job). The `command`, on the other hand, will resolve to the current context (the child job).
