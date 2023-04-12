| Name              | Route                       |
| ----------------- | --------------------------- |
| Liveness Probe    | 127.0.0.1:5001/             |
| Score             | 127.0.0.1:5001/score        |
| OpenAPI (swagger) | 127.0.0.1:5001/swagger.json |

## Server parameters

The following table contains the parameters accepted by the server:

| Parameter                       | Required | Default | Description                                                                                                        |
| ------------------------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------ |
| entry_script                    | True     | N/A     | The relative or absolute path to the scoring script.                                                               |
| model_dir                       | False    | N/A     | The relative or absolute path to the directory holding the model used for inferencing.                             |
| port                            | False    | 5001    | The serving port of the server.                                                                                    |
| worker_count                    | False    | 1       | The number of worker threads that will process concurrent requests.                                                |
| appinsights_instrumentation_key | False    | N/A     | The instrumentation key to the application insights where the logs will be published.                              |
| access_control_allow_origins    | False    | N/A     | Enable CORS for the specified origins. Separate multiple origins with ",". <br> Example: "microsoft.com, bing.com" |

> [!TIP]
> CORS (Cross-origin resource sharing) is a way to allow resources on a webpage to be requested from another domain. CORS works via HTTP headers sent with the client request and returned with the service response. For more information on CORS and valid headers, see [Cross-origin resource sharing](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) in Wikipedia. See [here](v1/how-to-deploy-advanced-entry-script.md#cross-origin-resource-sharing-cors) for an example of the scoring script.

## Request flow

The following steps explain how the Azure Machine Learning inference HTTP server (azmlinfsrv) handles incoming requests:

1. A Python CLI wrapper sits around the server's network stack and is used to start the server.
1. A client sends a request to the server.
1. When a request is received, it goes through the [WSGI](https://www.fullstackpython.com/wsgi-servers.html) server and is then dispatched to one of the workers.
    - [Gunicorn](https://docs.gunicorn.org/) is used on __Linux__.
    - [Waitress](https://docs.pylonsproject.org/projects/waitress/) is used on __Windows__.
1. The requests are then handled by a [Flask](https://flask.palletsprojects.com/) app, which loads the entry script & any dependencies.
1. Finally, the request is sent to your entry script. The entry script then makes an inference call to the loaded model and returns a response.

:::image type="content" source="./media/how-to-inference-server-http/inference-server-architecture.png" alt-text="Diagram of the HTTP server process.":::

## Understanding logs

Here we describe logs of the AzureML Inference HTTP Server. You can get the log when you run the `azureml-inference-server-http` locally, or [get container logs](how-to-troubleshoot-online-endpoints.md#get-container-logs) if you're using online endpoints. 

> [!NOTE]
> The logging format has changed since version 0.8.0. If you find your log in different style, update the `azureml-inference-server-http` package to the latest version.

> [!TIP]
> If you are using online endpoints, the log from the inference server starts with `Azure ML Inferencing HTTP server <version>`.

### Startup logs

When the server is started, the server settings are first displayed by the logs as follows:
