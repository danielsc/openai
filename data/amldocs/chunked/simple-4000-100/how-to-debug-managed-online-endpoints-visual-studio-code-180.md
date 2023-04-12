
> [!IMPORTANT]
> On Windows Subsystem for Linux (WSL), you'll need to update your PATH environment variable to include the path to the VS Code executable or use WSL interop. For more information, see [Windows interoperability with Linux](/windows/wsl/interop).

A Docker image is built locally. Any environment configuration or model file errors are surfaced at this stage of the process.

> [!NOTE]
> The first time you launch a new or updated dev container it can take several minutes.

Once the image successfully builds, your dev container opens in a VS Code window.

You'll use a few VS Code extensions to debug your deployments in the dev container. Azure Machine Learning automatically installs these extensions in your dev container.

- Inference Debug
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

> [!IMPORTANT]
> Before starting your debug session, make sure that the VS Code extensions have finished installing in your dev container.  





## Start debug session

Once your environment is set up, use the VS Code debugger to test and debug your deployment locally.

1. Open your scoring script in Visual Studio Code.

    > [!TIP]
    > The score.py script used by the endpoint deployed earlier is located at `azureml-samples/cli/endpoints/online/managed/sample/score.py` in the repository you cloned. However, the steps in this guide work with any scoring script.

1. Set a breakpoint anywhere in your scoring script.

    - To debug startup behavior, place your breakpoint(s) inside the `init` function.
    - To debug scoring behavior, place your breakpoint(s) inside the `run` function.

1. Select the VS Code Job view.
1. In the Run and Debug dropdown, select **Azure ML: Debug Local Endpoint** to start debugging your endpoint locally.

    In the **Breakpoints** section of the Run view, check that:

    - **Raised Exceptions** is **unchecked**
    - **Uncaught Exceptions** is **checked**

    :::image type="content" source="media/how-to-debug-managed-online-endpoints-visual-studio-code/configure-debug-profile.png" alt-text="Configure Azure ML Debug Local Environment debug profile":::

1. Select the play icon next to the Run and Debug dropdown to start your debugging session.

    At this point, any breakpoints in your `init` function are caught. Use the debug actions to step through your code. For more information on debug actions, see the [debug actions guide](https://code.visualstudio.com/Docs/editor/debugging#_debug-actions).

For more information on the VS Code debugger, see [Debugging in VS Code](https://code.visualstudio.com/Docs/editor/debugging)

## Debug your endpoint

# [Azure CLI](#tab/cli)

Now that your application is running in the debugger, try making a prediction to debug your scoring script.

Use the `ml` extension `invoke` command to make a request to your local endpoint.

```azurecli
az ml online-endpoint invoke --name <ENDPOINT-NAME> --request-file <REQUEST-FILE> --local
```

In this case, `<REQUEST-FILE>` is a JSON file that contains input data samples for the model to make predictions on similar to the following JSON:

```json
{"data": [
    [1,2,3,4,5,6,7,8,9,10], 
    [10,9,8,7,6,5,4,3,2,1]
]}
```

> [!TIP]
> The scoring URI is the address where your endpoint listens for requests. Use the `ml` extension to get the scoring URI.
>
>    ```azurecli
>    az ml online-endpoint show --name <ENDPOINT-NAME> --local
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
>The scoring URI can be found in the `scoring_uri` property.

At this point, any breakpoints in your `run` function are caught. Use the debug actions to step through your code. For more information on debug actions, see the [debug actions guide](https://code.visualstudio.com/Docs/editor/debugging#_debug-actions).
