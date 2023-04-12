For BERT, the model is fine-tuned and trained utilizing the user-provided labels. From here, document embeddings are output as features alongside others, like timestamp-based features, day of week. 

Learn how to [set up natural language processing (NLP) experiments that also use BERT with automated ML](how-to-auto-train-nlp-models.md).

### Steps to invoke BERT

In order to invoke BERT, set  `enable_dnn: True` in your automl_settings and use a GPU compute (`vm_size = "STANDARD_NC6"` or a higher GPU). If a CPU compute is used, then instead of BERT, AutoML enables the BiLSTM DNN featurizer.

Automated ML takes the following steps for BERT. 

1. **Preprocessing and tokenization of all text columns**. For example, the "StringCast" transformer can be found in the final model's featurization summary. An example of how to produce the model's featurization summary can be found in [this notebook](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/classification-text-dnn/auto-ml-classification-text-dnn.ipynb).

2. **Concatenate all text columns into a single text column**, hence the `StringConcatTransformer` in the final model. 

    Our implementation of BERT limits total text length of a training sample to 128 tokens. That means, all text columns when concatenated, should ideally be at most 128 tokens in length. If multiple columns are present, each column should be pruned so this condition is satisfied. Otherwise, for concatenated columns of length >128 tokens BERT's tokenizer layer truncates this input to 128 tokens.

3. **As part of feature sweeping, AutoML compares BERT against the baseline (bag of words features) on a sample of the data.** This comparison determines if BERT would give accuracy improvements. If BERT performs better than the baseline, AutoML then uses BERT for text featurization for the whole data. In that case, you will see the `PretrainedTextDNNTransformer` in the final model.

BERT generally runs longer than other featurizers. For better performance, we recommend using "STANDARD_NC24r" or "STANDARD_NC24rs_V3" for their RDMA capabilities. 

AutoML will distribute BERT training across multiple nodes if they are available (upto a max of eight nodes). This can be done in your `AutoMLConfig` object by setting the `max_concurrent_iterations` parameter to higher than 1. 

## Supported languages for BERT in AutoML 

AutoML currently supports around 100 languages and depending on the dataset's language, AutoML chooses the appropriate BERT model. For German data, we use the German BERT model. For English, we use the English BERT model. For all other languages, we use the multilingual BERT model.

In the following code, the German BERT model is triggered, since the dataset language is specified to `deu`, the three letter language code for German according to [ISO classification](https://iso639-3.sil.org/code/deu):

```python
from azureml.automl.core.featurization import FeaturizationConfig

featurization_config = FeaturizationConfig(dataset_language='deu')

automl_settings = {
    "experiment_timeout_minutes": 120,
    "primary_metric": 'accuracy',
# All other settings you want to use
    "featurization": featurization_config,
    
    "enable_dnn": True, # This enables BERT DNN featurizer
    "enable_voting_ensemble": False,
    "enable_stack_ensemble": False
}
```

## Next steps

* Learn how to set up your automated ML experiments:

    * For a code-first experience: [Configure automated ML experiments by using the Azure Machine Learning SDK](how-to-configure-auto-train.md).
    * For a low-code or no-code experience: [Create your automated ML experiments in the Azure Machine Learning studio](how-to-use-automated-ml-for-ml-models.md).

* Learn more about [how and where to deploy a model](./v1/how-to-deploy-and-where.md).

* Learn more about [how to train a regression model by using automated machine learning](./v1/how-to-auto-train-models-v1.md) or [how to train by using automated machine learning on a remote resource](./v1/concept-automated-ml-v1.md#local-remote).
