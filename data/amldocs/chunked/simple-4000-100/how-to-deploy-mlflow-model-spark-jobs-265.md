1. The YAML files shown above can be used in the `az ml job create` command, with the `--file` parameter, to create a standalone Spark job as shown:

    ```azurecli
    az ml job create -f mlflow-score-spark-job.yml
    ```

## Next steps

- [Deploy MLflow models to batch endpoints](how-to-mlflow-batch.md)
- [Deploy MLflow models to online endpoint](how-to-deploy-mlflow-models-online-endpoints.md)
- [Using MLflow models for no-code deployment](how-to-log-mlflow-models.md)