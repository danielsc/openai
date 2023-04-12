Now, it's time to develop the code of executing a step. You can use your preferred languages (python, R, etc.). The code must be able to be executed by a shell command. During the development, you may want to add a few inputs to control how this step is going to be executed. For example, for a training step, you may like to add learning rate, number of epochs as the inputs to control the training. These additional inputs plus the inputs and outputs required to connect with other steps are the interface of the component. The argument of a shell command is used to pass inputs and outputs to the code. The environment to execute the command and the code needs to be specified. The environment could be a curated AzureML environment, a docker image or a conda environment.

Finally, you can package everything including code, cmd, environment, input, outputs, metadata together into a component. Then connects these components together to build pipelines for your machine learning workflow. One component can be used in multiple pipelines.

To learn more about how to build a component, see:

- How to [build a component using Azure MLCLI v2](how-to-create-component-pipelines-cli.md).
- How to [build a component using Azure ML SDK v2](how-to-create-component-pipeline-python.md).

## Next steps

- [Define component with the Azure ML CLI v2](./how-to-create-component-pipelines-cli.md).
- [Define component with the Azure ML SDK v2](./how-to-create-component-pipeline-python.md).
- [Define component with Designer](./how-to-create-component-pipelines-ui.md).
- [Component CLI v2 YAML reference](./reference-yaml-component-command.md).
- [What is Azure Machine Learning Pipeline?](concept-ml-pipelines.md).
- Try out [CLI v2 component example](https://github.com/Azure/azureml-examples/tree/sdk-preview/cli/jobs/pipelines-with-components).
- Try out [Python SDK v2 component example](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/pipelines).
