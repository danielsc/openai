|CLI/SDK v2 | No | Yes|
|Training | No | Yes|
|Real-time inference | Yes | Yes |
|Batch inference | No | Yes |
|Real-time inference new features | No new features development | Active roadmap |

With these key differences and overall AzureML evolution to use SDK/CLI v2, AzureML recommends you to use Kubernetes compute target to deploy models if you decide to use AKS for model deployment.

## Next steps

- [Step 1: Deploy AzureML extension](how-to-deploy-kubernetes-extension.md)
- [Step 2: Attach Kubernetes cluster to workspace](how-to-attach-kubernetes-to-workspace.md)
- [Create and manage instance types](how-to-manage-kubernetes-instance-types.md)

### Other resources

- [Kubernetes version and region availability](./reference-kubernetes.md#supported-kubernetes-version-and-region)
- [Work with custom data storage](./reference-kubernetes.md#azureml-jobs-connect-with-custom-data-storage)


### Examples

All AzureML examples can be found in [https://github.com/Azure/azureml-examples.git](https://github.com/Azure/azureml-examples).

For any AzureML example, you only need to update the compute target name to your Kubernetes compute target, then you're all done. 
* Explore training job samples with CLI v2 - [https://github.com/Azure/azureml-examples/tree/main/cli/jobs](https://github.com/Azure/azureml-examples/tree/main/cli/jobs)
* Explore model deployment with online endpoint samples with CLI v2 - [https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online/kubernetes](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online/kubernetes)
* Explore batch endpoint samples with CLI v2 - [https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/batch](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/batch)
* Explore training job samples with SDK v2 -[https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs)
* Explore model deployment with online endpoint samples with SDK v2 -[https://github.com/Azure/azureml-examples/tree/main/sdk/python/endpoints/online/kubernetes](https://github.com/Azure/azureml-examples/tree/main/sdk/python/endpoints/online/kubernetes)
