
# Set up AutoML to train a natural language processing model 

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]
> [!div class="op_single_selector" title1="Select the version of the developer platform of Azure Machine Learning  you are using:"]
> * [v1](./v1/how-to-auto-train-nlp-models-v1.md)
> * [v2 (current version)](how-to-auto-train-nlp-models.md)
 

In this article, you learn how to train natural language processing (NLP) models with [automated ML](concept-automated-ml.md) in Azure Machine Learning. You can create NLP models with automated ML via the Azure Machine Learning Python SDK v2 or the Azure Machine Learning CLI v2. 

Automated ML supports NLP which allows ML professionals and data scientists to bring their own text data and build custom models for tasks such as, multi-class text classification, multi-label text classification, and named entity recognition (NER).  

You can seamlessly integrate with the [Azure Machine Learning data labeling](how-to-create-text-labeling-projects.md) capability to label your text data or bring your existing labeled data. Automated ML provides the option to use distributed training on multi-GPU compute clusters for faster model training. The resulting model can be operationalized at scale by leveraging Azure ML’s MLOps capabilities. 

## Prerequisites

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

* Azure subscription. If you don't have an Azure subscription, sign up to try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/) today.

* An Azure Machine Learning workspace with a GPU training compute. To create the workspace, see [Create workspace resources](quickstart-create-resources.md). See [GPU optimized virtual machine sizes](../virtual-machines/sizes-gpu.md) for more details of GPU instances provided by Azure.

    > [!WARNING]
    > Support for multilingual models and the use of models with longer max sequence length is necessary for several NLP use cases, such as non-english datasets and longer range documents. As a result, these scenarios may require higher GPU memory for model training to succeed, such as the NC_v3 series or the ND series. 
  
* The Azure Machine Learning CLI v2 installed. For guidance to update and install the latest version, see the [Install and set up CLI (v2)](how-to-configure-cli.md).

* This article assumes some familiarity with setting up an automated machine learning experiment. Follow the [how-to](how-to-configure-auto-train.md) to see the main automated machine learning experiment design patterns.

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

* Azure subscription. If you don't have an Azure subscription, sign up to try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/) today.

* An Azure Machine Learning workspace with a GPU training compute. To create the workspace, see [Create workspace resources](quickstart-create-resources.md). See [GPU optimized virtual machine sizes](../virtual-machines/sizes-gpu.md) for more details of GPU instances provided by Azure.

   > [!WARNING]
   > Support for multilingual models and the use of models with longer max sequence length is necessary for several NLP use cases, such as non-english datasets and longer range documents. As a result, these scenarios may require higher GPU memory for model training to succeed, such as the NC_v3 series or the ND series. 
  
* The Azure Machine Learning Python SDK v2 installed. 

    To install the SDK you can either, 
    * Create a compute instance, which automatically installs the SDK and is pre-configured for ML workflows. See [Create and manage an Azure Machine Learning compute instance](how-to-create-manage-compute-instance.md) for more information. 

    * [Install the `automl` package yourself](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/README.md#setup-using-a-local-conda-environment), which includes the [default installation](/python/api/overview/azure/ml/install#default-install) of the SDK.
