| CPU request | required | String values, which cannot be 0 or empty. <br>CPU can be specified in millicores; for example, `100m`. Can also be specified as full numbers; for example, `"1"` is equivalent to `1000m`.|
| Memory request | required | String values, which cannot be 0 or empty. <br>Memory can be specified as a full number + suffix; for example, `1024Mi` for 1024 MiB.|
| CPU limit | required | String values, which cannot be 0 or empty. <br>CPU can be specified in millicores; for example, `100m`. Can also be specified as full numbers; for example, `"1"` is equivalent to `1000m`.|
| Memory limit | required | String values, which cannot be 0 or empty. <br>Memory can be specified as a full number + suffix; for example, `1024Mi` for 1024 MiB.|
| GPU | optional | Integer values, which can only be specified in the `limits` section. <br>For more information, see the Kubernetes [documentation](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/#using-device-plugins). |
| nodeSelector | optional | Map of string keys and values. |


It's also possible to create multiple instance types at once:

```bash
kubectl apply -f my_instance_type_list.yaml
```

With `my_instance_type_list.yaml`:
```yaml
apiVersion: amlarc.azureml.com/v1alpha1
kind: InstanceTypeList
items:
  - metadata:
      name: cpusmall
    spec:
      resources:
        requests:
          cpu: "100m"
          memory: "100Mi"
        limits:
          cpu: "1"
          nvidia.com/gpu: 0
          memory: "1Gi"

  - metadata:
      name: defaultinstancetype
    spec:
      resources:
        requests:
          cpu: "1"
          memory: "1Gi" 
        limits:
          cpu: "1"
          nvidia.com/gpu: 0
          memory: "1Gi"
```

The above example creates two instance types: `cpusmall` and `defaultinstancetype`.  This `defaultinstancetype` definition will override the `defaultinstancetype` definition created when Kubernetes cluster was attached to AzureML workspace. 

If a training or inference workload is submitted without an instance type, it uses the `defaultinstancetype`.  To specify a default instance type for a Kubernetes cluster, create an instance type with name `defaultinstancetype`.  It will automatically be recognized as the default.


### Select instance type to submit training job

#### [Azure CLI](#tab/select-instancetype-to-trainingjob-with-cli)

To select an instance type for a training job using CLI (V2), specify its name as part of the
`resources` properties section in job YAML.  For example:

```yaml
command: python -c "print('Hello world!')"
environment:
  image: library/python:latest
compute: azureml:<Kubernetes-compute_target_name>
resources:
  instance_type: <instance_type_name>
```

#### [Python SDK](#tab/select-instancetype-to-trainingjob-with-sdk)

To select an instance type for a training job using SDK (V2), specify its name for `instance_type` property in `command` class.  For example:

```python
from azure.ai.ml import command

# define the command
command_job = command(
    command="python -c "print('Hello world!')"",
    environment="AzureML-lightgbm-3.2-ubuntu18.04-py37-cpu@latest",
    compute="<Kubernetes-compute_target_name>",
    instance_type="<instance_type_name>"
)
```

In the above example, replace `<Kubernetes-compute_target_name>` with the name of your Kubernetes compute
target and replace `<instance_type_name>` with the name of the instance type you wish to select. If there's no `instance_type` property specified, the system will use `defaultinstancetype` to submit the job.

### Select instance type to deploy model

#### [Azure CLI](#tab/select-instancetype-to-modeldeployment-with-cli)

To select an instance type for a model deployment using CLI (V2), specify its name for the `instance_type` property in the deployment YAML.  For example:

```yaml
name: blue
app_insights_enabled: true
endpoint_name: <endpoint name>
model: 
  path: ./model/sklearn_mnist_model.pkl
code_configuration:
  code: ./script/
  scoring_script: score.py
instance_type: <instance type name>
environment: 
  conda_file: file:./model/conda.yml
  image: mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:20210727.v1
```
