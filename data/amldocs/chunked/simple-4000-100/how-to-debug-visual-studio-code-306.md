
        > [!IMPORTANT]
        > If there are already other entries in the configurations section, add a comma (,) after the code that you inserted.

        > [!TIP]
        > The best practice, especially for pipelines is to keep the resources for scripts in separate directories so that code is relevant only for each of the steps. In this example the `localRoot` example value references `/code/step1`.
        >
        > If you are debugging multiple scripts, in different directories, create a separate configuration section for each script.

    1. Save the __launch.json__ file.

### Connect the debugger

1. Open VS Code and open a local copy of the script.
2. Set breakpoints where you want the script to stop once you've attached.
3. While the child process is running the script, and the `Timeout for debug connection` is displayed in the logs, use the F5 key or select __Debug__. When prompted, select the __Azure Machine Learning Compute: remote debug__ configuration. You can also select the debug icon from the side bar, the __Azure Machine Learning: remote debug__ entry from the Debug dropdown menu, and then use the green arrow to attach the debugger.

    At this point, VS Code connects to debugpy on the compute node and stops at the breakpoint you set previously. You can now step through the code as it runs, view variables, etc.

    > [!NOTE]
    > If the log displays an entry stating `Debugger attached = False`, then the timeout has expired and the script continued without the debugger. Submit the pipeline again and connect the debugger after the `Timeout for debug connection` message, and before the timeout expires.

## Debug and troubleshoot deployments

In some cases, you may need to interactively debug the Python code contained in your model deployment. For example, if the entry script is failing and the reason can't be determined by extra logging. By using VS Code and the debugpy, you can attach to the code running inside the Docker container.

> [!TIP]
> Save time and catch bugs early by debugging managed online endpoints and deployments locally. For more information, see [Debug managed online endpoints locally in Visual Studio Code (preview)](how-to-debug-managed-online-endpoints-visual-studio-code.md).

> [!IMPORTANT]
> This method of debugging does not work when using `Model.deploy()` and `LocalWebservice.deploy_configuration` to deploy a model locally. Instead, you must create an image using the [Model.package()](/python/api/azureml-core/azureml.core.model.model#package-workspace--models--inference-config-none--generate-dockerfile-false-) method.

Local web service deployments require a working Docker installation on your local system. For more information on using Docker, see the [Docker Documentation](https://docs.docker.com/). When working with compute instances, Docker is already installed.

### Configure development environment

1. To install debugpy on your local VS Code development environment, use the following command:

    ```bash
    python -m pip install --upgrade debugpy
    ```

    For more information on using debugpy with VS Code, see [Remote Debugging](https://code.visualstudio.com/docs/python/debugging#_debugging-by-attaching-over-a-network-connection).

1. To configure VS Code to communicate with the Docker image, create a new debug configuration:

    1. From VS Code, select the __Debug__ menu in the __Run__ extention and then select __Open configurations__. A file named __launch.json__ opens.

    1. In the __launch.json__ file, find the __"configurations"__ item (the line that contains `"configurations": [`), and insert the following text after it. 

        ```json
        {
            "name": "Azure Machine Learning Deployment: Docker Debug",
            "type": "python",
            "request": "attach",
            "connect": {
                "port": 5678,
                "host": "0.0.0.0",
            },
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}",
                    "remoteRoot": "/var/azureml-app"
                }
            ]
        }
        ```
