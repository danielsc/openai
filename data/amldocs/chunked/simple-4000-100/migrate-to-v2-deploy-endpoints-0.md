
# Upgrade deployment endpoints to SDK v2

We newly introduced [online endpoints](concept-endpoints.md) and batch endpoints as v2 concepts. There are several deployment funnels such as managed online endpoints, [kubernetes online endpoints](how-to-attach-kubernetes-anywhere.md) (including Azure Kubernetes Services and Arc-enabled Kubernetes) in v2, and Azure Container Instances (ACI) and Kubernetes Services (AKS) webservices in v1. In this article, we'll focus on the comparison of deploying to ACI webservices (v1) and managed online endpoints (v2).

Examples in this article show how to:

* Deploy your model to Azure
* Score using the endpoint
* Delete the webservice/endpoint

## Create inference resources

* SDK v1
    1. Configure a model, an environment, and a scoring script:
        ```python
        # configure a model. example for registering a model 
        from azureml.core.model import Model
        model = Model.register(ws, model_name="bidaf_onnx", model_path="./model.onnx")
        
        # configure an environment
        from azureml.core import Environment
        env = Environment(name='myenv')
        python_packages = ['nltk', 'numpy', 'onnxruntime']
        for package in python_packages:
            env.python.conda_dependencies.add_pip_package(package)
        
        # configure an inference configuration with a scoring script
        from azureml.core.model import InferenceConfig
        inference_config = InferenceConfig(
            environment=env,
            source_directory="./source_dir",
            entry_script="./score.py",
        )
        ```

    1. Configure and deploy an **ACI webservice**:
        ```python
        from azureml.core.webservice import AciWebservice
        
        # defince compute resources for ACI
        deployment_config = AciWebservice.deploy_configuration(
            cpu_cores=0.5, memory_gb=1, auth_enabled=True
        )
        
        # define an ACI webservice
        service = Model.deploy(
            ws,
            "myservice",
            [model],
            inference_config,
            deployment_config,
            overwrite=True,
        )
        
        # create the service 
        service.wait_for_deployment(show_output=True)
        ```

For more information on registering models, see [Register a model from a local file](v1/how-to-deploy-and-where.md?tabs=python#register-a-model-from-a-local-file).

* SDK v2

    1. Configure a model, an environment, and a scoring script:
        ```python
        from azure.ai.ml.entities import Model
        # configure a model
        model = Model(path="../model-1/model/sklearn_regression_model.pkl")
        
        # configure an environment
        from azure.ai.ml.entities import Environment
        env = Environment(
            conda_file="../model-1/environment/conda.yml",
            image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:20210727.v1",
        )
        
        # configure an inference configuration with a scoring script
        from azure.ai.ml.entities import CodeConfiguration
        code_config = CodeConfiguration(
                code="../model-1/onlinescoring", scoring_script="score.py"
            )
        ```

    1. Configure and create an **online endpoint**:
        ```python
        import datetime
        from azure.ai.ml.entities import ManagedOnlineEndpoint
        
        # create a unique endpoint name with current datetime to avoid conflicts
        online_endpoint_name = "endpoint-" + datetime.datetime.now().strftime("%m%d%H%M%f")
        
        # define an online endpoint
        endpoint = ManagedOnlineEndpoint(
            name=online_endpoint_name,
            description="this is a sample online endpoint",
            auth_mode="key",
            tags={"foo": "bar"},
        )
        
        # create the endpoint:
        ml_client.begin_create_or_update(endpoint)
        ```
    
    1. Configure and create an **online deployment**:
        ```python
        from azure.ai.ml.entities import ManagedOnlineDeployment
        
        # define a deployment
        blue_deployment = ManagedOnlineDeployment(
            name="blue",
            endpoint_name=online_endpoint_name,
            model=model,
            environment=env,
            code_configuration=code_config,
            instance_type="Standard_F2s_v2",
            instance_count=1,
        )
        
        # create the deployment:
        ml_client.begin_create_or_update(blue_deployment)
        
        # blue deployment takes 100 traffic
        endpoint.traffic = {"blue": 100}
        ml_client.begin_create_or_update(endpoint)
        ```
