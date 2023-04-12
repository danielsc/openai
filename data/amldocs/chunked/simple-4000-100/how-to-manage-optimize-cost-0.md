
[//]: # (needs PM review; ParallelJobStep or ParallelRunStep?)

# Manage and optimize Azure Machine Learning costs

Learn how to manage and optimize costs when training and deploying machine learning models to Azure Machine Learning.

Use the following tips to help you manage and optimize your compute resource costs.

- Configure your training clusters for autoscaling
- Set quotas on your subscription and workspaces
- Set termination policies on your training job
- Use low-priority virtual machines (VM)
- Schedule compute instances to shut down and start up automatically
- Use an Azure Reserved VM Instance
- Train locally
- Parallelize training
- Set data retention and deletion policies
- Deploy resources to the same region

For information on planning and monitoring costs, see the [plan to manage costs for Azure Machine Learning](concept-plan-manage-cost.md) guide.

## Use Azure Machine Learning compute cluster (AmlCompute)

With constantly changing data, you need fast and streamlined model training and retraining to maintain accurate models. However, continuous training comes at a cost, especially for deep learning models on GPUs. 

Azure Machine Learning users can use the managed Azure Machine Learning compute cluster, also called AmlCompute. AmlCompute supports a variety of GPU and CPU options. The AmlCompute is internally hosted on behalf of your subscription by Azure Machine Learning. It provides the same enterprise grade security, compliance and governance at Azure IaaS cloud scale.

Because these compute pools are inside of Azure's IaaS infrastructure, you can deploy, scale, and manage your training with the same security and compliance requirements as the rest of your infrastructure.  These deployments occur in your subscription and obey your governance rules. Learn more about [Azure Machine Learning compute](how-to-create-attach-compute-cluster.md).

## Configure training clusters for autoscaling

Autoscaling clusters based on the requirements of your workload helps reduce your costs so you only use what you need.

AmlCompute clusters are designed to scale dynamically based on your workload. The cluster can be scaled up to the maximum number of nodes you configure. As each job completes, the cluster will release nodes and scale to your configured minimum node count.

[!INCLUDE [min-nodes-note](../../includes/machine-learning-min-nodes.md)]

You can also configure the amount of time the node is idle before scale down. By default, idle time before scale down is set to 120 seconds.

+ If you perform less iterative experimentation, reduce this time to save costs.
+ If you perform highly iterative dev/test experimentation, you might need to increase the time so you aren't paying for constant scaling up and down after each change to your training script or environment.

AmlCompute clusters can be configured for your changing workload requirements in Azure portal, using the [AmlCompute SDK class](/python/api/azure-ai-ml/azure.ai.ml.entities.amlcompute), [AmlCompute CLI](/cli/azure/ml/compute#az-ml-compute-create), with the [REST APIs](https://github.com/Azure/azure-rest-api-specs/tree/master/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/stable).


## Set quotas on resources

AmlCompute comes with a [quota (or limit) configuration](how-to-manage-quotas.md#azure-machine-learning-compute). This quota is by VM family (for example, Dv2 series, NCv3 series) and varies by region for each subscription. Subscriptions start with small defaults to get you going, but use this setting to control the amount of Amlcompute resources available to be spun up in your subscription. 

Also configure [workspace level quota by VM family](how-to-manage-quotas.md#workspace-level-quotas), for each workspace within a subscription. Doing so allows you to have more granular control on the costs that each workspace might potentially incur and restrict certain VM families. 

To set quotas at the workspace level, start in the [Azure portal](https://portal.azure.com).  Select any workspace in your subscription, and select **Usages + quotas** in the left pane. Then select the **Configure quotas** tab to view the quotas. You need privileges at the subscription scope to set the quota, since it's a setting that affects multiple workspaces.
