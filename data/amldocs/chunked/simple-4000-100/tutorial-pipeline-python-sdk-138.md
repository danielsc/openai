[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=conda.yml)]

The specification contains some usual packages, that you'll use in your pipeline (numpy, pip), together with some Azure ML specific packages (azureml-defaults, azureml-mlflow).

The Azure ML packages aren't mandatory to run Azure ML jobs. However, adding these packages will let you interact with Azure ML for logging metrics and registering models, all inside the Azure ML job. You'll use them in the training script later in this tutorial.

Use the *yaml* file to create and register this custom environment in your workspace:

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=custom_env_name)]

## Build the training pipeline

Now that you have all assets required to run your pipeline, it's time to build the pipeline itself, using the Azure ML Python SDK v2.

Azure ML pipelines are reusable ML workflows that usually consist of several components. The typical life of a component is:

* Write the yaml specification of the component, or create it programmatically using `ComponentMethod`.
* Optionally, register the component with a name and version in your workspace, to make it reusable and shareable.
* Load that component from the pipeline code.
* Implement the pipeline using the component's inputs, outputs and parameters
* Submit the pipeline.

## Create component 1: data prep (using programmatic definition)

Let's start by creating the first component. This component handles the preprocessing of the data. The preprocessing task is performed in the *data_prep.py* Python file.

First create a source folder for the data_prep component:

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=data_prep_src_dir)]

This script performs the simple task of splitting the data into train and test datasets. 
Azure ML mounts datasets as folders to the computes, therefore, we created an auxiliary `select_first_file` function to access the data file inside the mounted input folder.

[MLFlow](https://mlflow.org/docs/latest/tracking.html) will be used to log the parameters and metrics during our pipeline run.

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=def-main)]

Now that you have a script that can perform the desired task, create an Azure ML Component from it. 

You'll use the general purpose **CommandComponent** that can run command line actions. This command line action can directly call system commands or run a script. The inputs/outputs are specified on the command line via the `${{ ... }}` notation.

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=data_prep_component)]

Optionally, register the component in the workspace for future re-use.


## Create component 2: training (using yaml definition)

The second component that you'll create will consume the training and test data, train a tree based model and return the output model. You'll use Azure ML logging capabilities to record and visualize the learning progress.

You used the `CommandComponent` class to create your first component. This time you'll use the yaml definition to define the second component. Each method has its own advantages. A yaml definition can actually be checked-in along the code, and would provide a readable history tracking. The programmatic method using `CommandComponent` can be easier with built-in class documentation and code completion.


Create the directory for this component:

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=train_src_dir)]

Create the training script in the directory:

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=train.py)]

As you can see in this training script, once the model is trained, the model file is saved and registered to the workspace. Now you can use the registered model in inferencing endpoints.
