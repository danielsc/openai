    The environment is used to build the Docker image that the training job runs in on the compute cluster.

1. From your training code, use the [Azure Identity SDK](/python/api/overview/azure/identity-readme) and [Key Vault client library](/python/api/overview/azure/keyvault-secrets-readme) to get the managed identity credentials and authenticate to key vault:

    ```python
    from azure.identity import DefaultAzureCredential
    from azure.keyvault.secrets import SecretClient

    credential = DefaultAzureCredential()

    secret_client = SecretClient(vault_url="https://my-key-vault.vault.azure.net/", credential=credential)
    ```

1. After authenticating, use the Key Vault client library to retrieve a secret by providing the associated key:

    ```python
    secret = secret_client.get_secret("secret-name")
    print(secret.value)
    ```

## Next steps

For an example of submitting a training job using the Azure Machine Learning Python SDK v2, see [Train models with the Python SDK v2](how-to-train-sdk.md).
