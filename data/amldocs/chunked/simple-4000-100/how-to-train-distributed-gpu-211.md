
If your training script uses the parameter server strategy for distributed training, such as for legacy TensorFlow 1.x, you'll also need to specify the number of parameter servers to use in the job, inside the `distribution` parameter of the `command`. In the above, for example, `"parameter_server_count" : 1` and `"worker_count": 2,

### TF_CONFIG

In TensorFlow, the **TF_CONFIG** environment variable is required for training on multiple machines. For TensorFlow jobs, Azure ML will configure and set the TF_CONFIG variable appropriately for each worker before executing your training script.

You can access TF_CONFIG from your training script if you need to: `os.environ['TF_CONFIG']`.

Example TF_CONFIG set on a chief worker node:
```json
TF_CONFIG='{
    "cluster": {
        "worker": ["host0:2222", "host1:2222"]
    },
    "task": {"type": "worker", "index": 0},
    "environment": "cloud"
}'
```

### TensorFlow example

- For the full notebook to run the above example, see [azureml-examples: Train a basic neural network with distributed MPI on the MNIST dataset using Tensorflow with Horovod](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/single-step/tensorflow/mnist-distributed-horovod/tensorflow-mnist-distributed-horovod.ipynb)

## Accelerating distributed GPU training with InfiniBand

As the number of VMs training a model increases, the time required to train that model should decrease. The decrease in time, ideally, should be linearly proportional to the number of training VMs. For instance, if training a model on one VM takes 100 seconds, then training the same model on two VMs should ideally take 50 seconds. Training the model on four VMs should take 25 seconds, and so on.

InfiniBand can be an important factor in attaining this linear scaling. InfiniBand enables low-latency, GPU-to-GPU communication across nodes in a cluster. InfiniBand requires specialized hardware to operate. Certain Azure VM series, specifically the NC, ND, and H-series, now have RDMA-capable VMs with SR-IOV and InfiniBand support. These VMs communicate over the low latency and high-bandwidth InfiniBand network, which is much more performant than Ethernet-based connectivity. SR-IOV for InfiniBand enables near bare-metal performance for any MPI library (MPI is used by many distributed training frameworks and tooling, including NVIDIA's NCCL software.) These SKUs are intended to meet the needs of computationally intensive, GPU-acclerated machine learning workloads. For more information, see [Accelerating Distributed Training in Azure Machine Learning with SR-IOV](https://techcommunity.microsoft.com/t5/azure-ai/accelerating-distributed-training-in-azure-machine-learning/ba-p/1059050).

Typically, VM SKUs with an 'r' in their name contain the required InfiniBand hardware, and those without an 'r' typically do not. ('r' is a reference to RDMA, which stands for "remote direct memory access.") For instance, the VM SKU `Standard_NC24rs_v3` is InfiniBand-enabled, but the SKU  `Standard_NC24s_v3` is not.  Aside from the InfiniBand capabilities, the specs between these two SKUs are largely the same – both have 24 cores, 448 GB RAM, 4 GPUs of the same SKU, etc. [Learn more about RDMA- and InfiniBand-enabled machine SKUs](../virtual-machines/sizes-hpc.md#rdma-capable-instances).

>[!WARNING]
>The older-generation machine SKU `Standard_NC24r`  is RDMA-enabled, but it does not contain SR-IOV hardware required for InfiniBand.

If you create an `AmlCompute` cluster of one of these RDMA-capable, InfiniBand-enabled sizes, the OS image will come with the Mellanox OFED driver required to enable InfiniBand preinstalled and preconfigured.

## Next steps

* [Deploy and score a machine learning model by using an online endpoint](how-to-deploy-online-endpoints.md)
* [Reference architecture for distributed deep learning training in Azure](/azure/architecture/reference-architectures/ai/training-deep-learning)
