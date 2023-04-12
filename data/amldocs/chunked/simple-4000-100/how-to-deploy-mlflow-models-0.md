
# Guidelines for deploying MLflow models

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning CLI extension you are using:"]
> * [v1](./v1/how-to-deploy-mlflow-models.md)
> * [v2 (current version)](how-to-deploy-mlflow-models.md)

In this article, learn how to deploy your [MLflow](https://www.mlflow.org) model to Azure Machine Learning for both real-time and batch inference. Learn also about the different tools you can use to perform management of the deployment.


## Deploying MLflow models vs custom models

When deploying MLflow models to Azure Machine Learning, you don't have to provide a scoring script or an environment for deployment as they are automatically generated for you. We typically refer to this functionality as no-code deployment.

For no-code-deployment, Azure Machine Learning:

* Ensures all the package dependencies indicated in the MLflow model are satisfied.
* Provides a MLflow base image/curated environment that contains the following items:
    * Packages required for Azure Machine Learning to perform inference, including [`mlflow-skinny`](https://github.com/mlflow/mlflow/blob/master/README_SKINNY.rst).
    * A scoring script to perform inference.

> [!WARNING]
> Online Endpoints dynamically installs Python packages provided MLflow model package during container runtime. deploying MLflow models to online endpoints with no-code deployment in a private network without egress connectivity is not supported by the moment. If that's your case, either enable egress connectivity or indicate the environment to use in the deployment as explained in [Customizing MLflow model deployments (Online Endpoints)](how-to-deploy-mlflow-models-online-endpoints.md#customizing-mlflow-model-deployments). This limitation is not present in Batch Endpoints.

### Python packages and dependencies

Azure Machine Learning automatically generates environments to run inference of MLflow models. Those environments are built by reading the conda dependencies specified in the MLflow model. Azure Machine Learning also adds any required package to run the inferencing server, which will vary depending on the type of deployment you are doing.

__conda.yaml__

```yaml
channels:
- conda-forge
dependencies:
- python=3.7.11
- pip
- pip:
  - mlflow
  - scikit-learn==0.24.1
  - cloudpickle==2.0.0
  - psutil==5.8.0
name: mlflow-env

```

> [!WARNING]
> MLflow performs automatic package detection when logging models, and pins their versions in the conda dependencies of the model. However, such action is performed at the best of its knowledge and there may be cases when the detection doesn't reflect your intentions or requirements. On those cases consider [logging models with a custom conda dependencies definition](how-to-log-mlflow-models.md?#logging-models-with-a-custom-signature-environment-or-samples).

### Implications of models with signatures

MLflow models can include a signature that indicates the expected inputs and their types. For those models containing a signature, Azure Machine Learning enforces compliance with it, both in terms of the number of inputs and their types. This means that your data input should comply with the types indicated in the model signature. If the data can't be parsed as expected, the invocation will fail. This applies for both online and batch endpoints.

__MLmodel__

```yaml
artifact_path: model
flavors:
  python_function:
    env: conda.yaml
    loader_module: mlflow.sklearn
    model_path: model.pkl
    python_version: 3.7.11
  sklearn:
    pickled_model: model.pkl
    serialization_format: cloudpickle
    sklearn_version: 0.24.1
run_id: f1e06708-641d-4a49-8f36-e9dcd8d34346
signature:
  inputs: '[{"name": "age", "type": "double"}, {"name": "sex", "type": "double"},
    {"name": "bmi", "type": "double"}, {"name": "bp", "type": "double"}, {"name":
    "s1", "type": "double"}, {"name": "s2", "type": "double"}, {"name": "s3", "type":
    "double"}, {"name": "s4", "type": "double"}, {"name": "s5", "type": "double"},
    {"name": "s6", "type": "double"}]'
  outputs: '[{"type": "double"}]'
utc_time_created: '2022-03-17 01:56:03.706848'

```
