> Backup and restore of workspace metadata such as run history, models and environments is unavailable. Specifying assets and configurations as code using YAML specs, will help you re-recreate assets across workspaces in case of a disaster.

Jobs in Azure Machine Learning are defined by a job specification. This specification includes dependencies on input artifacts that are managed on a workspace-instance level, including environments, datasets, and compute. For multi-region job submission and deployments, we recommend the following practices:

* Manage your code base locally, backed by a Git repository.
    * Export important notebooks from Azure Machine Learning studio.
    * Export pipelines authored in studio as code.

      > [!NOTE]
      > Pipelines created in studio designer cannot currently be exported as code.

* Manage configurations as code.

    * Avoid hardcoded references to the workspace. Instead, configure a reference to the workspace instance using a [config file](how-to-configure-environment.md#local-and-dsvm-only-create-a-workspace-configuration-file) and use [Workspace.from_config()](/python/api/azureml-core/azureml.core.workspace.workspace#remarks) to initialize the workspace. To automate the process, use the [Azure CLI extension for machine learning](v1/reference-azure-machine-learning-cli.md) command [az ml folder attach](/cli/azure/ml(v1)/folder#az-ml(v1)-folder-attach).
    * Use job submission helpers such as [ScriptRunConfig](/python/api/azureml-core/azureml.core.scriptrunconfig) and [Pipeline](/python/api/azureml-pipeline-core/azureml.pipeline.core.pipeline(class)).
    * Use [Environments.save_to_directory()](/python/api/azureml-core/azureml.core.environment(class)#save-to-directory-path--overwrite-false-) to save your environment definitions.
    * Use a Dockerfile if you use custom Docker images.
    * Use the [Dataset](/python/api/azureml-core/azureml.core.dataset(class)) class to define the collection of data [paths](/python/api/azureml-core/azureml.data.datapath) used by your solution.
    * Use the [Inferenceconfig](/python/api/azureml-core/azureml.core.model.inferenceconfig) class to deploy models as inference endpoints.

## Initiate a failover

### Continue work in the failover workspace

When your primary workspace becomes unavailable, you can switch over the secondary workspace to continue experimentation and development. Azure Machine Learning does not automatically submit jobs to the secondary workspace if there is an outage. Update your code configuration to point to the new workspace resource. We recommend to avoiding hardcoding workspace references. Instead, use a [workspace config file](how-to-configure-environment.md#local-and-dsvm-only-create-a-workspace-configuration-file) to minimize manual user steps when changing workspaces. Make sure to also update any automation, such as continuous integration and deployment pipelines to the new workspace.

Azure Machine Learning cannot sync or recover artifacts or metadata between workspace instances. Dependent on your application deployment strategy, you might have to move artifacts or recreate experimentation inputs such as dataset objects in the failover workspace in order to continue job submission. In case you have configured your primary workspace and secondary workspace resources to share associated resources with geo-replication enabled, some objects might be directly available to the failover workspace. For example, if both workspaces share the same docker images, configured datastores, and Azure Key Vault resources. The following diagram shows a configuration where two workspaces share the same images (1), datastores (2), and Key Vault (3).

![Reference resource configuration](./media/how-to-high-availability-machine-learning/bcdr-resource-configuration.png)

> [!NOTE]
> Any jobs that are running when a service outage occurs will not automatically transition to the secondary workspace. It is also unlikely that the jobs will resume and finish successfully in the primary workspace once the outage is resolved. Instead, these jobs must be resubmitted, either in the secondary workspace or in the primary (once the outage is resolved).
