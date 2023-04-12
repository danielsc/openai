
# Azure Machine Learning Curated Environments

This article lists the curated environments with latest framework versions in Azure Machine Learning. Curated environments are provided by Azure Machine Learning and are available in your workspace by default. They are backed by cached Docker images that use the latest version of the Azure Machine Learning SDK, reducing the run preparation cost and allowing for faster deployment time. Use these environments to quickly get started with various machine learning frameworks.

> [!NOTE]
> Use the [Python SDK](how-to-use-environments.md), [CLI](/cli/azure/ml/environment#az-ml-environment-list), or Azure Machine Learning [studio](how-to-manage-environments-in-studio.md) to get the full list of environments and their dependencies. For more information, see the [environments article](how-to-use-environments.md#use-a-curated-environment). 

## Why should I use curated environments?

* Reduces training and deployment latency.
* Improves training and deployment success rate.
* Avoid unnecessary image builds.
* Only have required dependencies and access right in the image/container. 

>[!IMPORTANT] 
> To view more information about curated environment packages and versions, visit the Environments tab in the Azure Machine Learning [studio](./how-to-manage-environments-in-studio.md). 

## Curated environments


> [!IMPORTANT]
> Items marked (preview) in this article are currently in public preview.
> The preview version is provided without a service level agreement, and it's not recommended for production workloads. Certain features might not be supported or might have constrained capabilities.
> For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

### Azure Container for PyTorch (ACPT) (preview)

**Name**: AzureML-ACPT-pytorch-1.12-py39-cuda11.6-gpu  
**Description**: The Azure Curated Environment for PyTorch is our latest PyTorch curated environment. It is optimized for large, distributed deep learning workloads and comes pre-packaged with the best of Microsoft technologies for accelerated training, e.g., OnnxRuntime Training (ORT), DeepSpeed, MSCCL, etc. 

The following configurations are supported: 

| Environment Name | OS | GPU Version| Python Version | PyTorch Version | ORT-training Version | DeepSpeed Version | torch-ort Version | 
| --- | --- | --- | --- | --- | --- | --- | --- |
| AzureML-ACPT-pytorch-1.12-py39-cuda11.6-gpu | Ubuntu 20.04  | cu116 | 3.9 | 1.12.1 | 1.13.1 | 0.7.3 | 1.13.1 |
| AzureML-ACPT-pytorch-1.12-py38-cuda11.6-gpu | Ubuntu 20.04  | cu116 | 3.8 | 1.12.1 | 1.12.0 | 0.7.3 | 1.12.0 |
| AzureML-ACPT-pytorch-1.11-py38-cuda11.5-gpu | Ubuntu 20.04  | cu115 | 3.8 | 1.11.0 | 1.11.1 | 0.7.3 | 1.11.0 | 
| AzureML-ACPT-pytorch-1.11-py38-cuda11.3-gpu | Ubuntu 20.04  | cu113 | 3.8 | 1.11.0 | 1.11.1 | 0.7.3 | 1.11.0 |

> [!NOTE]
> Currently, due to underlying cuda and cluster incompatibilities, on [NC series](../virtual-machines/nc-series.md) only AzureML-ACPT-pytorch-1.11-py38-cuda11.3-gpu with cuda 11.3 can be used.

### PyTorch

**Name**: AzureML-pytorch-1.10-ubuntu18.04-py38-cuda11-gpu  
**Description**: An environment for deep learning with PyTorch containing the AzureML Python SDK and other Python packages.  
* GPU: Cuda11
* OS: Ubuntu18.04
* PyTorch: 1.10

Other available PyTorch environments:
* AzureML-pytorch-1.9-ubuntu18.04-py37-cuda11-gpu  
* AzureML-pytorch-1.8-ubuntu18.04-py37-cuda11-gpu
* AzureML-pytorch-1.7-ubuntu18.04-py37-cuda11-gpu


### LightGBM

**Name**: AzureML-lightgbm-3.2-ubuntu18.04-py37-cpu  
**Description**: An environment for machine learning with Scikit-learn, LightGBM, XGBoost, Dask containing the AzureML Python SDK and other packages.  
* OS: Ubuntu18.04
* Dask: 2021.6
* LightGBM: 3.2
* Scikit-learn: 0.24
* XGBoost: 1.4


### Sklearn
**Name**: AzureML-sklearn-1.0-ubuntu20.04-py38-cpu  
**Description**: An environment for tasks such as regression, clustering, and classification with Scikit-learn. Contains the AzureML Python SDK and other Python packages.  
