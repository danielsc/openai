   
   c. Refresh the object to reflect the changes:
   
   ```python
   heart_dataset_unlabeled = ml_client.data.get(name=dataset_name, label="latest")
   ```
   
2. Now that the data is uploaded and ready to be used, let's invoke the endpoint:

   # [Azure CLI](#tab/cli)
   
   ```azurecli
   JOB_NAME = $(az ml batch-endpoint invoke --name $ENDPOINT_NAME --input azureml:heart-dataset-unlabeled@latest | jq -r '.name') 
   ```
   
   > [!NOTE]
   > The utility `jq` may not be installed on every installation. You can get installation instructions in [this link](https://stedolan.github.io/jq/download/).
   
   # [Python](#tab/sdk)
   
   ```python
   input = Input(type=AssetTypes.URI_FOLDER, path=heart_dataset_unlabeled.id)
   job = ml_client.batch_endpoints.invoke(
      endpoint_name=endpoint.name,
      input=input,
   )
   ```
   
   > [!TIP]
   > Notice how we are not indicating the deployment name in the invoke operation. That's because the endpoint automatically routes the job to the default deployment. Since our endpoint only has one deployment, then that one is the default one. You can target an specific deployment by indicating the argument/parameter `deployment_name`.

3. A batch job is started as soon as the command returns. You can monitor the status of the job until it finishes:

   # [Azure CLI](#tab/cli)
   
   ```azurecli
   az ml job show --name $JOB_NAME
   ```
   
   # [Python](#tab/sdk)
   
   ```python
   ml_client.jobs.get(job.name)
   ```
   
## Analyzing the outputs

Output predictions are generated in the `predictions.csv` file as indicated in the deployment configuration. The job generates a named output called `score` where this file is placed. Only one file is generated per batch job.

The file is structured as follows:

* There is one row per each data point that was sent to the model. For tabular data, this means that one row is generated for each row in the input files and hence the number of rows in the generated file (`predictions.csv`) equals the sum of all the rows in all the processed files. For other data types, there is one row per each processed file.
* Two columns are indicated:
   * The file name where the data was read from. In tabular data, use this field to know which prediction belongs to which input data. For any given file, predictions are returned in the same order they appear in the input file so you can rely on the row number to match the corresponding prediction.
   * The prediction associated with the input data. This value is returned "as-is" it was provided by the model's `predict().` function. 


You can download the results of the job by using the job name:

# [Azure CLI](#tab/cli)

To download the predictions, use the following command:

```azurecli
az ml job download --name $JOB_NAME --output-name score --download-path ./
```

# [Python](#tab/sdk)

```python
ml_client.jobs.download(name=job.name, output_name='score', download_path='./')
```

Once the file is downloaded, you can open it using your favorite tool. The following example loads the predictions using `Pandas` dataframe.

```python
import pandas as pd
from ast import literal_eval

with open('named-outputs/score/predictions.csv', 'r') as f:
   pd.DataFrame(literal_eval(f.read().replace('\n', ',')), columns=['file', 'prediction'])
```

> [!WARNING]
> The file `predictions.csv` may not be a regular CSV file and can't be read correctly using `pandas.read_csv()` method.

The output looks as follows:

| file                       | prediction  |
| -------------------------- | ----------- |
| heart-unlabeled-0.csv      | 0           |
| heart-unlabeled-0.csv      | 1           |
| ...                        | 1           |
| heart-unlabeled-3.csv      | 0           |

> [!TIP]
> Notice that in this example the input data was tabular data in `CSV` format and there were 4 different input files (heart-unlabeled-0.csv, heart-unlabeled-1.csv, heart-unlabeled-2.csv and heart-unlabeled-3.csv).

## Considerations when deploying to batch inference
