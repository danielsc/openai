1. Create a `command` and specify the type as `PyTorch` and the `process_count_per_instance` in the `distribution` parameter. The `process_count_per_instance` corresponds to the total number of processes you want to run for your job. `process_count_per_instance` should typically equal `# GPUs per node x # nodes`. If `process_count_per_instance` isn't specified, Azure ML will by default launch one process per node.

Azure ML will set the `MASTER_ADDR`, `MASTER_PORT`, `WORLD_SIZE`, and `NODE_RANK` environment variables on each node, and set the process-level `RANK` and `LOCAL_RANK` environment variables.

```python
from azure.ai.ml import command
from azure.ai.ml.entities import Data
from azure.ai.ml import Input
from azure.ai.ml import Output
from azure.ai.ml.constants import AssetTypes

# === Note on path ===
# can be can be a local path or a cloud path. AzureML supports https://`, `abfss://`, `wasbs://` and `azureml://` URIs.
# Local paths are automatically uploaded to the default datastore in the cloud.
# More details on supported paths: https://docs.microsoft.com/azure/machine-learning/how-to-read-write-data-v2#supported-paths

inputs = {
    "cifar": Input(
        type=AssetTypes.URI_FOLDER, path=returned_job.outputs.cifar.path
    ),  # path="azureml:azureml_stoic_cartoon_wgb3lgvgky_output_data_cifar:1"), #path="azureml://datastores/workspaceblobstore/paths/azureml/stoic_cartoon_wgb3lgvgky/cifar/"),
    "epoch": 10,
    "batchsize": 64,
    "workers": 2,
    "lr": 0.01,
    "momen": 0.9,
    "prtfreq": 200,
    "output": "./outputs",
}

job = command(
    code="./src",  # local path where the code is stored
    command="python train.py --data-dir ${{inputs.cifar}} --epochs ${{inputs.epoch}} --batch-size ${{inputs.batchsize}} --workers ${{inputs.workers}} --learning-rate ${{inputs.lr}} --momentum ${{inputs.momen}} --print-freq ${{inputs.prtfreq}} --model-dir ${{inputs.output}}",
    inputs=inputs,
    environment="azureml:AzureML-pytorch-1.9-ubuntu18.04-py37-cuda11-gpu:6",
    compute="gpu-cluster",  # Change the name to the gpu cluster of your workspace.
    instance_count=2,  # In this, only 2 node cluster was created.
    distribution={
        "type": "PyTorch",
        # set process count to the number of gpus per node
        # NV6 has only 1 GPU
        "process_count_per_instance": 1,
    },
)
```

### Pytorch example

- For the full notebook to run the above example, see [azureml-examples: Distributed training with PyTorch on CIFAR-10](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/single-step/pytorch/distributed-training/distributed-cifar10.ipynb)

## DeepSpeed

[DeepSpeed](https://www.deepspeed.ai/tutorials/azure/) is supported as a first-class citizen within Azure Machine Learning to run distributed jobs with near linear scalabibility in terms of 

* Increase in model size
* Increase in number of GPUs

`DeepSpeed` can be enabled using either Pytorch distribution or MPI for running distributed training. Azure Machine Learning supports the `DeepSpeed` launcher to launch distributed training as well as autotuning to get optimal `ds` configuration.

You can use a [curated environment](resource-curated-environments.md#azure-container-for-pytorch-acpt-preview) for an out of the box environment with the latest state of art technologies including `DeepSpeed`, `ORT`, `MSSCCL`, and `Pytorch` for your DeepSpeed training jobs.

### DeepSpeed example

- For DeepSpeed training and autotuning examples, see [these folders](https://github.com/Azure/azureml-examples/tree/main/cli/jobs/deepspeed).

## TensorFlow

If you're using [native distributed TensorFlow](https://www.tensorflow.org/guide/distributed_training) in your training code, such as TensorFlow 2.x's `tf.distribute.Strategy` API, you can launch the distributed job via Azure ML using `distribution` parameters or the `TensorFlowDistribution` object.


```python
# create the command
job = command(
    code="./src",  # local path where the code is stored
    command="python main.py --epochs ${{inputs.epochs}} --model-dir ${{inputs.model_dir}}",
    inputs={"epochs": 1, "model_dir": "outputs/keras-model"},
    environment="AzureML-tensorflow-2.4-ubuntu18.04-py37-cuda11-gpu@latest",
    compute="cpu-cluster",
    instance_count=2,
    # distribution = {"type": "mpi", "process_count_per_instance": 1},
    distribution={
        "type": "tensorflow",
        "parameter_server_count": 1,
        "worker_count": 2,
        "added_property": 7,
    },
    # distribution = {
    #        "type": "pytorch",
    #        "process_count_per_instance": 4,
    #        "additional_prop": {"nested_prop": 3},
    #    },
    display_name="tensorflow-mnist-distributed-example"
    # experiment_name: tensorflow-mnist-distributed-example
    # description: Train a basic neural network with TensorFlow on the MNIST dataset, distributed via TensorFlow.
)

# can also set the distribution in a separate step and using the typed objects instead of a dict
job.distribution = TensorFlowDistribution(parameter_server_count=1, worker_count=2)
```
