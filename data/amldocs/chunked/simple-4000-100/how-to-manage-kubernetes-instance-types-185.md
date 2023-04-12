
#### [Python SDK](#tab/select-instancetype-to-modeldeployment-with-sdk)

To select an instance type for a model deployment using SDK (V2), specify its name for the `instance_type` property in the `KubernetesOnlineDeployment` class.  For example:

```python
from azure.ai.ml import KubernetesOnlineDeployment,Model,Environment,CodeConfiguration

model = Model(path="./model/sklearn_mnist_model.pkl")
env = Environment(
    conda_file="./model/conda.yml",
    image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:20210727.v1",
)

# define the deployment
blue_deployment = KubernetesOnlineDeployment(
    name="blue",
    endpoint_name="<endpoint name>",
    model=model,
    environment=env,
    code_configuration=CodeConfiguration(
        code="./script/", scoring_script="score.py"
    ),
    instance_count=1,
    instance_type="<instance type name>",
)
```

In the above example, replace `<instance_type_name>` with the name of the instance type you wish to select. If there's no `instance_type` property specified, the system will use `defaultinstancetype` to deploy the model.


## Next steps

- [AzureML inference router and connectivity requirements](./how-to-kubernetes-inference-routing-azureml-fe.md)
- [Secure AKS inferencing environment](./how-to-secure-kubernetes-inferencing-environment.md)
