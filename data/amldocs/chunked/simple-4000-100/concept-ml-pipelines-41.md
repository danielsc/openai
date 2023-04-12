The Azure cloud provides several types of pipeline, each with a different purpose. The following table lists the different pipelines and what they're used for:

| Scenario | Primary persona | Azure offering | OSS offering | Canonical pipe | Strengths |
| -------- | --------------- | -------------- | ------------ | -------------- | --------- |
| Model orchestration (Machine learning) | Data scientist | Azure Machine Learning Pipelines | Kubeflow Pipelines | Data -> Model | Distribution, caching, code-first, reuse | 
| Data orchestration (Data prep) | Data engineer | [Azure Data Factory pipelines](../data-factory/concepts-pipelines-activities.md) | Apache Airflow | Data -> Data | Strongly typed movement, data-centric activities |
| Code & app orchestration (CI/CD) | App Developer / Ops | [Azure Pipelines](https://azure.microsoft.com/services/devops/pipelines/) | Jenkins | Code + Model -> App/Service | Most open and flexible activity support, approval queues, phases with gating |

## Next steps

Azure Machine Learning pipelines are a powerful facility that begins delivering value in the early development stages.

+ [Define pipelines with the Azure ML CLI v2](./how-to-create-component-pipelines-cli.md)
+ [Define pipelines with the Azure ML SDK v2](./how-to-create-component-pipeline-python.md)
+ [Define pipelines with Designer](./how-to-create-component-pipelines-ui.md)
+ Try out [CLI v2 pipeline example](https://github.com/Azure/azureml-examples/tree/sdk-preview/cli/jobs/pipelines-with-components)
+ Try out [Python SDK v2 pipeline example](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/pipelines)
