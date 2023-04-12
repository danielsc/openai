Azure Machine Learning has several inbound and outbound network dependencies. Some of these dependencies can expose a data exfiltration risk by malicious agents within your organization. These risks are associated with the outbound requirements to Azure Storage, Azure Front Door, and Azure Monitor. For recommendations on mitigating this risk, see the [Azure Machine Learning data exfiltration prevention](how-to-prevent-data-loss-exfiltration.md) article.

## Vulnerability scanning

[Microsoft Defender for Cloud](../security-center/security-center-introduction.md) provides unified security management and advanced threat protection across hybrid cloud workloads. For Azure machine learning, you should enable scanning of your [Azure Container Registry](../container-registry/container-registry-intro.md) resource and Azure Kubernetes Service resources. For more information, see [Azure Container Registry image scanning by Defender for Cloud](../security-center/defender-for-container-registries-introduction.md) and [Azure Kubernetes Services integration with Defender for Cloud](../security-center/defender-for-kubernetes-introduction.md).

## Audit and manage compliance

[Azure Policy](../governance/policy/index.yml) is a governance tool that allows you to ensure that Azure resources are compliant with your policies. You can set policies to allow or enforce specific configurations, such as whether your Azure Machine Learning workspace uses a private endpoint. For more information on Azure Policy, see the [Azure Policy documentation](../governance/policy/overview.md). For more information on the policies specific to Azure Machine Learning, see [Audit and manage compliance with Azure Policy](how-to-integrate-azure-policy.md).

## Next steps

* [Azure Machine Learning best practices for enterprise security](/azure/cloud-adoption-framework/ready/azure-best-practices/ai-machine-learning-enterprise-security)
* [Use Azure Machine Learning with Azure Firewall](how-to-access-azureml-behind-firewall.md)
* [Use Azure Machine Learning with Azure Virtual Network](how-to-network-security-overview.md)
* [Data encryption at rest and in transit](concept-data-encryption.md)
* [Build a real-time recommendation API on Azure](/azure/architecture/reference-architectures/ai/real-time-recommendation)