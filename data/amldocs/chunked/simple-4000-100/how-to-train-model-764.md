The `az ml job create` command used in this example requires a YAML job definition file. The contents of the file used in this example are:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
code: src
command: >-
  python main.py 
  --iris-csv ${{inputs.iris_csv}}
  --C ${{inputs.C}}
  --kernel ${{inputs.kernel}}
  --coef0 ${{inputs.coef0}}
inputs:
  iris_csv: 
    type: uri_file
    path: wasbs://datasets@azuremlexamples.blob.core.windows.net/iris.csv
  C: 0.8
  kernel: "rbf"
  coef0: 0.1
environment: azureml:AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest
compute: azureml:cpu-cluster
display_name: sklearn-iris-example
experiment_name: sklearn-iris-example
description: Train a scikit-learn SVM on the Iris dataset.

```
In the above, you configured:
- `code` - path where the code to run the command is located
- `command` - command that needs to be run
- `inputs` - dictionary of inputs using name value pairs to the command. The key is a name for the input within the context of the job and the value is the input value. Inputs are referenced in the `command` using the `${{inputs.<input_name>}}` expression. 
- `environment` - the environment needed to run the training script. In this example, we use a curated or ready-made environment provided by AzureML called `AzureML-sklearn-0.24-ubuntu18.04-py37-cpu`. We use the latest version of this environment by using the `@latest` directive. You can also use custom environments by specifying a base docker image and specifying a conda yaml on top of it.
To submit the job, use the following command. The run ID (name) of the training job is stored in the `$run_id` variable:

```azurecli
run_id=$(az ml job create -f jobs/single-step/scikit-learn/iris/job.yml --query name -o tsv)
```

You can use the stored run ID to return information about the job. The `--web` parameter opens the AzureML studio web UI where you can drill into details on the job:

```azurecli
# <hello_world>
az ml job create -f jobs/basics/hello-world.yml --web
# </hello_world>

# <hello_world_set>
az ml job create -f jobs/basics/hello-world.yml \
  --set environment.image="python:3.8" \
  --web
# </hello_world_set>

# <hello_world_name>
run_id=$(az ml job create -f jobs/basics/hello-world.yml --query name -o tsv)
# </hello_world_name>

# <hello_world_show>
az ml job show -n $run_id --web
# </hello_world_show>

# <hello_world_org>
az ml job create -f jobs/basics/hello-world-org.yml --web
# </hello_world_org>

run_id=$(az ml job create -f jobs/basics/hello-world-org.yml --query name -o tsv)
# <hello_world_org_set>
az ml job update -n $run_id --set \
  display_name="updated display name" \
  experiment_name="updated experiment name" \
  description="updated description"  \
  tags.hello="updated tag"
# </hello_world_org_set>

# <hello_world_env_var>
az ml job create -f jobs/basics/hello-world-env-var.yml --web
# </hello_world_env_var>

# <hello_mlflow>
az ml job create -f jobs/basics/hello-mlflow.yml --web
# </hello_mlflow>

# <mlflow_uri>
az ml workspace show --query mlflow_tracking_uri -o tsv
# </mlflow_uri>

# <hello_world_input>
az ml job create -f jobs/basics/hello-world-input.yml --web
# </hello_world_input>

# <hello_world_input_set>
az ml job create -f jobs/basics/hello-world-input.yml --set \
  inputs.hello_string="hello there" \
  inputs.hello_number=24 \
  --web
# </hello_world_input_set>

# <hello_sweep>
az ml job create -f jobs/basics/hello-sweep.yml --web
# </hello_sweep>

# <hello_world_output>
az ml job create -f jobs/basics/hello-world-output.yml --web
# </hello_world_output>

run_id=$(az ml job create -f jobs/basics/hello-world-output.yml --query name -o tsv)
if [[ -z "$run_id" ]]
then
  echo "Job creation failed"
  exit 3
fi
status=$(az ml job show -n $run_id --query status -o tsv)
if [[ -z "$status" ]]
then
  echo "Status query failed"
  exit 4
fi
running=("Queued" "Starting" "Preparing" "Running" "Finalizing")
while [[ ${running[*]} =~ $status ]]
do
  sleep 8 
  status=$(az ml job show -n $run_id --query status -o tsv)
  echo $status
done

# <hello_world_output_download>
az ml job download -n $run_id
# </hello_world_output_download>
rm -r $run_id

# <iris_file>
az ml job create -f jobs/basics/hello-iris-file.yml --web
# </iris_file>

# <iris_folder>
az ml job create -f jobs/basics/hello-iris-folder.yml --web
# </iris_folder>

# <iris_datastore_file>
az ml job create -f jobs/basics/hello-iris-datastore-file.yml --web
# </iris_datastore_file>

# <iris_datastore_folder>
az ml job create -f jobs/basics/hello-iris-datastore-folder.yml --web
# </iris_datastore_folder>

# <hello_world_output_data>
az ml job create -f jobs/basics/hello-world-output-data.yml --web
# </hello_world_output_data>

# <hello_pipeline>
az ml job create -f jobs/basics/hello-pipeline.yml --web
# </hello_pipeline>

# <hello_pipeline_io>
az ml job create -f jobs/basics/hello-pipeline-io.yml --web
# </hello_pipeline_io>

# <hello_pipeline_settings>
az ml job create -f jobs/basics/hello-pipeline-settings.yml --web
# </hello_pipeline_settings>

# <hello_pipeline_abc>
az ml job create -f jobs/basics/hello-pipeline-abc.yml --web
# </hello_pipeline_abc>

# <sklearn_iris>
az ml job create -f jobs/single-step/scikit-learn/iris/job.yml --web
# </sklearn_iris>

run_id=$(az ml job create -f jobs/single-step/scikit-learn/iris/job.yml --query name -o tsv)
if [[ -z "$run_id" ]]
then
  echo "Job creation failed"
  exit 3
fi
status=$(az ml job show -n $run_id --query status -o tsv)
if [[ -z "$status" ]]
then
  echo "Status query failed"
  exit 4
fi
running=("Queued" "Starting" "Preparing" "Running" "Finalizing")
while [[ ${running[*]} =~ $status ]]
do
  sleep 8 
  status=$(az ml job show -n $run_id --query status -o tsv)
  echo $status
done

# <sklearn_download_register_model>
az ml model create -n sklearn-iris-example -v 1 -p runs:/$run_id/model --type mlflow_model
# </sklearn_download_register_model>
rm -r $run_id

# <sklearn_sweep>
az ml job create -f jobs/single-step/scikit-learn/iris/job-sweep.yml --web
# </sklearn_sweep>

# <pytorch_cifar>
az ml job create -f jobs/single-step/pytorch/cifar-distributed/job.yml --web
# </pytorch_cifar>

# # <pipeline_cifar>
# az ml job create -f jobs/pipelines/cifar-10/pipeline.yml --web
# # </pipeline_cifar>

```
