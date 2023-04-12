
# Audit and manage Azure Machine Learning

When teams collaborate on Azure Machine Learning, they may face varying requirements to the configuration and organization of resources. Machine learning teams may look for flexibility in how to organize workspaces for collaboration, or size compute clusters to the requirements of their use cases. In these scenarios, it may lead to most productivity if the application team can manage their own infrastructure.

As a platform administrator, you can use policies to lay out guardrails for teams to manage their own resources. [Azure Policy](../governance/policy/index.yml) helps audit and govern resource state. In this article, you learn about available auditing controls and governance practices for Azure Machine Learning.

## Policies for Azure Machine Learning

[Azure Policy](../governance/policy/index.yml) is a governance tool that allows you to ensure that Azure resources are compliant with your policies.

Azure Machine Learning provides a set of policies that you can use for common scenarios with Azure Machine Learning. You can assign these policy definitions to your existing subscription or use them as the basis to create your own custom definitions.

The table below includes a selection of policies you can assign with Azure Machine Learning. For a complete list of the built-in policies for Azure Machine Learning, see [Built-in policies for Azure Machine Learning](../governance/policy/samples/built-in-policies.md#machine-learning).

| Policy | Description |
| ----- | ----- |
| **Customer-managed key** | Audit or enforce whether workspaces must use a customer-managed key. |
| **Private link** | Audit or enforce whether workspaces use a private endpoint to communicate with a virtual network. |
| **Private endpoint** | Configure the Azure Virtual Network subnet where the private endpoint should be created. |
| **Private DNS zone** | Configure the private DNS zone to use for the private link. |
| **User-assigned managed identity** | Audit or enforce whether workspaces use a user-assigned managed identity. |
| **Disable public network access** | Audit or enforce whether workspaces disable access from the public internet. |
| **Disable local authentication** | Audit or enforce whether Azure Machine Learning compute resources should have local authentication methods disabled. |
| **Modify/disable local authentication** | Configure compute resources to disable local authentication methods. |
| **Compute cluster and instance is behind virtual network** | Audit whether compute resources are behind a virtual network. |

Policies can be set at different scopes, such as at the subscription or resource group level. For more information, see the [Azure Policy documentation](../governance/policy/overview.md).

## Assigning built-in policies

To view the built-in policy definitions related to Azure Machine Learning, use the following steps:

1. Go to __Azure Policy__ in the [Azure portal](https://portal.azure.com).
1. Select __Definitions__.
1. For __Type__, select _Built-in_, and for __Category__, select __Machine Learning__.

From here, you can select policy definitions to view them. While viewing a definition, you can use the __Assign__ link to assign the policy to a specific scope, and configure the parameters for the policy. For more information, see [Assign a policy - portal](../governance/policy/assign-policy-portal.md).

You can also assign policies by using [Azure PowerShell](../governance/policy/assign-policy-powershell.md), [Azure CLI](../governance/policy/assign-policy-azurecli.md), and [templates](../governance/policy/assign-policy-template.md).

## Conditional access policies

> [!IMPORTANT]
> [Azure AD Conditional Access](/azure/active-directory/conditional-access/overview) is __not__ supported with Azure Machine Learning.

## Enable self-service using landing zones

Landing zones are an architectural pattern to set up Azure environments that accounts for scale, governance, security, and productivity. A data landing zone is an administator-configured environment that an application team uses to host a data and analytics workload.
