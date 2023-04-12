* Automated machine learning UI: Learn how to create [automated ML experiments](tutorial-first-experiment-automated-ml.md) with an easy-to-use interface.

* Data labeling: Use Azure Machine Learning data labeling to efficiently coordinate [image labeling](how-to-create-image-labeling-projects.md) or [text labeling](how-to-create-text-labeling-projects.md) projects.


## Enterprise-readiness and security

Azure Machine Learning integrates with the Azure cloud platform to add security to ML projects. 

Security integrations include:

* Azure Virtual Networks (VNets) with network security groups 
* Azure Key Vault where you can save security secrets, such as access information for storage accounts
* Azure Container Registry set up behind a VNet

See [Tutorial: Set up a secure workspace](tutorial-create-secure-workspace.md).

## Azure integrations for complete solutions

Other integrations with Azure services support a machine learning project from end-to-end. They include:

* Azure Synapse Analytics to process and stream data with Spark
* Azure Arc, where you can run Azure services in a Kubernetes environment
* Storage and database options, such as Azure SQL Database, Azure Storage Blobs, and so on
* Azure App Service allowing you to deploy and manage ML-powered apps

> [!Important]
> Azure Machine Learning doesn't store or process your data outside of the region where you deploy.
>

## Machine learning project workflow

Typically models are developed as part of a project with an objective and goals. Projects often involve more than one person. When experimenting with data, algorithms, and models, development is iterative. 

### Project lifecycle

While the project lifecycle can vary by project, it will often look like this:

![Machine learning project lifecycle diagram](./media/overview-what-is-azure-machine-learning/overview-ml-development-lifecycle.png)

A workspace organizes a project and allows for collaboration for many users all working toward a common objective. Users in a workspace can easily share the results of their runs from experimentation in the studio user interface or use versioned assets for jobs like environments and storage references.

For more information, see [Manage Azure Machine Learning workspaces](how-to-manage-workspace.md?tabs=python).

When a project is ready for operationalization, users' work can be automated in a machine learning pipeline and triggered on a schedule or HTTPS request.

Models can be deployed to the managed inferencing solution, for both real-time and batch deployments, abstracting away the infrastructure management typically required for deploying models.

## Train models

In Azure Machine Learning, you can run your training script in the cloud or build a model from scratch. Customers often bring models they've built and trained in open-source frameworks, so they can operationalize them in the cloud. 

### Open and interoperable

Data scientists can use models in Azure Machine Learning that they've created in common Python frameworks, such as: 

* PyTorch
* TensorFlow
* scikit-learn
* XGBoost
* LightGBM

Other languages and frameworks are supported as well, including: 
* R
* .NET

See [Open-source integration with Azure Machine Learning](concept-open-source.md).

### Automated featurization and algorithm selection (AutoML)

In a repetitive, time-consuming process, in classical machine learning data scientists use prior experience and intuition to select the right data featurization and algorithm for training. Automated ML (AutoML) speeds this process and can be used through the studio UI or Python SDK.

See [What is automated machine learning?](concept-automated-ml.md)

### Hyperparameter optimization

Hyperparameter optimization, or hyperparameter tuning, can be a tedious task. Azure Machine Learning can automate this task for arbitrary parameterized commands with little modification to your job definition. Results are visualized in the studio.

See [How to tune hyperparameters](how-to-tune-hyperparameters.md).
