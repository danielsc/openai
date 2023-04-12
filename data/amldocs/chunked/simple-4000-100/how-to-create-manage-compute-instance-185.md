Activity on custom applications installed on the compute instance isn't considered. There are also some basic bounds around inactivity time periods; compute instance must be inactive for a minimum of 15 mins and a maximum of three days. 

Also, if a compute instance has already been idle for a certain amount of time, if idle shutdown settings are updated to  an amount of time shorter than the current idle duration, the idle time clock will be reset to 0. For example, if the compute instance has already been idle for 20 minutes, and the shutdown settings are updated to 15 minutes, the idle time clock will be reset to 0.

Use **Manage preview features** to access this feature.

1. In the workspace toolbar, select the **Manage preview features** image.
1. Scroll down until you see **Configure auto-shutdown for idle compute instances**.
1. Toggle the switch to enable the feature.

:::image type="content" source="media/how-to-create-manage-compute-instance/enable-preview.png" alt-text="Screenshot: Enable auto-shutdown.":::

Once enabled, the setting can be configured during compute instance creation or for existing compute instances via the following interfaces:

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

When creating a new compute instance, add the `idle_time_before_shutdown_minutes` parameter.

```Python
# Note that idle_time_before_shutdown has been deprecated.
ComputeInstance(name=ci_basic_name, size="STANDARD_DS3_v2", idle_time_before_shutdown_minutes="30")
```

You cannot change the idle time of an existing compute instance with the Python SDK.

# [Azure CLI](#tab/azure-cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

When creating a new compute instance, add `idle_time_before_shutdown_minutes` to the YAML definition.

```YAML
# Note that this is just a snippet for the idle shutdown property. Refer to the "Create" Azure CLI section for more information.
# Note that idle_time_before_shutdown has been deprecated.
idle_time_before_shutdown_minutes: 30
```

You cannot change the idle time of an existing compute instance with the CLI.

# [Studio](#tab/azure-studio)

* When creating a new compute instance:

    1. Select **Advanced** after completing required settings.  
    1. Select **Enable idle shutdown**

        :::image type="content" source="media/how-to-create-manage-compute-instance/enable-idle-shutdown.png" alt-text="Screenshot: Enable compute instance idle shutdown." lightbox="media/how-to-create-manage-compute-instance/enable-idle-shutdown.png":::

    1. Specify the shutdown period.

* For an existing compute instance:

    1. In the left navigation bar, select **Compute**
    1. In the list, select the compute instance you wish to change
    1. Select the **Edit** pencil in the **Schedules** section.

        :::image type="content" source="media/how-to-create-manage-compute-instance/edit-idle-time.png" alt-text="Screenshot: Edit idle time for a compute instance." lightbox="media/how-to-create-manage-compute-instance/edit-idle-time.png":::


You can also change the idle time using:

* REST API

    Endpoint:
    ```
    POST https://management.azure.com/subscriptions/{SUB_ID}/resourceGroups/{RG_NAME}/providers/Microsoft.MachineLearningServices/workspaces/{WS_NAME}/computes/{CI_NAME}/updateIdleShutdownSetting?api-version=2021-07-01
    ```

    Body:
    ```JSON
    {
        "idleTimeBeforeShutdown": "PT30M" // this must be a string in ISO 8601 format
    }
    ```


* ARM Templates: only configurable during new compute instance creation

    ```JSON
    // Note that this is just a snippet for the idle shutdown property in an ARM template
    {
        "idleTimeBeforeShutdown":"PT30M" // this must be a string in ISO 8601 format
    }
    ```

### Azure policy support
Administrators can use a built-in [Azure Policy](./../governance/policy/overview.md) definition to enforce auto-stop on all compute instances in a given subscription/resource-group. 
