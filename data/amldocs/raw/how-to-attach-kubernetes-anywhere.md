---
title: Introduction to Kubernetes compute target in AzureML
titleSuffix: Azure Machine Learning
description: Learn how Azure Machine Learning Kubernetes compute enable AzureML across different infrastructures in cloud and on-premises
services: machine-learning
ms.service: machine-learning
ms.subservice: mlops
ms.topic: conceptual
author: bozhong68
ms.author: bozhlin
ms.reviewer: ssalgado
ms.custom: devplatv2, ignite-fall-2021, event-tier1-build-2022, ignite-2022
ms.date: 08/31/2022
#Customer intent: As part of ML Professionals focusing on ML infratrasture setup using self-managed compute, I want to understand what Kubernetes compute target is and why do I need it.
---

# Introduction to Kubernetes compute target in AzureML

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

With AzureML CLI/Python SDK v2, AzureML introduced a new compute target - Kubernetes compute target. You can easily enable an existing **Azure Kubernetes Service** (AKS) cluster or **Azure Arc-enabled Kubernetes** (Arc Kubernetes) cluster to become a Kubernetes compute target in AzureML, and use it to train or deploy models. 

:::image type="content" source="./media/how-to-attach-kubernetes-to-workspace/machine-learning-anywhere-overview.png" alt-text="Diagram illustrating how Azure ML connects to Kubernetes." lightbox="./media/how-to-attach-kubernetes-to-workspace/machine-learning-anywhere-overview.png":::
 
In this article, you learn about:
> [!div class="checklist"]
> * How it works
> * Usage scenarios
> * Recommended best practices
> * KubernetesCompute and legacy AksCompute

## How it works

AzureML Kubernetes compute supports two kinds of Kubernetes cluster:
* **[AKS cluster](https://azure.microsoft.com/services/kubernetes-service/)** in Azure. With your self-managed AKS cluster in Azure, you can gain security and controls to meet compliance requirement and flexibility to manage teams' ML workload.
* **[Arc Kubernetes cluster](../azure-arc/kubernetes/overview.md)** outside of Azure. With Arc Kubernetes cluster, you can train or deploy models in any infrastructure on-premises, across multicloud, or the edge. 

With a simple cluster extension deployment on AKS or Arc Kubernetes cluster, Kubernetes cluster is seamlessly supported in AzureML to run training or inference workload. It's easy to enable and use an existing Kubernetes cluster for AzureML workload with the following simple steps:

1. Prepare an [Azure Kubernetes Service cluster](../aks/learn/quick-kubernetes-deploy-cli.md) or [Arc Kubernetes cluster](../azure-arc/kubernetes/quickstart-connect-cluster.md).
1. [Deploy the AzureML extension](how-to-deploy-kubernetes-extension.md).
1. [Attach Kubernetes cluster to your Azure ML workspace](how-to-attach-kubernetes-to-workspace.md).
1. Use the Kubernetes compute target from CLI v2, SDK v2, and the Studio UI.

**IT-operation team**. The IT-operation team is responsible for the first 3 steps above: prepare an AKS or Arc Kubernetes cluster, deploy Azure ML cluster extension, and attach Kubernetes cluster to Azure ML workspace. In addition to these essential compute setup steps, IT-operation team also uses familiar tools such as Azure CLI or kubectl to take care of the following tasks for the data-science team:

- Network and security configurations, such as outbound proxy server connection or Azure firewall configuration, inference router (azureml-fe) setup, SSL/TLS termination, and VNET configuration.
- Create and manage instance types for different ML workload scenarios and gain efficient compute resource utilization.
- Trouble shooting workload issues related to Kubernetes cluster.

**Data-science team**. Once the IT-operations team finishes compute setup and compute target(s) creation, the data-science team can discover a list of available compute targets and instance types in AzureML workspace. These compute resources can be used for training or inference workload. Data science specifies compute target name and instance type name using their preferred tools or APIs such as AzureML CLI v2, Python SDK v2, or Studio UI.

## Kubernetes usage scenarios

With Arc Kubernetes cluster, you can build, train, and deploy models in any infrastructure on-premises and across multicloud using Kubernetes. This opens some new use patterns previously not possible in cloud setting environment. The following table provides a summary of the new use patterns enabled by AzureML Kubernetes compute:

| Usage pattern | Location of data | Motivation | Infra setup & Azure ML implementation |
| ----- | ----- | ----- | ----- |
Train model in cloud, deploy model on-premises | Cloud | Make use of cloud compute. Either because of elastic compute needs or special hardware such as a GPU.<br/>Model must be deployed on-premises because of security, compliance, or latency requirements | 1. Azure managed compute in cloud.<br/>2. Customer managed Kubernetes on-premises.<br/>3. Fully automated MLOps in hybrid mode, including training and model deployment steps transitioning seamlessly from cloud to on-premises and vice versa.<br/>4. Repeatable, with all assets tracked properly. Model retrained when necessary, and model deployment updated automatically after retraining. |
| Train model on-premises, deploy model in cloud | On-premises | Data must remain on-premises due to data-residency requirements.<br/>Deploy model in the cloud for global service access or for compute elasticity for scale and throughput. | 1. Azure managed compute in cloud.<br/>2. Customer managed Kubernetes on-premises.<br/>3. Fully automated MLOps in hybrid mode, including training and model deployment steps transitioning seamlessly from cloud to on-premises and vice versa.<br/>4. Repeatable, with all assets tracked properly. Model retrained when necessary, and model deployment updated automatically after retraining. |
| Bring your own AKS in Azure | Cloud | More security and controls.<br/>All private IP machine learning to prevent data exfiltration. | 1. AKS cluster behind an Azure VNet.<br/>2. Create private endpoints in the same VNet for AzureML workspace and its associated resources.<br/>3. Fully automated MLOps. |
| Full ML lifecycle on-premises | On-premises | Secure sensitive data or proprietary IP, such as ML models and code/scripts. | 1. Outbound proxy server connection on-premises.<br/>2. Azure ExpressRoute and Azure Arc private link to Azure resources.<br/>3. Customer managed Kubernetes on-premises.<br/>4. Fully automated MLOps. |

## Recommended best practices

**Separation of responsibilities between the IT-operations team and data-science team**. As we mentioned above, managing your own compute and infrastructure for ML workload is a complicated task, and it's best to be done by IT-operations team so data-science team can focus on ML models for organizational efficiency.

**Create and manage instance types for different ML workload scenarios**. Each ML workload uses different amounts of compute resources such as CPU/GPU and memory. AzureML implements instance type as Kubernetes custom resource definition (CRD) with properties of nodeSelector and resource request/limit. With a carefully curated list of instance types, IT-operations can target ML workload on specific node(s) and manage compute resource utilization efficiently.

**Multiple AzureML workspaces share the same Kubernetes cluster**. You can attach Kubernetes cluster multiple times to the same AzureML workspace or different AzureML workspaces, creating multiple compute targets in one workspace or multiple workspaces. Since many customers organize data science projects around AzureML workspace, multiple data science projects can now share the same Kubernetes cluster. This significantly reduces ML infrastructure management overheads and IT cost saving.

**Team/project workload isolation using Kubernetes namespace**. When you attach Kubernetes cluster to AzureML workspace, you can specify a Kubernetes namespace for the compute target. All workloads run by the compute target will be placed under the specified namespace.

## KubernetesCompute and legacy AksCompute

With AzureML CLI/Python SDK v1, you can deploy models on AKS using AksCompute target. Both KubernetesCompute target and AksCompute target support AKS integration, however they support it differently. The following table shows their key differences:

|Capabilities  |AKS integration with AksCompute (legacy)  |AKS integration with KubernetesCompute|
|--|--|--|
|CLI/SDK v1 | Yes | No|
|CLI/SDK v2 | No | Yes|
|Training | No | Yes|
|Real-time inference | Yes | Yes |
|Batch inference | No | Yes |
|Real-time inference new features | No new features development | Active roadmap |

With these key differences and overall AzureML evolution to use SDK/CLI v2, AzureML recommends you to use Kubernetes compute target to deploy models if you decide to use AKS for model deployment.

## Next steps

- [Step 1: Deploy AzureML extension](how-to-deploy-kubernetes-extension.md)
- [Step 2: Attach Kubernetes cluster to workspace](how-to-attach-kubernetes-to-workspace.md)
- [Create and manage instance types](how-to-manage-kubernetes-instance-types.md)

### Other resources

- [Kubernetes version and region availability](./reference-kubernetes.md#supported-kubernetes-version-and-region)
- [Work with custom data storage](./reference-kubernetes.md#azureml-jobs-connect-with-custom-data-storage)


### Examples

All AzureML examples can be found in [https://github.com/Azure/azureml-examples.git](https://github.com/Azure/azureml-examples).

For any AzureML example, you only need to update the compute target name to your Kubernetes compute target, then you're all done. 
* Explore training job samples with CLI v2 - [https://github.com/Azure/azureml-examples/tree/main/cli/jobs](https://github.com/Azure/azureml-examples/tree/main/cli/jobs)
* Explore model deployment with online endpoint samples with CLI v2 - [https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online/kubernetes](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online/kubernetes)
* Explore batch endpoint samples with CLI v2 - [https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/batch](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/batch)
* Explore training job samples with SDK v2 -[https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs)
* Explore model deployment with online endpoint samples with SDK v2 -[https://github.com/Azure/azureml-examples/tree/main/sdk/python/endpoints/online/kubernetes](https://github.com/Azure/azureml-examples/tree/main/sdk/python/endpoints/online/kubernetes)
