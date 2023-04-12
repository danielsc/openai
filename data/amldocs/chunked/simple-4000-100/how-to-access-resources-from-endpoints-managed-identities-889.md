Then, get the Principal ID and Client ID of the User-assigned managed identity. To assign roles, we only need the Principal ID. However, we will use the Client ID to fill the `UAI_CLIENT_ID` placeholder environment variable before creating the deployment.

```python
uai_identity = msi_client.user_assigned_identities.get(
    resource_group_name=resource_group, resource_name=uai_name
)
uai_principal_id = uai_identity.principal_id
uai_client_id = uai_identity.client_id
```

Next, assign the `Storage Blob Data Reader` role to the endpoint. The Role Definition is retrieved by name and passed along with the Principal ID of the endpoint. The role is applied at the scope of the storage account created above to allow the endpoint to read the file. 

```python
role_name = "Storage Blob Data Reader"
scope = storage_account.id

role_defs = role_definition_client.role_definitions.list(scope=scope)
role_def = next((r for r in role_defs if r.role_name == role_name))

role_assignment_client.role_assignments.create(
    scope=scope,
    role_assignment_name=str(uuid.uuid4()),
    parameters=RoleAssignmentCreateParameters(
        role_definition_id=role_def.id,
        principal_id=uai_principal_id,
        principal_type="ServicePrincipal",
    ),
)
```

For the next two permissions, we'll need the workspace and container registry objects: 

```python
workspace = ml_client.workspaces.get(workspace_name)
container_registry = workspace.container_registry
```

Next, assign the `AcrPull` role to the User-assigned identity. This role allows images to be pulled from an Azure Container Registry. The scope is applied at the level of the container registry associated with the workspace.

```python
role_name = "AcrPull"
scope = container_registry

role_defs = role_definition_client.role_definitions.list(scope=scope)
role_def = next((r for r in role_defs if r.role_name == role_name))

role_assignment_client.role_assignments.create(
    scope=scope,
    role_assignment_name=str(uuid.uuid4()),
    parameters=RoleAssignmentCreateParameters(
        role_definition_id=role_def.id,
        principal_id=uai_principal_id,
        principal_type="ServicePrincipal",
    ),
)
```

Finally, assign the `Storage Blob Data Reader` role to the endpoint at the workspace storage account scope. This role assignment will allow the endpoint to read blobs in the workspace storage account as well as the newly created storage account.

The role has the same name and capabilities as the first role assigned above, however it is applied at a different scope and has a different ID. 

```python
role_name = "Storage Blob Data Reader"
scope = workspace.storage_account

role_defs = role_definition_client.role_definitions.list(scope=scope)
role_def = next((r for r in role_defs if r.role_name == role_name))

role_assignment_client.role_assignments.create(
    scope=scope,
    role_assignment_name=str(uuid.uuid4()),
    parameters=RoleAssignmentCreateParameters(
        role_definition_id=role_def.id,
        principal_id=uai_principal_id,
        principal_type="ServicePrincipal",
    ),
)
```


## Scoring script to access Azure resource

Refer to the following script to understand how to use your identity token to access Azure resources, in this scenario, the storage account created in previous sections. 

```python
import os
import logging
import json
import numpy
import joblib
import requests
from azure.identity import ManagedIdentityCredential
from azure.storage.blob import BlobClient


def access_blob_storage_sdk():
    credential = ManagedIdentityCredential(client_id=os.getenv("UAI_CLIENT_ID"))
    storage_account = os.getenv("STORAGE_ACCOUNT_NAME")
    storage_container = os.getenv("STORAGE_CONTAINER_NAME")
    file_name = os.getenv("FILE_NAME")

    blob_client = BlobClient(
        account_url=f"https://{storage_account}.blob.core.windows.net/",
        container_name=storage_container,
        blob_name=file_name,
        credential=credential,
    )
    blob_contents = blob_client.download_blob().content_as_text()
    logging.info(f"Blob contains: {blob_contents}")


def get_token_rest():
    """
    Retrieve an access token via REST.
    """

    access_token = None
    msi_endpoint = os.environ.get("MSI_ENDPOINT", None)
    msi_secret = os.environ.get("MSI_SECRET", None)

    # If UAI_CLIENT_ID is provided then assume that endpoint was created with user assigned identity,
    # # otherwise system assigned identity deployment.
    client_id = os.environ.get("UAI_CLIENT_ID", None)
    if client_id is not None:
        token_url = (
            msi_endpoint + f"?clientid={client_id}&resource=https://storage.azure.com/"
        )
    else:
        token_url = msi_endpoint + f"?resource=https://storage.azure.com/"

    logging.info("Trying to get identity token...")
    headers = {"secret": msi_secret, "Metadata": "true"}
    resp = requests.get(token_url, headers=headers)
    resp.raise_for_status()
    access_token = resp.json()["access_token"]
    logging.info("Retrieved token successfully.")
    return access_token


def access_blob_storage_rest():
    """
    Access a blob via REST.
    """

    logging.info("Trying to access blob storage...")
    storage_account = os.environ.get("STORAGE_ACCOUNT_NAME")
    storage_container = os.environ.get("STORAGE_CONTAINER_NAME")
    file_name = os.environ.get("FILE_NAME")
    logging.info(
        f"storage_account: {storage_account}, container: {storage_container}, filename: {file_name}"
    )
    token = get_token_rest()

    blob_url = f"https://{storage_account}.blob.core.windows.net/{storage_container}/{file_name}?api-version=2019-04-01"
    auth_headers = {
        "Authorization": f"Bearer {token}",
        "x-ms-blob-type": "BlockBlob",
        "x-ms-version": "2019-02-02",
    }
    resp = requests.get(blob_url, headers=auth_headers)
    resp.raise_for_status()
    logging.info(f"Blob contains: {resp.text}")


def init():
    global model
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
    # For multiple models, it points to the folder containing all deployed models (./azureml-models)
    # Please provide your model's folder name if there is one
    model_path = os.path.join(
        os.getenv("AZUREML_MODEL_DIR"), "model/sklearn_regression_model.pkl"
    )
    # deserialize the model file back into a sklearn model
    model = joblib.load(model_path)
    logging.info("Model loaded")

    # Access Azure resource (Blob storage) using system assigned identity token
    access_blob_storage_rest()
    access_blob_storage_sdk()

    logging.info("Init complete")


# note you can pass in multiple rows for scoring
def run(raw_data):
    logging.info("Request received")
    data = json.loads(raw_data)["data"]
    data = numpy.array(data)
    result = model.predict(data)
    logging.info("Request processed")
    return result.tolist()

```
