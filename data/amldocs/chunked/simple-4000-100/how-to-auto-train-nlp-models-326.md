All the pre-trained text DNN models currently available in AutoML NLP for fine-tuning are listed below: 

* bert_base_cased 
* bert_large_uncased 
* bert_base_multilingual_cased 
* bert_base_german_cased 
* bert_large_cased 
* distilbert_base_cased 
* distilbert_base_uncased 
* roberta_base 
* roberta_large 
* distilroberta_base 
* xlm_roberta_base 
* xlm_roberta_large 
* xlnet_base_cased 
* xlnet_large_cased 

Note that the large models are significantly larger than their base counterparts. They are typically more performant, but they take up more GPU memory and time for training. As such, their SKU requirements are more stringent: we recommend running on ND-series VMs for the best results. 

## Supported hyperparameters 

The following table describes the hyperparameters that AutoML NLP supports. 

| Parameter name | Description | Syntax |
|-------|---------|---------| 
| gradient_accumulation_steps | The number of backward operations whose gradients are to be summed up before performing one step of gradient descent by calling the optimizer’s step function. <br><br> This is leveraged to use an effective batch size which is gradient_accumulation_steps times larger than the maximum size that fits the GPU. | Must be a positive integer.
| learning_rate | Initial learning rate. | Must be a float in the range (0, 1). |
| learning_rate_scheduler |Type of learning rate scheduler. | Must choose from `linear, cosine, cosine_with_restarts, polynomial, constant, constant_with_warmup`.  |
| model_name | Name of one of the supported models.  | Must choose from `bert_base_cased, bert_base_uncased, bert_base_multilingual_cased, bert_base_german_cased, bert_large_cased, bert_large_uncased, distilbert_base_cased, distilbert_base_uncased, roberta_base, roberta_large, distilroberta_base, xlm_roberta_base, xlm_roberta_large, xlnet_base_cased, xlnet_large_cased`. |
| number_of_epochs | Number of training epochs. | Must be a positive integer. |
| training_batch_size | Training batch size. | Must be a positive integer. |
| validation_batch_size | Validation batch size. | Must be a positive integer. |
| warmup_ratio | Ratio of total training steps used for a linear warmup from 0 to learning_rate.  | Must be a float in the range [0, 1]. |
| weight_decay | Value of weight decay when optimizer is sgd, adam, or adamw. | Must be a float in the range [0, 1]. |

All discrete hyperparameters only allow choice distributions, such as the integer-typed `training_batch_size` and the string-typed `model_name` hyperparameters. All continuous hyperparameters like `learning_rate` support all distributions. 

## Configure your sweep settings 

You can configure all the sweep-related parameters. Multiple model subspaces can be constructed with hyperparameters conditional to the respective model, as seen below in each example.   

The same discrete and continuous distribution options that are available for general HyperDrive jobs are supported here. See all nine options in [Hyperparameter tuning a model](how-to-tune-hyperparameters.md#define-the-search-space)


# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
limits: 
  timeout_minutes: 120  
  max_trials: 4 
  max_concurrent_trials: 2 

sweep: 
  sampling_algorithm: grid 
  early_termination: 
    type: bandit 
    evaluation_interval: 10 
    slack_factor: 0.2 

search_space: 
  - model_name: 
      type: choice 
      values: [bert_base_cased, roberta_base] 
    number_of_epochs: 
      type: choice 
      values: [3, 4] 
  - model_name: 
      type: choice 
      values: [distilbert_base_cased] 
    learning_rate: 
      type: uniform 
      min_value: 0.000005 
      max_value: 0.00005 
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

You can set the limits for your model sweeping job: 

```python
text_ner_job.set_limits( 
                        timeout_minutes=120, 
                        trial_timeout_minutes=20, 
                        max_trials=4, 
                        max_concurrent_trials=2, 
                        max_nodes=4) 
```
