
# CLI (v2) Azure Arc-enabled Kubernetes online deployment YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The source JSON schema can be found at https://azuremlschemas.azureedge.net/latest/kubernetesOnlineDeployment.schema.json.

[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `$schema` | string | The YAML schema. If you use the Azure Machine Learning VS Code extension to author the YAML file, including `$schema` at the top of your file enables you to invoke schema and resource completions. | | |
| `name` | string | **Required.** Name of the deployment. <br><br> Naming rules are defined [here](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints).| | |
| `description` | string | Description of the deployment. | | |
| `tags` | object | Dictionary of tags for the deployment. | | |
| `endpoint_name` | string | **Required.** Name of the endpoint to create the deployment under. | | |
| `model` | string or object | The model to use for the deployment. This value can be either a reference to an existing versioned model in the workspace or an inline model specification. <br><br> To reference an existing model, use the `azureml:<model-name>:<model-version>` syntax. <br><br> To define a model inline, follow the [Model schema](reference-yaml-model.md#yaml-syntax). <br><br> As a best practice for production scenarios, you should create the model separately and reference it here. <br><br> This field is optional for [custom container deployment](how-to-deploy-custom-container.md) scenarios.| | |
| `model_mount_path` | string | The path to mount the model in a custom container. Applicable only for [custom container deployment](how-to-deploy-custom-container.md) scenarios. If the `model` field is specified, it's mounted on this path in the container. | | |
| `code_configuration` | object | Configuration for the scoring code logic. <br><br> This field is optional for [custom container deployment](how-to-deploy-custom-container.md) scenarios. | | |
| `code_configuration.code` | string | Local path to the source code directory for scoring the model. | | |
| `code_configuration.scoring_script` | string | Relative path to the scoring file in the source code directory. | | |
| `environment_variables` | object | Dictionary of environment variable key-value pairs to set in the deployment container. You can access these environment variables from your scoring scripts. | | |
| `environment` | string or object | **Required.** The environment to use for the deployment. This value can be either a reference to an existing versioned environment in the workspace or an inline environment specification. <br><br> To reference an existing environment, use the `azureml:<environment-name>:<environment-version>` syntax. <br><br> To define an environment inline, follow the [Environment schema](reference-yaml-environment.md#yaml-syntax). <br><br> As a best practice for production scenarios, you should create the environment separately and reference it here. | | |
| `instance_type` | string | The instance type used to place the inference workload. If omitted, the inference workload will be placed on the default instance type of the Kubernetes cluster specified in the endpoint's `compute` field. If specified, the inference workload will be placed on that selected instance type. <br><br> The set of instance types for a Kubernetes cluster is configured via the Kubernetes cluster custom resource definition (CRD), hence they aren't part of the Azure ML YAML schema for attaching Kubernetes compute.For more information, see [Create and select Kubernetes instance types](./how-to-manage-kubernetes-instance-types.md). | | |
| `instance_count` | integer | The number of instances to use for the deployment. Specify the value based on the workload you expect. This field is only required if you're using the `default` scale type (`scale_settings.type: default`). <br><br> `instance_count` can be updated after deployment creation using `az ml online-deployment update` command. | | |
