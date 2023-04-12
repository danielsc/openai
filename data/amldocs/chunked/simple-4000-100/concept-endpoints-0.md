
# What are Azure Machine Learning endpoints?

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]


Use Azure Machine Learning endpoints to streamline model deployments for both real-time and batch inference deployments. Endpoints provide a unified interface to invoke and manage model deployments across compute types.

In this article, you learn about:
> [!div class="checklist"]
> * Endpoints
> * Deployments
> * Managed online endpoints
> * Kubernetes online endpoints
> * Batch inference endpoints

## What are endpoints and deployments?

After you train a machine learning model, you need to deploy the model so that others can use it to do inferencing. In Azure Machine Learning, you can use **endpoints** and **deployments** to do so.

An **endpoint**, in this context, is an HTTPS path that provides an interface for clients to send requests (input data) and receive the inferencing (scoring) output of a trained model. An endpoint provides:
- Authentication using "key & token" based auth 
- SSL termination 
- A stable scoring URI (endpoint-name.region.inference.ml.azure.com)


A **deployment** is a set of resources required for hosting the model that does the actual inferencing. 

A single endpoint can contain multiple deployments. Endpoints and deployments are independent Azure Resource Manager resources that appear in the Azure portal.

Azure Machine Learning allows you to implement both [online endpoints](#what-are-online-endpoints) and [batch endpoints](#what-are-batch-endpoints).

### Multiple developer interfaces

Create and manage batch and online endpoints with multiple developer tools:
- The Azure CLI and the Python SDK
- Azure Resource Manager/REST API
- Azure Machine Learning studio web portal
- Azure portal (IT/Admin)
- Support for CI/CD MLOps pipelines using the Azure CLI interface & REST/ARM interfaces

## What are online endpoints?

**Online endpoints** are endpoints that are used for online (real-time) inferencing. Compared to **batch endpoints**, **online endpoints** contain **deployments** that are ready to receive data from clients and can send responses back in real time.

The following diagram shows an online endpoint that has two deployments, 'blue' and 'green'. The blue deployment uses VMs with a CPU SKU, and runs version 1 of a model. The green deployment uses VMs with a GPU SKU, and uses version 2 of the model. The endpoint is configured to route 90% of incoming traffic to the blue deployment, while green receives the remaining 10%.

:::image type="content" source="media/concept-endpoints/endpoint-concept.png" alt-text="Diagram showing an endpoint splitting traffic to two deployments.":::

### Online deployments requirements

To create an online endpoint, you need to specify the following elements:
- Model files (or specify a registered model in your workspace) 
- Scoring script - code needed to do scoring/inferencing
- Environment - a Docker image with Conda dependencies, or a dockerfile 
- Compute instance & scale settings 

Learn how to deploy online endpoints from the [CLI/SDK](how-to-deploy-online-endpoints.md) and the [studio web portal](how-to-use-managed-online-endpoint-studio.md).

### Test and deploy locally for faster debugging

Deploy locally to test your endpoints without deploying to the cloud. Azure Machine Learning creates a local Docker image that mimics the Azure ML image. Azure Machine Learning will build and run deployments for you locally, and cache the image for rapid iterations.

### Native blue/green deployment 

Recall, that a single endpoint can have multiple deployments. The online endpoint can do load balancing to give any percentage of traffic to each deployment.

Traffic allocation can be used to do safe rollout blue/green deployments by balancing requests between different instances.

> [!TIP]
> A request can bypass the configured traffic load balancing by including an HTTP header of `azureml-model-deployment`. Set the header value to the name of the deployment you want the request to route to.
