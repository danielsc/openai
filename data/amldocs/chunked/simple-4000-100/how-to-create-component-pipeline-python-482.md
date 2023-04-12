The pipeline has a pipeline level input `pipeline_input_data`. You can assign value to pipeline input when you submit a pipeline job.

The pipeline contains three nodes, prepare_data_node, train_node and score_node. 

- The `input_data` of `prepare_data_node` uses the value of `pipeline_input_data`.

- The `input_data` of `train_node` is from the `training_data` output of the prepare_data_node. 

- The `input_data` of score_node is from the `test_data` output of prepare_data_node, and the `input_model` is from the `output_model` of train_node. 
    
- Since `train_node` will train a CNN model, you can specify its compute as the gpu_compute_target, which can improve the training performance.

## Submit your pipeline job

Now you've constructed the pipeline, you can submit to your workspace. To submit a job, you need to firstly connect to a workspace.

### Get access to your workspace

#### Configure credential

We'll use `DefaultAzureCredential` to get access to the workspace. `DefaultAzureCredential` should be capable of handling most Azure SDK authentication scenarios.

Reference for more available credentials if it doesn't work for you: [configure credential example](https://github.com/Azure/MachineLearningNotebooks/blob/master/configuration.ipynb), [azure-identity reference doc](/python/api/azure-identity/azure.identity?view=azure-python&preserve-view=true ).


```python
try:
    credential = DefaultAzureCredential()
    # Check if given credential can get token successfully.
    credential.get_token("https://management.azure.com/.default")
except Exception as ex:
    # Fall back to InteractiveBrowserCredential in case DefaultAzureCredential not work
    credential = InteractiveBrowserCredential()
```

#### Get a handle to a workspace with compute

Create a `MLClient` object to manage Azure Machine Learning services.

```python
# Get a handle to workspace
ml_client = MLClient.from_config(credential=credential)

# Retrieve an already attached Azure Machine Learning Compute.
cpu_compute_target = "cpu-cluster"
print(ml_client.compute.get(cpu_compute_target))
gpu_compute_target = "gpu-cluster"
print(ml_client.compute.get(gpu_compute_target))
```

> [!IMPORTANT]
> This code snippet expects the workspace configuration json file to be saved in the current directory or its parent. For more information on creating a workspace, see [Create workspace resources](quickstart-create-resources.md). For more information on saving the configuration to file, see [Create a workspace configuration file](how-to-configure-environment.md#local-and-dsvm-only-create-a-workspace-configuration-file).

#### Submit pipeline job to workspace

Now you've get a handle to your workspace, you can submit your pipeline job.

```python
pipeline_job = ml_client.jobs.create_or_update(
    pipeline_job, experiment_name="pipeline_samples"
)
pipeline_job
```


The code above submit this image classification pipeline job to experiment called `pipeline_samples`. It will auto create the experiment if not exists. The `pipeline_input_data` uses `fashion_ds`.

The call to `pipeline_job`produces output similar to:

The call to `submit` the `Experiment` completes quickly, and produces output similar to:

| Experiment | Name | Type | Status | Details Page |
| --- | ---- | ----------- | -------------- | ------------- |
| pipeline_samples | sharp_pipe_4gvqx6h1fb | pipeline | Preparing | Link to Azure Machine Learning studio. |

You can monitor the pipeline run by opening the link or you can block until it completes by running:

```python
# wait until the job completes
ml_client.jobs.stream(pipeline_job.name)
```

> [!IMPORTANT]
> The first pipeline run takes roughly *15 minutes*. All dependencies must be downloaded, a Docker image is created, and the Python environment is provisioned and created. Running the pipeline again takes significantly less time because those resources are reused instead of created. However, total run time for the pipeline depends on the workload of your scripts and the processes that are running in each pipeline step.
