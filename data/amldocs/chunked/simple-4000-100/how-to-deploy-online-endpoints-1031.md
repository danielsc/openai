For more information about the YAML schema, see the [online endpoint YAML reference](reference-yaml-endpoint-online.md).

> [!NOTE]
> To use Kubernetes instead of managed endpoints as a compute target:
> 1. Create and attach your Kubernetes cluster as a compute target to your Azure Machine Learning workspace by using [Azure Machine Learning studio](how-to-attach-kubernetes-to-workspace.md).
> 1. Use the [endpoint YAML](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/kubernetes/kubernetes-endpoint.yml) to target Kubernetes instead of the managed endpoint YAML. You'll need to edit the YAML to change the value of `target` to the name of your registered compute target. You can use this [deployment.yaml](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/kubernetes/kubernetes-blue-deployment.yml) that has additional properties applicable to Kubernetes deployment.
>
> All the commands that are used in this article (except the optional SLA monitoring and Azure Log Analytics integration) can be used either with managed endpoints or with Kubernetes endpoints.

# [Python](#tab/python)

In this article, we first define names of online endpoint and deployment for debug locally.

1. Define endpoint (with name for local endpoint):
      ```python
    # Creating a local endpoint
    import datetime

    local_endpoint_name = "local-" + datetime.datetime.now().strftime("%m%d%H%M%f")

    # create an online endpoint
    endpoint = ManagedOnlineEndpoint(
        name=local_endpoint_name, description="this is a sample local endpoint"
    )
    ```

1. Define deployment (with name for local deployment)

    The example contains all the files needed to deploy a model on an online endpoint. To deploy a model, you must have:

    * Model files (or the name and version of a model that's already registered in your workspace). In the example, we have a scikit-learn model that does regression.
    * The code that's required to score the model. In this case, we have a score.py file.
    * An environment in which your model runs. As you'll see, the environment might be a Docker image with Conda dependencies, or it might be a Dockerfile.
    * Settings to specify the instance type and scaling capacity.

    **Key aspects of deployment**
    * `name` - Name of the deployment.
    * `endpoint_name` - Name of the endpoint to create the deployment under.
    * `model` - The model to use for the deployment. This value can be either a reference to an existing versioned model in the workspace or an inline model specification.
    * `environment` - The environment to use for the deployment. This value can be either a reference to an existing versioned environment in the workspace or an inline environment specification.
    * `code_configuration` - the configuration for the source code and scoring script
        * `path`- Path to the source code directory for scoring the model
        * `scoring_script` - Relative path to the scoring file in the source code directory
    * `instance_type` - The VM size to use for the deployment. For the list of supported sizes, see [Managed online endpoints SKU list](reference-managed-online-endpoints-vm-sku-list.md).
    * `instance_count` - The number of instances to use for the deployment

    ```python
    model = Model(path="../model-1/model/sklearn_regression_model.pkl")
    env = Environment(
        conda_file="../model-1/environment/conda.yml",
        image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest",
    )

    blue_deployment = ManagedOnlineDeployment(
        name="blue",
        endpoint_name=local_endpoint_name,
        model=model,
        environment=env,
        code_configuration=CodeConfiguration(
            code="../model-1/onlinescoring", scoring_script="score.py"
        ),
        instance_type="Standard_DS2_v2",
        instance_count=1,
    )
    ```

# [ARM template](#tab/arm)

The Azure Resource Manager templates [online-endpoint.json](https://github.com/Azure/azureml-examples/tree/main/arm-templates/online-endpoint.json) and [online-endpoint-deployment.json](https://github.com/Azure/azureml-examples/tree/main/arm-templates/online-endpoint-deployment.json) are used by the steps in this article.
