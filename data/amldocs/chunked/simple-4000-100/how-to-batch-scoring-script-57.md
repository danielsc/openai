> Batch deployments distribute work at the file level, which means that a folder containing 100 files with mini-batches of 10 files will generate 10 batches of 10 files each. Notice that this will happen regardless of the size of the files involved. If your files are too big to be processed in large mini-batches we suggest to either split the files in smaller files to achieve a higher level of parallelism or to decrease the number of files per mini-batch. At this moment, batch deployment can't account for skews in the file's size distribution.

The `run()` method should return a Pandas `DataFrame` or an array/list. Each returned output element indicates one successful run of an input element in the input `mini_batch`. For file datasets, each row/element will represent a single file processed. For a tabular dataset, each row/element will represent a row in a processed file.

> [!IMPORTANT]
> __How to write predictions?__
> 
> Use __arrays__ when you need to output a single prediction. Use __pandas DataFrames__ when you need to return multiple pieces of information. For instance, for tabular data, you may want to append your predictions to the original record. Use a pandas DataFrame for this case. For file datasets, __we still recommend to output a pandas DataFrame__ as they provide a more robust approach to read the results.
> 
> Although pandas DataFrame may contain column names, they are not included in the output file. If needed, please see [Customize outputs in batch deployments](how-to-deploy-model-custom-output.md).

> [!WARNING]
> Do not not output complex data types (or lists of complex data types) in the `run` function. Those outputs will be transformed to string and they will be hard to read.

The resulting DataFrame or array is appended to the output file indicated. There's no requirement on the cardinality of the results (1 file can generate 1 or many rows/elements in the output). All elements in the result DataFrame or array will be written to the output file as-is (considering the `output_action` isn't `summary_only`).

#### Python packages for scoring

Any library that your scoring script requires to run needs to be indicated in the environment where your batch deployment runs. As for scoring scripts, environments are indicated per deployment. Usually, you will indicate your requirements using a `conda.yml` dependencies file which may look as follows:

__mnist/environment/conda.yml__
        
```yaml
name: mnist-env
channels:
  - conda-forge
dependencies:
  - python=3.6.2
  - pip<22.0
  - pip:
    - tensorflow==1.15.2
    - pillow
    - pandas
    - azureml-core
    - azureml-dataset-runtime[fuse]

```

Refer to [Create a batch deployment](how-to-use-batch-endpoint.md#create-a-batch-deployment) for more details about how to indicate the environment for your model.

## Writing predictions in a different way

By default, the batch deployment will write the model's predictions in a single file as indicated in the deployment. However, there are some cases where you need to write the predictions in multiple files. For instance, if the input data is partitioned, you typically would want to generate your output partitioned too. On those cases you can [Customize outputs in batch deployments](how-to-deploy-model-custom-output.md) to indicate:

> [!div class="checklist"]
> * The file format used (CSV, parquet, json, etc).
> * The way data is partitioned in the output.

Read the article [Customize outputs in batch deployments](how-to-deploy-model-custom-output.md) for an example about how to achieve it.

## Source control of scoring scripts

It is highly advisable to put scoring scripts under source control. 

## Best practices for writing scoring scripts

When writing scoring scripts that work with big amounts of data, you need to take into account several factors, including:

* The size of each file.
* The amount of data on each file.
* The amount of memory required to read each file.
* The amount of memory required to read an entire batch of files.
