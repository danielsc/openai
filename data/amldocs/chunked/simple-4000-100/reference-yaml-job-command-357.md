
## YAML: distributed TensorFlow

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
code: src
command: >-
  python train.py 
  --epochs ${{inputs.epochs}}
  --model-dir ${{inputs.model_dir}}
inputs:
  epochs: 1
  model_dir: outputs/keras-model
environment: azureml:AzureML-tensorflow-2.4-ubuntu18.04-py37-cuda11-gpu@latest
compute: azureml:gpu-cluster
resources:
  instance_count: 2
distribution:
  type: tensorflow
  worker_count: 2
display_name: tensorflow-mnist-distributed-example
experiment_name: tensorflow-mnist-distributed-example
description: Train a basic neural network with TensorFlow on the MNIST dataset, distributed via TensorFlow.

```

## YAML: distributed MPI

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
code: src
command: >-
  python train.py
  --epochs ${{inputs.epochs}}
inputs:
  epochs: 1
environment: azureml:AzureML-tensorflow-2.7-ubuntu20.04-py38-cuda11-gpu@latest
compute: azureml:gpu-cluster
resources:
  instance_count: 2
distribution:
  type: mpi
  process_count_per_instance: 1
display_name: tensorflow-mnist-distributed-horovod-example
experiment_name: tensorflow-mnist-distributed-horovod-example
description: Train a basic neural network with TensorFlow on the MNIST dataset, distributed via Horovod.

```

## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
