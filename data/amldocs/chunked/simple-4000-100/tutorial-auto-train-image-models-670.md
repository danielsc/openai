You can also keep the resource group but delete a single workspace. Display the workspace properties and select **Delete**.

## Next steps

In this automated machine learning tutorial, you did the following tasks:

> [!div class="checklist"]
> * Configured a workspace and prepared data for an experiment.
> * Trained an automated object detection model
> * Specified hyperparameter values for your model
> * Performed a hyperparameter sweep
> * Deployed your model
> * Visualized detections

* [Learn more about computer vision in automated ML](concept-automated-ml.md#computer-vision).
* [Learn how to set up AutoML to train computer vision models with Python](how-to-auto-train-image-models.md).
* [Learn how to configure incremental training on computer vision models](how-to-auto-train-image-models.md#incremental-training-optional).
* See [what hyperparameters are available for computer vision tasks](reference-automl-images-hyperparameters.md).
* Code examples:

    # [Azure CLI](#tab/cli)
    [!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]
    
    * Review detailed code examples and use cases in the [azureml-examples repository for automated machine learning samples](https://github.com/Azure/azureml-examples/tree/sdk-preview/cli/jobs/automl-standalone-jobs). Please check the folders with 'cli-automl-image-' prefix for samples specific to building computer vision models.
    
    # [Python SDK](#tab/python)
    [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

    * Review detailed code examples and use cases in the [GitHub notebook repository for automated machine learning samples](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs). Please check the folders with 'automl-image-' prefix for samples specific to building computer vision models.
    

> [!NOTE]
> Use of the fridge objects dataset is available through the license under the [MIT License](https://github.com/microsoft/computervision-recipes/blob/master/LICENSE).
