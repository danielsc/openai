
# [System-assigned (Python)](#tab/system-identity-python)

* To use Azure Machine Learning, you must have an Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/) today.

* Install and configure the Azure ML Python SDK (v2). For more information, see [Install and set up SDK (v2)](https://aka.ms/sdk-v2-install).

* An Azure Resource group, in which you (or the service principal you use) need to have `User Access Administrator` and  `Contributor` access. You'll have such a resource group if you configured your ML extension per the above article.

* An Azure Machine Learning workspace. You'll have a workspace if you configured your ML extension per the above article.

* A trained machine learning model ready for scoring and deployment. If you are following along with the sample, a model is provided.

* Clone the samples repository. 

    ```azurecli
    git clone https://github.com/Azure/azureml-examples --depth 1
    cd azureml-examples/sdk/endpoints/online/managed/managed-identities
    ```
* To follow along with this notebook, access the companion [example notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/managed/managed-identities/online-endpoints-managed-identity-uai.ipynb) within in the  `sdk/endpoints/online/managed/managed-identities` directory. 

* Additional Python packages are required for this example: 

    * Microsoft Azure Storage Management Client 

    * Microsoft Azure Authorization Management Client

    Install them with the following code: 
    
```python
%pip install --pre azure-mgmt-storage
%pip install --pre azure-mgmt-authorization
```

# [User-assigned (Python)](#tab/user-identity-python)

* To use Azure Machine Learning, you must have an Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/) today.

* Role creation permissions for your subscription or the Azure resources accessed by the User-assigned identity. 

* Install and configure the Azure ML Python SDK (v2). For more information, see [Install and set up SDK (v2)](https://aka.ms/sdk-v2-install).

* An Azure Resource group, in which you (or the service principal you use) need to have `User Access Administrator` and  `Contributor` access. You'll have such a resource group if you configured your ML extension per the above article.

* An Azure Machine Learning workspace. You'll have a workspace if you configured your ML extension per the above article.

* A trained machine learning model ready for scoring and deployment. If you are following along with the sample, a model is provided.

* Clone the samples repository. 

    ```azurecli
    git clone https://github.com/Azure/azureml-examples --depth 1
    cd azureml-examples/sdk/endpoints/online/managed/managed-identities
    ```
* To follow along with this notebook, access the companion [example notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/managed/managed-identities/online-endpoints-managed-identity-uai.ipynb) within in the  `sdk/endpoints/online/managed/managed-identities` directory. 

* Additional Python packages are required for this example: 

    * Microsoft Azure Msi Management Client 

    * Microsoft Azure Storage Client

    * Microsoft Azure Authorization Management Client

    Install them with the following code: 
    
```python
%pip install --pre azure-mgmt-msi
%pip install --pre azure-mgmt-storage
%pip install --pre azure-mgmt-authorization
```
    

## Limitations

* The identity for an endpoint is immutable. During endpoint creation, you can associate it with a system-assigned identity (default) or a user-assigned identity. You can't change the identity after the endpoint has been created.

## Configure variables for deployment

Configure the variable names for the workspace, workspace location, and the endpoint you want to create for use with your deployment.
