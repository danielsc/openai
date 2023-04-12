1. Keep all the defaults on the first page, select **Next**. If you don't see any available compute, you'll need to request a quota increase. Learn more about [managing and increasing quotas](how-to-manage-quotas.md).
1. Name the cluster **cpu-cluster**.  If this name already exists, add your initials to the name to make it unique.
1. Leave the **Minimum number of nodes** at 0.
1. Change the **Maximum number of nodes** to 4 if possible.  Depending on your settings, you may have a smaller limit.
1. Change the **Idle seconds before scale down** to 2400.
1. Leave the rest of the defaults, and select **Create**.

In less than a minute, the **State** of the cluster will change from *Creating* to *Succeeded*.  The list shows the provisioned compute cluster, along with the number of idle nodes, busy nodes, and unprovisioned nodes.  Since you haven't used the cluster yet, all the nodes are currently unprovisioned. 

> [!NOTE]
> When the cluster is created, it will have 0 nodes provisioned. The cluster *does not* incur costs until you submit a job. This cluster will scale down when it has been idle for 2,400 seconds (40 minutes).  This will give you time to use it in a few tutorials if you wish without waiting for it to scale back up.

## Quick tour of the studio

The studio is your web portal for Azure Machine Learning. This portal combines no-code and code-first experiences for an inclusive data science platform.

Review the parts of the studio on the left-hand navigation bar:

* The **Author** section of the studio contains multiple ways to get started in creating machine learning models.  You can:

    * **Notebooks** section allows you to create Jupyter Notebooks, copy sample notebooks, and run notebooks and Python scripts.
    * **Automated ML** steps you through creating a machine learning model without writing code.
    * **Designer** gives you a drag-and-drop way to build models using prebuilt components.

* The **Assets** section of the studio helps you keep track of the assets you create as you run your jobs.  If you have a new workspace, there's nothing in any of these sections yet.

* You already used the **Manage** section of the studio to create your compute resources.  This section also lets you create and manage  data and external services you link to your workspace.  

### Workspace diagnostics

[!INCLUDE [machine-learning-workspace-diagnostics](../../includes/machine-learning-workspace-diagnostics.md)]

## Clean up resources

If you plan to continue now to the next tutorial, skip to [Next steps](#next-steps).

### Stop compute instance

If you're not going to use it now, stop the compute instance:

1. In the studio, on the left, select **Compute**.
1. In the top tabs, select **Compute instances**
1. Select the compute instance in the list.
1. On the top toolbar, select **Stop**.

### Delete all resources

[!INCLUDE [aml-delete-resource-group](../../includes/aml-delete-resource-group.md)]

## Next steps

You now have an Azure Machine Learning workspace that contains:

- A compute instance to use for your development environment.
- A compute cluster to use for submitting training runs.

Use these resources to learn more about Azure Machine Learning and train a model with Python scripts.

> [!div class="nextstepaction"]
> [Quickstart: Run Jupyter notebook in Azure Machine Learning studio](quickstart-run-notebooks.md)
>
