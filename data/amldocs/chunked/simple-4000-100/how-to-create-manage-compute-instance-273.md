Administrators can use a built-in [Azure Policy](./../governance/policy/overview.md) definition to enforce auto-stop on all compute instances in a given subscription/resource-group. 

1. Navigate to Azure Policy in the Azure portal.
2. Under "Definitions", look for the idle shutdown policy.

      :::image type="content" source="media/how-to-create-attach-studio/idle-shutdown-policy.png" alt-text="Screenshot for the idle shutdown policy in Azure portal." lightbox="media/how-to-create-attach-studio/idle-shutdown-policy.png":::

3. Assign policy to the necessary scope.

You can also create your own custom Azure policy. For example, if the below policy is assigned, all new compute instances will have auto-stop configured with a 60-minute inactivity period. 

```json
{
  "mode": "All",
  "policyRule": {
    "if": {
      "allOf": [
        {
          "field": "type",
          "equals": "Microsoft.MachineLearningServices/workspaces/computes"
        },
        {
          "field": "Microsoft.MachineLearningServices/workspaces/computes/computeType",
          "equals": "ComputeInstance"
        },
        {
          "anyOf": [
            {
              "field": "Microsoft.MachineLearningServices/workspaces/computes/idleTimeBeforeShutdown",
              "exists": false
            },
            {
              "value": "[empty(field('Microsoft.MachineLearningServices/workspaces/computes/idleTimeBeforeShutdown'))]",
              "equals": true
            }
          ]
        }
      ]
    },
    "then": {
      "effect": "append",
      "details": [
        {
          "field": "Microsoft.MachineLearningServices/workspaces/computes/idleTimeBeforeShutdown",
          "value": "PT60M"
        }
      ]
    }
  },
  "parameters": {}
}
```

## Schedule automatic start and stop

Define multiple schedules for auto-shutdown and auto-start. For instance, create a schedule to start at 9 AM and stop at 6 PM from Monday-Thursday, and a second schedule to start at 9 AM and stop at 4 PM for Friday.  You can create a total of four schedules per compute instance.

Schedules can also be defined for [create on behalf of](#create-on-behalf-of-preview) compute instances. You can create a schedule that creates the compute instance in a stopped state. Stopped compute instances are useful when you create a compute instance on behalf of another user.

Prior to a scheduled shutdown, users will see a notification alerting them that the Compute Instance is about to shut down. At that point, the user can choose to dismiss the upcoming shutdown event, if for example they are in the middle of using their Compute Instance.

### Create a schedule in studio

1. [Fill out the form](?tabs=azure-studio#create).
1. On the second page of the form, open **Show advanced settings**.
1. Select **Add schedule** to add a new schedule.

    :::image type="content" source="media/how-to-create-attach-studio/create-schedule.png" alt-text="Screenshot: Add schedule in advanced settings.":::

1. Select **Start compute instance** or **Stop compute instance**.
1. Select the **Time zone**.
1. Select the **Startup time** or **Shutdown time**.
1. Select the days when this schedule is active.

    :::image type="content" source="media/how-to-create-attach-studio/stop-compute-schedule.png" alt-text="Screenshot: schedule a compute instance to shut down.":::

1. Select **Add schedule** again if you want to create another schedule.

Once the compute instance is created, you can view, edit, or add new schedules from the compute instance details section.


> [!NOTE]
> Timezone labels don't account for day light savings. For instance,  (UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna is actually UTC+02:00 during day light savings.

### Create a schedule with CLI

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```azurecli
az ml compute create -f create-instance.yml
```

Where the file *create-instance.yml* is:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/computeInstance.schema.json 
name: schedule-example-i
type: computeinstance
size: STANDARD_DS3_v2
schedules:
   compute_start_stop:
      - action: stop
        trigger:
         type: cron
         start_time: "2021-03-10T21:21:07"
         time_zone: Pacific Standard Time
         expression: 0 18 * * *
         

```
