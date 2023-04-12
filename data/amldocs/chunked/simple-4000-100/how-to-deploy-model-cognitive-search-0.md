

# Deploy a model for use with Cognitive Search

[!INCLUDE [sdk v1](../../includes/machine-learning-sdk-v1.md)]

This article teaches you how to use Azure Machine Learning to deploy a model for use with [Azure Cognitive Search](../search/search-what-is-azure-search.md).

Cognitive Search performs content processing over heterogenous content, to make it queryable by humans or applications. This process can be enhanced by using a model deployed from Azure Machine Learning.

Azure Machine Learning can deploy a trained model as a web service. The web service is then embedded in a Cognitive Search _skill_, which becomes part of the processing pipeline.

> [!IMPORTANT]
> The information in this article is specific to the deployment of the model. It provides information on the supported deployment configurations that allow the model to be used by Cognitive Search.
>
> For information on how to configure Cognitive Search to use the deployed model, see the [Build and deploy a custom skill with Azure Machine Learning](../search/cognitive-search-tutorial-aml-custom-skill.md) tutorial.
>
> For the sample that the tutorial is based on, see [https://github.com/Azure-Samples/azure-search-python-samples/tree/master/AzureML-Custom-Skill](https://github.com/Azure-Samples/azure-search-python-samples/tree/master/AzureML-Custom-Skill).

When deploying a model for use with Azure Cognitive Search, the deployment must meet the following requirements:

* Use Azure Kubernetes Service to host the model for inference.
* Enable transport layer security (TLS) for the Azure Kubernetes Service. TLS is used to secure HTTPS communications between Cognitive Search and the deployed model.
* The entry script must use the `inference_schema` package to generate an OpenAPI (Swagger) schema for the service.
* The entry script must also accept JSON data as input, and generate JSON as output.


## Prerequisites

* An Azure Machine Learning workspace. For more information, see [Create workspace resources](quickstart-create-resources.md).

* A Python development environment with the Azure Machine Learning SDK installed. For more information, see [Azure Machine Learning SDK](/python/api/overview/azure/ml/install).  

* A registered model. If you do not have a model, use the example notebook at [https://github.com/Azure-Samples/azure-search-python-samples/tree/master/AzureML-Custom-Skill](https://github.com/Azure-Samples/azure-search-python-samples/tree/master/AzureML-Custom-Skill).

* A general understanding of [How and where to deploy models](v1/how-to-deploy-and-where.md).

## Connect to your workspace

An Azure Machine Learning workspace provides a centralized place to work with all the artifacts you create when you use Azure Machine Learning. The workspace keeps a history of all training jobs, including logs, metrics, output, and a snapshot of your scripts.

To connect to an existing workspace, use the following code:

> [!IMPORTANT]
> This code snippet expects the workspace configuration to be saved in the current directory or its parent. For more information, see [Create and manage Azure Machine Learning workspaces](how-to-manage-workspace.md). For more information on saving the configuration to file, see [Create a workspace configuration file](v1/how-to-configure-environment-v1.md).

```python
from azureml.core import Workspace

try:
    # Load the workspace configuration from local cached inffo
    ws = Workspace.from_config()
    print(ws.name, ws.location, ws.resource_group, ws.location, sep='\t')
    print('Library configuration succeeded')
except:
    print('Workspace not found')
```

## Create a Kubernetes cluster

**Time estimate**: Approximately 20 minutes.

A Kubernetes cluster is a set of virtual machine instances (called nodes) that are used for running containerized applications.

When you deploy a model from Azure Machine Learning to Azure Kubernetes Service, the model and all the assets needed to host it as a web service are packaged into a Docker container. This container is then deployed onto the cluster.
