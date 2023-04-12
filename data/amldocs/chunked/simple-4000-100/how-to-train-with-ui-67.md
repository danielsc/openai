Curated environments are Azure-defined collections of Python packages used in common ML workloads. Curated environments are available in your workspace by default. These environments are backed by cached Docker images, which reduce the job preparation overhead. The cards displayed in the "Curated environments" page show details of each environment. To learn more, see [curated environments in Azure Machine Learning](resource-curated-environments.md).

 [![Curated environments](media/how-to-train-with-ui/curated-env.png)](media/how-to-train-with-ui/curated-env.png)

### Custom environments

Custom environments are environments you've specified yourself. You can specify an environment or reuse an environment that you've already created. To learn more, see [Manage software environments in Azure Machine Learning studio (preview)](how-to-manage-environments-in-studio.md#create-an-environment). 

### Container registry image

If you don't want to use the Azure Machine Learning curated environments or specify your own custom environment, you can use a docker image from a public container registry such as [Docker Hub](https://hub.docker.com/). If the image is in a private container, toggle **This is a private container registry**. For private registries, you will need to enter a valid username and password so Azure can get the image. 
[![Container registry image](media/how-to-train-with-ui/container-registry-image.png)](media/how-to-train-with-ui/container-registry-image.png)

## Configure your job

After specifying the environment, you can configure your job with more settings. 

|Field| Description|
|------| ------|
|Job name| The job name field is used to uniquely identify your job. It's also used as the display name for your job. Setting this field is optional; Azure will generate a GUID name for the job if you don't enter anything. Note: the job name must be unique.|
|Experiment name| This helps organize the job in Azure Machine Learning studio. Each job's run record will be organized under the corresponding experiment in the studio's "Experiment" tab. By default, Azure will put the job in the **Default** experiment.|
|Code| You can upload a code file or a folder from your machine, or upload a code file from the workspace's default blob storage. Azure will show the files to be uploaded after you make the selection. |
|Command| The command to execute. Command-line arguments can be explicitly written into the command or inferred from other sections, specifically **inputs** using curly braces notation, as discussed in the next section.|
|Inputs| Specify the input binding. We support three types of inputs: 1) Azure Machine Learning registered dataset; 2) workspace default blob storage; 3) upload local file. You can add multiple inputs. |
|Environment variables| Setting environment variables allows you to provide dynamic configuration of the job. You can add the variable and value here.|
|Tags| Add tags to your job to help with organization.|

### Specify code and inputs in the command box

#### Code

The command is run from the root directory of the uploaded code folder. After you select your code file or folder, you can see the files to be uploaded. Copy the relative path to the code containing your entry point and paste it into the box labeled **Enter the command to start the job**. 

If the code is in the root directory, you can directly refer to it in the command. For instance, `python main.py`.

If the code isn't in the root directory, you should use the relative path. For example, the structure of the [word language model](https://github.com/Azure/azureml-examples/tree/main/cli/jobs/single-step/pytorch/word-language-model) is:

```tree
.
├── job.yml
├── data
└── src
    └── main.py
```
Here, the source code is in the `src` subdirectory. The command would be `python ./src/main.py` (plus other command-line arguments).

[![Refer code in the command](media/how-to-train-with-ui/code-command.png)](media/how-to-train-with-ui/code-command.png)
