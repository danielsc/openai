
# High-performance serving with Triton Inference Server (Preview)

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

Learn how to use [NVIDIA Triton Inference Server](https://aka.ms/nvidia-triton-docs) in Azure Machine Learning with [online endpoints](concept-endpoints.md#what-are-online-endpoints).

Triton is multi-framework, open-source software that is optimized for inference. It supports popular machine learning frameworks like TensorFlow, ONNX Runtime, PyTorch, NVIDIA TensorRT, and more. It can be used for your CPU or GPU workloads. No-code deployment for Triton models is supported in both [managed online endpoints and Kubernetes online endpoints](concept-endpoints.md#managed-online-endpoints-vs-kubernetes-online-endpoints).

In this article, you will learn how to deploy Triton and a model to a [managed online endpoint](concept-endpoints.md#managed-online-endpoints). Information is provided on using the CLI (command line), Python SDK v2, and Azure Machine Learning studio. 

> [!NOTE]
> * [NVIDIA Triton Inference Server](https://aka.ms/nvidia-triton-docs) is an open-source third-party software that is integrated in Azure Machine Learning.
> * While Azure Machine Learning online endpoints are generally available, _using Triton with an online endpoint/deployment is still in preview_. 

## Prerequisites

# [Azure CLI](#tab/azure-cli)

[!INCLUDE [basic prereqs](../../includes/machine-learning-cli-prereqs.md)]

* A working Python 3.8 (or higher) environment. 

* You must have additional Python packages installed for scoring and may install them with the code below. They include:
    * Numpy - An array and numerical computing library 
    * [Triton Inference Server Client](https://github.com/triton-inference-server/client) - Facilitates requests to the Triton Inference Server
    * Pillow - A library for image operations
    * Gevent - A networking library used when connecting to the Triton Server

```azurecli
pip install numpy
pip install tritonclient[http]
pip install pillow
pip install gevent
```

* Access to NCv3-series VMs for your Azure subscription.

    > [!IMPORTANT]
    > You may need to request a quota increase for your subscription before you can use this series of VMs. For more information, see [NCv3-series](../virtual-machines/ncv3-series.md).

NVIDIA Triton Inference Server requires a specific model repository structure, where there is a directory for each model and subdirectories for the model version. The contents of each model version subdirectory is determined by the type of the model and the requirements of the backend that supports the model. To see all the model repository structure [https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_repository.md#model-files](https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_repository.md#model-files)

The information in this document is based on using a model stored in ONNX format, so the directory structure of the model repository is `<model-repository>/<model-name>/1/model.onnx`. Specifically, this model performs image identification.

[!INCLUDE [clone repo & set defaults](../../includes/machine-learning-cli-prepare.md)]

# [Python](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

[!INCLUDE [sdk](../../includes/machine-learning-sdk-v2-prereqs.md)]

* A working Python 3.8 (or higher) environment.

* You must have additional Python packages installed for scoring and may install them with the code below. They include:
    * Numpy - An array and numerical computing library 
    * [Triton Inference Server Client](https://github.com/triton-inference-server/client) - Facilitates requests to the Triton Inference Server
    * Pillow - A library for image operations
    * Gevent - A networking library used when connecting to the Triton Server

    ```azurecli
    pip install numpy
    pip install tritonclient[http]
    pip install pillow
    pip install gevent
    ```

* Access to NCv3-series VMs for your Azure subscription.
