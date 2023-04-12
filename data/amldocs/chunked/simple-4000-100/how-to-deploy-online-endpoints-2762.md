::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="create_deployment" :::

This deployment might take up to 15 minutes, depending on whether the underlying environment or image is being built for the first time. Subsequent deployments that use the same environment will finish processing more quickly.

> [!TIP]
> * If you prefer not to block your CLI console, you may add the flag `--no-wait` to the command. However, this will stop the interactive display of the deployment status.

> [!IMPORTANT]
> The `--all-traffic` flag in the above `az ml online-deployment create` allocates 100% of the traffic to the endpoint to the newly created deployment. Though this is helpful for development and testing purposes, for production, you might want to open traffic to the new deployment through an explicit command. For example,
> `az ml online-endpoint update -n $ENDPOINT_NAME --traffic "blue=100"` 

# [Python](#tab/python)

1. Configure online endpoint:

    > [!TIP]
    > * `endpoint_name`: The name of the endpoint. It must be unique in the Azure region. For more information on the naming rules, see [managed online endpoint limits](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints).
    > * `auth_mode` : Use `key` for key-based authentication. Use `aml_token` for Azure Machine Learning token-based authentication. A `key` doesn't expire, but `aml_token` does expire. For more information on authenticating, see [Authenticate to an online endpoint](how-to-authenticate-online-endpoint.md).
    > * Optionally, you can add description, tags to your endpoint.

    ```python
    # Creating a unique endpoint name with current datetime to avoid conflicts
    import datetime

    online_endpoint_name = "endpoint-" + datetime.datetime.now().strftime("%m%d%H%M%f")

    # create an online endpoint
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="this is a sample online endpoint",
        auth_mode="key",
        tags={"foo": "bar"},
    )
    ```

1. Create the endpoint:

    Using the `MLClient` created earlier, we'll now create the Endpoint in the workspace. This command will start the endpoint creation and return a confirmation response while the endpoint creation continues.

    ```python
    ml_client.online_endpoints.begin_create_or_update(endpoint)
    ```

2. Configure online deployment:

    A deployment is a set of resources required for hosting the model that does the actual inferencing. We'll create a deployment for our endpoint using the `ManagedOnlineDeployment` class.

    ```python
    model = Model(path="../model-1/model/sklearn_regression_model.pkl")
    env = Environment(
        conda_file="../model-1/environment/conda.yml",
        image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:latest",
    )

    blue_deployment = ManagedOnlineDeployment(
        name="blue",
        endpoint_name=online_endpoint_name,
        model=model,
        environment=env,
        code_configuration=CodeConfiguration(
            code="../model-1/onlinescoring", scoring_script="score.py"
        ),
        instance_type="Standard_DS2_v2",
        instance_count=1,
    )
    ```

3. Create the deployment:

    Using the `MLClient` created earlier, we'll now create the deployment in the workspace. This command will start the deployment creation and return a confirmation response while the deployment creation continues.

    ```python
    ml_client.online_deployments.begin_create_or_update(blue_deployment)
    ```

    > [!TIP]
    > * If you prefer not to block your Python console, you may add the flag `no_wait=True` to the parameters. However, this will stop the interactive display of the deployment status.

    ```python
    # blue deployment takes 100 traffic
    endpoint.traffic = {"blue": 100}
    ml_client.online_endpoints.begin_create_or_update(endpoint)
    ```

# [ARM template](#tab/arm)

1. The following example demonstrates using the template to create an online endpoint:
