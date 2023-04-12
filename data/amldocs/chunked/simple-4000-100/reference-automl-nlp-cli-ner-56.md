| gradient_accumulation_steps | The number of backward operations whose gradients are to be summed up before performing one step of gradient descent by calling the optimizer’s step function. <br><br> This is leveraged to use an effective batch size which is gradient_accumulation_steps times larger than the maximum size that fits the GPU. | Must be a positive integer.
| learning_rate | Initial learning rate. | Must be a float in the range (0, 1). |
| learning_rate_scheduler |Type of learning rate scheduler. | Must choose from `linear, cosine, cosine_with_restarts, polynomial, constant, constant_with_warmup`.  |
| model_name | Name of one of the supported models.  | Must choose from `bert_base_cased, bert_base_uncased, bert_base_multilingual_cased, bert_base_german_cased, bert_large_cased, bert_large_uncased, distilbert_base_cased, distilbert_base_uncased, roberta_base, roberta_large, distilroberta_base, xlm_roberta_base, xlm_roberta_large, xlnet_base_cased, xlnet_large_cased`. |
| number_of_epochs | Number of training epochs. | Must be a positive integer. |
| training_batch_size | Training batch size. | Must be a positive integer. |
| validation_batch_size | Validation batch size. | Must be a positive integer. |
| warmup_ratio | Ratio of total training steps used for a linear warmup from 0 to learning_rate.  | Must be a float in the range [0, 1]. |
| weight_decay | Value of weight decay when optimizer is sgd, adam, or adamw. | Must be a float in the range [0, 1]. |

### Training or validation data

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `description` | string | The detailed information that describes this input data. | | |
| `path` | string | The path from where data should be loaded. Path can be a `file` path, `folder` path or `pattern` for paths. `pattern` specifies a search pattern to allow globbing(`*` and `**`) of files and folders containing data. URI types are `azureml`, `https`, `wasbs`, `abfss`, and `adl`. For more information on how to use the `azureml://` URI format, see [core yaml syntax](./reference-yaml-core-syntax.md). URI of the location of the artifact file. If this URI doesn't have a scheme (for example, http:, azureml: etc.), then it's considered a local reference and the file it points to is uploaded to the default workspace blob-storage as the entity is created.  | | |
| `mode` | string | Dataset delivery mechanism. | `direct` | `direct` |
| `type` | const |  In order to generate nlp models, the user needs to bring training data in the form of an MLTable. For more information, see [preparing data](./how-to-auto-train-nlp-models.md#preparing-data) | mltable | mltable|

### Best model output configuration

| Key | Type | Description | Allowed values |Default value |
| --- | ---- | ----------- | -------------- | ------------ |
| `type` | string | **Required.** Type of best model. AutoML allows only mlflow models. | `mlflow_model` | `mlflow_model` |
| `path` | string | **Required.** URI of the location where the model-artifact file(s) are stored. If this URI doesn't have a scheme (for example, http:, azureml: etc.), then it's considered a local reference and the file it points to is uploaded to the default workspace blob-storage as the entity is created. |  |  |
| `storage_uri` | string | The HTTP URL of the Model. Use this URL with `az storage copy -s THIS_URL -d DESTINATION_PATH --recursive` to download the data.  | | |

## Remarks

The `az ml job` command can be used for managing Azure Machine Learning jobs.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/jobs). Examples relevant to text NER job are linked below.  

## YAML: AutoML text NER job

```yaml
$schema: https://azuremlsdk2.blob.core.windows.net/preview/0.0.1/autoMLJob.schema.json

type: automl
experiment_name: dpv2-cli-text-ner
description: A text named entity recognition job using CoNLL 2003 data

compute: azureml:gpu-cluster

task: text_ner
primary_metric: accuracy
log_verbosity: debug

limits:
  timeout_minutes: 60

training_data:
  path: "./training-mltable-folder"
  type: mltable
validation_data:
  type: mltable
  path: "./validation-mltable-folder"

# featurization:
#   dataset_language: "eng"

```
