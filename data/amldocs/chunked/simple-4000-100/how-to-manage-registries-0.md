
# Manage Azure Machine Learning registries (preview)

Azure Machine Learning entities can be grouped into two broad categories:

* Assets such as __models__, __environments__, __components__, and __datasets__ are durable entities that are _workspace agnostic_. For example, a model can be registered with any workspace and deployed to any endpoint. 
* Resources such as __compute__, __job__, and __endpoints__ are _transient entities that are workspace specific_. For example, an online endpoint has a scoring URI that is unique to a specific instance in a specific workspace. Similarly, a job runs for a known duration and generates logs and metrics each time it's run. 

Assets lend themselves to being stored in a central repository and used in different workspaces, possibly in different regions. Resources are workspace specific. 

AzureML registries (preview) enable you to create and use those assets in different workspaces. Registries support multi-region replication for low latency access to assets, so you can use assets in workspaces located in different Azure regions. Creating a registry will provision Azure resources required to facilitate replication. First, Azure blob storage accounts in each supported region. Second, a single Azure Container Registry with replication enabled to each supported region. 

:::image type="content" source="./media/how-to-manage-registries/machine-learning-registry-block-diagram.png" alt-text="Diagram of the relationships between assets in workspace and registry.":::

## Prerequisites

[!INCLUDE [CLI v2 preres](../../includes/machine-learning-cli-prereqs.md)]

## Prepare to create registry

You need to decide the following information carefully before proceeding to create a registry:

### Choose a name

Consider the following factors before picking a name.
* Registries are meant to facilitate sharing of ML assets across teams within your organization across all workspaces. Choose a name that is reflective of the sharing scope. The name should help identify your group, division or organization. 
* Registry unique with your organization (Azure Active Directory tenant). It's recommended to prefix your team or organization name and avoid generic names. 
* Registry names can't be changed once created because they're used in IDs of models, environments and components that are referenced in code. 
  * Length can be 2-32 characters. 
  * Alphanumerics, underscore, hyphen are allowed. No other special characters. No spaces - registry names are part of model, environment, and component IDs that can be referenced in code.  
  * Name can contain underscore or hyphen but can't start with an underscore or hyphen. Needs to start with an alphanumeric. 

### Choose Azure regions 

Registries enable sharing of assets across workspaces. To do so, a registry replicates content across multiple Azure regions. You need to define the list of regions that a registry supports when creating the registry. Create a list of all regions in which you have workspaces today and plan to add in near future. This list is a good set of regions to start with. When creating a registry, you define a primary region and a set of additional regions. The primary region can't be changed after registry creation, but the additional regions can be updated at a later point.

### Check permissions

Make sure you're the "Owner" or "Contributor" of the subscription or resource group in which you plan to create the registry. If you don't have one of these built-in roles, review the section on permissions toward the end of this article. 


## Create a registry

# [Azure CLI](#tab/cli)

Create the YAML definition and name it `registry.yml`.

> [!NOTE]
> The primary location is listed twice in the YAML file. In the following example, `eastus` is listed first as the primary location (`location` item) and also in the `replication_locations` list. 

```YAML
name: DemoRegistry1
description: Basic registry with one primary region and to additional regions
tags:
  foo: bar
location: eastus
replication_locations:
  - location: eastus
  - location: eastus2
  - location: westus
```
