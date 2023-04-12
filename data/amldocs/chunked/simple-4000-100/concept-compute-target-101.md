While Azure Machine Learning supports these VM series, they might not be available in all Azure regions. To check whether VM series are available, see [Products available by region](https://azure.microsoft.com/global-infrastructure/services/?products=virtual-machines).

> [!NOTE]
> Azure Machine Learning doesn't support all VM sizes that Azure Compute supports. To list the available VM sizes, use one of the following methods:
> * [REST API](https://github.com/Azure/azure-rest-api-specs/blob/master/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/stable/2020-08-01/examples/ListVMSizesResult.json)
> * The [Azure CLI extension 2.0 for machine learning](how-to-configure-cli.md) command, [az ml compute list-sizes](/cli/azure/ml/compute#az-ml-compute-list-sizes).

If using the GPU-enabled compute targets, it is important to ensure that the correct CUDA drivers are installed in the training environment. Use the following table to determine the correct CUDA version to use:

| **GPU Architecture**  | **Azure VM Series** | **Supported CUDA versions** |
|------------|------------|------------|
| Ampere | NDA100_v4 | 11.0+ |
| Turing | NCT4_v3 | 10.0+ |
| Volta | NCv3, NDv2 | 9.0+ |
| Pascal | NCv2, ND | 9.0+ |
| Maxwell | NV, NVv3 | 9.0+ |
| Kepler | NC, NC Promo| 9.0+ |

In addition to ensuring the CUDA version and hardware are compatible, also ensure that the CUDA version is compatible with the version of the machine learning framework you are using: 

- For PyTorch, you can check the compatibility by visiting [Pytorch's previous versions page](https://pytorch.org/get-started/previous-versions/). 
- For Tensorflow, you can check the compatibility by visiting [Tensorflow's build from source page](https://www.tensorflow.org/install/source#gpu).

### Compute isolation

Azure Machine Learning compute offers VM sizes that are isolated to a specific hardware type and dedicated to a single customer. Isolated VM sizes are best suited for workloads that require a high degree of isolation from other customers' workloads for reasons that include meeting compliance and regulatory requirements. Utilizing an isolated size guarantees that your VM will be the only one running on that specific server instance.

The current isolated VM offerings include:

* Standard_M128ms
* Standard_F72s_v2
* Standard_NC24s_v3
* Standard_NC24rs_v3*

*RDMA capable

To learn more about isolation, see [Isolation in the Azure public cloud](../security/fundamentals/isolation-choices.md).

## Unmanaged compute

An unmanaged compute target is *not* managed by Azure Machine Learning. You create this type of compute target outside Azure Machine Learning and then attach it to your workspace. Unmanaged compute resources can require additional steps for you to maintain or to improve performance for machine learning workloads. 

Azure Machine Learning supports the following unmanaged compute types:

* Remote virtual machines
* Azure HDInsight
* Azure Databricks
* Azure Data Lake Analytics
* [Azure Synapse Spark pool](v1/how-to-link-synapse-ml-workspaces.md) (preview)

    > [!TIP]
    > Currently this requires the Azure Machine Learning SDK v1.
* [Kubernetes](how-to-attach-kubernetes-anywhere.md)

For more information, see [Manage compute resources](how-to-create-attach-compute-studio.md).

## Next steps

Learn how to:
* [Deploy your model to a compute target](how-to-deploy-online-endpoints.md)
