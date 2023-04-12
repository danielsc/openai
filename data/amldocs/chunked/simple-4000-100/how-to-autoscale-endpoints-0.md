# Autoscale an online endpoint

Autoscale automatically runs the right amount of resources to handle the load on your application. [Online endpoints](concept-endpoints.md) supports autoscaling through integration with the Azure Monitor autoscale feature.

Azure Monitor autoscaling supports a rich set of rules. You can configure metrics-based scaling (for instance, CPU utilization >70%), schedule-based scaling (for example, scaling rules for peak business hours), or a combination. For more information, see [Overview of autoscale in Microsoft Azure](../azure-monitor/autoscale/autoscale-overview.md).

:::image type="content" source="media/how-to-autoscale-endpoints/concept-autoscale.png" alt-text="Diagram for autoscale adding/removing instance as needed":::

Today, you can manage autoscaling using either the Azure CLI, REST, ARM, or the browser-based Azure portal. Other Azure ML SDKs, such as the Python SDK, will add support over time.

## Prerequisites

* A deployed endpoint. [Deploy and score a machine learning model by using an online endpoint](how-to-deploy-online-endpoints.md). 
* To use autoscale, the role `microsoft.insights/autoscalesettings/write` must be assigned to the identity that manages autoscale. You can use any built-in or custom roles that allow this action. For general guidance on managing roles for Azure Machine Learning, see [Manage users and roles](/azure/machine-learning/how-to-assign-roles). For more on autoscale settings from Azure Monitor, see [Microsoft.Insights autoscalesettings](/azure/templates/microsoft.insights/autoscalesettings).

## Define an autoscale profile

To enable autoscale for an endpoint, you first define an autoscale profile. This profile defines the default, minimum, and maximum scale set capacity. The following example sets the default and minimum capacity as two VM instances, and the maximum capacity as five:

# [Azure CLI](#tab/azure-cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The following snippet sets the endpoint and deployment names:

```azurecli
# Note: this is based on the deploy-managed-online-endpoint.sh: it just adds autoscale settings in the end
set -e

#set the endpoint name from the how-to-deploy excercise
# <set_endpoint_deployment_name>
# set your existing endpoint name
ENDPOINT_NAME=your-endpoint-name
DEPLOYMENT_NAME=blue
# </set_endpoint_deployment_name>

export ENDPOINT_NAME=autoscale-endpt-`echo $RANDOM`

# create endpoint and deployment
az ml online-endpoint create --name $ENDPOINT_NAME -f endpoints/online/managed/sample/endpoint.yml
az ml online-deployment create --name blue --endpoint $ENDPOINT_NAME -f endpoints/online/managed/sample/blue-deployment.yml --all-traffic
az ml online-endpoint show -n $ENDPOINT_NAME

# <set_other_env_variables>
# ARM id of the deployment
DEPLOYMENT_RESOURCE_ID=$(az ml online-deployment show -e $ENDPOINT_NAME -n $DEPLOYMENT_NAME -o tsv --query "id")
# ARM id of the deployment. todo: change to --query "id"
ENDPOINT_RESOURCE_ID=$(az ml online-endpoint show -n $ENDPOINT_NAME -o tsv --query "properties.\"azureml.onlineendpointid\"")
# set a unique name for autoscale settings for this deployment. The below will append a random number to make the name unique.
AUTOSCALE_SETTINGS_NAME=autoscale-$ENDPOINT_NAME-$DEPLOYMENT_NAME-`echo $RANDOM`
# </set_other_env_variables>

# create autoscale settings. Note if you followed the how-to-deploy doc example, the instance count would have been 1. Now after applying this poilcy, it will scale up 2 (since min count and count are 2).
# <create_autoscale_profile>
az monitor autoscale create \
  --name $AUTOSCALE_SETTINGS_NAME \
  --resource $DEPLOYMENT_RESOURCE_ID \
  --min-count 2 --max-count 5 --count 2
# </create_autoscale_profile>

# Add rule to default profile: scale up if cpu util > 70 %
# <scale_out_on_cpu_util>
az monitor autoscale rule create \
  --autoscale-name $AUTOSCALE_SETTINGS_NAME \
  --condition "CpuUtilizationPercentage > 70 avg 5m" \
  --scale out 2
# </scale_out_on_cpu_util>

# Add rule to default profile: scale down if cpu util < 25 %
# <scale_in_on_cpu_util>
az monitor autoscale rule create \
  --autoscale-name $AUTOSCALE_SETTINGS_NAME \
  --condition "CpuUtilizationPercentage < 25 avg 5m" \
  --scale in 1
# </scale_in_on_cpu_util>

# add rule to default profile: scale up based on avg. request latency (endpoint metric)
# <scale_up_on_request_latency>
az monitor autoscale rule create \
 --autoscale-name $AUTOSCALE_SETTINGS_NAME \
 --condition "RequestLatency > 70 avg 5m" \
 --scale out 1 \
 --resource $ENDPOINT_RESOURCE_ID
# </scale_up_on_request_latency>

#create weekend profile: scale to 2 nodes in weekend
# <weekend_profile>
az monitor autoscale profile create \
  --name weekend-profile \
  --autoscale-name $AUTOSCALE_SETTINGS_NAME \
  --min-count 2 --count 2 --max-count 2 \
  --recurrence week sat sun --timezone "Pacific Standard Time" 
# </weekend_profile>

# <delete_endpoint>
# delete the autoscaling profile
az monitor autoscale delete -n "$AUTOSCALE_SETTINGS_NAME"

# delete the endpoint
az ml online-endpoint delete --name $ENDPOINT_NAME --yes --no-wait
# </delete_endpoint>
```
