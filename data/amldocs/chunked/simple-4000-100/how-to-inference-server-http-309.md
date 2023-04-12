### Startup logs

When the server is started, the server settings are first displayed by the logs as follows:

```
Azure ML Inferencing HTTP server <version>


Server Settings
---------------
Entry Script Name: <entry_script>
Model Directory: <model_dir>
Worker Count: <worker_count>
Worker Timeout (seconds): None
Server Port: <port>
Application Insights Enabled: false
Application Insights Key: <appinsights_instrumentation_key>
Inferencing HTTP server version: azmlinfsrv/<version>
CORS for the specified origins: <access_control_allow_origins>


Server Routes
---------------
Liveness Probe: GET   127.0.0.1:<port>/
Score:          POST  127.0.0.1:<port>/score

<logs>
```

For example, when you launch the server followed the [end-to-end example](#end-to-end-example):

```
Azure ML Inferencing HTTP server v0.8.0


Server Settings
---------------
Entry Script Name: /home/user-name/azureml-examples/cli/endpoints/online/model-1/onlinescoring/score.py
Model Directory: ./
Worker Count: 1
Worker Timeout (seconds): None
Server Port: 5001
Application Insights Enabled: false
Application Insights Key: None
Inferencing HTTP server version: azmlinfsrv/0.8.0
CORS for the specified origins: None


Server Routes
---------------
Liveness Probe: GET   127.0.0.1:5001/
Score:          POST  127.0.0.1:5001/score

2022-12-24 07:37:53,318 I [32726] gunicorn.error - Starting gunicorn 20.1.0
2022-12-24 07:37:53,319 I [32726] gunicorn.error - Listening at: http://0.0.0.0:5001 (32726)
2022-12-24 07:37:53,319 I [32726] gunicorn.error - Using worker: sync
2022-12-24 07:37:53,322 I [32756] gunicorn.error - Booting worker with pid: 32756
Initializing logger
2022-12-24 07:37:53,779 I [32756] azmlinfsrv - Starting up app insights client
2022-12-24 07:37:54,518 I [32756] azmlinfsrv.user_script - Found user script at /home/user-name/azureml-examples/cli/endpoints/online/model-1/onlinescoring/score.py
2022-12-24 07:37:54,518 I [32756] azmlinfsrv.user_script - run() is not decorated. Server will invoke it with the input in JSON string.
2022-12-24 07:37:54,518 I [32756] azmlinfsrv.user_script - Invoking user's init function
2022-12-24 07:37:55,974 I [32756] azmlinfsrv.user_script - Users's init has completed successfully
2022-12-24 07:37:55,976 I [32756] azmlinfsrv.swagger - Swaggers are prepared for the following versions: [2, 3, 3.1].
2022-12-24 07:37:55,977 I [32756] azmlinfsrv - AML_FLASK_ONE_COMPATIBILITY is set, but patching is not necessary.
```


### Log format

The logs from the inference server are generated in the following format, except for the launcher scripts since they aren't part of the python package: 

`<UTC Time> | <level> [<pid>] <logger name> - <message>`

Here `<pid>` is the process ID and `<level>` is the first character of the [logging level](https://docs.python.org/3/library/logging.html#logging-levels) – E for ERROR, I for INFO, etc.  

There are six levels of logging in Python, with numbers associated with severity:

| Logging level | Numeric value |
| ------------- | ------------- |
| CRITICAL      | 50            |
| ERROR         | 40            |
| WARNING       | 30            |
| INFO          | 20            |
| DEBUG         | 10            |
| NOTSET        | 0             |

## Troubleshooting guide
In this section, we'll provide basic troubleshooting tips for Azure Machine Learning inference HTTP server. If you want to troubleshoot online endpoints, see also [Troubleshooting online endpoints deployment](how-to-troubleshoot-online-endpoints.md)

[!INCLUDE [inference server TSGs](../../includes/machine-learning-inference-server-troubleshooting.md)]

## Next steps

* For more information on creating an entry script and deploying models, see [How to deploy a model using Azure Machine Learning](how-to-deploy-online-endpoints.md).
* Learn about [Prebuilt docker images for inference](concept-prebuilt-docker-images-inference.md)
