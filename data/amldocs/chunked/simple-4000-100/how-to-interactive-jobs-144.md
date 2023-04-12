    The `services` section specifies the training applications you want to interact with.  

    You can put `sleep <specific time>` at the end of the command to specify the amount of time you want to reserve the compute resource. The format follows: 
    * sleep 1s
    * sleep 1m
    * sleep 1h
    * sleep 1d

    You can also use the `sleep infinity` command that would keep the job alive indefinitely. 
    
    > [!NOTE]
    > If you use `sleep infinity`, you will need to manually [cancel the job](./how-to-interactive-jobs.md#end-job) to let go of the compute resource (and stop billing). 

2. Run command `az ml job create --file <path to your job yaml file> --workspace-name <your workspace name> --resource-group <your resource group name> --subscription <sub-id> `to submit your training job. For more details on running a job via CLIv2, check out this [article](./how-to-train-model.md). 


### Connect to endpoints
# [Azure Machine Learning Studio](#tab/ui)
To interact with your running job, click the button **Debug and monitor** on the job details page. 

:::image type="content" source="media/interactive-jobs/debug-and-monitor.png" alt-text="Screenshot of interactive jobs debug and monitor panel location.":::


Clicking the applications in the panel opens a new tab for the applications. You can access the applications only when they are in **Running** status and only the **job owner** is authorized to access the applications. If you're training on multiple nodes, you can pick the specific node you would like to interact with.

:::image type="content" source="media/interactive-jobs/interactive-jobs-application-list.png" alt-text="Screenshot of interactive jobs right panel information. Information content will vary depending on the user's data.":::

It might take a few minutes to start the job and the training applications specified during job creation. If you don't see the above options, make sure you have enabled the "Debug & monitor your training jobs" flight via the [preview panel](./how-to-enable-preview-features.md#how-do-i-enable-preview-features).

# [Python SDK](#tab/python)
- Once the job is submitted, you can use `ml_client.jobs.show_services("<job name>", <compute node index>)` to view the interactive service endpoints.
    
- To connect via SSH to the container where the job is running, run the command `az ml job connect-ssh --name <job-name> --node-index <compute node index> --private-key-file-path <path to private key>`. To set up the Azure Machine Learning CLIv2, follow this [guide](./how-to-configure-cli.md). 
  
You can find the reference documentation for the SDKv2 [here](./index.yml).

You can access the applications only when they are in **Running** status and only the **job owner** is authorized to access the applications. If you're training on multiple nodes, you can pick the specific node you would like to interact with by passing in the node index.

# [Azure CLI](#tab/azurecli)
- When the job is **running**, Run the command `az ml job show-services --name <job name> --node-index <compute node index>` to get the URL to the applications. The endpoint URL will show under `services` in the output. Note that for VS Code, you must copy and paste the provided URL in your browser. 

- To connect via SSH to the container where the job is running, run the command `az ml job connect-ssh --name <job-name> --node-index <compute node index> --private-key-file-path <path to private key>`. 

You can find the reference documentation for these commands [here](/cli/azure/ml).

You can access the applications only when they are in **Running** status and only the **job owner** is authorized to access the applications. If you're training on multiple nodes, you can pick the specific node you would like to interact with by passing in the node index.


### Interact with the applications
When you click on the endpoints to interact when your job, you're taken to the user container under your working directory, where you can access your code, inputs, outputs, and logs. If you run into any issues while connecting to the applications, the interactive capability and applications logs can be found from **system_logs->interactive_capability** under **Outputs + logs** tab.
