   
   # [Python](#tab/sdk)
   
   ```python
   endpoint.defaults.deployment_name = deployment.name
   ml_client.batch_endpoints.begin_create_or_update(endpoint)
   ```

4. At this point, our batch endpoint is ready to be used. 


## Considerations when deploying models that process text

As mentioned in some of the notes along this tutorial, processing text may have some peculiarities that require specific configuration for batch deployments. Take the following consideration when designing the batch deployment:

> [!div class="checklist"]
> * Some NLP models may be very expensive in terms of memory and compute time. If this is the case, consider decreasing the number of files included on each mini-batch. In the example above, the number was taken to the minimum, 1 file per batch. While this may not be your case, take into consideration how many files your model can score at each time. Have in mind that the relationship between the size of the input and the memory footprint of your model may not be linear for deep learning models.
> * If your model can't even handle one file at a time (like in this example), consider reading the input data in rows/chunks. Implement batching at the row level if you need to achieve higher throughput or hardware utilization.
> * Set the `timeout` value of your deployment accordly to how expensive your model is and how much data you expect to process. Remember that the `timeout` indicates the time the batch deployment would wait for your scoring script to run for a given batch. If your batch have many files or files with many rows, this will impact the right value of this parameter.

## Considerations for MLflow models that process text

MLflow models in Batch Endpoints support reading CSVs as input data, which may contain long sequences of text. The same considerations mentioned above apply to MLflow models. However, since you are not required to provide a scoring script for your MLflow model deployment, some of the recommendation there may be harder to achieve. 

* Only `CSV` files are supported for MLflow deployments processing text. You will need to author a scoring script if you need to process other file types like `TXT`, `PARQUET`, etc. See [Using MLflow models with a scoring script](how-to-mlflow-batch.md#customizing-mlflow-models-deployments-with-a-scoring-script) for details.
* Batch deployments will call your MLflow model's predict function with the content of an entire file in as Pandas dataframe. If your input data contains many rows, chances are that running a complex model (like the one presented in this tutorial) will result in an out-of-memory exception. If this is your case, you can consider:
   * Customize how your model runs predictions and implement batching. To learn how to customize MLflow model's inference, see [Logging custom models](how-to-log-mlflow-models.md?#logging-custom-models).
   * Author a scoring script and load your model using `mlflow.<flavor>.load_model()`. See [Using MLflow models with a scoring script](how-to-mlflow-batch.md#customizing-mlflow-models-deployments-with-a-scoring-script) for details.


