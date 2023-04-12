
# Troubleshooting batch endpoints

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

Learn how to troubleshoot and solve, or work around, common errors you may come across when using [batch endpoints](how-to-use-batch-endpoint.md) for batch scoring. In this article you will learn:

> [!div class="checklist"]
> * How [logs of a batch scoring job are organized](#understanding-logs-of-a-batch-scoring-job).
> * How to [solve common errors](#common-issues).
> * Identify [not supported scenarios in batch endpoints](#limitations-and-not-supported-scenarios) and their limitations.

## Understanding logs of a batch scoring job

### Get logs

After you invoke a batch endpoint using the Azure CLI or REST, the batch scoring job will run asynchronously. There are two options to get the logs for a batch scoring job.

Option 1: Stream logs to local console

You can run the following command to stream system-generated logs to your console. Only logs in the `azureml-logs` folder will be streamed.

```azurecli
az ml job stream -name <job_name>
```

Option 2: View logs in studio 

To get the link to the run in studio, run: 

```azurecli
az ml job show --name <job_name> --query interaction_endpoints.Studio.endpoint -o tsv
```

1. Open the job in studio using the value returned by the above command. 
1. Choose __batchscoring__
1. Open the __Outputs + logs__ tab 
1. Choose the log(s) you wish to review

### Understand log structure

There are two top-level log folders, `azureml-logs` and `logs`. 

The file `~/azureml-logs/70_driver_log.txt` contains information from the controller that launches the scoring script.  

Because of the distributed nature of batch scoring jobs, there are logs from several different sources. However, two combined files are created that provide high-level information: 

- `~/logs/job_progress_overview.txt`: This file provides high-level information about the number of mini-batches (also known as tasks) created so far and the number of mini-batches processed so far. As the mini-batches end, the log records the results of the job. If the job failed, it will show the error message and where to start the troubleshooting.

- `~/logs/sys/master_role.txt`: This file provides the principal node (also known as the orchestrator) view of the running job. This log provides information on task creation, progress monitoring, the job result.

For a concise understanding of errors in your script there is:

- `~/logs/user/error.txt`: This file will try to summarize the errors in your script.

For more information on errors in your script, there is:

- `~/logs/user/error/`: This file contains full stack traces of exceptions thrown while loading and running the entry script.

When you need a full understanding of how each node executed the score script, look at the individual process logs for each node. The process logs can be found in the `sys/node` folder, grouped by worker nodes:

- `~/logs/sys/node/<ip_address>/<process_name>.txt`: This file provides detailed info about each mini-batch as it's picked up or completed by a worker. For each mini-batch, this file includes:

    - The IP address and the PID of the worker process. 
    - The total number of items, the number of successfully processed items, and the number of failed items.
    - The start time, duration, process time, and run method time.

You can also view the results of periodic checks of the resource usage for each node. The log files and setup files are in this folder:

- `~/logs/perf`: Set `--resource_monitor_interval` to change the checking interval in seconds. The default interval is `600`, which is approximately 10 minutes. To stop the monitoring, set the value to `0`. Each `<ip_address>` folder includes:

    - `os/`: Information about all running processes in the node. One check runs an operating system command and saves the result to a file. On Linux, the command is `ps`.
        - `%Y%m%d%H`: The sub folder name is the time to hour.
            - `processes_%M`: The file ends with the minute of the checking time.
