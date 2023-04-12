
> [!NOTE]
> For more, see the [reference page for autoscale](/cli/azure/monitor/autoscale)


# [Python](#tab/python)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

Import modules:
```python
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient
from azure.mgmt.monitor.models import AutoscaleProfile, ScaleRule, MetricTrigger, ScaleAction, Recurrence, RecurrentSchedule
import random 
import datetime 
``` 

Define variables for the workspace, endpoint, and deployment:

```python
subscription_id = "<YOUR-SUBSCRIPTION-ID>"
resource_group = "<YOUR-RESOURCE-GROUP>"
workspace = "<YOUR-WORKSPACE>"

endpoint_name = "<YOUR-ENDPOINT-NAME>"
deployment_name = "blue"
``` 

Get Azure ML and Azure Monitor clients:

```python
credential = DefaultAzureCredential()
ml_client = MLClient(
    credential, subscription_id, resource_group, workspace
)

mon_client = MonitorManagementClient(
    credential, subscription_id
)
```

Get the endpoint and deployment objects: 

```python 
deployment = ml_client.online_deployments.get(
    deployment_name, endpoint_name
)

endpoint = ml_client.online_endpoints.get(
    endpoint_name
)
```

Create an autoscale profile: 

```python
# Set a unique name for autoscale settings for this deployment. The below will append a random number to make the name unique.
autoscale_settings_name = f"autoscale-{endpoint_name}-{deployment_name}-{random.randint(0,1000)}"

mon_client.autoscale_settings.create_or_update(
    resource_group, 
    autoscale_settings_name, 
    parameters = {
        "location" : endpoint.location,
        "target_resource_uri" : deployment.id,
        "profiles" : [
            AutoscaleProfile(
                name="my-scale-settings",
                capacity={
                    "minimum" : 2, 
                    "maximum" : 5,
                    "default" : 2
                },
                rules = []
            )
        ]
    }
)
```

# [Studio](#tab/azure-studio)

In [Azure Machine Learning studio](https://ml.azure.com), select your workspace and then select __Endpoints__ from the left side of the page. Once the endpoints are listed, select the one you want to configure.

:::image type="content" source="media/how-to-autoscale-endpoints/select-endpoint.png" alt-text="Screenshot of an endpoint deployment entry in the portal.":::

From the __Details__ tab for the endpoint, select __Configure auto scaling__.

:::image type="content" source="media/how-to-autoscale-endpoints/configure-auto-scaling.png" alt-text="Screenshot of the configure auto scaling link in endpoint details.":::

Under __Choose how to scale your resources__, select __Custom autoscale__ to begin the configuration. For the default scale condition, use the following values:

* Set __Scale mode__ to __Scale based on a metric__.
* Set __Minimum__ to __2__.
* Set __Maximum__ to __5__.
* Set __Default__ to __2__.

:::image type="content" source="media/how-to-autoscale-endpoints/choose-custom-autoscale.png" alt-text="Screenshot showing custom autoscale choice.":::


## Create a rule to scale out using metrics

A common scaling out rule is one that increases the number of VM instances when the average CPU load is high. The following example will allocate two more nodes (up to the maximum) if the CPU average a load of greater than 70% for five minutes::

# [Azure CLI](#tab/azure-cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

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
