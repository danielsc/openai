
# Debugging scoring script with Azure Machine Learning inference HTTP server (preview)

The Azure Machine Learning inference HTTP server [(preview)](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) is a Python package that exposes your scoring function as an HTTP endpoint and wraps the Flask server code and dependencies into a singular package. It's included in the [prebuilt Docker images for inference](concept-prebuilt-docker-images-inference.md) that are used when deploying a model with Azure Machine Learning. Using the package alone, you can deploy the model locally for production, and you can also easily validate your scoring (entry) script in a local development environment. If there's a problem with the scoring script, the server will return an error and the location where the error occurred.

The server can also be used to create validation gates in a continuous integration and deployment pipeline. For example, you can start the server with the candidate script and run the test suite against the local endpoint.

This article mainly targets users who want to use the inference server to debug locally, but it will also help you understand how to use the inference server with online endpoints.

## Online endpoint local debugging

Debugging endpoints locally before deploying them to the cloud can help you catch errors in your code and configuration earlier. To debug endpoints locally, you could use:

- the Azure Machine Learning inference HTTP server
- a [local endpoint](how-to-debug-managed-online-endpoints-visual-studio-code.md)

This article focuses on the Azure Machine Learning inference HTTP server.

The following table provides an overview of scenarios to help you choose what works best for you.

| Scenario                                                                | Inference HTTP Server | Local endpoint |
| ----------------------------------------------------------------------- | --------------------- | -------------- |
| Update local Python environment **without** Docker image rebuild        | Yes                   | No             |
| Update scoring script                                                   | Yes                   | Yes            |
| Update deployment configurations (deployment, environment, code, model) | No                    | Yes            |
| Integrate VS Code Debugger                                              | Yes                   | Yes            |

By running the inference HTTP server locally, you can focus on debugging your scoring script without being affected by the deployment container configurations.

## Prerequisites

- Requires: Python >=3.7
- Anaconda

> [!TIP]
> The Azure Machine Learning inference HTTP server runs on Windows and Linux based operating systems.

## Installation

> [!NOTE]
> To avoid package conflicts, install the server in a virtual environment.

To install the `azureml-inference-server-http package`, run the following command in your cmd/terminal:

```bash
python -m pip install azureml-inference-server-http
```

## Debug your scoring script locally

To debug your scoring script locally, you can test how the server behaves with a dummy scoring script, use VS Code to debug with the [azureml-inference-server-http](https://pypi.org/project/azureml-inference-server-http/) package, or test the server with an actual scoring script, model file, and environment file from our [examples repo](https://github.com/Azure/azureml-examples).

### Test the server behavior with a dummy scoring script
1. Create a directory to hold your files:

    ```bash
    mkdir server_quickstart
    cd server_quickstart
    ```

1. To avoid package conflicts, create a virtual environment and activate it:

    ```bash
    python -m venv myenv
    source myenv/bin/activate
    ```

    > [!TIP]
    > After testing, run `deactivate` to deactivate the Python virtual environment.

1. Install the `azureml-inference-server-http` package from the [pypi](https://pypi.org/project/azureml-inference-server-http/) feed:
