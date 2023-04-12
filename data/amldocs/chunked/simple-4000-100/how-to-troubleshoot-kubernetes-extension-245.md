1. Set `volcanoScheduler.schedulerConfigMap=<configmap name>` in the extension config to apply this configmap. And you need to skip the resource validation when installing the extension by configuring `amloperator.skipResourceValidation=true`. For example:
    ```azurecli
    az k8s-extension update --name <extension-name> --extension-type Microsoft.AzureML.Kubernetes --config volcanoScheduler.schedulerConfigMap=<configmap name> amloperator.skipResourceValidation=true --cluster-type managedClusters --cluster-name <your-AKS-cluster-name> --resource-group <your-RG-name> --scope cluster
    ```

> [!NOTE]
> Since the gang plugin is removed, there's potential that the deadlock happens when volcano schedules the job. 
> 
> * To avoid this situation, you can **use same instance type across the jobs**.
>
> Note that you need to disable `job/validate` webhook in the volcano admission if your **volcano version is lower than 1.6**.



