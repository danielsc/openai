> Notice that in this example the input data was tabular data in `CSV` format and there were 4 different input files (heart-unlabeled-0.csv, heart-unlabeled-1.csv, heart-unlabeled-2.csv and heart-unlabeled-3.csv).

## Considerations when deploying to batch inference

Azure Machine Learning supports no-code deployment for batch inference in [managed endpoints](concept-endpoints.md). This represents a convenient way to deploy models that require processing of big amounts of data in a batch-fashion.

### How work is distributed on workers

Work is distributed at the file level, for both structured and unstructured data. As a consequence, only [file datasets](v1/how-to-create-register-datasets.md#filedataset) or [URI folders](reference-yaml-data.md) are supported for this feature. Each worker processes batches of `Mini batch size` files at a time. Further parallelism can be achieved if `Max concurrency per instance` is increased. 

> [!WARNING]
> Nested folder structures are not explored during inference. If you are partitioning your data using folders, make sure to flatten the structure beforehand.

> [!WARNING]
> Batch deployments will call the `predict` function of the MLflow model once per file. For CSV files containing multiple rows, this may impose a memory pressure in the underlying compute. When sizing your compute, take into account not only the memory consumption of the data being read but also the memory footprint of the model itself. This is specially true for models that processes text, like transformer-based models where the memory consumption is not linear with the size of the input. If you encouter several out-of-memory exceptions, consider splitting the data in smaller files with less rows or implement batching at the row level inside of the model/scoring script.

### File's types support

The following data types are supported for batch inference when deploying MLflow models without an environment and a scoring script:

| File extension | Type returned as model's input | Signature requirement |
| :- | :- | :- |
| `.csv` | `pd.DataFrame` | `ColSpec`. If not provided, columns typing is not enforced. |
| `.png`, `.jpg`, `.jpeg`, `.tiff`, `.bmp`, `.gif` | `np.ndarray` | `TensorSpec`. Input is reshaped to match tensors shape if available. If no signature is available, tensors of type `np.uint8` are inferred. For additional guidance read [Considerations for MLflow models processing images](how-to-image-processing-batch.md#considerations-for-mlflow-models-processing-images). |

> [!WARNING]
> Be advised that any unsupported file that may be present in the input data will make the job to fail. You will see an error entry as follows: *"ERROR:azureml:Error processing input file: '/mnt/batch/tasks/.../a-given-file.parquet'. File type 'parquet' is not supported."*.

> [!TIP]
> If you like to process a different file type, or execute inference in a different way that batch endpoints do by default you can always create the deploymnet with a scoring script as explained in [Using MLflow models with a scoring script](#customizing-mlflow-models-deployments-with-a-scoring-script).

### Signature enforcement for MLflow models

Input's data types are enforced by batch deployment jobs while reading the data using the available MLflow model signature. This means that your data input should comply with the types indicated in the model signature. If the data can't be parsed as expected, the job will fail with an error message similar to the following one: *"ERROR:azureml:Error processing input file: '/mnt/batch/tasks/.../a-given-file.csv'. Exception: invalid literal for int() with base 10: 'value'"*.

> [!TIP]
> Signatures in MLflow models are optional but they are highly encouraged as they provide a convenient way to early detect data compatibility issues. For more information about how to log models with signatures read [Logging models with a custom signature, environment or samples](how-to-log-mlflow-models.md#logging-models-with-a-custom-signature-environment-or-samples).
