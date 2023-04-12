
# MLOps: Model management, deployment, and monitoring with Azure Machine Learning

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning developer platform you are using:"]
> * [v1](./v1/concept-model-management-and-deployment.md)
> * [v2 (current version)](concept-model-management-and-deployment.md)

In this article, learn how to apply Machine Learning Operations (MLOps) practices in Azure Machine Learning for the purpose of managing the lifecycle of your models. Applying MLOps practices can improve the quality and consistency of your machine learning solutions. 

## What is MLOps?

MLOps is based on [DevOps](https://azure.microsoft.com/overview/what-is-devops/) principles and practices that increase the efficiency of workflows. Examples include continuous integration, delivery, and deployment. MLOps applies these principles to the machine learning process, with the goal of:

* Faster experimentation and development of models.
* Faster deployment of models into production.
* Quality assurance and end-to-end lineage tracking.

## MLOps in Machine Learning

Machine Learning provides the following MLOps capabilities:

- **Create reproducible machine learning pipelines.** Use machine learning pipelines to define repeatable and reusable steps for your data preparation, training, and scoring processes.
- **Create reusable software environments.** Use these environments for training and deploying models.
- **Register, package, and deploy models from anywhere.** You can also track associated metadata required to use the model.
- **Capture the governance data for the end-to-end machine learning lifecycle.** The logged lineage information can include who is publishing models and why changes were made. It can also include when models were deployed or used in production.
- **Notify and alert on events in the machine learning lifecycle.** Event examples include experiment completion, model registration, model deployment, and data drift detection.
- **Monitor machine learning applications for operational and machine learning-related issues.** Compare model inputs between training and inference. Explore model-specific metrics. Provide monitoring and alerts on your machine learning infrastructure.
- **Automate the end-to-end machine learning lifecycle with Machine Learning and Azure Pipelines.** By using pipelines, you can frequently update models. You can also test new models. You can continually roll out new machine learning models alongside your other applications and services.

For more information on MLOps, see [Machine learning DevOps](/azure/cloud-adoption-framework/ready/azure-best-practices/ai-machine-learning-mlops).

## Create reproducible machine learning pipelines

Use machine learning pipelines from Machine Learning to stitch together all the steps in your model training process.

A machine learning pipeline can contain steps from data preparation to feature extraction to hyperparameter tuning to model evaluation. For more information, see [Machine learning pipelines](concept-ml-pipelines.md).

If you use the [designer](concept-designer.md) to create your machine learning pipelines, you can at any time select the **...** icon in the upper-right corner of the designer page. Then select **Clone**. When you clone your pipeline, you iterate your pipeline design without losing your old versions.

## Create reusable software environments

By using Machine Learning environments, you can track and reproduce your projects' software dependencies as they evolve. You can use environments to ensure that builds are reproducible without manual software configurations.

Environments describe the pip and conda dependencies for your projects. You can use them for training and deployment of models. For more information, see [What are Machine Learning environments?](concept-environments.md).

## Register, package, and deploy models from anywhere

The following sections discuss how to register, package, and deploy models.
