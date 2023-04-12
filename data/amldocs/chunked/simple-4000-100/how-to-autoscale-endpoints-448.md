
The rule is part of the `my-scale-settings` profile (`autoscale-name` matches the `name` of the profile). The value of its `condition` argument says the rule should trigger when "The average CPU consumption among the VM instances exceeds 70% for five minutes." When that condition is satisfied, two more VM instances are allocated. 

> [!NOTE]
> For more information on the CLI syntax, see [`az monitor autoscale`](/cli/azure/monitor/autoscale).


# [Python](#tab/python)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

Create the rule definition:

```python 
rule_scale_out = ScaleRule(
    metric_trigger = MetricTrigger(
        metric_name="CpuUtilizationPercentage",
        metric_resource_uri = deployment.id, 
        time_grain = datetime.timedelta(minutes = 1),
        statistic = "Average",
        operator = "GreaterThan", 
        time_aggregation = "Last",
        time_window = datetime.timedelta(minutes = 5), 
        threshold = 70
    ), 
    scale_action = ScaleAction(
        direction = "Increase", 
        type = "ChangeCount", 
        value = 2, 
        cooldown = datetime.timedelta(hours = 1)
    )
)
```
This rule is refers to the last 5 minute average of `CPUUtilizationpercentage` from the arguments `metric_name`, `time_window` and `time_aggregation`. When value of the metric is greater than the `threshold` of 70, two more VM instances are allocated. 

Update the `my-scale-settings` profile to include this rule: 

```python 
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
                rules = [
                    rule_scale_out
                ]
            )
        ]
    }
)
``` 

# [Studio](#tab/azure-studio)

In the __Rules__ section, select __Add a rule__. The __Scale rule__ page is displayed. Use the following information to populate the fields on this page:

* Set __Metric name__ to __CPU Utilization Percentage__.
* Set __Operator__ to __Greater than__ and set the __Metric threshold__ to __70__.
* Set __Duration (minutes)__ to 5. Leave the __Time grain statistic__ as __Average__.
* Set __Operation__ to __Increase count by__ and set __Instance count__ to __2__.

Finally, select the __Add__ button to create the rule.

:::image type="content" source="media/how-to-autoscale-endpoints/scale-out-rule.png" lightbox="media/how-to-autoscale-endpoints/scale-out-rule.png" alt-text="Screenshot showing scale out rule >70% CPU for 5 minutes.":::


## Create a rule to scale in using metrics

When load is light, a scaling in rule can reduce the number of VM instances. The following example will release a single node, down to a minimum of 2, if the CPU load is less than 30% for 5 minutes:

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
