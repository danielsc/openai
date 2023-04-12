> To register the model, you'll need to know the location where the model has been stored. If you are using `autolog` feature of MLflow, the path will depend on the type and framework of the model being used. We recommend to check the jobs output to identify which is the name of this folder. You can look for the folder that contains a file named `MLModel`. If you are logging your models manually using `log_model`, then the path is the argument you pass to such method. As an example, if you log the model using `mlflow.sklearn.log_model(my_model, "classifier")`, then the path where the model is stored is `classifier`.

```python
model_name = 'heart-classifier'

registered_model = mlflow_client.create_model_version(
    name=model_name, source=f"runs://{RUN_ID}/{MODEL_PATH}"
)
version = registered_model.version
```

> [!NOTE]
> The path `MODEL_PATH` is the location where the model has been stored in the run.


### Get input data to score

We'll need some input data to run or jobs on. In this example, we'll download sample data from internet and place it in a shared storage used by the Spark cluster.

```python
import urllib

urllib.request.urlretrieve("https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/data/heart.csv", "/tmp/data")
```

Move the data to a mounted storage account available to the entire cluster.

```python
dbutils.fs.mv("file:/tmp/data", "dbfs:/")
```

> [!IMPORTANT]
> The previous code uses `dbutils`, which is a tool available in Azure Databricks cluster. Use the appropriate tool depending on the platform you are using.

The input data is then placed in the following folder:

```python
input_data_path = "dbfs:/data"
```

## Run the model in Spark clusters

The following section explains how to run MLflow models registered in Azure Machine Learning in Spark jobs.

1. Ensure the following libraries are installed in the cluster:

```yaml
channels:
- conda-forge
dependencies:
- python=3.8.5
- pip<=21.3.1
- pip:
  - mlflow<3,>=2.1
  - cloudpickle==2.2.0
  - scikit-learn==1.2.0
  - xgboost==1.7.2
name: mlflow-env

```

1. We'll use a notebook to demonstrate how to create a scoring routine with an MLflow model registered in Azure Machine Learning. Create a notebook and use PySpark as the default language.

1. Import the required namespaces:

    ```python
    import mlflow
    import pyspark.sql.functions as f
    ```  

1. Configure the model URI. The following URI brings a model named `heart-classifier` in its latest version.

    ```python
    model_uri = "models:/heart-classifier/latest"
    ```

1. Load the model as an UDF function. A user-defined function (UDF) is a function defined by a user, allowing custom logic to be reused in the user environment.

    ```python
    predict_function = mlflow.pyfunc.spark_udf(spark, model_uri, result_type='double') 
    ```

    > [!TIP]
    > Use the argument `result_type` to control the type returned by the `predict()` function.

1. Read the data you want to score:

    ```python
    df = spark.read.option("header", "true").option("inferSchema", "true").csv(input_data_path).drop("target")
    ```

    In our case, the input data is on `CSV` format and placed in the folder `dbfs:/data/`. We're also dropping the column `target` as this dataset contains the target variable to predict. In production scenarios, your data won't have this column.

1. Run the function `predict_function` and place the predictions on a new column. In this case, we're placing the predictions in the column `predictions`.

    ```python
    df.withColumn("predictions", score_function(*df.columns))
    ```

    > [!TIP]
    > The `predict_function` receives as arguments the columns required. In our case, all the columns of the data frame are expected by the model and hence `df.columns` is used. If your model requires a subset of the columns, you can introduce them manually. If you model has a signature, types need to be compatible between inputs and expected types.

1. You can write your predictions back to storage:
