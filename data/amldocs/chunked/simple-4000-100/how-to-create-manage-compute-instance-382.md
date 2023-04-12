

### Create a schedule with SDK

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
from azure.ai.ml import MLClient
from azure.ai.ml.constants import TimeZone
from azure.ai.ml.entities import ComputeInstance, AmlCompute, ComputeSchedules, ComputeStartStopSchedule, RecurrencePattern, RecurrenceTrigger
from azure.identity import DefaultAzureCredential
from dateutil import tz
import datetime
# Enter details of your AML workspace
subscription_id = "<guid>"
resource_group = "sample-rg"
workspace = "sample-ws"
# get a handle to the workspace
ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace
)
ci_minimal_name = "sampleCI"
mytz = tz.gettz("Asia/Kolkata")
now = datetime.datetime.now(tz = mytz)
starttime = now + datetime.timedelta(minutes=25)
triggers = RecurrenceTrigger(frequency="day", interval=1, schedule=RecurrencePattern(hours=17, minutes=30))
myschedule = ComputeStartStopSchedule(start_time=starttime, time_zone=TimeZone.INDIA_STANDARD_TIME, trigger=triggers, action="Stop")
com_sch = ComputeSchedules(compute_start_stop=[myschedule])
ci_minimal = ComputeInstance(name=ci_minimal_name, schedules=com_sch)
ml_client.begin_create_or_update(ci_minimal)
```

### Create a schedule with a Resource Manager template

You can schedule the automatic start and stop of a compute instance by using a Resource Manager [template](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-compute-create-computeinstance).

In the Resource Manager template, add:

```
"schedules": "[parameters('schedules')]"
```

Then use either cron or LogicApps expressions to define the schedule that starts or stops the instance in your parameter file:
 
```json
        "schedules": {
        "value": {
        "computeStartStop": [
          {
            "triggerType": "Cron",
            "cron": {              
              "timeZone": "UTC",
              "expression": "0 18 * * *"
            },
            "action": "Stop",
            "status": "Enabled"
          },
          {
            "triggerType": "Cron",
            "cron": {              
              "timeZone": "UTC",
              "expression": "0 8 * * *"
            },
            "action": "Start",
            "status": "Enabled"
          },
          { 
            "triggerType": "Recurrence", 
            "recurrence": { 
              "frequency": "Day", 
              "interval": 1, 
              "timeZone": "UTC", 
              "schedule": { 
                "hours": [17], 
                "minutes": [0]
              } 
            }, 
            "action": "Stop", 
            "status": "Enabled" 
          } 
        ]
      }
    }
```

* Action can have value of “Start” or “Stop”.
* For trigger type of `Recurrence` use the same syntax as logic app, with this [recurrence schema](../logic-apps/logic-apps-workflow-actions-triggers.md#recurrence-trigger).
* For trigger type of `cron`, use standard cron syntax:  

    ```cron
    // Crontab expression format: 
    // 
    // * * * * * 
    // - - - - - 
    // | | | | | 
    // | | | | +----- day of week (0 - 6) (Sunday=0) 
    // | | | +------- month (1 - 12) 
    // | | +--------- day of month (1 - 31) 
    // | +----------- hour (0 - 23) 
    // +------------- min (0 - 59) 
    // 
    // Star (*) in the value field above means all legal values as in 
    // braces for that column. The value column can have a * or a list 
    // of elements separated by commas. An element is either a number in 
    // the ranges shown above or two numbers in the range separated by a 
    // hyphen (meaning an inclusive range). 
    ```

### Azure Policy support to default a schedule
Use Azure Policy to enforce a shutdown schedule exists for every compute instance in a subscription or default to a schedule if nothing exists.
Following is a sample policy to default a shutdown schedule at 10 PM PST.
```json
{
    "mode": "All",
    "policyRule": {
     "if": {
      "allOf": [
       {
        "field": "Microsoft.MachineLearningServices/workspaces/computes/computeType",
        "equals": "ComputeInstance"
       },
       {
        "field": "Microsoft.MachineLearningServices/workspaces/computes/schedules",
        "exists": "false"
       }
      ]
     },
     "then": {
      "effect": "append",
      "details": [
       {
        "field": "Microsoft.MachineLearningServices/workspaces/computes/schedules",
        "value": {
         "computeStartStop": [
          {
           "triggerType": "Cron",
           "cron": {
            "startTime": "2021-03-10T21:21:07",
            "timeZone": "Pacific Standard Time",
            "expression": "0 22 * * *"
           },
           "action": "Stop",
           "status": "Enabled"
          }
         ]
        }
       }
      ]
     }
    }
}    
```
