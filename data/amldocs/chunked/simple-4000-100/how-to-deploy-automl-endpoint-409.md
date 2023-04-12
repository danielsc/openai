
## Create the endpoint and deployment

Next, we'll create the managed online endpoints and deployments.

1. Configure online endpoint:

    > [!TIP]
    > * `name`: The name of the endpoint. It must be unique in the Azure region. The name for an endpoint must start with an upper- or lowercase letter and only consist of '-'s and alphanumeric characters. For more information on the naming rules, see [managed online endpoint limits](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints).
    > * `auth_mode` : Use `key` for key-based authentication. Use `aml_token` for Azure Machine Learning token-based authentication. A `key` doesn't expire, but `aml_token` does expire. For more information on authenticating, see [Authenticate to an online endpoint](how-to-authenticate-online-endpoint.md).


    ```python
    # Creating a unique endpoint name with current datetime to avoid conflicts
    import datetime

    online_endpoint_name = "endpoint-" + datetime.datetime.now().strftime("%m%d%H%M%f")

    # create an online endpoint
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="this is a sample online endpoint",
        auth_mode="key",
    )
    ```

1. Create the endpoint:

    Using the `MLClient` created earlier, we'll now create the Endpoint in the workspace. This command will start the endpoint creation and return a confirmation response while the endpoint creation continues.

    ```python
    ml_client.begin_create_or_update(endpoint)
    ```

1. Configure online deployment:

    A deployment is a set of resources required for hosting the model that does the actual inferencing. We'll create a deployment for our endpoint using the `ManagedOnlineDeployment` class.

    ```python
    model = Model(path="./src/model.pkl")
    env = Environment(
        conda_file="./src/conda_env_v_1_0_0.yml",
        image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:latest",
    )

    blue_deployment = ManagedOnlineDeployment(
        name="blue",
        endpoint_name=online_endpoint_name,
        model=model,
        environment=env,
        code_configuration=CodeConfiguration(
            code="./src", scoring_script="scoring_file_v_2_0_0.py"
        ),
        instance_type="Standard_DS2_v2",
        instance_count=1,
    )
    ```

    In the above example, we assume the files you downloaded from the AutoML Models page are in the `src` directory. You can modify the parameters in the code to suit your situation.
    
    | Parameter | Change to |
    | --- | --- |
    | `model:path` | The path to the `model.pkl` file you downloaded. |
    | `code_configuration:code:path` | The directory in which you placed the scoring file. | 
    | `code_configuration:scoring_script` | The name of the Python scoring file (`scoring_file_<VERSION>.py`). |
    | `environment:conda_file` | A file URL for the downloaded conda environment file (`conda_env_<VERSION>.yml`). |

1. Create the deployment:

    Using the `MLClient` created earlier, we'll now create the deployment in the workspace. This command will start the deployment creation and return a confirmation response while the deployment creation continues.

    ```python
    ml_client.begin_create_or_update(blue_deployment)
    ```

After you create a deployment, you can score it as described in [Test the endpoint with sample data](how-to-deploy-managed-online-endpoint-sdk-v2.md#test-the-endpoint-with-sample-data).

You can learn to deploy to managed online endpoints with SDK more in [Deploy machine learning models to managed online endpoint using Python SDK v2](how-to-deploy-managed-online-endpoint-sdk-v2.md).


## Next steps

- [Troubleshooting online endpoints deployment](how-to-troubleshoot-managed-online-endpoints.md)
- [Safe rollout for online endpoints](how-to-safely-rollout-online-endpoints.md)
