The hosts in this section are used to install Visual Studio Code packages to establish a remote connection between Visual Studio Code and compute instances in your Azure Machine Learning workspace.

> [!NOTE]
> This is not a complete list of the hosts required for all Visual Studio Code resources on the internet, only the most commonly used. For example, if you need access to a GitHub repository or other host, you must identify and add the required hosts for that scenario.

| __Host name__ | __Purpose__ |
| ---- | ---- |
| `*.vscode.dev`<br>`*.vscode-unpkg.net`<br>`*.vscode-cdn.net`<br>`*.vscodeexperiments.azureedge.net`<br>`default.exp-tas.com` | Required to access vscode.dev (Visual Studio Code for the Web) |
| `code.visualstudio.com` | Required to download and install VS Code desktop. This host isn't required for VS Code Web. |
| `update.code.visualstudio.com`<br>`*.vo.msecnd.net` | Used to retrieve VS Code server bits that are installed on the compute instance through a setup script. |
| `marketplace.visualstudio.com`<br>`vscode.blob.core.windows.net`<br>`*.gallerycdn.vsassets.io` | Required to download and install VS Code extensions. These hosts enable the remote connection to compute instances using the Azure ML extension for VS Code. For more information, see [Connect to an Azure Machine Learning compute instance in Visual Studio Code](./how-to-set-up-vs-code-remote.md) |
| `raw.githubusercontent.com/microsoft/vscode-tools-for-ai/master/azureml_remote_websocket_server/*` | Used to retrieve websocket server bits that are installed on the compute instance. The websocket server is used to transmit requests from Visual Studio Code client (desktop application) to Visual Studio Code server running on the compute instance. |

## Scenario: Third party firewall

The guidance in this section is generic, as each firewall has its own terminology and specific configurations. If you have questions, check the documentation for the firewall you're using.

If not configured correctly, the firewall can cause problems using your workspace. There are various host names that are used both by the Azure Machine Learning workspace. The following sections list hosts that are required for Azure Machine Learning.

### Dependencies API

You can also use the Azure Machine Learning REST API to get a list of hosts and ports that you must allow __outbound__ traffic to. To use this API, use the following steps:

1. Get an authentication token. The following command demonstrates using the [Azure CLI](/cli/azure/install-azure-cli) to get an authentication token and subscription ID:

    ```azurecli-interactive
    TOKEN=$(az account get-access-token --query accessToken -o tsv)
    SUBSCRIPTION=$(az account show --query id -o tsv)
    ```

2. Call the API. In the following command, replace the following values:
    * Replace `<region>` with the Azure region your workspace is in. For example, `westus2`.
    * Replace `<resource-group>` with the resource group that contains your workspace.
    * Replace `<workspace-name>` with the name of your workspace.

    ```azurecli-interactive
    az rest --method GET \
        --url "https://<region>.api.azureml.ms/rp/workspaces/subscriptions/$SUBSCRIPTION/resourceGroups/<resource-group>/providers/Microsoft.MachineLearningServices/workspaces/<workspace-name>/outboundNetworkDependenciesEndpoints?api-version=2018-03-01-preview" \
        --header Authorization="Bearer $TOKEN"
    ```

The result of the API call is a JSON document. The following snippet is an excerpt of this document:

```json
{
  "value": [
    {
      "properties": {
        "category": "Azure Active Directory",
        "endpoints": [
          {
            "domainName": "login.microsoftonline.com",
            "endpointDetails": [
              {
                "port": 80
              },
              {
                "port": 443
              }
            ]
          }
        ]
      }
    },
    {
      "properties": {
        "category": "Azure portal",
        "endpoints": [
          {
            "domainName": "management.azure.com",
            "endpointDetails": [
              {
                "port": 443
              }
            ]
          }
        ]
      }
    },
...
```
