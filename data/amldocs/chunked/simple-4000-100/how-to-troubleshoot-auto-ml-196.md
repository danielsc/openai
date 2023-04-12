If you are under virtual networks (VNets), you may run into model download failures when using AutoML NLP. This is because network traffic is blocked from downloading the models and tokenizers from Azure CDN. To unblock this, please allow list the below URLs in the “Application rules” setting of the VNet firewall policy:

* aka.ms 
* https://automlresources-prod.azureedge.net 

Please follow the instructions [here to configure the firewall settings.](how-to-access-azureml-behind-firewall.md)

Instructions for configuring workspace under vnet are available [here.](tutorial-create-secure-workspace.md)

## Next steps

+ Learn more about [how to train a regression model with Automated machine learning](./v1/how-to-auto-train-models-v1.md) or [how to train using Automated machine learning on a remote resource](./v1/concept-automated-ml-v1.md#local-remote).

+ Learn more about [how and where to deploy a model](./v1/how-to-deploy-and-where.md).
