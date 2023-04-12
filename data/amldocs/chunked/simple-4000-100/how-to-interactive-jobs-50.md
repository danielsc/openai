  > If you use `sleep infinity`, you will need to manually [cancel the job](./how-to-interactive-jobs.md#end-job) to let go of the compute resource (and stop billing). 

5. Select the training applications you want to use to interact with the job.

  :::image type="content" source="./media/interactive-jobs/select-training-apps.png" alt-text="Screenshot of selecting a training application for the user to use for a job.":::

6. Review and create the job.

If you don't see the above options, make sure you have enabled the "Debug & monitor your training jobs" flight via the [preview panel](./how-to-enable-preview-features.md#how-do-i-enable-preview-features).

# [Python SDK](#tab/python)
1. Define the interactive services you want to use for your job. Make sure to replace `your compute name` with your own value. If you want to use your own custom environment, follow the examples in [this tutorial](how-to-manage-environments-v2.md) to create a custom environment. 

   Note that you have to import the `JobService` class from the `azure.ai.ml.entities` package to configure interactive services via the SDKv2. 

    ```python
    command_job = command(...
        code="./src",  # local path where the code is stored
        command="python main.py", # you can add a command like "sleep 1h" to reserve the compute resource is reserved after the script finishes running
        environment="AzureML-tensorflow-2.7-ubuntu20.04-py38-cuda11-gpu@latest",
        compute="<name-of-compute>",
        services={
          "My_jupyterlab": JobService(
            job_service_type="jupyter_lab",
            nodes="all" # For distributed jobs, use the `nodes` property to pick which node you want to enable interactive services on. If `nodes` are not selected, by default, interactive applications are only enabled on the head node. Values are "all", or compute node index (for ex. "0", "1" etc.)
          ),
          "My_vscode": JobService(
            job_service_type="vs_code",
            nodes="all"
          ),
          "My_tensorboard": JobService(
            job_service_type="tensor_board",
            nodes="all",
            properties={
                "logDir": "output/tblogs"  # relative path of Tensorboard logs (same as in your training script)
            }          
          ),
          "My_ssh": JobService(
            job_service_type="ssh",
            sshPublicKeys="<add-public-key>",
            nodes="all"
            properties={
                "sshPublicKeys":"<add-public-key>"
            }    
          ),
        }
    )

    # submit the command
    returned_job = ml_client.jobs.create_or_update(command_job)
    ```

    The `services` section specifies the training applications you want to interact with.  

    You can put `sleep <specific time>` at the end of your command to specify the amount of time you want to reserve the compute resource. The format follows: 
    * sleep 1s
    * sleep 1m
    * sleep 1h
    * sleep 1d

    You can also use the `sleep infinity` command that would keep the job alive indefinitely. 
    
    > [!NOTE]
    > If you use `sleep infinity`, you will need to manually [cancel the job](./how-to-interactive-jobs.md#end-job) to let go of the compute resource (and stop billing). 

2. Submit your training job. For more details on how to train with the Python SDKv2, check out this [article](./how-to-train-model.md).

# [Azure CLI](#tab/azurecli)

1. Create a job yaml `job.yaml` with below sample content. Make sure to replace `your compute name` with your own value. If you want to use custom environment, follow the examples in [this tutorial](how-to-manage-environments-v2.md) to create a custom environment. 
    ```dotnetcli
    code: src 
    command: 
      python train.py 
      # you can add a command like "sleep 1h" to reserve the compute resource is reserved after the script finishes running.
    environment: azureml:AzureML-tensorflow-2.4-ubuntu18.04-py37-cuda11-gpu:41
    compute: azureml:<your compute name>
    services:
        my_vs_code:
          job_service_type: vs_code
          nodes: all # For distributed jobs, use the `nodes` property to pick which node you want to enable interactive services on. If `nodes` are not selected, by default, interactive applications are only enabled on the head node. Values are "all", or compute node index (for ex. "0", "1" etc.)
        my_tensor_board:
          job_service_type: tensor_board
          properties:
            logDir: "output/tblogs" # relative path of Tensorboard logs (same as in your training script)
          nodes: all
        my_jupyter_lab:
          job_service_type: jupyter_lab
          nodes: all
        my_ssh:
         job_service_type: ssh
         properties:
           sshPublicKeys: <paste the entire pub key content>
         nodes: all
    ```
