        After insertion, the __launch.json__ file should be similar to the following:
        ```json
        {
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/linkid=830387
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal"
            },
            {
                "name": "Azure Machine Learning Deployment: Docker Debug",
                "type": "python",
                "request": "attach",
                "connect": {
                    "port": 5678,
                    "host": "0.0.0.0"
                    },
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "/var/azureml-app"
                    }
                ]
            }
            ]
        }
        ```

        > [!IMPORTANT]
        > If there are already other entries in the configurations section, add a comma ( __,__ ) after the code that you inserted.

        This section attaches to the Docker container using port __5678__.

    1. Save the __launch.json__ file.

### Create an image that includes debugpy

1. Modify the conda environment for your deployment so that it includes debugpy. The following example demonstrates adding it using the `pip_packages` parameter:

    ```python
    from azureml.core.conda_dependencies import CondaDependencies 


    # Usually a good idea to choose specific version numbers
    # so training is made on same packages as scoring
    myenv = CondaDependencies.create(conda_packages=['numpy==1.15.4',
                                'scikit-learn==0.19.1', 'pandas==0.23.4'],
                                 pip_packages = ['azureml-defaults==1.0.83', 'debugpy'])

    with open("myenv.yml","w") as f:
        f.write(myenv.serialize_to_string())
    ```

1. To start debugpy and wait for a connection when the service starts, add the following to the top of your `score.py` file:

    ```python
    import debugpy
    # Allows other computers to attach to debugpy on this IP address and port.
    debugpy.listen(('0.0.0.0', 5678))
    # Wait 30 seconds for a debugger to attach. If none attaches, the script continues as normal.
    debugpy.wait_for_client()
    print("Debugger attached...")
    ```

1. Create an image based on the environment definition and pull the image to the local registry. 

    > [!NOTE]
    > This example assumes that `ws` points to your Azure Machine Learning workspace, and that `model` is the model being deployed. The `myenv.yml` file contains the conda dependencies created in step 1.

    ```python
    from azureml.core.conda_dependencies import CondaDependencies
    from azureml.core.model import InferenceConfig
    from azureml.core.environment import Environment


    myenv = Environment.from_conda_specification(name="env", file_path="myenv.yml")
    myenv.docker.base_image = None
    myenv.docker.base_dockerfile = "FROM mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:20210615.v1"
    inference_config = InferenceConfig(entry_script="score.py", environment=myenv)
    package = Model.package(ws, [model], inference_config)
    package.wait_for_creation(show_output=True)  # Or show_output=False to hide the Docker build logs.
    package.pull()
    ```

    Once the image has been created and downloaded (this process may take more than 10 minutes), the image path (includes repository, name, and tag, which in this case is also its digest) is finally displayed in a message similar to the following:

    ```text
    Status: Downloaded newer image for myregistry.azurecr.io/package@sha256:<image-digest>
    ```

1. To make it easier to work with the image locally, you can use the following command to add a tag for this image. Replace `myimagepath` in the following command with the location value from the previous step.
