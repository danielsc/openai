
## YAML: write to named data output

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: echo "hello world" > ${{outputs.hello_output}}/helloworld.txt
outputs:
  hello_output:
environment:
  image: python
compute: azureml:cpu-cluster

```

## YAML: datastore URI file input

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: |
  echo "--iris-csv: ${{inputs.iris_csv}}"
  python hello-iris.py --iris-csv ${{inputs.iris_csv}}
code: src
inputs:
  iris_csv:
    type: uri_file 
    path: azureml://datastores/workspaceblobstore/paths/example-data/iris.csv
environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
compute: azureml:cpu-cluster

```

## YAML: datastore URI folder input

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: |
  ls ${{inputs.data_dir}}
  echo "--iris-csv: ${{inputs.data_dir}}/iris.csv"
  python hello-iris.py --iris-csv ${{inputs.data_dir}}/iris.csv
code: src
inputs:
  data_dir:
    type: uri_folder 
    path: azureml://datastores/workspaceblobstore/paths/example-data/
environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
compute: azureml:cpu-cluster

```

## YAML: URI file input

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: |
  echo "--iris-csv: ${{inputs.iris_csv}}"
  python hello-iris.py --iris-csv ${{inputs.iris_csv}}
code: src
inputs:
  iris_csv:
    type: uri_file 
    path: https://azuremlexamples.blob.core.windows.net/datasets/iris.csv
environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
compute: azureml:cpu-cluster

```

## YAML: URI folder input

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: |
  ls ${{inputs.data_dir}}
  echo "--iris-csv: ${{inputs.data_dir}}/iris.csv"
  python hello-iris.py --iris-csv ${{inputs.data_dir}}/iris.csv
code: src
inputs:
  data_dir:
    type: uri_folder 
    path: wasbs://datasets@azuremlexamples.blob.core.windows.net/
environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
compute: azureml:cpu-cluster

```

## YAML: Notebook via papermill

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: |
  pip install ipykernel papermill
  papermill hello-notebook.ipynb outputs/out.ipynb -k python
code: src
environment:
  image: library/python:latest
compute: azureml:cpu-cluster

```

## YAML: basic Python model training

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
code: src
command: >-
  python main.py 
  --iris-csv ${{inputs.iris_csv}}
  --C ${{inputs.C}}
  --kernel ${{inputs.kernel}}
  --coef0 ${{inputs.coef0}}
inputs:
  iris_csv: 
    type: uri_file
    path: wasbs://datasets@azuremlexamples.blob.core.windows.net/iris.csv
  C: 0.8
  kernel: "rbf"
  coef0: 0.1
environment: azureml:AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest
compute: azureml:cpu-cluster
display_name: sklearn-iris-example
experiment_name: sklearn-iris-example
description: Train a scikit-learn SVM on the Iris dataset.

```

## YAML: basic R model training with local Docker build context

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: >
  Rscript train.R 
  --data_folder ${{inputs.iris}}
code: src
inputs:
  iris: 
    type: uri_file
    path: https://azuremlexamples.blob.core.windows.net/datasets/iris.csv
environment:
  build:
    path: docker-context
compute: azureml:cpu-cluster
display_name: r-iris-example
experiment_name: r-iris-example
description: Train an R model on the Iris dataset.

```

## YAML: distributed PyTorch

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
code: src
command: >-
  python train.py 
  --epochs ${{inputs.epochs}}
  --learning-rate ${{inputs.learning_rate}}
  --data-dir ${{inputs.cifar}}
inputs:
  epochs: 1
  learning_rate: 0.2
  cifar: 
     type: uri_folder
     path: azureml:cifar-10-example@latest
environment: azureml:AzureML-pytorch-1.9-ubuntu18.04-py37-cuda11-gpu@latest
compute: azureml:gpu-cluster
distribution:
  type: pytorch 
  process_count_per_instance: 1
resources:
  instance_count: 2
display_name: pytorch-cifar-distributed-example
experiment_name: pytorch-cifar-distributed-example
description: Train a basic convolutional neural network (CNN) with PyTorch on the CIFAR-10 dataset, distributed via PyTorch.

```
