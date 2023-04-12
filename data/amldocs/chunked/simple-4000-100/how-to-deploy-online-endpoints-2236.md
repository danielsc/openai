

This example uses the [score.py file](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/model-1/onlinescoring/score.py):
__score.py__
```python
import os
import logging
import json
import numpy
import joblib


def init():
    """
    This function is called when the container is initialized/started, typically after create/update of the deployment.
    You can write the logic here to perform init operations like caching the model in memory
    """
    global model
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
    # Please provide your model's folder name if there is one
    model_path = os.path.join(
        os.getenv("AZUREML_MODEL_DIR"), "model/sklearn_regression_model.pkl"
    )
    # deserialize the model file back into a sklearn model
    model = joblib.load(model_path)
    logging.info("Init complete")


def run(raw_data):
    """
    This function is called for every invocation of the endpoint to perform the actual scoring/prediction.
    In the example we extract the data from the json input and call the scikit-learn model's predict()
    method and return the result back
    """
    logging.info("model 1: request received")
    data = json.loads(raw_data)["data"]
    data = numpy.array(data)
    result = model.predict(data)
    logging.info("Request processed")
    return result.tolist()

```

The `init()` function is called when the container is initialized or started. Initialization typically occurs shortly after the deployment is created or updated. Write logic here for global initialization operations like caching the model in memory (as we do in this example). The `run()` function is called for every invocation of the endpoint and should do the actual scoring and prediction. In the example, we extract the data from the JSON input, call the scikit-learn model's `predict()` method, and then return the result.

## Deploy and debug locally by using local endpoints

To save time debugging, we *highly recommend* that you test-run your endpoint locally. For more, see [Debug online endpoints locally in Visual Studio Code](how-to-debug-managed-online-endpoints-visual-studio-code.md).

> [!NOTE]
> * To deploy locally, [Docker Engine](https://docs.docker.com/engine/install/) must be installed.
> * Docker Engine must be running. Docker Engine typically starts when the computer starts. If it doesn't, you can [troubleshoot Docker Engine](https://docs.docker.com/config/daemon/#start-the-daemon-manually).

> [!IMPORTANT]
> The goal of a local endpoint deployment is to validate and debug your code and configuration before you deploy to Azure. Local deployment has the following limitations:
> - Local endpoints do *not* support traffic rules, authentication, or probe settings. 
> - Local endpoints support only one deployment per endpoint. 

> [!TIP]
> You can use [Azure Machine Learning inference HTTP server Python package](how-to-inference-server-http.md) to debug your scoring script locally **without Docker Engine**. Debugging with the inference server helps you to debug the scoring script before deploying to local endpoints so that you can debug without being affected by the deployment container configurations.

### Deploy the model locally

First create an endpoint. Optionally, for a local endpoint, you can skip this step and directly create the deployment (next step), which will, in turn, create the required metadata. Deploying models locally is useful for development and testing purposes.

# [Azure CLI](#tab/azure-cli)

```azurecli
set -e

# <set_endpoint_name> 
export ENDPOINT_NAME="<YOUR_ENDPOINT_NAME>"
# </set_endpoint_name>

export ENDPOINT_NAME=endpt-`echo $RANDOM`

# <create_endpoint>
az ml online-endpoint create --local -n $ENDPOINT_NAME -f endpoints/online/managed/sample/endpoint.yml
# </create_endpoint>

# <create_deployment>
az ml online-deployment create --local -n blue --endpoint $ENDPOINT_NAME -f endpoints/online/managed/sample/blue-deployment.yml
# </create_deployment>

# <get_status>
az ml online-endpoint show -n $ENDPOINT_NAME --local
# </get_status>

# check if create was successful
endpoint_status=`az ml online-endpoint show --local --name $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $endpoint_status
if [[ $endpoint_status == "Succeeded" ]]
then
  echo "Endpoint created successfully"
else
  echo "Endpoint creation failed"
  exit 1
fi

deploy_status=`az ml online-deployment show --local --name blue --endpoint $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $deploy_status
if [[ $deploy_status == "Succeeded" ]]
then
  echo "Deployment completed successfully"
else
  echo "Deployment failed"
  exit 1
fi

# <test_endpoint>
az ml online-endpoint invoke --local --name $ENDPOINT_NAME --request-file endpoints/online/model-1/sample-request.json
# </test_endpoint>

# <test_endpoint_using_curl>
SCORING_URI=$(az ml online-endpoint show --local -n $ENDPOINT_NAME -o tsv --query scoring_uri)

curl --request POST "$SCORING_URI" --header 'Content-Type: application/json' --data @endpoints/online/model-1/sample-request.json
# </test_endpoint_using_curl>

# <get_logs>
az ml online-deployment get-logs --local -n blue --endpoint $ENDPOINT_NAME
# </get_logs>

# <delete_endpoint>
az ml online-endpoint delete --local --name $ENDPOINT_NAME --yes
# </delete_endpoint>
```
