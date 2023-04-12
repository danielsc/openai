
# Upgrade to v2

Azure Machine Learning's v2 REST APIs, Azure CLI extension, and Python SDK introduce consistency and a set of new features to accelerate the production machine learning lifecycle. This article provides an overview of upgrading to v2 with recommendations to help you decide on v1, v2, or both.

## Prerequisites

- General familiarity with Azure ML and the v1 Python SDK.
- Understand [what is v2?](concept-v2.md)

## Should I use v2?

You should use v2 if you're starting a new machine learning project or workflow. You should use v2 if you want to use the new features offered in v2. The features include:
* Managed Inferencing
* Reusable components in pipelines
* Improved scheduling of pipelines
* Responsible AI dashboard
* Registry of assets

A new v2 project can reuse existing resources like workspaces and compute and existing assets like models and environments created using v1. 

Some feature gaps in v2 include:

- Spark support in jobs - this is currently in preview in v2.
- Publishing jobs (pipelines in v1) as endpoints. You can however, schedule pipelines without publishing.
- Support for SQL/database datastores.
- Ability to use classic prebuilt components in the designer with v2.

You should then ensure the features you need in v2 meet your organization's requirements, such as being generally available. 

> [!IMPORTANT]
> New features in Azure ML will only be launched in v2.

## Should I upgrade existing code to v2

You can reuse your existing assets in your v2 workflows. For instance a model created in v1 can be used to perform Managed Inferencing in v2.

Optionally, if you want to upgrade specific parts of your existing code to v2, please refer to the comparison links provided in the details of each resource or asset in the rest of this document.

## Which v2 API should I use?

In v2 interfaces via REST API, CLI, and Python SDK are available. The interface you should use depends on your scenario and preferences.

|API|Notes|
|-|-|
|REST|Fewest dependencies and overhead. Use for building applications on Azure ML as a platform, directly in programming languages without an SDK provided, or per personal preference.|
|CLI|Recommended for automation with CI/CD or per personal preference. Allows quick iteration with YAML files and straightforward separation between Azure ML and ML model code.|
|Python SDK|Recommended for complicated scripting (for example, programmatically generating large pipeline jobs) or per personal preference. Allows quick iteration with YAML files or development solely in Python.|

## Can I use v1 and v2 together?

v1 and v2 can co-exist in a workspace. You can reuse your existing assets in your v2 workflows. For instance a model created in v1 can be used to perform Managed Inferencing in v2. Resources like workspace, compute, and datastore work across v1 and v2, with exceptions. A user can call the v1 Python SDK to change a workspace's description, then using the v2 CLI extension change it again. Jobs (experiments/runs/pipelines in v1) can be submitted to the same workspace from the v1 or v2 Python SDK. A workspace can have both v1 and v2 model deployment endpoints. 

### Using v1 and v2 code together
We do not recommend using the v1 and v2 SDKs together in the same code. It is technically possible to use v1 and v2 in the same code because they use different Azure namespaces. However, there are many classes with the same name across these namespaces (like Workspace, Model) which can cause confusion and make code readability and debuggability challenging. 

> [!IMPORTANT]
> If your workspace uses a private endpoint, it will automatically have the `v1_legacy_mode` flag enabled, preventing usage of v2 APIs. See [how to configure network isolation with v2](how-to-configure-network-isolation-with-v2.md) for details.

## Resources and assets in v1 and v2

This section gives an overview of specific resources and assets in Azure ML. See the concept article for each entity for details on their usage in v2.
