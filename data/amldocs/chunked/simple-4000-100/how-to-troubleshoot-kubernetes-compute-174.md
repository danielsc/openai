   > More troubleshoot guide of common errors when creating/updating the Kubernetes online endpoints and deployments, you can find in [How to troubleshoot online endpoints](how-to-troubleshoot-online-endpoints.md).


## Training guide

### UserError

#### AzureML Kubernetes job failed. E45004

If the error message is:

```bash
AzureML Kubernetes job failed. E45004:"Training feature is not enabled, please enable it when install the extension."
```

Please check whether you have `enableTraining=True` set when doing the AzureML extension installation. More details could be found at [Deploy AzureML extension on AKS or Arc Kubernetes cluster](how-to-deploy-kubernetes-extension.md)

#### Unable to mount data store workspaceblobstore. Give either an account key or SAS token

If you need to access Azure Container Registry (ACR) for Docker image, and Storage Account for training data, this issue should occur when the compute is not specified with a managed identity. This is because machine learning workspace default storage account without any credentials is not supported for training jobs. 

To mitigate this issue, you can assign Managed Identity to the compute in compute attach step, or you can assign Managed Identity to the compute after it has been attached. More details could be found at [Assign Managed Identity to the compute target](how-to-attach-kubernetes-to-workspace.md#assign-managed-identity-to-the-compute-target).

#### Unable to upload project files to working directory in AzureBlob because the authorization failed

If the error message is:

```bash
Unable to upload project files to working directory in AzureBlob because the authorization failed. 
```

You can check the following items to troubleshoot the issue:
*  Make sure the storage account has enabled the exceptions of “Allow Azure services on the trusted service list to access this storage account” and the workspace is in the resource instances list. 
*  Make sure the workspace has a system assigned managed identity.

### Encountered an error when attempting to connect to the Azure ML token service

If the error message is:

```bash
AzureML Kubernetes job failed. 400:{"Msg":"Encountered an error when attempting to connect to the Azure ML token service","Code":400}
```
You can follow [Private Link troubleshooting section](#private-link-issue) to check your network settings.

### ServiceError

#### Job pod get stuck in Init state

If the job runs longer than you expected and if you find that your job pods are getting stuck in an Init state with this warning `Unable to attach or mount volumes: *** failed to get plugin from volumeSpec for volume ***-blobfuse-*** err=no volume plugin matched`,  the issue might be occurring because AzureML extension doesn't support download mode for input data. 

To resolve this issue, change to mount mode for your input data.

#### AzureML Kubernetes job failed

If the error message is:

```bash
AzureML Kubernetes job failed. 137:PodPattern matched: {"containers":[{"name":"training-identity-sidecar","message":"Updating certificates in /etc/ssl/certs...\n1 added, 0 removed; done.\nRunning hooks in /etc/ca-certificates/update.d...\ndone.\n * Serving Flask app 'msi-endpoint-server' (lazy loading)\n * Environment: production\n   WARNING: This is a development server. Do not use it in a production deployment.\n   Use a production WSGI server instead.\n * Debug mode: off\n * Running on http://127.0.0.1:12342/ (Press CTRL+C to quit)\n","code":137}]}
```

Check your proxy setting and check whether 127.0.0.1 was added to proxy-skip-range when using `az connectedk8s connect` by following this [network configuring](how-to-access-azureml-behind-firewall.md#scenario-use-kubernetes-compute).

## Private link issue

We could use the method below to check private link setup by logging into one pod in the Kubernetes cluster and then check related network settings.

*  Find workspace ID in Azure portal or get this ID by running `az ml workspace show` in the command line.
