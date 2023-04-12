> If you have not configured the default workspace and resource group as explained in the prerequisites section, you will need to specify the `--workspace-name` and `--resource-group` parameters for the `az ml job create` to work.


Alternatively, ou can skip editing `single-job-pipeline.yml` and override the component name used by `train_job` in the CLI.

```azurecli
az ml job create --file single-job-pipeline.yml --set jobs.train_job.component=azureml://registries/<registry-name>/component/train_linear_regression_model/versions/1
```

Since the component used in the training job is shared through a registry, you can submit the job to any workspace that you have access to in your organization, even across different subscriptions. For example, if you have `dev-workspace`, `test-workspace` and `prod-workspace`, running the training job in these three workspaces is as easy as running three `az ml job create` commands. 

```azurecli
az ml job create --file single-job-pipeline.yml --workspace-name dev-workspace --resource-group <resource-group-of-dev-workspace>
az ml job create --file single-job-pipeline.yml --workspace-name test-workspace --resource-group <resource-group-of-test-workspace>
az ml job create --file single-job-pipeline.yml --workspace-name prod-workspace --resource-group <resource-group-of-prod-workspace>
```

# [Python SDK](#tab/python)

You'll run a pipeline job with the Scikit Learn training component created in the previous section to train a model. The training dataset is located in the `cli/jobs/pipelines-with-components/nyc_taxi_data_regression/data_transformed` folder. Construct the pipeline using the component created in the previous step. 

The key aspect is that this pipeline is going to run in a workspace using a component that isn't in the specific workspace. The component is in a registry that can be used with any workspace in your organization. You can run this training job in any workspace you have access to without having worry about making the training code and environment available in that workspace. 

```Python
@pipeline()
def pipeline_with_registered_components(
    training_data
):
    train_job = train_component_from_registry(
        training_data=training_data,
    )
pipeline_job = pipeline_with_registered_components(
    training_data=Input(type="uri_folder", path=parent_dir + "/data_transformed/"),
)
pipeline_job.settings.default_compute = "cpu-cluster"
print(pipeline_job)
```

> [!WARNING]
> * Confirm that the workspace in which you will run this job is in a Azure location that is supported by the registry in which you created the component before you run the pipeline job.
> * Confirm that the workspace has a compute cluster with the name `cpu-cluster` or update it `pipeline_job.settings.default_compute=<compute-cluster-name>`.

Run the pipeline job and wait for it to complete. 

```python
pipeline_job = ml_client_workspace.jobs.create_or_update(
    pipeline_job, experiment_name="sdk_job_component_from_registry" ,  skip_validation=True
)
ml_client_workspace.jobs.stream(pipeline_job.name)
pipeline_job=ml_client_workspace.jobs.get(pipeline_job.name)
pipeline_job
```

> [!TIP]
> Notice that you are using `ml_client_workspace` to run the pipeline job whereas you had used `ml_client_registry` to use create environment and component.

Since the component used in the training job is shared through a registry, you can submit the job to any workspace that you have access to in your organization, even across different subscriptions. For example, if you have `dev-workspace`, `test-workspace` and `prod-workspace`, you can connect to those workspaces and resubmit the job.


In AzureML studio, select the endpoint link in the job output to view the job. Here you can analyze training metrics, verify that the job is using the component and environment from registry, and review the trained model. Note down the `name` of the job from the output or find the same information from the job overview in AzureML studio. You'll need this information to download the trained model in the next section on creating models in registry.
