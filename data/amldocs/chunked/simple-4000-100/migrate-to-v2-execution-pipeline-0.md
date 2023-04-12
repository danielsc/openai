
# Upgrade pipelines to SDK v2

In SDK v2, "pipelines" are consolidated into jobs.

A job has a type. Most jobs are command jobs that run a `command`, like `python main.py`. What runs in a job is agnostic to any programming language, so you can run `bash` scripts, invoke `python` interpreters, run a bunch of `curl` commands, or anything else.

A `pipeline` is another type of job, which defines child jobs that may have input/output relationships, forming a directed acyclic graph (DAG).

To upgrade, you'll need to change your code for defining and submitting the pipelines to SDK v2. What you run _within_ the child job doesn't need to be upgraded to SDK v2. However, it's recommended to remove any code specific to Azure ML from your model training scripts. This separation allows for an easier transition between local and cloud and is considered best practice for mature MLOps. In practice, this means removing `azureml.*` lines of code. Model logging and tracking code should be replaced with MLflow. For more information, see [how to use MLflow in v2](how-to-use-mlflow-cli-runs.md).

This article gives a comparison of scenario(s) in SDK v1 and SDK v2. In the following examples, we'll build three steps (train, score and evaluate) into a dummy pipeline job. This demonstrates how to build pipeline jobs using SDK v1 and SDK v2, and how to consume data and transfer data between steps.

## Run a pipeline

* SDK v1

    ```python
    # import required libraries
    import os
    import azureml.core
    from azureml.core import (
        Workspace,
        Dataset,
        Datastore,
        ComputeTarget,
        Experiment,
        ScriptRunConfig,
    )
    from azureml.pipeline.steps import PythonScriptStep
    from azureml.pipeline.core import Pipeline
    
    # check core SDK version number
    print("Azure ML SDK Version: ", azureml.core.VERSION)
    
    # load workspace
    workspace = Workspace.from_config()
    print(
        "Workspace name: " + workspace.name,
        "Azure region: " + workspace.location,
        "Subscription id: " + workspace.subscription_id,
        "Resource group: " + workspace.resource_group,
        sep="\n",
    )
    
    # create an ML experiment
    experiment = Experiment(workspace=workspace, name="train_score_eval_pipeline")
    
    # create a directory
    script_folder = "./src"
    
    # create compute
    from azureml.core.compute import ComputeTarget, AmlCompute
    from azureml.core.compute_target import ComputeTargetException
    
    # Choose a name for your CPU cluster
    amlcompute_cluster_name = "cpu-cluster"
    
    # Verify that cluster does not exist already
    try:
        aml_compute = ComputeTarget(workspace=workspace, name=amlcompute_cluster_name)
        print('Found existing cluster, use it.')
    except ComputeTargetException:
        compute_config = AmlCompute.provisioning_configuration(vm_size='STANDARD_DS12_V2',
                                                               max_nodes=4)
        aml_compute = ComputeTarget.create(ws, amlcompute_cluster_name, compute_config)
    
    aml_compute.wait_for_completion(show_output=True)
    
    # define data set
    data_urls = ["wasbs://demo@dprepdata.blob.core.windows.net/Titanic.csv"]
    input_ds = Dataset.File.from_files(data_urls)
    
    # define steps in pipeline
    from azureml.data import OutputFileDatasetConfig
    model_output = OutputFileDatasetConfig('model_output')
    train_step = PythonScriptStep(
        name="train step",
        script_name="train.py",
        arguments=['--training_data', input_ds.as_named_input('training_data').as_mount() ,'--max_epocs', 5, '--learning_rate', 0.1,'--model_output', model_output],
        source_directory=script_folder,
        compute_target=aml_compute,
        allow_reuse=True,
    )
    
    score_output = OutputFileDatasetConfig('score_output')
    score_step = PythonScriptStep(
        name="score step",
        script_name="score.py",
        arguments=['--model_input',model_output.as_input('model_input'), '--test_data', input_ds.as_named_input('test_data').as_mount(), '--score_output', score_output],
        source_directory=script_folder,
        compute_target=aml_compute,
        allow_reuse=True,
    )
    
    eval_output = OutputFileDatasetConfig('eval_output')
    eval_step = PythonScriptStep(
        name="eval step",
        script_name="eval.py",
        arguments=['--scoring_result',score_output.as_input('scoring_result'), '--eval_output', eval_output],
        source_directory=script_folder,
        compute_target=aml_compute,
        allow_reuse=True,
    )
    
    # built pipeline
    from azureml.pipeline.core import Pipeline
    
    pipeline_steps = [train_step, score_step, eval_step]
    
    pipeline = Pipeline(workspace = workspace, steps=pipeline_steps)
    print("Pipeline is built.")
    
    pipeline_run = experiment.submit(pipeline, regenerate_outputs=False)
    
    print("Pipeline submitted for execution.")
    
    ```
