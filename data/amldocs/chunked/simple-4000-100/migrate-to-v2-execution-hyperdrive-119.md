
## Run hyperparameter tuning in a pipeline

* SDK v1

    ````python
    
    tf_env = Environment.get(ws, name='AzureML-TensorFlow-2.0-GPU')
    data_folder = dataset.as_mount()
    src = ScriptRunConfig(source_directory=script_folder,
                          script='tf_mnist.py',
                          arguments=['--data-folder', data_folder],
                          compute_target=compute_target,
                          environment=tf_env)
    
    #Define HyperDrive configs
    ps = RandomParameterSampling(
        {
            '--batch-size': choice(25, 50, 100),
            '--first-layer-neurons': choice(10, 50, 200, 300, 500),
            '--second-layer-neurons': choice(10, 50, 200, 500),
            '--learning-rate': loguniform(-6, -1)
        }
    )
    
    early_termination_policy = BanditPolicy(evaluation_interval=2, slack_factor=0.1)
    
    hd_config = HyperDriveConfig(run_config=src, 
                                 hyperparameter_sampling=ps,
                                 policy=early_termination_policy,
                                 primary_metric_name='validation_acc', 
                                 primary_metric_goal=PrimaryMetricGoal.MAXIMIZE, 
                                 max_total_runs=4,
                                 max_concurrent_runs=4)
                                 
    metrics_output_name = 'metrics_output'
    metrics_data = PipelineData(name='metrics_data',
                                datastore=datastore,
                                pipeline_output_name=metrics_output_name,
                                training_output=TrainingOutput("Metrics"))
    
    model_output_name = 'model_output'
    saved_model = PipelineData(name='saved_model',
                                datastore=datastore,
                                pipeline_output_name=model_output_name,
                                training_output=TrainingOutput("Model",
                                                               model_file="outputs/model/saved_model.pb"))
    #Create HyperDriveStep
    hd_step_name='hd_step01'
    hd_step = HyperDriveStep(
        name=hd_step_name,
        hyperdrive_config=hd_config,
        inputs=[data_folder],
        outputs=[metrics_data, saved_model])                             
    
    #Find and register best model
    conda_dep = CondaDependencies()
    conda_dep.add_pip_package("azureml-sdk")
    
    rcfg = RunConfiguration(conda_dependencies=conda_dep)
    
    register_model_step = PythonScriptStep(script_name='register_model.py',
                                           name="register_model_step01",
                                           inputs=[saved_model],
                                           compute_target=cpu_cluster,
                                           arguments=["--saved-model", saved_model],
                                           allow_reuse=True,
                                           runconfig=rcfg)
    
    register_model_step.run_after(hd_step)
    
    #Run the pipeline
    pipeline = Pipeline(workspace=ws, steps=[hd_step, register_model_step])
    pipeline_run = exp.submit(pipeline)
    
    ````

* SDK v2

    ```python
    train_component_func = load_component(path="./train.yml")
    score_component_func = load_component(path="./predict.yml")
    
    # define a pipeline
    @pipeline()
    def pipeline_with_hyperparameter_sweep():
        """Tune hyperparameters using sample components."""
        train_model = train_component_func(
            data=Input(
                type="uri_file",
                path="wasbs://datasets@azuremlexamples.blob.core.windows.net/iris.csv",
            ),
            c_value=Uniform(min_value=0.5, max_value=0.9),
            kernel=Choice(["rbf", "linear", "poly"]),
            coef0=Uniform(min_value=0.1, max_value=1),
            degree=3,
            gamma="scale",
            shrinking=False,
            probability=False,
            tol=0.001,
            cache_size=1024,
            verbose=False,
            max_iter=-1,
            decision_function_shape="ovr",
            break_ties=False,
            random_state=42,
        )
        sweep_step = train_model.sweep(
            primary_metric="training_f1_score",
            goal="minimize",
            sampling_algorithm="random",
            compute="cpu-cluster",
        )
        sweep_step.set_limits(max_total_trials=20, max_concurrent_trials=10, timeout=7200)
    
        score_data = score_component_func(
            model=sweep_step.outputs.model_output, test_data=sweep_step.outputs.test_data
        )
    
    
    pipeline_job = pipeline_with_hyperparameter_sweep()
    
    # set pipeline level compute
    pipeline_job.settings.default_compute = "cpu-cluster"
    
    # submit job to workspace
    pipeline_job = ml_client.jobs.create_or_update(
        pipeline_job, experiment_name="pipeline_samples"
    )
    pipeline_job
    ```
