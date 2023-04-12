| `<account>.blob.core.windows.net` | Azure Storage Account (blob storage) |
| `api.azureml.ms` | Azure Active Directory (Azure AD) authentication |
| `ingest-vienna<region>.kusto.windows.net` | Kusto endpoint for uploading telemetry |

### Connectivity requirements in chronological order: from cluster creation to model deployment

Right after azureml-fe is deployed, it will attempt to start and this requires to:
* Resolve DNS for AKS API server
* Query AKS API server to discover other instances of itself (it's a multi-pod service)
* Connect to other instances of itself

Once azureml-fe is started, it requires the following connectivity to function properly:
* Connect to Azure Storage to download dynamic configuration
* Resolve DNS for Azure AD authentication server api.azureml.ms and communicate with it when the deployed service uses Azure AD authentication.
* Query AKS API server to discover deployed models
* Communicate to deployed model PODs

At model deployment time, for a successful model deployment AKS node should be able to: 
* Resolve DNS for customer's ACR
* Download images from customer's ACR
* Resolve DNS for Azure BLOBs where model is stored
* Download models from Azure BLOBs

After the model is deployed and service starts, azureml-fe will automatically discover it using AKS API, and will be ready to route request to it. It must be able to communicate to model PODs.
>[!Note]
>If the deployed model requires any connectivity (e.g. querying external database or other REST service, downloading a BLOB etc), then both DNS resolution and outbound communication for these services should be enabled.

## Next steps

- [Create and manage instance types](./how-to-manage-kubernetes-instance-types.md)
- [Secure AKS inferencing environment](./how-to-secure-kubernetes-inferencing-environment.md)

