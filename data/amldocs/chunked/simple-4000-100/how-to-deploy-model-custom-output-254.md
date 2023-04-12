   
   Then, create the data asset:
   
   ```python
   ml_client.data.create_or_update(heart_dataset_unlabeled)
   ```
   
   To get the newly created data asset, use:
   
   ```python
   heart_dataset_unlabeled = ml_client.data.get(name=dataset_name, label="latest")
   ```
   
1. Now that the data is uploaded and ready to be used, let's invoke the endpoint:

   # [Azure CLI](#tab/cli)
   
   ```azurecli
   JOB_NAME = $(az ml batch-endpoint invoke --name $ENDPOINT_NAME --deployment-name $DEPLOYMENT_NAME --input azureml:heart-dataset-unlabeled@latest | jq -r '.name')
   ```
   
   > [!NOTE]
   > The utility `jq` may not be installed on every installation. You can get instructions in [this link](https://stedolan.github.io/jq/download/).
   
   # [Python](#tab/sdk)
   
   ```python
   input = Input(type=AssetTypes.URI_FOLDER, path=heart_dataset_unlabeled.id)
   job = ml_client.batch_endpoints.invoke(
      endpoint_name=endpoint.name,
      deployment_name=deployment.name,
      input=input,
   )
   ```
   
1. A batch job is started as soon as the command returns. You can monitor the status of the job until it finishes:

   # [Azure CLI](#tab/cli)
   
   ```azurecli
   az ml job show --name $JOB_NAME
   ```
   
   # [Python](#tab/sdk)
   
   ```python
   ml_client.jobs.get(job.name)
   ```
   
## Analyzing the outputs

The job generates a named output called `score` where all the generated files are placed. Since we wrote into the directory directly, one file per each input file, then we can expect to have the same number of files. In this particular example we decided to name the output files the same as the inputs, but they will have a parquet extension.

> [!NOTE]
> Notice that a file `predictions.csv` is also included in the output folder. This file contains the summary of the processed files.

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
import glob

output_files = glob.glob("named-outputs/score/*.parquet")
score = pd.concat((pd.read_parquet(f) for f in output_files))
```

The output looks as follows:

| age |	sex |	... |	thal       |	prediction |
|-----|------|-----|------------|--------------|
| 63  |	1   |	... |	fixed      |	0          |
| 67  |	1   |	... |	normal     |	1          |
| 67  |	1   |	... |	reversible |	0          |
| 37  |	1   |	... |	normal     |	0          |


## Next steps

* [Using batch deployments for image file processing](how-to-image-processing-batch.md)
* [Using batch deployments for NLP processing](how-to-nlp-processing-batch.md)
