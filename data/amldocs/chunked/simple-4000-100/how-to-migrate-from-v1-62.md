This section gives an overview of specific resources and assets in Azure ML. See the concept article for each entity for details on their usage in v2.

### Workspace

Workspaces don't need to be upgraded with v2. You can use the same workspace, regardless of whether you're using v1 or v2. 

If you create workspaces using automation, do consider upgrading the code for creating a workspace to v2. Typically Azure resources are managed via Azure Resource Manager (and Bicep) or similar resource provisioning tools. Alternatively, you can use the [CLI (v2) and YAML files](how-to-manage-workspace-cli.md#create-a-workspace).

For a comparison of SDK v1 and v2 code, see [Workspace management in SDK v1 and SDK v2](migrate-to-v2-resource-workspace.md).

> [!IMPORTANT]
> If your workspace uses a private endpoint, it will automatically have the `v1_legacy_mode` flag enabled, preventing usage of v2 APIs. See [how to configure network isolation with v2](how-to-configure-network-isolation-with-v2.md) for details.

### Connection (workspace connection in v1)

Workspace connections from v1 are persisted on the workspace, and fully available with v2.

For a comparison of SDK v1 and v2 code, see [Workspace management in SDK v1 and SDK v2](migrate-to-v2-resource-workspace.md).


### Datastore

Object storage datastore types created with v1 are fully available for use in v2. Database datastores are not supported; export to object storage (usually Azure Blob) is the recommended migration path.

For a comparison of SDK v1 and v2 code, see [Datastore management in SDK v1 and SDK v2](migrate-to-v2-resource-datastore.md).

### Compute

Compute of type `AmlCompute` and `ComputeInstance` are fully available for use in v2.

For a comparison of SDK v1 and v2 code, see [Compute management in SDK v1 and SDK v2](migrate-to-v2-resource-compute.md).

### Endpoint and deployment (endpoint and web service in v1)

With SDK/CLI v1, you can deploy models on ACI or AKS as web services. Your existing v1 model deployments and web services will continue to function as they are, but Using SDK/CLI v1 to deploy models on ACI or AKS as web services is now consiered as **legacy**. For new model deployments, we recommend upgrading to v2. In v2, we offer [managed endpoints or Kubernetes endpoints](./concept-endpoints.md). The following table guides our recommendation:

|Endpoint type in v2|Upgrade from|Notes|
|-|-|-|
|Local|ACI|Quick test of model deployment locally; not for production.|
|Managed online endpoint|ACI, AKS|Enterprise-grade managed model deployment infrastructure with near real-time responses and massive scaling for production.|
|Managed batch endpoint|ParallelRunStep in a pipeline for batch scoring|Enterprise-grade managed model deployment infrastructure with massively parallel batch processing for production.|
|Azure Kubernetes Service (AKS)|ACI, AKS|Manage your own AKS cluster(s) for model deployment, giving flexibility and granular control at the cost of IT overhead.|
|Azure Arc Kubernetes|N/A|Manage your own Kubernetes cluster(s) in other clouds or on-premises, giving flexibility and granular control at the cost of IT overhead.|

For a comparison of SDK v1 and v2 code, see [Upgrade deployment endpoints to SDK v2](migrate-to-v2-deploy-endpoints.md).
For migration steps from your existing ACI web services to managed online endpoints, see our [upgrade guide article](migrate-to-v2-managed-online-endpoints.md) and [blog](https://aka.ms/acimoemigration).

### Jobs (experiments, runs, pipelines in v1)

In v2, "experiments", "runs", and "pipelines" are consolidated into jobs. A job has a type. Most jobs are `command` jobs that run a command, like `python main.py`. What runs in a job is agnostic to any programming language, so you can run `bash` scripts, invoke `python` interpreters, run a bunch of `curl` commands, or anything else. Another common type of job is `pipeline`, which defines child jobs that may have input/output relationships, forming a directed acyclic graph (DAG).
