1. Select the filters tab and scroll down to Advanced filters. For the **Key** and **Value**, provide the property types you want to filter by. Here you can see the event will only trigger when the run type is a pipeline run or pipeline step run.  

    :::image type="content" source="media/how-to-use-event-grid/select-event-filters.png" alt-text="filter events":::


+ **Filter by event type:** An event subscription can specify one or more Azure Machine Learning event types.

+ **Filter by event subject:** Azure Event Grid supports subject filters based on __begins with__ and __ends with__ matches, so that events with a matching subject are delivered to the subscriber. Different machine learning events have different subject format.

  | Event type | Subject format | Sample subject |
  | ---------- | ----------- | ----------- |
  | `Microsoft.MachineLearningServices.RunCompleted` | `experiments/{ExperimentId}/runs/{RunId}` | `experiments/b1d7966c-f73a-4c68-b846-992ace89551f/runs/my_exp1_1554835758_38dbaa94` |
  | `Microsoft.MachineLearningServices.ModelRegistered` | `models/{modelName}:{modelVersion}` | `models/sklearn_regression_model:3` |
  | `Microsoft.MachineLearningServices.ModelDeployed` | `endpoints/{serviceId}` | `endpoints/my_sklearn_aks` |
  | `Microsoft.MachineLearningServices.DatasetDriftDetected` | `datadrift/{data.DataDriftId}/run/{data.RunId}` | `datadrift/4e694bf5-712e-4e40-b06a-d2a2755212d4/run/my_driftrun1_1550564444_fbbcdc0f` |
  | `Microsoft.MachineLearningServices.RunStatusChanged` | `experiments/{ExperimentId}/runs/{RunId}` | `experiments/b1d7966c-f73a-4c68-b846-992ace89551f/runs/my_exp1_1554835758_38dbaa94` | 

+ **Advanced filtering**: Azure Event Grid also supports advanced filtering based on published event schema. Azure Machine Learning event schema details can be found in [Azure Event Grid event schema for Azure Machine Learning](../event-grid/event-schema-machine-learning.md).  Some sample advanced filterings you can perform include:

  For `Microsoft.MachineLearningServices.ModelRegistered` event, to filter model's tag value:

  ```
  --advanced-filter data.ModelTags.key1 StringIn ('value1')
  ```

  To learn more about how to apply filters, see [Filter events for Event Grid](../event-grid/how-to-filter-events.md).

## Consume Machine Learning events

Applications that handle Machine Learning events should follow a few recommended practices:

> [!div class="checklist"]
> * As multiple subscriptions can be configured to route events to the same event handler, it is important not to assume events are from a particular source, but to check the topic of the message to ensure that it comes from the machine learning workspace you are expecting.
> * Similarly, check that the eventType is one you are prepared to process, and do not assume that all events you receive will be the types you expect.
> * As messages can arrive out of order and after some delay, use the etag fields to understand if your information about objects is still up-to-date.  Also, use the sequencer fields to understand the order of events on any particular object.
> * Ignore fields you don't understand. This practice will help keep you resilient to new features that might be added in the future.
> * Failed or cancelled Azure Machine Learning operations will not trigger an event. For example, if a model deployment fails Microsoft.MachineLearningServices.ModelDeployed won't be triggered. Consider such failure mode when design your applications. You can always use Azure Machine Learning SDK, CLI or portal to check the status of an operation and understand the detailed failure reasons.

Azure Event Grid allows customers to build de-coupled message handlers, which can be triggered by Azure Machine Learning events. Some notable examples of message handlers are:
* Azure Functions
* Azure Logic Apps
* Azure Event Hubs
* Azure Data Factory Pipeline
* Generic webhooks, which may be hosted on the Azure platform or elsewhere

## Set up in Azure portal
