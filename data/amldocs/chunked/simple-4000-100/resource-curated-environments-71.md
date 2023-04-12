**Description**: An environment for tasks such as regression, clustering, and classification with Scikit-learn. Contains the AzureML Python SDK and other Python packages.  
* OS: Ubuntu20.04
* Scikit-learn: 1.0

Other available Sklearn environments:
* AzureML-sklearn-0.24-ubuntu18.04-py37-cpu


### TensorFlow

**Name**: AzureML-tensorflow-2.4-ubuntu18.04-py37-cuda11-gpu  
**Description**: An environment for deep learning with TensorFlow containing the AzureML Python SDK and other Python packages.  
* GPU: Cuda11
* Horovod: 2.4.1
* OS: Ubuntu18.04
* TensorFlow: 2.4


## Automated ML (AutoML)

Azure ML pipeline training workflows that use AutoML automatically selects a curated environment based on the compute type and whether DNN is enabled. AutoML provides the following curated environments:

| Name | Compute Type | DNN enabled |
| --- | --- | --- |
|AzureML-AutoML | CPU | No |
|AzureML-AutoML-DNN | CPU | Yes |
| AzureML-AutoML-GPU | GPU | No |
| AzureML-AutoML-DNN-GPU | GPU | Yes |

For more information on AutoML and Azure ML pipelines, see [use automated ML in an Azure Machine Learning pipeline in Python](v1/how-to-use-automlstep-in-pipelines.md).

## Support
Version updates for supported environments, including the base images they reference, are released every two weeks to address vulnerabilities no older than 30 days. Based on usage, some environments may be deprecated (hidden from the product but usable) to support more common machine learning scenarios.
