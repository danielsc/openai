Or use the following examples to create a compute instance with more options:

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
# Compute Instances need to have a unique name across the region.
# Here we create a unique name with current datetime
from azure.ai.ml.entities import ComputeInstance, AmlCompute
import datetime

ci_basic_name = "basic-ci" + datetime.datetime.now().strftime("%Y%m%d%H%M")
ci_basic = ComputeInstance(name=ci_basic_name, size="STANDARD_DS3_v2")
ml_client.begin_create_or_update(ci_basic).result()
```

For more information on the classes, methods, and parameters used in this example, see the following reference documents:

* [`AmlCompute` class](/python/api/azure-ai-ml/azure.ai.ml.entities.amlcompute)
* [`ComputeInstance` class](/python/api/azure-ai-ml/azure.ai.ml.entities.computeinstance)

# [Azure CLI](#tab/azure-cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```azurecli
az ml compute create -f create-instance.yml
```

Where the file *create-instance.yml* is:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/computeInstance.schema.json 
name: basic-example-i
type: computeinstance
size: STANDARD_DS3_v2

```


# [Studio](#tab/azure-studio)

1. Navigate to [Azure Machine Learning studio](https://ml.azure.com).
1. Under __Manage__, select __Compute__.
1. Select **Compute instance** at the top.
1. If you have no compute instances, select  **Create** in the middle of the page.
  
    :::image type="content" source="media/how-to-create-attach-studio/create-compute-target.png" alt-text="Create compute target":::

1. If you see a list of compute resources, select **+New** above the list.

    :::image type="content" source="media/how-to-create-attach-studio/select-new.png" alt-text="Select new":::
1. Fill out the form:

    |Field  |Description  |
    |---------|---------|
    |Compute name     |  <ul><li>Name is required and must be between 3 to 24 characters long.</li><li>Valid characters are upper and lower case letters, digits, and the  **-** character.</li><li>Name must start with a letter</li><li>Name needs to be unique across all existing computes within an Azure region. You'll see an alert if the name you choose isn't unique</li><li>If **-**  character is used, then it needs to be followed by at least one letter later in the name</li></ul>     |
    |Virtual machine type |  Choose CPU or GPU. This type can't be changed after creation     |
    |Virtual machine size     |  Supported virtual machine sizes might be restricted in your region. Check the [availability list](https://azure.microsoft.com/global-infrastructure/services/?products=virtual-machines)     |

1. Select **Create** unless you want to configure advanced settings for the compute instance.
1. <a name="advanced-settings"></a> Select **Next: Advanced Settings** if you want to:

    * Enable idle shutdown (preview). Configure a compute instance to automatically shut down if it's inactive. For more information, see [enable idle shutdown](#enable-idle-shutdown-preview).
    * Add schedule. Schedule times for the compute instance to automatically start and/or shut down. See [schedule details](#schedule-automatic-start-and-stop) below.
    * Enable SSH access.  Follow the [detailed SSH access instructions](#enable-ssh-access) below.
    * Enable virtual network. Specify the **Resource group**, **Virtual network**, and **Subnet** to create the compute instance inside an Azure Virtual Network (vnet). You can also select __No public IP__ to prevent the creation of a public IP address, which requires a private link workspace. You must also satisfy these [network requirements](./how-to-secure-training-vnet.md) for virtual network setup. 
    * Assign the computer to another user. For more about assigning to other users, see [Create on behalf of](#create-on-behalf-of-preview)
    * Provision with a setup script (preview) - for more information about how to create and use a setup script, see [Customize the compute instance with a script](how-to-customize-compute-instance.md).
