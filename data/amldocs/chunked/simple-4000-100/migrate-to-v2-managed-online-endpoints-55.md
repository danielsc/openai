You can find our examples on [azureml-examples](https://github.com/Azure/azureml-examples). Specifically, this is the [SDK example for managed online endpoint](https://github.com/Azure/azureml-examples/tree/main/sdk/python/endpoints/online/managed).

### With our [upgrade tool](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online/managed/migration)
This tool will automatically create new managed online endpoint based on your existing web services. Your original services won't be affected. You can safely route the traffic to the new endpoint and then delete the old one.

> [!NOTE]
> The upgrade script is a sample script and is provided without a service level agreement (SLA).

Use the following steps to run the scripts:

> [!TIP]
> The new endpoint created by the scripts will be created under the same workspace.

1. Use a bash shell to run the scripts. For example, a terminal session on Linux or the Windows Subsystem for Linux (WSL).
2. Install [Python SDK V1](/python/api/overview/azure/ml/install) to run the Python script.
3. Install [Azure CLI](/cli/azure/install-azure-cli).
4. Clone [the repository](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online/managed/migration) to your local env. For example, `git clone https://github.com/Azure/azureml-examples`.
5. Edit the following values in the `migrate-service.sh` file. Replace the values with ones that apply to your configuration.

    * `<SUBSCRIPTION_ID>` - The subscription ID of your Azure subscription that contains your workspace.
    * `<RESOURCEGROUP_NAME>` - The resource group that contains your workspace.
    * `<WORKSPACE_NAME>` - The workspace name.
    * `<SERVICE_NAME>` - The name of your existing ACI service.
    * `<LOCAL_PATH>` - A local path where resources and templates used by the script are downloaded.
    * `<NEW_ENDPOINT_NAME>` - The name of the new endpoint that will be created. We recommend that the new endpoint name is different from the previous service name. Otherwise, the original service won't be displayed if you check your endpoints on the portal.
    * `<NEW_DEPLOYMENT_NAME>` - The name of the deployment to the new endpoint.
6. Run the bash script. For example, `./migrate-service.sh`. It will take about 5-10 minutes to finish the new deployment.

    > [!TIP]
    > If you receive an error that the script is not executable, or an editor opens when you try to run the script, use the following command to mark the script as executable:
    > ```bash
    > chmod +x migrate-service.sh
    > ```
7. After the deployment is completes successfully, you can verify the endpoint with the [az ml online-endpoint invoke](/cli/azure/ml/online-endpoint#az-ml-online-endpoint-invoke) command.

## Contact us
If you have any questions or feedback on the upgrade script, contact us at moeonboard@microsoft.com.

## Next steps

* [What are Azure Machine Learning endpoints?](concept-endpoints.md)
* [Deploy and score a model with an online endpoint](how-to-deploy-online-endpoints.md)
