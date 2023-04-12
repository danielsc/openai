When running MPI jobs with Open MPI images, the following environment variables for each process launched:

1. `OMPI_COMM_WORLD_RANK` - the rank of the process
2. `OMPI_COMM_WORLD_SIZE` - the world size
3. `AZ_BATCH_MASTER_NODE` - primary address with port, `MASTER_ADDR:MASTER_PORT`
4. `OMPI_COMM_WORLD_LOCAL_RANK` - the local rank of the process on the node
5. `OMPI_COMM_WORLD_LOCAL_SIZE` - number of processes on the node

> [!TIP]
> Despite the name, environment variable `OMPI_COMM_WORLD_NODE_RANK` does not corresponds to the `NODE_RANK`. To use per-node-launcher, set `process_count_per_node=1` and use `OMPI_COMM_WORLD_RANK` as the `NODE_RANK`.

## PyTorch

Azure ML supports running distributed jobs using PyTorch's native distributed training capabilities (`torch.distributed`).

> [!TIP]
> For data parallelism, the [official PyTorch guidance](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html#comparison-between-dataparallel-and-distributeddataparallel) is to use DistributedDataParallel (DDP) over DataParallel for both single-node and multi-node distributed training. PyTorch also [recommends using DistributedDataParallel over the multiprocessing package](https://pytorch.org/docs/stable/notes/cuda.html#use-nn-parallel-distributeddataparallel-instead-of-multiprocessing-or-nn-dataparallel). Azure Machine Learning documentation and examples will therefore focus on DistributedDataParallel training.

### Process group initialization

The backbone of any distributed training is based on a group of processes that know each other and can communicate with each other using a backend. For PyTorch, the process group is created by calling [torch.distributed.init_process_group](https://pytorch.org/docs/stable/distributed.html#torch.distributed.init_process_group) in __all distributed processes__ to collectively form a process group.

```
torch.distributed.init_process_group(backend='nccl', init_method='env://', ...)
```

The most common communication backends used are `mpi`, `nccl`, and `gloo`. For GPU-based training `nccl` is recommended for best performance and should be used whenever possible. 

`init_method` tells how each process can discover each other, how they initialize and verify the process group using the communication backend. By default if `init_method` is not specified PyTorch will use the environment variable initialization method (`env://`). `init_method` is the recommended initialization method to use in your training code to run distributed PyTorch on Azure ML.  PyTorch will look for the following environment variables for initialization:

- **`MASTER_ADDR`** - IP address of the machine that will host the process with rank 0.
- **`MASTER_PORT`** - A free port on the machine that will host the process with rank 0.
- **`WORLD_SIZE`** - The total number of processes. Should be equal to the total number of devices (GPU) used for distributed training.
- **`RANK`** - The (global) rank of the current process. The possible values are 0 to (world size - 1).

For more information on process group initialization, see the [PyTorch documentation](https://pytorch.org/docs/stable/distributed.html#torch.distributed.init_process_group).

Beyond these, many applications will also need the following environment variables:
- **`LOCAL_RANK`** - The local (relative) rank of the process within the node. The possible values are 0 to (# of processes on the node - 1). This information is useful because many operations such as data preparation only should be performed once per node --- usually on local_rank = 0.
- **`NODE_RANK`** - The rank of the node for multi-node training. The possible values are 0 to (total # of nodes - 1).


You don't need to use a launcher utility like `torch.distributed.launch`. To run a distributed PyTorch job:

1. Specify the training script and arguments
1. Create a `command` and specify the type as `PyTorch` and the `process_count_per_instance` in the `distribution` parameter. The `process_count_per_instance` corresponds to the total number of processes you want to run for your job. `process_count_per_instance` should typically equal `# GPUs per node x # nodes`. If `process_count_per_instance` isn't specified, Azure ML will by default launch one process per node.
