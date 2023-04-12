> The first pipeline run takes roughly *15 minutes*. All dependencies must be downloaded, a Docker image is created, and the Python environment is provisioned and created. Running the pipeline again takes significantly less time because those resources are reused instead of created. However, total run time for the pipeline depends on the workload of your scripts and the processes that are running in each pipeline step.

### Checkout outputs and debug your pipeline in UI

You can open the `Link to Azure Machine Learning studio`, which is the job detail page of your pipeline. You'll see the pipeline graph like following.

:::image type="content" source="./media/how-to-create-component-pipeline-python/pipeline-ui.png" alt-text="Screenshot of the pipeline job detail page." lightbox ="./media/how-to-create-component-pipeline-python/pipeline-ui.png":::

You can check the logs and outputs of each component by right clicking the component, or select the component to open its detail pane. To learn more about how to debug your pipeline in UI, see [How to use studio UI to build and debug Azure ML pipelines](how-to-use-pipeline-ui.md).

## (Optional) Register components to workspace

In the previous section, you have built a pipeline using three components to E2E complete an image classification task. You can also register components to your workspace so that they can be shared and resued within the workspace. Following is an example to register prep-data component.

```python
try:
    # try get back the component
    prep = ml_client.components.get(name="prep_data", version="1")
except:
    # if not exists, register component using following code
    prep = ml_client.components.create_or_update(prepare_data_component)

# list all components registered in workspace
for c in ml_client.components.list():
    print(c)
```

Using `ml_client.components.get()`, you can get a registered component by name and version. Using `ml_client.compoennts.create_or_update()`, you can register a component previously loaded from Python function or yaml.

## Next steps

* For more examples of how to build pipelines by using the machine learning SDK, see the [example repository](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/pipelines).
* For how to use studio UI to submit and debug your pipeline, refer to [how to create pipelines using component in the UI](how-to-create-component-pipelines-ui.md).
* For how to use Azure Machine Learning CLI to create components and pipelines, refer to [how to create pipelines using component with CLI](how-to-create-component-pipelines-cli.md).
