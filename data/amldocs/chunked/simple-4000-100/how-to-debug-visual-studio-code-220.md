
### Configure ML pipeline

To provide the Python packages needed to start debugpy and get the run context, create an environment
and set `pip_packages=['debugpy', 'azureml-sdk==<SDK-VERSION>']`. Change the SDK version to match the one you're using. The following code snippet demonstrates how to create an environment:

```python
# Use a RunConfiguration to specify some additional requirements for this step.
from azureml.core.runconfig import RunConfiguration
from azureml.core.conda_dependencies import CondaDependencies
from azureml.core.runconfig import DEFAULT_CPU_IMAGE

# create a new runconfig object
run_config = RunConfiguration()

# enable Docker 
run_config.environment.docker.enabled = True

# set Docker base image to the default CPU-based image
run_config.environment.docker.base_image = DEFAULT_CPU_IMAGE

# use conda_dependencies.yml to create a conda environment in the Docker image for execution
run_config.environment.python.user_managed_dependencies = False

# specify CondaDependencies obj
run_config.environment.python.conda_dependencies = CondaDependencies.create(conda_packages=['scikit-learn'],
                                                                           pip_packages=['debugpy', 'azureml-sdk==<SDK-VERSION>'])
```

In the [Configure Python scripts](#configure-python-scripts) section, new arguments were added to the scripts used by your ML pipeline steps. The following code snippet demonstrates how to use these arguments to enable debugging for the component and set a timeout. It also demonstrates how to use the environment created earlier by setting `runconfig=run_config`:

```python
# Use RunConfig from a pipeline step
step1 = PythonScriptStep(name="train_step",
                         script_name="train.py",
                         arguments=['--remote_debug', '--remote_debug_connection_timeout', 300,'--remote_debug_client_ip','<VS-CODE-CLIENT-IP>','--remote_debug_port',5678],
                         compute_target=aml_compute,
                         source_directory=source_directory,
                         runconfig=run_config,
                         allow_reuse=False)
```

When the pipeline runs, each step creates a child run. If debugging is enabled, the modified script logs information similar to the following text in the `70_driver_log.txt` for the child run:

```text
Timeout for debug connection: 300
ip_address: 10.3.0.5
```

Save the `ip_address` value. It's used in the next section.

> [!TIP]
> You can also find the IP address from the run logs for the child run for this pipeline step. For more information on viewing this information, see [Monitor Azure ML experiment runs and metrics](how-to-log-view-metrics.md).

### Configure development environment

1. To install debugpy on your VS Code development environment, use the following command:

    ```bash
    python -m pip install --upgrade debugpy
    ```

    For more information on using debugpy with VS Code, see [Remote Debugging](https://code.visualstudio.com/docs/python/debugging#_debugging-by-attaching-over-a-network-connection).

1. To configure VS Code to communicate with the Azure Machine Learning compute that is running the debugger, create a new debug configuration:

    1. From VS Code, select the __Debug__ menu and then select __Open configurations__. A file named __launch.json__ opens.

    1. In the __launch.json__ file, find the line that contains `"configurations": [`, and insert the following text after it. Change the `"host": "<IP-ADDRESS>"` entry to the IP address returned in your logs from the previous section. Change the `"localRoot": "${workspaceFolder}/code/step"` entry to a local directory that contains a copy of the script being debugged:

        ```json
        {
            "name": "Azure Machine Learning Compute: remote debug",
            "type": "python",
            "request": "attach",
            "port": 5678,
            "host": "<IP-ADDRESS>",
            "redirectOutput": true,
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}/code/step1",
                    "remoteRoot": "."
                }
            ]
        }
        ```
