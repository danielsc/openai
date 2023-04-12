    > The `predict_function` receives as arguments the columns required. In our case, all the columns of the data frame are expected by the model and hence `df.columns` is used. If your model requires a subset of the columns, you can introduce them manually. If you model has a signature, types need to be compatible between inputs and expected types.

1. You can write your predictions back to storage:

    ```python
    scored_data_path = "dbfs:/scored-data"
    scored_data.to_csv(scored_data_path)
    ```

## Run the model in a standalone Spark job in Azure Machine Learning

 Azure Machine Learning supports creation of a standalone Spark job, and creation of a reusable Spark component that can be used in [Azure Machine Learning pipelines](concept-ml-pipelines.md). In this example, we'll deploy a scoring job that runs in Azure Machine Learning standalone Spark job and runs an MLflow model to perform inference.

> [!NOTE]
> To learn more about Spark jobs in Azure Machine Learning, see [Submit Spark jobs in Azure Machine Learning (preview)](how-to-submit-spark-jobs.md).

1. A Spark job requires a Python script that takes arguments. Create a scoring script:

    __score.py__

    ```python
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--model")
    parser.add_argument("--input_data")
    parser.add_argument("--scored_data")
    
    args = parser.parse_args()
    print(args.model)
    print(args.input_data)
    
    # Load the model as an UDF function
    predict_function = mlflow.pyfunc.spark_udf(spark, args.model, env_manager="conda")
    
    # Read the data you want to score
    df = spark.read.option("header", "true").option("inferSchema", "true").csv(input_data).drop("target")
    
    # Run the function `predict_function` and place the predictions on a new column
    scored_data = df.withColumn("predictions", score_function(*df.columns))
    
    # Save the predictions
    scored_data.to_csv(args.scored_data)
    ```
    
    The above script takes three arguments `--model`, `--input_data` and `--scored_data`. The first two are inputs and represent the model we want to run and the input data, the last one is an output and it is the output folder where predictions will be placed.

    > [!TIP]
    > **Installation of Python packages:** The previous scoring script loads the MLflow model into an UDF function, but it indicates the parameter `env_manager="conda"`. When this parameter is set, MLflow will restore the required packages as specified in the model definition in an isolated environment where only the UDF function runs. For more details see [`mlflow.pyfunc.spark_udf`](https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html?highlight=env_manager#mlflow.pyfunc.spark_udf) documentation.

1. Create a job definition:

    __mlflow-score-spark-job.yml__

    ```yml
    $schema: http://azureml/sdk-2-0/SparkJob.json
    type: spark
    
    code: ./src
    entry:
      file: score.py
    
    conf:
      spark.driver.cores: 1
      spark.driver.memory: 2g
      spark.executor.cores: 2
      spark.executor.memory: 2g
      spark.executor.instances: 2
    
    inputs:
      model:
        type: mlflow_model
        path: azureml:heart-classifier@latest
      input_data:
        type: uri_file
        path: https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/data/heart.csv
        mode: direct
    
    outputs:
      scored_data:
        type: uri_folder
    
    args: >-
      --model ${{inputs.model}}
      --input_data ${{inputs.input_data}}
      --scored_data ${{outputs.scored_data}}
    
    identity:
      type: user_identity
    
    resources:
      instance_type: standard_e4s_v3
      runtime_version: "3.2"
    ```

    > [!TIP]
    > To use an attached Synapse Spark pool, define `compute` property in the sample YAML specification file shown above instead of `resources` property.

1. The YAML files shown above can be used in the `az ml job create` command, with the `--file` parameter, to create a standalone Spark job as shown:
