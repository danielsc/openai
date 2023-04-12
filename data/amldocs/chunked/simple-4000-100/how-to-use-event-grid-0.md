
# Trigger applications, processes, or CI/CD workflows based on Azure Machine Learning events (preview)

In this article, you learn how to set up event-driven applications, processes, or CI/CD workflows based on Azure Machine Learning events, such as failure notification emails or ML pipeline runs, when certain conditions are detected by [Azure Event Grid](../event-grid/index.yml).

Azure Machine Learning manages the entire lifecycle of machine learning process, including model training, model deployment, and monitoring. You can use Event Grid to react to Azure Machine Learning events, such as the completion of training runs, the registration and deployment of models, and the detection of data drift, by using modern serverless architectures. You can then subscribe and consume events such as run status changed, run completion, model registration, model deployment, and data drift detection within a workspace.

When to use Event Grid for event driven actions:
* Send emails on run failure and run completion
* Use an Azure function after a model is registered
* Streaming events from Azure Machine Learning to various of endpoints
* Trigger an ML pipeline when drift is detected

## Prerequisites

To use Event Grid, you need contributor or owner access to the Azure Machine Learning workspace you will create events for.

## The event model & types

Azure Event Grid reads events from sources, such as Azure Machine Learning and other Azure services. These events are then sent to event handlers such as Azure Event Hubs, Azure Functions, Logic Apps, and others. The following diagram shows how Event Grid connects sources and handlers, but is not a comprehensive list of supported integrations.

![Azure Event Grid functional model](./media/concept-event-grid-integration/azure-event-grid-functional-model.png)

For more information on event sources and event handlers, see [What is Event Grid?](../event-grid/overview.md)

### Event types for Azure Machine Learning

Azure Machine Learning provides events in the various points of machine learning lifecycle: 

| Event type | Description |
| ---------- | ----------- |
| `Microsoft.MachineLearningServices.RunCompleted` | Raised when a machine learning experiment run is completed |
| `Microsoft.MachineLearningServices.ModelRegistered` | Raised when a machine learning model is registered in the workspace |
| `Microsoft.MachineLearningServices.ModelDeployed` | Raised when a deployment of inference service with one or more models is completed |
| `Microsoft.MachineLearningServices.DatasetDriftDetected` | Raised when a data drift detection job for two datasets is completed |
| `Microsoft.MachineLearningServices.RunStatusChanged` | Raised when a run status is changed |

### Filter & subscribe to events

These events are published through Azure Event Grid. Using Azure portal, PowerShell or Azure CLI, customers can easily subscribe to events by [specifying one or more event types, and filtering conditions](../event-grid/event-filtering.md). 

When setting up your events, you can apply filters to only trigger on specific event data. In the example below, for run status changed events, you can filter by run types. The event only triggers when the criteria is met. Refer to the [Azure Machine Learning event grid schema](../event-grid/event-schema-machine-learning.md) to learn about event data you can filter by. 

Subscriptions for Azure Machine Learning events are protected by Azure role-based access control (Azure RBAC). Only [contributor or owner](how-to-assign-roles.md#default-roles) of a workspace can create, update, and delete event subscriptions.  Filters can be applied to event subscriptions either during the [creation](/cli/azure/eventgrid/event-subscription) of the event subscription or at a later time. 


1. Go to the Azure portal, select a new subscription or an existing one.
1. Select the Events entry from the left navigation area, and then select **+ Event subscription**.
1. Select the filters tab and scroll down to Advanced filters. For the **Key** and **Value**, provide the property types you want to filter by. Here you can see the event will only trigger when the run type is a pipeline run or pipeline step run.  
