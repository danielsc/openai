When you click on the endpoints to interact when your job, you're taken to the user container under your working directory, where you can access your code, inputs, outputs, and logs. If you run into any issues while connecting to the applications, the interactive capability and applications logs can be found from **system_logs->interactive_capability** under **Outputs + logs** tab.

:::image type="content" source="./media/interactive-jobs/interactive-logs.png" alt-text="Screenshot of interactive jobs interactive logs panel location.":::

- You can open a terminal from Jupyter Lab and start interacting within the job container. You can also directly iterate on your training script with Jupyter Lab. 

  :::image type="content" source="./media/interactive-jobs/jupyter-lab.png" alt-text="Screenshot of interactive jobs Jupyter lab content panel.":::

- You can also interact with the job container within VS Code. To attach a debugger to a job during job submission and pause execution, [navigate here](./how-to-interactive-jobs.md#attach-a-debugger-to-a-job).

  :::image type="content" source="./media/interactive-jobs/vs-code-open.png" alt-text="Screenshot of interactive jobs VS Code panel when first opened. This shows the sample python file that was created to print two lines.":::

- If you have logged tensorflow events for your job, you can use TensorBoard to monitor the metrics when your job is running.

  :::image type="content" source="./media/interactive-jobs/tensorboard-open.png" alt-text="Screenshot of interactive jobs tensorboard panel when first opened. This information will vary depending upon customer data":::
  
If you don't see the above options, make sure you have enabled the "Debug & monitor your training jobs" flight via the [preview panel](./how-to-enable-preview-features.md#how-do-i-enable-preview-features).

### End job
Once you're done with the interactive training, you can also go to the job details page to cancel the job which will release the compute resource. Alternatively, use `az ml job cancel -n <your job name>` in the CLI or `ml_client.job.cancel("<job name>")` in the SDK. 

:::image type="content" source="./media/interactive-jobs/cancel-job.png" alt-text="Screenshot of interactive jobs cancel job option and its location for user selection":::

## Attach a debugger to a job
To submit a job with a debugger attached and the execution paused, you can use debugpy and VS Code (`debugpy` must be installed in your job environment). 

1. During job submission (either through the UI, the CLIv2 or the SDKv2) use the debugpy command to run your python script. For example, the below screenshot shows a sample command that uses debugpy to attach the debugger for a tensorflow script (`tfevents.py` can be replaced with the name of your training script).
   
:::image type="content" source="./media/interactive-jobs/use-debugpy.png" alt-text="Screenshot of interactive jobs configuration of debugpy":::

2. Once the job has been submitted, [connect to the VS Code](./how-to-interactive-jobs.md#connect-to-endpoints), and click on the in-built debugger.
   
   :::image type="content" source="./media/interactive-jobs/open-debugger.png" alt-text="Screenshot of interactive jobs location of open debugger on the left side panel":::

3. Use the "Remote Attach" debug configuration to attach to the submitted job and pass in the path and port you configured in your job submission command. You can also find this information on the job details page.
   
   :::image type="content" source="./media/interactive-jobs/debug-path-and-port.png" alt-text="Screenshot of interactive jobs completed jobs":::

   :::image type="content" source="./media/interactive-jobs/remote-attach.png" alt-text="Screenshot of interactive jobs add a remote attach button":::

4. Set breakpoints and walk through your job execution as you would in your local debugging workflow. 
   
    :::image type="content" source="./media/interactive-jobs/set-breakpoints.png" alt-text="Screenshot of location of an example breakpoint that is set in the Visual Studio Code editor":::
