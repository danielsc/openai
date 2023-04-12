At this point, any breakpoints in your `run` function are caught. Use the debug actions to step through your code. For more information on debug actions, see the [debug actions guide](https://code.visualstudio.com/Docs/editor/debugging#_debug-actions).


# [Python](#tab/python)

Now that your application is running in the debugger, try making a prediction to debug your scoring script.

Use the `invoke` method on your `MLClient` object to make a request to your local endpoint.

```python
endpoint = ml_client.online_endpoints.get(name=endpoint_name, local=True)

request_file_path = "../model-1/sample-request.json"

ml_client.online_endpoints.invoke(endpoint_name, request_file_path, local=True)
```

In this case, `<REQUEST-FILE>` is a JSON file that contains input data samples for the model to make predictions on similar to the following JSON:

```json
{"data": [
    [1,2,3,4,5,6,7,8,9,10], 
    [10,9,8,7,6,5,4,3,2,1]
]}
```

> [!TIP]
> The scoring URI is the address where your endpoint listens for requests. The `as_dict` method of endpoint objects returns information similar to `show` in the Azure CLI. The endpoint object can be obtained through `.get`. 
>
>    ```python 
>    print(endpoint)
>    ```
>
> The output should look similar to the following:
>
> ```json
> {
>  "auth_mode": "aml_token",
>  "location": "local",
>  "name": "my-new-endpoint",
>  "properties": {},
>  "provisioning_state": "Succeeded",
>  "scoring_uri": "http://localhost:5001/score",
>  "tags": {},
>  "traffic": {},
>  "type": "online"
>}
>```
>
>The scoring URI can be found in the `scoring_uri` key.

At this point, any breakpoints in your `run` function are caught. Use the debug actions to step through your code. For more information on debug actions, see the [debug actions guide](https://code.visualstudio.com/Docs/editor/debugging#_debug-actions).




## Edit your endpoint

# [Azure CLI](#tab/cli)

As you debug and troubleshoot your application, there are scenarios where you need to update your scoring script and configurations.

To apply changes to your code:

1. Update your code
1. Restart your debug session using the `Developer: Reload Window` command in the command palette. For more information, see the [command palette documentation](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).

> [!NOTE]
> Since the directory containing your code and endpoint assets is mounted onto the dev container, any changes you make in the dev container are synced with your local file system.

For more extensive changes involving updates to your environment and endpoint configuration, use the `ml` extension `update` command. Doing so will trigger a full image rebuild with your changes.

```azurecli
az ml online-deployment update --file <DEPLOYMENT-YAML-SPECIFICATION-FILE> --local --vscode-debug
```

Once the updated image is built and your development container launches, use the VS Code debugger to test and troubleshoot your updated endpoint.

# [Python](#tab/python)

As you debug and troubleshoot your application, there are scenarios where you need to update your scoring script and configurations.

To apply changes to your code:

1. Update your code
1. Restart your debug session using the `Developer: Reload Window` command in the command palette. For more information, see the [command palette documentation](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).

> [!NOTE]
> Since the directory containing your code and endpoint assets is mounted onto the dev container, any changes you make in the dev container are synced with your local file system.

For more extensive changes involving updates to your environment and endpoint configuration, use your `MLClient`'s `online_deployments.update` module/method. Doing so will trigger a full image rebuild with your changes.

```python
new_deployment = ManagedOnlineDeployment(
    name="green",
    endpoint_name=endpoint_name,
    model=Model(path="../model-2/model/sklearn_regression_model.pkl"),
    code_configuration=CodeConfiguration(
        code="../model-2/onlinescoring", scoring_script="score.py"
    ),
    environment=Environment(
        conda_file="../model-2/environment/conda.yml",
        image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:20210727.v1",
    ),
    instance_type="Standard_DS3_v2",
    instance_count=2,
)

deployment = ml_client.online_deployments.begin_create_or_update(
    new_deployment, local=True, vscode_debug=True
).result()
```
