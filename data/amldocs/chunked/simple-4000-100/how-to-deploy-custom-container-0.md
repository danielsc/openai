
# Deploy a TensorFlow model served with TensorFlow Serving using a custom container in an online endpoint

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

Learn how to deploy a custom container as an online endpoint in Azure Machine Learning.

Custom container deployments can use web servers other than the default Python Flask server used by Azure Machine Learning. Users of these deployments can still take advantage of Azure Machine Learning's built-in monitoring, scaling, alerting, and authentication.

You can find [various examples](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online/custom-container) for TensorFlow Serving, TorchServe, Triton Inference Server, Plumber R package, and AzureML Inference Minimal image as below:

|Example|Script (CLI)|Description| 
|-------|------|---------|
|[minimal/multimodel](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/custom-container/minimal/multimodel)|[deploy-custom-container-minimal-multimodel](https://github.com/Azure/azureml-examples/blob/main/cli/deploy-custom-container-minimal-multimodel.sh)|Deploy multiple models to a single deployment by extending the AzureML Inference Minimal image.|
|[minimal/single-model](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/custom-container/minimal/single-model)|[deploy-custom-container-minimal-single-model](https://github.com/Azure/azureml-examples/blob/main/cli/deploy-custom-container-minimal-single-model.sh)|Deploy a single model by extending the AzureML Inference Minimal image.|
|[mlflow/multideployment-scikit](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/custom-container/mlflow/multideployment-scikit)|[deploy-custom-container-mlflow-multideployment-scikit](https://github.com/Azure/azureml-examples/blob/main/cli/deploy-custom-container-mlflow-multideployment-scikit.sh)|Deploy two MLFlow models with different Python requirements to two separate deployments behind a single endpoint using the AzureML Inference Minimal Image.|
|[r/multimodel-plumber](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/custom-container/r/multimodel-plumber)|[deploy-custom-container-r-multimodel-plumber](https://github.com/Azure/azureml-examples/blob/main/cli/deploy-custom-container-r-multimodel-plumber.sh)|Deploy three regression models to one endpoint using the Plumber R package|
|[tfserving/half-plus-two](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/custom-container/tfserving/half-plus-two)|[deploy-custom-container-tfserving-half-plus-two](https://github.com/Azure/azureml-examples/blob/main/cli/deploy-custom-container-tfserving-half-plus-two.sh)|Deploy a simple Half Plus Two model using a TensorFlow Serving custom container using the standard model registration process.|
|[tfserving/half-plus-two-integrated](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/custom-container/tfserving/half-plus-two-integrated)|[deploy-custom-container-tfserving-half-plus-two-integrated](https://github.com/Azure/azureml-examples/blob/main/cli/deploy-custom-container-tfserving-half-plus-two-integrated.sh)|Deploy a simple Half Plus Two model using a TensorFlow Serving custom container with the model integrated into the image.|
|[torchserve/densenet](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/custom-container/torchserve/densenet)|[deploy-custom-container-torchserve-densenet](https://github.com/Azure/azureml-examples/blob/main/cli/deploy-custom-container-torchserve-densenet.sh)|Deploy a single model using a TorchServe custom container.|
|[torchserve/huggingface-textgen](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/custom-container/torchserve/huggingface-textgen)|[deploy-custom-container-torchserve-huggingface-textgen](https://github.com/Azure/azureml-examples/blob/main/cli/deploy-custom-container-torchserve-huggingface-textgen.sh)|Deploy Hugging Face models to an online endpoint and follow along with the Hugging Face Transformers TorchServe example.| 
