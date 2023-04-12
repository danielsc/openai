
For more information on entry scripts, see [How and where to deploy](v1/how-to-deploy-and-where.md).

## Define the software environment

The environment class is used to define the Python dependencies for the service. It includes dependencies required by both the model and the entry script. In this example, it installs packages from the regular pypi index, as well as from a GitHub repo. 

```python
from azureml.core.conda_dependencies import CondaDependencies 
from azureml.core import Environment

conda = None
pip = ["azureml-defaults", "azureml-monitoring", 
       "git+https://github.com/NervanaSystems/nlp-architect.git@absa", 'nlp-architect', 'inference-schema',
       "spacy==2.0.18"]

conda_deps = CondaDependencies.create(conda_packages=None, pip_packages=pip)

myenv = Environment(name='myenv')
myenv.python.conda_dependencies = conda_deps
```

For more information on environments, see [Create and manage environments for training and deployment](how-to-use-environments.md).

## Define the deployment configuration

The deployment configuration defines the Azure Kubernetes Service hosting environment used to run the web service.

> [!TIP]
> If you aren't sure about the memory, CPU, or GPU needs of your deployment, you can use profiling to learn these. For more information, see [How and where to deploy a model](v1/how-to-deploy-and-where.md).

```python
from azureml.core.model import Model
from azureml.core.webservice import Webservice
from azureml.core.image import ContainerImage
from azureml.core.webservice import AksWebservice, Webservice

# If deploying to a cluster configured for dev/test, ensure that it was created with enough
# cores and memory to handle this deployment configuration. Note that memory is also used by
# things such as dependencies and AzureML components.

aks_config = AksWebservice.deploy_configuration(autoscale_enabled=True, 
                                                       autoscale_min_replicas=1, 
                                                       autoscale_max_replicas=3, 
                                                       autoscale_refresh_seconds=10, 
                                                       autoscale_target_utilization=70,
                                                       auth_enabled=True, 
                                                       cpu_cores=1, memory_gb=2, 
                                                       scoring_timeout_ms=5000, 
                                                       replica_max_concurrent_requests=2, 
                                                       max_request_wait_time=5000)
```

For more information, see the reference documentation for [AksService.deploy_configuration](/python/api/azureml-core/azureml.core.webservice.akswebservice#deploy-configuration-autoscale-enabled-none--autoscale-min-replicas-none--autoscale-max-replicas-none--autoscale-refresh-seconds-none--autoscale-target-utilization-none--collect-model-data-none--auth-enabled-none--cpu-cores-none--memory-gb-none--enable-app-insights-none--scoring-timeout-ms-none--replica-max-concurrent-requests-none--max-request-wait-time-none--num-replicas-none--primary-key-none--secondary-key-none--tags-none--properties-none--description-none--gpu-cores-none--period-seconds-none--initial-delay-seconds-none--timeout-seconds-none--success-threshold-none--failure-threshold-none--namespace-none--token-auth-enabled-none--compute-target-name-none-).

## Define the inference configuration

The inference configuration points to the entry script and the environment object:

```python
from azureml.core.model import InferenceConfig
inf_config = InferenceConfig(entry_script='score.py', environment=myenv)
```

For more information, see the reference documentation for [InferenceConfig](/python/api/azureml-core/azureml.core.model.inferenceconfig).

## Deploy the model

Deploy the model to your AKS cluster and wait for it to create your service. In this example, two registered models are loaded from the registry and deployed to AKS. After deployment, the `score.py` file in the deployment loads these models and uses them to perform inference.
