The Bandit early termination policy is also used. This policy terminates poor performing trials; that is, those trials that are not within 20% slack of the best performing trial, which significantly saves compute resources.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
sweep:
  sampling_algorithm: random
  early_termination:
    type: bandit
    evaluation_interval: 2
    slack_factor: 0.2
    delay_evaluation: 6
```

```yaml
search_space:
  - model_name:
      type: choice
      values: [yolov5]
    learning_rate:
      type: uniform
      min_value: 0.0001
      max_value: 0.01
    model_size:
      type: choice
      values: [small, medium]

  - model_name:
      type: choice
      values: [fasterrcnn_resnet50_fpn]
    learning_rate:
      type: uniform
      min_value: 0.0001
      max_value: 0.001
    optimizer:
      type: choice
      values: [sgd, adam, adamw]
    min_size:
      type: choice
      values: [600, 800]
```

# [Python SDK](#tab/python)
 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]


[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=sweep-settings)]

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=search-space-settings)]


Once the search space and sweep settings are defined, you can then submit the job to train an image model using your training dataset.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

To submit your AutoML job, you run the following CLI v2 command with the path to your .yml file, workspace name, resource group and subscription ID.

```azurecli
az ml job create --file ./hello-automl-job-basic.yml --workspace-name [YOUR_AZURE_WORKSPACE] --resource-group [YOUR_AZURE_RESOURCE_GROUP] --subscription [YOUR_AZURE_SUBSCRIPTION]
```

# [Python SDK](#tab/python)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

When you've configured your AutoML Job to the desired settings, you can submit the job.

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=submit-run)]


When doing a hyperparameter sweep, it can be useful to visualize the different trials that were tried using the HyperDrive UI. You can navigate to this UI by going to the 'Child jobs' tab in the UI of the main automl_image_job from above, which is the HyperDrive parent job. Then you can go into the 'Child jobs' tab of this one.

Alternatively, here below you can see directly the HyperDrive parent job and navigate to its 'Child jobs' tab:

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]
```yaml
CLI example not available, please use Python SDK.
```


# [Python SDK](#tab/python)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
hd_job = ml_client.jobs.get(returned_job.name + '_HD')
hd_job
```


## Register and deploy model

Once the job completes, you can register the model that was created from the best trial (configuration that resulted in the best primary metric). You can either register the model after downloading or by specifying the azureml path with corresponding jobid.  

### Get the best trial


# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]
```yaml
CLI example not available, please use Python SDK.
```


# [Python SDK](#tab/python)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=best_run)] 
