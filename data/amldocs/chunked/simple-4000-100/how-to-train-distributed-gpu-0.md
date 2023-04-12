
# Distributed GPU training guide (SDK v2)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

Learn more about how to use distributed GPU training code in Azure Machine Learning (ML). This article will not teach you about distributed training.  It will help you run your existing distributed training code on Azure Machine Learning. It offers tips and examples for you to follow for each framework:

* Message Passing Interface (MPI)
    * Horovod
    * Environment variables from Open MPI
* PyTorch
* TensorFlow 
* Accelerate GPU training with InfiniBand

## Prerequisites

Review these [basic concepts of distributed GPU training](concept-distributed-training.md) such as _data parallelism_, _distributed data parallelism_, and _model parallelism_.

> [!TIP]
> If you don't know which type of parallelism to use, more than 90% of the time you should use __Distributed Data Parallelism__.

## MPI

Azure ML offers an [MPI job](https://www.mcs.anl.gov/research/projects/mpi/) to launch a given number of processes in each node. Azure ML constructs the full MPI launch command (`mpirun`) behind the scenes.  You can't provide your own full head-node-launcher commands like `mpirun` or `DeepSpeed launcher`.

> [!TIP]
> The base Docker image used by an Azure Machine Learning MPI job needs to have an MPI library installed. [Open MPI](https://www.open-mpi.org/) is included in all the [AzureML GPU base images](https://github.com/Azure/AzureML-Containers). When you use a custom Docker image, you are responsible for making sure the image includes an MPI library. Open MPI is recommended, but you can also use a different MPI implementation such as Intel MPI. Azure ML also provides [curated environments](resource-curated-environments.md) for popular frameworks. 

To run distributed training using MPI, follow these steps:

1. Use an Azure ML environment with the preferred deep learning framework and MPI. AzureML provides [curated environment](resource-curated-environments.md) for popular frameworks.
1. Define  a `command` with `instance_count`. `instance_count` should be equal to the number of GPUs per node for per-process-launch, or set to 1 (the default) for per-node-launch if the user script will be responsible for launching the processes per node.
1. Use the `distribution` parameter of the `command` to specify settings for `MpiDistribution`.

```python
from azure.ai.ml import command, MpiDistribution

job = command(
    code="./src",  # local path where the code is stored
    command="python train.py --epochs ${{inputs.epochs}}",
    inputs={"epochs": 1},
    environment="AzureML-tensorflow-2.7-ubuntu20.04-py38-cuda11-gpu@latest",
    compute="gpu-cluster",
    instance_count=2,
    distribution=MpiDistribution(process_count_per_instance=2),
    display_name="tensorflow-mnist-distributed-horovod-example"
    # experiment_name: tensorflow-mnist-distributed-horovod-example
    # description: Train a basic neural network with TensorFlow on the MNIST dataset, distributed via Horovod.
)
```


### Horovod

Use the MPI job configuration when you use [Horovod](https://horovod.readthedocs.io/en/stable/index.html) for distributed training with the deep learning framework.

Make sure your code follows these tips:

* The training code is instrumented correctly with Horovod before adding the Azure ML parts
* Your Azure ML environment contains Horovod and MPI. The PyTorch and TensorFlow curated GPU environments come pre-configured with Horovod and its dependencies.
* Create a `command` with your desired distribution.

### Horovod example

* For the full notebook to run the above example, see [azureml-examples: Train a basic neural network with distributed MPI on the MNIST dataset using Horovod](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/single-step/tensorflow/mnist-distributed-horovod/tensorflow-mnist-distributed-horovod.ipynb)

### Environment variables from Open MPI

When running MPI jobs with Open MPI images, the following environment variables for each process launched:
