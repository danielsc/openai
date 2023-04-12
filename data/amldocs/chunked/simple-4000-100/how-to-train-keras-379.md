
You can then register this model.

```python
registered_model = ml_client.models.create_or_update(model=model)
```


## Deploy the model as an online endpoint

After you've registered your model, you can deploy it as an [online endpoint](concept-endpoints.md)—that is, as a web service in the Azure cloud.

To deploy a machine learning service, you'll typically need:
- The model assets that you want to deploy. These assets include the model's file and metadata that you already registered in your training job.
- Some code to run as a service. The code executes the model on a given input request (an entry script). This entry script receives data submitted to a deployed web service and passes it to the model. After the model processes the data, the script returns the model's response to the client. The script is specific to your model and must understand the data that the model expects and returns. When you use an MLFlow model, AzureML automatically creates this script for you.

For more information about deployment, see [Deploy and score a machine learning model with managed online endpoint using Python SDK v2](how-to-deploy-managed-online-endpoint-sdk-v2.md).

### Create a new online endpoint

As a first step to deploying your model, you need to create your online endpoint. The endpoint name must be unique in the entire Azure region. For this article, you'll create a unique name using a universally unique identifier (UUID).

```python
import uuid

# Creating a unique name for the endpoint
online_endpoint_name = "keras-dnn-endpoint-" + str(uuid.uuid4())[:8]
```

```python
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    Model,
    Environment,
)

# create an online endpoint
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="Classify handwritten digits using a deep neural network (DNN) using Keras",
    auth_mode="key",
)

endpoint = ml_client.begin_create_or_update(endpoint).result()

print(f"Endpint {endpoint.name} provisioning state: {endpoint.provisioning_state}")
```

Once you've created the endpoint, you can retrieve it as follows:

```python
endpoint = ml_client.online_endpoints.get(name=online_endpoint_name)

print(
    f'Endpint "{endpoint.name}" with provisioning state "{endpoint.provisioning_state}" is retrieved'
)
```

### Deploy the model to the endpoint

After you've created the endpoint, you can deploy the model with the entry script. An endpoint can have multiple deployments. Using rules, the endpoint can then direct traffic to these deployments.

In the following code, you'll create a single deployment that handles 100% of the incoming traffic. We've specified an arbitrary color name (*tff-blue*) for the deployment. You could also use any other name such as *tff-green* or *tff-red* for the deployment.
The code to deploy the model to the endpoint does the following:

- deploys the best version of the model that you registered earlier;
- scores the model, using the `score.py` file; and
- uses the custom environment (that you created earlier) to perform inferencing.

```python
from azure.ai.ml.entities import ManagedOnlineDeployment, CodeConfiguration

model = registered_model

# create an online deployment.
blue_deployment = ManagedOnlineDeployment(
    name="keras-blue-deployment",
    endpoint_name=online_endpoint_name,
    model=model,
    # code_configuration=CodeConfiguration(code="./src", scoring_script="score.py"),
    instance_type="Standard_DS3_v2",
    instance_count=1,
)

blue_deployment = ml_client.begin_create_or_update(blue_deployment).result()
```

> [!NOTE]
> Expect this deployment to take a bit of time to finish.

### Test the deployed model

Now that you've deployed the model to the endpoint, you can predict the output of the deployed model, using the `invoke` method on the endpoint. 

To test the endpoint you need some test data. Let us locally download the test data which we used in our training script.

```python
import urllib.request

data_folder = os.path.join(os.getcwd(), "data")
os.makedirs(data_folder, exist_ok=True)

urllib.request.urlretrieve(
    "https://azureopendatastorage.blob.core.windows.net/mnist/t10k-images-idx3-ubyte.gz",
    filename=os.path.join(data_folder, "t10k-images-idx3-ubyte.gz"),
)
urllib.request.urlretrieve(
    "https://azureopendatastorage.blob.core.windows.net/mnist/t10k-labels-idx1-ubyte.gz",
    filename=os.path.join(data_folder, "t10k-labels-idx1-ubyte.gz"),
)
```
