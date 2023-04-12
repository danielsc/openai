    
    This class allows user to configure the following key aspects.
    * `name` - Name of the deployment.
    * `endpoint_name` - Name of the endpoint to create the deployment under.
    * `model` - The model to use for the deployment. This value can be either a reference to an existing versioned model in the workspace or an inline model specification.
    * `environment` - The environment to use for the deployment. This value can be either a reference to an existing versioned environment in the workspace or an inline environment specification.
    * `code_path`- Path to the source code directory for scoring the model
    * `scoring_script` - Relative path to the scoring file in the source code directory
    * `compute` - Name of the compute target to execute the batch scoring jobs on
    * `instance_count`- The number of nodes to use for each batch scoring job.
    * `max_concurrency_per_instance`- The maximum number of parallel scoring_script runs per instance.
    * `mini_batch_size` - The number of files the code_configuration.scoring_script can process in one `run`() call.
    * `retry_settings`- Retry settings for scoring each mini batch.
        * `max_retries`- The maximum number of retries for a failed or timed-out mini batch (default is 3)
        * `timeout`- The timeout in seconds for scoring a mini batch (default is 30)
    * `output_action`- Indicates how the output should be organized in the output file. Allowed values are `append_row` or `summary_only`. Default is `append_row`
    * `output_file_name`- Name of the batch scoring output file. Default is `predictions.csv`
    * `environment_variables`- Dictionary of environment variable name-value pairs to set for each batch scoring job.
    * `logging_level`- The log verbosity level. Allowed values are `warning`, `info`, `debug`. Default is `info`.

    # [Studio](#tab/azure-studio)
   
    On [Azure ML studio portal](https://ml.azure.com), follow these steps:
    
    1. Navigate to the __Endpoints__ tab on the side menu.
    1. Select the tab __Batch endpoints__ > __Create__.
    1. Give the endpoint a name, in this case `mnist-batch`. You can configure the rest of the fields or leave them blank.
    1. Select __Next__.
    1. On the model list, select the model `mnist` and select __Next__.
    1. On the deployment configuration page, give the deployment a name.
    1. On __Output action__, ensure __Append row__ is selected.
    1. On __Output file name__, ensure the batch scoring output file is the one you need. Default is `predictions.csv`.
    1. On __Mini batch size__, adjust the size of the files that will be included on each mini-batch. This will control the amount of data your scoring script receives per each batch.
    1. On __Scoring timeout (seconds)__, ensure you're giving enough time for your deployment to score a given batch of files. If you increase the number of files, you usually have to increase the timeout value too. More expensive models (like those based on deep learning), may require high values in this field.
    1. On __Max concurrency per instance__, configure the number of executors you want to have per each compute instance you get in the deployment. A higher number here guarantees a higher degree of parallelization but it also increases the memory pressure on the compute instance. Tune this value altogether with __Mini batch size__.
    1. Once done, select __Next__.
    1. On environment, go to __Select scoring file and dependencies__ and select __Browse__.
    1. Select the scoring script file on `/mnist/code/batch_driver.py`.
    1. On the section __Choose an environment__, select the environment you created a previous step.
    1. Select __Next__.
    1. On the section __Compute__, select the compute cluster you created in a previous step.

        > [!WARNING]
        > Azure Kubernetes cluster are supported in batch deployments, but only when created using the Azure ML CLI or Python SDK.

    1. On __Instance count__, enter the number of compute instances you want for the deployment. In this case, we'll use 2.
