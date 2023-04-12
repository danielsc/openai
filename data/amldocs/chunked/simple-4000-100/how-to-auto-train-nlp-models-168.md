   * In order to use the long range text feature, you should use a NC6 or higher/better SKUs for GPU such as: [NCv3](../virtual-machines/ncv3-series.md) series or [ND](../virtual-machines/nd-series.md) series.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

For CLI v2 AutoML jobs you configure your experiment in a YAML file like the following. 



# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]


For AutoML jobs via the SDK, you configure the job with the specific NLP task function. The following example demonstrates the configuration for `text_classification`.
```Python
# general job parameters
compute_name = "gpu-cluster"
exp_name = "dpv2-nlp-text-classification-experiment"

# Create the AutoML job with the related factory-function.
text_classification_job = automl.text_classification(
    compute=compute_name,
    # name="dpv2-nlp-text-classification-multiclass-job-01",
    experiment_name=exp_name,
    training_data=my_training_data_input,
    validation_data=my_validation_data_input,
    target_column_name="Sentiment",
    primary_metric="accuracy",
    tags={"my_custom_tag": "My custom value"},
)

text_classification_job.set_limits(timeout=120)

```

### Language settings

As part of the NLP functionality, automated ML supports 104 languages leveraging language specific and multilingual pre-trained text DNN models, such as the BERT family of models. Currently, language selection defaults to English. 

The following table summarizes what model is applied based on task type and language. See  the full list of [supported languages and their codes](/python/api/azureml-automl-core/azureml.automl.core.constants.textdnnlanguages#azureml-automl-core-constants-textdnnlanguages-supported).

 Task type |Syntax for `dataset_language` | Text model algorithm
----|----|---
Multi-label text classification|`"eng"` <br>  `"deu"` <br> `"mul"`|  English&nbsp;BERT&nbsp;[uncased](https://huggingface.co/bert-base-uncased) <br>  [German BERT](https://huggingface.co/bert-base-german-cased)<br>  [Multilingual BERT](https://huggingface.co/bert-base-multilingual-cased) <br><br>For all other languages, automated ML applies multilingual BERT
Multi-class text classification|`"eng"` <br>  `"deu"` <br> `"mul"`|  English&nbsp;BERT&nbsp;[cased](https://huggingface.co/bert-base-cased)<br>  [Multilingual BERT](https://huggingface.co/bert-base-multilingual-cased) <br><br>For all other languages, automated ML applies multilingual BERT
Named entity recognition (NER)|`"eng"` <br>  `"deu"` <br> `"mul"`|  English&nbsp;BERT&nbsp;[cased](https://huggingface.co/bert-base-cased) <br>  [German BERT](https://huggingface.co/bert-base-german-cased)<br>  [Multilingual BERT](https://huggingface.co/bert-base-multilingual-cased) <br><br>For all other languages, automated ML applies multilingual BERT

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

You can specify your dataset language in the featurization section of your configuration YAML file. BERT is also used in the featurization process of automated ML experiment training, learn more about [BERT integration and featurization in automated ML](how-to-configure-auto-features.md#bert-integration-in-automated-ml).

```azurecli
featurization:
   dataset_language: "eng"
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

You can specify your dataset language with the `set_featurization()` method. BERT is also used in the featurization process of automated ML experiment training, learn more about [BERT integration and featurization in automated ML](how-to-configure-auto-features.md#bert-integration-in-automated-ml).

```python
text_classification_job.set_featurization(dataset_language='eng')
```


## Distributed training

You can also run your NLP experiments with distributed training on an Azure ML compute cluster. 

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]
