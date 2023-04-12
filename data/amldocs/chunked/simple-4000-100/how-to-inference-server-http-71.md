1. Install the `azureml-inference-server-http` package from the [pypi](https://pypi.org/project/azureml-inference-server-http/) feed:

    ```bash
    python -m pip install azureml-inference-server-http
    ```

1. Create your entry script (`score.py`). The following example creates a basic entry script:

    ```bash
    echo '
    import time

    def init():
        time.sleep(1)

    def run(input_data):
        return {"message":"Hello, World!"}
    ' > score.py
    ```

1. Start the server (azmlinfsrv) and set `score.py` as the entry script:

    ```bash
    azmlinfsrv --entry_script score.py
    ```

    > [!NOTE]
    > The server is hosted on 0.0.0.0, which means it will listen to all IP addresses of the hosting machine.

1. Send a scoring request to the server using `curl`:

    ```bash
    curl -p 127.0.0.1:5001/score
    ```

    The server should respond like this.

    ```bash
    {"message": "Hello, World!"}
    ```

After testing, you can press `Ctrl + C` to terminate the server. 
Now you can modify the scoring script (`score.py`) and test your changes by running the server again (`azmlinfsrv --entry_script score.py`).

### How to integrate with Visual Studio Code

There are two ways to use Visual Studio Code (VS Code) and [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) to debug with [azureml-inference-server-http](https://pypi.org/project/azureml-inference-server-http/) package ([Launch and Attach modes](https://code.visualstudio.com/docs/editor/debugging#_launch-versus-attach-configurations)). 

-  **Launch mode**: set up the `launch.json` in VS Code and start the AzureML Inference HTTP Server within VS Code.
   1. Start VS Code and open the folder containing the script (`score.py`).
   1. Add the following configuration to `launch.json` for that workspace in VS Code:

        **launch.json**
        ```json
        {
            "version": "0.2.0",
            "configurations": [
                {
                    "name": "Debug score.py",
                    "type": "python",
                    "request": "launch",
                    "module": "azureml_inference_server_http.amlserver",
                    "args": [
                        "--entry_script",
                        "score.py"
                    ]
                }
            ]
        }
        ```

    1. Start debugging session in VS Code. Select "Run" -> "Start Debugging" (or `F5`).

-  **Attach mode**: start the AzureML Inference HTTP Server in a command line and use VS Code + Python Extension to attach to the process.
    > [!NOTE]
    > If you're using Linux environment, first install the `gdb` package by running `sudo apt-get install -y gdb`.
   1. Add the following configuration to `launch.json` for that workspace in VS Code:
        
        **launch.json**
        ```json
        {
            "version": "0.2.0",
            "configurations": [
                {
                    "name": "Python: Attach using Process Id",
                    "type": "python",
                    "request": "attach",
                    "processId": "${command:pickProcess}",
                    "justMyCode": true
                },
            ]
        }
        ```
   1. Start the inference server using CLI (`azmlinfsrv --entry_script score.py`).
   1. Start debugging session in VS Code.
      1. In VS Code, select "Run" -> "Start Debugging" (or `F5`).
      1. Enter the process ID of the `azmlinfsrv` (not the `gunicorn`) using the logs (from the inference server) displayed in the CLI.
        :::image type="content" source="./media/how-to-inference-server-http/debug-attach-pid.png" alt-text="Screenshot of the CLI which shows the process ID of the server.":::
        > [!NOTE]
        > If the process picker does not display, manually enter the process ID in the `processId` field of the `launch.json`.

In both ways, you can set [breakpoint](https://code.visualstudio.com/docs/editor/debugging#_breakpoints) and debug step by step.
