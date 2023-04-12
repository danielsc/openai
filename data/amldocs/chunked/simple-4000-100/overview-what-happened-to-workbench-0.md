# What happened to Azure Machine Learning Workbench?

The Azure Machine Learning Workbench application and some other early features were deprecated and replaced in the **September 2018** release to make way for an improved [architecture](v1/concept-azure-machine-learning-architecture.md).

To improve your experience, the release contains many significant updates prompted by customer feedback. The core functionality from experiment runs to model deployment hasn't changed. But now, you can use the robust <a href="/python/api/overview/azure/ml/intro" target="_blank">Python SDK</a>, and the [Azure CLI](v1/reference-azure-machine-learning-cli.md) to accomplish your machine learning tasks and pipelines.

Most of the artifacts that were created in the earlier version of Azure Machine Learning are stored in your own local or cloud storage. These artifacts won't ever disappear.

In this article, you learn about what changed and how it affects your pre-existing work with the Azure Machine Learning Workbench and its APIs.

>[!Warning]
>This article is not for Azure Machine Learning Studio users. It is for Azure Machine Learning customers who have installed the Workbench (preview) application and/or have experimentation and model management preview accounts.


## What changed?

The latest release of Azure Machine Learning includes the following features:
+ A [simplified Azure resources model](v1/concept-azure-machine-learning-architecture.md).
+ A [new portal UI](how-to-log-view-metrics.md) to manage your experiments and compute targets.
+ A new, more comprehensive Python <a href="/python/api/overview/azure/ml/intro" target="_blank">SDK</a>.
+ The new expanded [Azure CLI extension](v1/reference-azure-machine-learning-cli.md) for machine learning.

The [architecture](v1/concept-azure-machine-learning-architecture.md) was redesigned for ease of use. Instead of multiple Azure resources and accounts, you only need an [Azure Machine Learning Workspace](concept-workspace.md). You can create workspaces quickly in the [Azure portal](quickstart-create-resources.md). By using a workspace, multiple users can store training and deployment compute targets, model experiments, Docker images, deployed models, and so on.

Although there are new improved CLI and SDK clients in the current release, the desktop workbench application itself has been retired. Experiments can be managed in the [workspace dashboard in Azure Machine Learning studio](how-to-log-view-metrics.md#view-the-experiment-in-the-web-portal). Use the dashboard to get your experiment history, manage the compute targets attached to your workspace, manage your models and Docker images, and even deploy web services.

<a name="timeline"></a>

## Support timeline

On January 9th, 2019 support for Machine Learning Workbench, Azure Machine Learning Experimentation and Model Management accounts, and their associated SDK and CLI ended.

All the latest capabilities are available by using this <a href="/python/api/overview/azure/ml/intro" target="_blank">SDK</a>, the [CLI](v1/reference-azure-machine-learning-cli.md), and the [Azure portal](quickstart-create-resources.md).

## What about run histories?

Older run histories are no longer accessible, how you can still see your runs in the latest version.

Run histories are now called **experiments**. You can collect your model's experiments and explore them by using the SDK, the CLI, or the Azure Machine Learning studio.

The Azure Machine Learning studio is supported on Microsoft Edge, Chrome, and Firefox browsers only:

[![Screenshot of Azure Machine Learning studio](./media/overview-what-happened-to-workbench/jobs-experiments.png)](./media/overview-what-happened-to-workbench/jobs-experiments.png#lightbox)

Start training your models and tracking the run histories using the new CLI and SDK. You can learn how with the [Tutorial: train models with Azure Machine Learning](tutorial-train-deploy-notebook.md).

## Will projects persist?

You won't lose any code or work. In the older version, projects are cloud entities with a local directory. In the latest version, you attach local directories to the Azure Machine Learning workspace by using a local config file. See a [diagram of the latest architecture](v1/concept-azure-machine-learning-architecture.md).
