Your deployment configuration controls the size of each mini-batch and the number of workers on each node. Take into account them when deciding if you want to read the entire mini-batch to perform inference. When running multiple workers on the same instance, take into account that memory will be shared across all the workers. Usually, increasing the number of workers per node should be accompanied by a decrease in the mini-batch size or by a change in the scoring strategy (if data size remains the same).

## Next steps

* [Troubleshooting batch endpoints](how-to-troubleshoot-batch-endpoints.md).
* [Use MLflow models in batch deployments](how-to-mlflow-batch.md).
* [Image processing with batch deployments](how-to-image-processing-batch.md).
