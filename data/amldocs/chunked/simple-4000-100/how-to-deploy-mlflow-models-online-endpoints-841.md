1. Let's create an environment where the scoring script can be executed. Since our model is MLflow, the conda requirements are also specified in the model package (for more details about MLflow models and the files included on it see The MLmodel format). We are going then to build the environment using the conda dependencies from the file. However, we need also to include the package `azureml-inference-server-http` which is required for Online Deployments in Azure Machine Learning.
    
    The conda definition file looks as follows:

    __conda.yml__

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
      - pandas==1.3.5
      - azureml-inference-server-http
    name: mlflow-env
    ```

    > [!NOTE]
    > Note how the package `azureml-inference-server-http` has been added to the original conda dependencies file. 

    We will use this conda dependencies file to create the environment:

    # [Azure CLI](#tab/cli)
    
    *The environment will be created inline in the deployment configuration.*
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```pythonS
    environment = Environment(
        conda_file="sklearn-diabetes/environment/conda.yml",
        image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:latest",
    )
    ```

    # [Python (MLflow SDK)](#tab/mlflow)

    *This operation is not supported in MLflow SDK*

    # [Studio](#tab/studio)
    
    On [Azure ML studio portal](https://ml.azure.com), follow these steps:
    
    1. Navigate to the __Environments__ tab on the side menu.
    1. Select the tab __Custom environments__ > __Create__.
    1. Enter the name of the environment, in this case `sklearn-mlflow-online-py37`.
    1. On __Select environment type__ select __Use existing docker image with conda__.
    1. On __Container registry image path__, enter `mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04`.
    1. On __Customize__ section copy the content of the file `sklearn-diabetes/environment/conda.yml` we introduced before. 
    1. Click on __Next__ and then on __Create__.
    1. The environment is ready to be used.   


1. Let's create the deployment now:

    # [Azure CLI](#tab/cli)
    
    Create a deployment configuration file:
    
    ```yaml
    $schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
    name: sklearn-diabetes-custom
    endpoint_name: my-endpoint
    model: azureml:sklearn-diabetes@latest
    environment: 
      image: mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04
      conda_file: mlflow/sklearn-diabetes/environment/conda.yml
    code_configuration:
      source: mlflow/sklearn-diabetes/src
      scoring_script: score.py
    instance_type: Standard_F2s_v2
    instance_count: 1
    ```
    
    Create the deployment:
    
    ```azurecli
    az ml online-deployment create -f deployment.yml
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    blue_deployment = ManagedOnlineDeployment(
        name="blue",
        endpoint_name=endpoint_name,
        model=model,
        environment=environment,
        code_configuration=CodeConfiguration(
            code="sklearn-diabetes/src",
            scoring_script="score.py"
        ),
        instance_type="Standard_F4s_v2",
        instance_count=1,
    )
    ```

    # [Python (MLflow SDK)](#tab/mlflow)

    *This operation is not supported in MLflow SDK*

    # [Studio](#tab/studio)
    
    > [!IMPORTANT]
    > You can't create custom MLflow deployments in Online Endpoints using the Azure Machine Learning portal. Switch to [Azure ML CLI](?tabs=azure-cli) or the [Azure ML SDK for Python](?tabs=python).


1. Once your deployment completes, your deployment is ready to serve request. One of the easier ways to test the deployment is by using a sample request file along with the `invoke` method.

    **sample-request-sklearn.json**
