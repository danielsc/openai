
### Manage components

You can check component details and manage the component using CLI (v2). Use `az ml component -h` to get detailed instructions on component command. Below table lists all available commands. See more examples in [Azure CLI reference](/cli/azure/ml/component?view=azure-cli-latest&preserve-view=true)

|commands|description|
|------|------|
|`az ml component create`|Create a component|
|`az ml component list`|List components in a workspace|
|`az ml component show`|Show details of a component|
|`az ml component update`|Update a component. Only a few fields(description, display_name) support update|
|`az ml component archive`|Archive a component container|
|`az ml component restore`|Restore an archived component|

## Next steps

- Try out [CLI v2 component example](https://github.com/Azure/azureml-examples/tree/main/cli/jobs/pipelines-with-components)
