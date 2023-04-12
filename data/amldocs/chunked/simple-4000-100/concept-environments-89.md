Actual cached images in your workspace ACR will have names like `azureml/azureml_e9607b2514b066c851012848913ba19f` with the hash appearing at the end.

>[!IMPORTANT]
> * If you create an environment with an unpinned package dependency (for example, `numpy`), the environment uses the package version that was *available when the environment was created*. Any future environment that uses a matching definition will use the original version. 
>
>   To update the package, specify a version number to force an image rebuild. An example of this would be changing `numpy` to `numpy==1.18.1`. New dependencies--including nested ones--will be installed, and they might break a previously working scenario.
>
> * Using an unpinned base image like `mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04` in your environment definition results in rebuilding the image every time the `latest` tag is updated. This helps the image receive the latest patches and system updates.zzs

### Image patching

Microsoft is responsible for patching the base images for known security vulnerabilities. Updates for supported images are released every two weeks, with a commitment of no unpatched vulnerabilities older than 30 days in the the latest version of the image. Patched images are released with a new immutable tag and the `:latest` tag is updated to the latest version of the patched image. 

If you provide your own images, you are responsible for updating them.

For more information on the base images, see the following links:

* [Azure Machine Learning base images](https://github.com/Azure/AzureML-Containers) GitHub repository.
* [Deploy a TensorFlow model using a custom container](how-to-deploy-custom-container.md)

## Next steps

* Learn how to [create and use environments](how-to-use-environments.md) in Azure Machine Learning.
* See the Python SDK reference documentation for the [environment class](/python/api/azure-ai-ml/azure.ai.ml.entities.environment).
