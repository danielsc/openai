    Is server ready - True
    Is model ready - True
    /azureml-examples/cli/endpoints/online/triton/single-model/densenet_labels.txt
    84 : PEACOCK
    ```

# [Python](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

1. To get the endpoint scoring uri, use the following command:

    ```python 
    endpoint = ml_client.online_endpoints.get(endpoint_name)
    scoring_uri = endpoint.scoring_uri
    ```

1. To get an authentication key, use the following command:
    keys = ml_client.online_endpoints.list_keys(endpoint_name)
    auth_key = keys.primary_key

1. The following scoring code uses the [Triton Inference Server Client](https://github.com/triton-inference-server/client) to submit the image of a peacock to the endpoint. This script is available in the companion notebook to this example - [Deploy a model to online endpoints using Triton](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/triton/single-model/online-endpoints-triton.ipynb).

    ```python
    # Test the blue deployment with some sample data
    import requests
    import gevent.ssl
    import numpy as np
    import tritonclient.http as tritonhttpclient
    from pathlib import Path
    import prepost

    img_uri = "http://aka.ms/peacock-pic"

    # We remove the scheme from the url
    url = scoring_uri[8:]

    # Initialize client handler
    triton_client = tritonhttpclient.InferenceServerClient(
        url=url,
        ssl=True,
        ssl_context_factory=gevent.ssl._create_default_https_context,
    )

    # Create headers
    headers = {}
    headers["Authorization"] = f"Bearer {auth_key}"

    # Check status of triton server
    health_ctx = triton_client.is_server_ready(headers=headers)
    print("Is server ready - {}".format(health_ctx))

    # Check status of model
    model_name = "model_1"
    status_ctx = triton_client.is_model_ready(model_name, "1", headers)
    print("Is model ready - {}".format(status_ctx))

    if Path(img_uri).exists():
        img_content = open(img_uri, "rb").read()
    else:
        agent = f"Python Requests/{requests.__version__} (https://github.com/Azure/azureml-examples)"
        img_content = requests.get(img_uri, headers={"User-Agent": agent}).content

    img_data = prepost.preprocess(img_content)

    # Populate inputs and outputs
    input = tritonhttpclient.InferInput("data_0", img_data.shape, "FP32")
    input.set_data_from_numpy(img_data)
    inputs = [input]
    output = tritonhttpclient.InferRequestedOutput("fc6_1")
    outputs = [output]

    result = triton_client.infer(model_name, inputs, outputs=outputs, headers=headers)
    max_label = np.argmax(result.as_numpy("fc6_1"))
    label_name = prepost.postprocess(max_label)
    print(label_name)
    ``` 

1. The response from the script is similar to the following text:

    ```
    Is server ready - True
    Is model ready - True
    /azureml-examples/sdk/endpoints/online/triton/single-model/densenet_labels.txt
    84 : PEACOCK
    ```

# [Studio](#tab/azure-studio)

Azure Machine Learning studio provides the ability to test endpoints with JSON. However, serialized JSON is not currently included for this example. 

To test an endpoint using Azure Machine Learning studio, click `Test` from the Endpoint page. 


### Delete the endpoint and model
# [Azure CLI](#tab/azure-cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

1. Once you're done with the endpoint, use the following command to delete it:

```azurecli
set -e

BASE_PATH=endpoints/online/triton/single-model

# <installing-requirements>
pip install numpy
pip install tritonclient[http]
pip install pillow
pip install gevent
# </installing-requirements>

# <set_endpoint_name>
export ENDPOINT_NAME=triton-single-endpt-`echo $RANDOM`
# </set_endpoint_name>

# <create_endpoint>
az ml online-endpoint create -n $ENDPOINT_NAME -f $BASE_PATH/create-managed-endpoint.yaml
# </create_endpoint>

# <create_deployment>
az ml online-deployment create --name blue --endpoint $ENDPOINT_NAME -f $BASE_PATH/create-managed-deployment.yaml --all-traffic
# </create_deployment>

# <get_status>
az ml online-endpoint show -n $ENDPOINT_NAME
# </get_status>

# check if create was successful
endpoint_status=`az ml online-endpoint show --name $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $endpoint_status
if [[ $endpoint_status == "Succeeded" ]]
then
  echo "Endpoint created successfully"
else
  echo "Endpoint creation failed"
  exit 1
fi

deploy_status=`az ml online-deployment show --name blue --endpoint $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $deploy_status
if [[ $deploy_status == "Succeeded" ]]
then
  echo "Deployment completed successfully"
else
  echo "Deployment failed"
  exit 1
fi

# <get_scoring_uri>
scoring_uri=$(az ml online-endpoint show -n $ENDPOINT_NAME --query scoring_uri -o tsv)
scoring_uri=${scoring_uri%/*}
# </get_scoring_uri>

# <get_token>
auth_token=$(az ml online-endpoint get-credentials -n $ENDPOINT_NAME --query accessToken -o tsv)
# </get_token>

# <check_scoring_of_model>
python $BASE_PATH/triton_densenet_scoring.py --base_url=$scoring_uri --token=$auth_token --image_path $BASE_PATH/data/peacock.jpg
# </check_scoring_of_model>

# <delete_endpoint>
az ml online-endpoint delete -n $ENDPOINT_NAME --yes
# </delete_endpoint>


```
