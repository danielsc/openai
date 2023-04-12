
# [Python](#tab/python)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python 
mon_client.autoscale_settings.create_or_update(
    resource_group, 
    autoscale_settings_name, 
    parameters = {
        "location" : endpoint.location,
        "target_resource_uri" : deployment.id,
        "profiles" : [
            AutoscaleProfile(
                name="Default",
                capacity={
                    "minimum" : 2, 
                    "maximum" : 2,
                    "default" : 2
                },
                recurrence = Recurrence(
                    frequency = "Week", 
                    schedule = RecurrentSchedule(
                        time_zone = "Pacific Standard Time", 
                        days = ["Saturday", "Sunday"], 
                        hours = [], 
                        minutes = []
                    )
                )
            )
        ]
    }
)
``` 

# [Studio](#tab/azure-studio)

From the bottom of the page, select __+ Add a scale condition__. On the new scale condition, use the following information to populate the fields:
 
* Select __Scale to a specific instance count__.
* Set the __Instance count__ to __2__.
* Set the __Schedule__ to __Repeat specific days__.
* Set the schedule to __Repeat every__ __Saturday__ and __Sunday__.

:::image type="content" source="media/how-to-autoscale-endpoints/schedule-rules.png" lightbox="media/how-to-autoscale-endpoints/schedule-rules.png" alt-text="Screenshot showing schedule-based rules.":::


## Delete resources

If you are not going to use your deployments, delete them:

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
