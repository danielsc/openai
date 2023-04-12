
# Upgrade hyperparameter tuning to SDK v2

In SDK v2, tuning hyperparameters are consolidated into jobs.

A job has a type. Most jobs are command jobs that run a `command`, like `python main.py`. What runs in a job is agnostic to any programming language, so you can run `bash` scripts, invoke `python` interpreters, run a bunch of `curl` commands, or anything else.

A sweep job is another type of job, which defines sweep settings and can be initiated by calling the sweep method of command.

To upgrade, you'll need to change your code for defining and submitting your hyperparameter tuning experiment to SDK v2. What you run _within_ the job doesn't need to be upgraded to SDK v2. However, it's recommended to remove any code specific to Azure ML from your model training scripts. This separation allows for an easier transition between local and cloud and is considered best practice for mature MLOps. In practice, this means removing `azureml.*` lines of code. Model logging and tracking code should be replaced with MLflow. For more information, see [how to use MLflow in v2](how-to-use-mlflow-cli-runs.md).

This article gives a comparison of scenario(s) in SDK v1 and SDK v2.

## Run hyperparameter tuning in an experiment

* SDK v1

    ```python
    from azureml.core import ScriptRunConfig, Experiment, Workspace
    from azureml.train.hyperdrive import RandomParameterSampling, BanditPolicy, HyperDriveConfig, PrimaryMetricGoal
    from azureml.train.hyperdrive import choice, loguniform
    
    dataset = Dataset.get_by_name(ws, 'mnist-dataset')
    
    # list the files referenced by mnist dataset
    dataset.to_path()
    
    #define the search space for your hyperparameters
    param_sampling = RandomParameterSampling(
        {
            '--batch-size': choice(25, 50, 100),
            '--first-layer-neurons': choice(10, 50, 200, 300, 500),
            '--second-layer-neurons': choice(10, 50, 200, 500),
            '--learning-rate': loguniform(-6, -1)
        }
    )
    
    args = ['--data-folder', dataset.as_named_input('mnist').as_mount()]
    
    #Set up your script run
    src = ScriptRunConfig(source_directory=script_folder,
                          script='keras_mnist.py',
                          arguments=args,
                          compute_target=compute_target,
                          environment=keras_env)
    
    # Set early stopping on this one
    early_termination_policy = BanditPolicy(evaluation_interval=2, slack_factor=0.1)
    
    # Define the configurations for your hyperparameter tuning experiment
    hyperdrive_config = HyperDriveConfig(run_config=src,
                                         hyperparameter_sampling=param_sampling,
                                         policy=early_termination_policy,
                                         primary_metric_name='Accuracy',
                                         primary_metric_goal=PrimaryMetricGoal.MAXIMIZE,
                                         max_total_runs=20,
                                         max_concurrent_runs=4)
    # Specify your experiment details                                     
    experiment = Experiment(workspace, experiment_name)
    
    hyperdrive_run = experiment.submit(hyperdrive_config)
    
    #Find the best model
    best_run = hyperdrive_run.get_best_run_by_primary_metric()
    ```

* SDK v2

    ```python
    from azure.ai.ml import MLClient
    from azure.ai.ml import command, Input
    from azure.ai.ml.sweep import Choice, Uniform, MedianStoppingPolicy
    from azure.identity import DefaultAzureCredential
    
    # Create your command
    command_job_for_sweep = command(
        code="./src",
        command="python main.py --iris-csv ${{inputs.iris_csv}} --learning-rate ${{inputs.learning_rate}} --boosting ${{inputs.boosting}}",
        environment="AzureML-lightgbm-3.2-ubuntu18.04-py37-cpu@latest",
        inputs={
            "iris_csv": Input(
                type="uri_file",
                path="https://azuremlexamples.blob.core.windows.net/datasets/iris.csv",
            ),
            #define the search space for your hyperparameters
            "learning_rate": Uniform(min_value=0.01, max_value=0.9),
            "boosting": Choice(values=["gbdt", "dart"]),
        },
        compute="cpu-cluster",
    )
    
    # Call sweep() on your command job to sweep over your parameter expressions
    sweep_job = command_job_for_sweep.sweep(
        compute="cpu-cluster", 
        sampling_algorithm="random",
        primary_metric="test-multi_logloss",
        goal="Minimize",
    )
    
    # Define the limits for this sweep
    sweep_job.set_limits(max_total_trials=20, max_concurrent_trials=10, timeout=7200)
    
    # Set early stopping on this one
    sweep_job.early_termination = MedianStoppingPolicy(delay_evaluation=5, evaluation_interval=2)
    
    # Specify your experiment details
    sweep_job.display_name = "lightgbm-iris-sweep-example"
    sweep_job.experiment_name = "lightgbm-iris-sweep-example"
    sweep_job.description = "Run a hyperparameter sweep job for LightGBM on Iris dataset."
    
    # submit the sweep
    returned_sweep_job = ml_client.create_or_update(sweep_job)
    
    # get a URL for the status of the job
    returned_sweep_job.services["Studio"].endpoint
    
    # Download best trial model output
    ml_client.jobs.download(returned_sweep_job.name, output_name="model")
    ```
