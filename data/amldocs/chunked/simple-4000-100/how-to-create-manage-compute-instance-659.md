   * Specify **/home/azureuser/cloudfiles** for **Host path**.  
   * Specify **/home/azureuser/cloudfiles** for the **Container path**.
   * Select **Add** to add this mounting.  Because the files are mounted, changes you make to them will be available in other compute instances and applications.
1. Select **Create** to set up the custom application on your compute instance.

:::image type="content" source="media/how-to-create-manage-compute-instance/custom-service.png" alt-text="Screenshot show custom application settings." lightbox="media/how-to-create-manage-compute-instance/custom-service.png":::

[!INCLUDE [private link ports](../../includes/machine-learning-private-link-ports.md)]

### Accessing custom applications in studio

Access the custom applications that you set up in studio:

1. On the left, select **Compute**.
1. On the **Compute instance** tab, see your applications under the **Applications** column.

:::image type="content" source="media/how-to-create-manage-compute-instance/custom-service-access.png" alt-text="Screenshot shows studio access for your custom applications.":::
> [!NOTE]
> It might take a few minutes after setting up a custom application until you can access it via the links above. The amount of time taken will depend on the size of the image used for your custom application. If you see a 502 error message when trying to access the application, wait for some time for the application to be set up and try again.

## Manage

Start, stop, restart, and delete a compute instance. A compute instance doesn't automatically scale down, so make sure to stop the resource to prevent ongoing charges. Stopping a compute instance deallocates it. Then start it again when you need it. While stopping the compute instance stops the billing for compute hours, you'll still be billed for disk, public IP, and standard load balancer. 

You can [create a schedule](#schedule-automatic-start-and-stop) for the compute instance to automatically start and stop based on a time and day of week.

> [!TIP]
> The compute instance has 120GB OS disk. If you run out of disk space, [use the terminal](how-to-access-terminal.md) to clear at least 1-2 GB before you stop or restart the compute instance. Please do not stop the compute instance by issuing sudo shutdown from the terminal. The temp disk size on compute instance depends on the VM size chosen and is mounted on /mnt.

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]


In the examples below, the name of the compute instance is stored in the variable `ci_basic_name`.

* Get status

```python
from azure.ai.ml.entities import ComputeInstance, AmlCompute

# Get compute
ci_basic_state = ml_client.compute.get(ci_basic_name)
```


* Stop

```python
from azure.ai.ml.entities import ComputeInstance, AmlCompute

# Stop compute
ml_client.compute.begin_stop(ci_basic_name).wait()
```


* Start

```python
from azure.ai.ml.entities import ComputeInstance, AmlCompute

# Start compute
ml_client.compute.begin_start(ci_basic_name).wait()
```


* Restart

```python
from azure.ai.ml.entities import ComputeInstance, AmlCompute

# Restart compute
ml_client.compute.begin_restart(ci_basic_name).wait()
```


* Delete

```python
from azure.ai.ml.entities import ComputeInstance, AmlCompute

ml_client.compute.begin_delete(ci_basic_name).wait()
```


# [Azure CLI](#tab/azure-cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

In the examples below, the name of the compute instance is **instance**, in workspace **my-workspace**, in resource group **my-resource-group**.

* Stop

    ```azurecli
    az ml compute stop --name instance --resource-group my-resource-group --workspace-name my-workspace
    ```

* Start

    ```azurecli
    az ml compute start --name instance --resource-group my-resource-group --workspace-name my-workspace
    ```

* Restart

    ```azurecli
    az ml compute restart --name instance --resource-group my-resource-group --workspace-name my-workspace
    ```
