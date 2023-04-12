
1. Create a conda environment for the Azure Machine Learning SDK:

    ```bash
    conda create -n py310 python=310
    ```

1. Once the environment has been created, activate it and install the SDK

    ```bash
    conda activate py310
    pip install azure-ai-ml
    ``` 

1. To configure the Data Science VM to use your Azure Machine Learning workspace, [create a workspace configuration file](#local-and-dsvm-only-create-a-workspace-configuration-file) or use an existing one.

    > [!TIP]
    > Similar to local environments, you can use Visual Studio Code and the [Azure Machine Learning Visual Studio Code extension](#visual-studio-code) to interact with Azure Machine Learning.
    >
    > For more information, see [Data Science Virtual Machines](https://azure.microsoft.com/services/virtual-machines/data-science-virtual-machines/).


## Next steps

- [Train and deploy a model](tutorial-train-deploy-notebook.md) on Azure Machine Learning with the MNIST dataset.
- See the [Azure Machine Learning SDK for Python reference](https://aka.ms/sdk-v2-install). 
