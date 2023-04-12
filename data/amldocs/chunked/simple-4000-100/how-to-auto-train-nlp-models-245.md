You can also run your NLP experiments with distributed training on an Azure ML compute cluster. 

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]


# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]


This is handled automatically by automated ML when the parameters `max_concurrent_iterations = number_of_vms` and `enable_distributed_dnn_training = True` are provided in your `AutoMLConfig` during experiment setup. Doing so, schedules distributed training of the NLP models and automatically scales to every GPU on your virtual machine or cluster of virtual machines. The max number of virtual machines allowed is 32. The training is scheduled with number of virtual machines that is in powers of two.

```python
max_concurrent_iterations = number_of_vms
enable_distributed_dnn_training = True
```

In AutoML NLP only hold-out validation is supported and it requires a validation dataset.


## Submit the AutoML job

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

To submit your AutoML job, you can run the following CLI v2 command with the path to your .yml file, workspace name, resource group and subscription ID.

```azurecli

az ml job create --file ./hello-automl-job-basic.yml --workspace-name [YOUR_AZURE_WORKSPACE] --resource-group [YOUR_AZURE_RESOURCE_GROUP] --subscription [YOUR_AZURE_SUBSCRIPTION]
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]


With the `MLClient` created earlier, you can run this `CommandJob` in the workspace.

```python
returned_job = ml_client.jobs.create_or_update(
    text_classification_job
)  # submit the job to the backend

print(f"Created job: {returned_job}")
ml_client.jobs.stream(returned_job.name)
```


## Code examples

# [Azure CLI](#tab/cli)

 [!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]


See the following sample YAML files for each NLP task.

* [Multi-class text classification](https://github.com/Azure/azureml-examples/blob/main/cli/jobs/automl-standalone-jobs/cli-automl-text-classification-newsgroup/cli-automl-text-classification-newsgroup.yml)
* [Multi-label text classification](https://github.com/Azure/azureml-examples/blob/main/cli/jobs/automl-standalone-jobs/cli-automl-text-classification-multilabel-paper-cat/cli-automl-text-classification-multilabel-paper-cat.yml)
* [Named entity recognition](https://github.com/Azure/azureml-examples/blob/main/cli/jobs/automl-standalone-jobs/cli-automl-text-ner-conll/cli-automl-text-ner-conll2003.yml)

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

See the sample notebooks for detailed code examples for each NLP task. 

* [Multi-class text classification](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs/automl-nlp-text-classification-multiclass-task-sentiment-analysis/automl-nlp-multiclass-sentiment.ipynb)
* [Multi-label text classification](
https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs/automl-nlp-text-classification-multilabel-task-paper-categorization/automl-nlp-multilabel-paper-cat.ipynb)
* [Named entity recognition](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs/automl-nlp-text-named-entity-recognition-task/automl-nlp-text-ner-task.ipynb)


## Model sweeping and hyperparameter tuning (preview) 

[!INCLUDE [preview disclaimer](../../includes/machine-learning-preview-generic-disclaimer.md)]

AutoML NLP allows you to provide a list of models and combinations of hyperparameters, via the hyperparameter search space in the config. Hyperdrive generates several child runs, each of which is a fine-tuning run for a given NLP model and set of hyperparameter values that were chosen and swept over based on the provided search space.

## Supported model algorithms  

All the pre-trained text DNN models currently available in AutoML NLP for fine-tuning are listed below: 
