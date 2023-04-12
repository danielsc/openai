> * For a compute *instance*, [enable idle shutdown](how-to-create-manage-compute-instance.md#enable-idle-shutdown-preview).

### Supported VM series and sizes

> [!NOTE] 
> H-series virtual machine series will be retired on August 31, 2022. Create compute instance and compute clusters with alternate VM sizes. Existing compute instances and clusters with H-series virtual machines will not work after August 31, 2022.

When you select a node size for a managed compute resource in Azure Machine Learning, you can choose from among select VM sizes available in Azure. Azure offers a range of sizes for Linux and Windows for different workloads. To learn more, see [VM types and sizes](../virtual-machines/sizes.md).

There are a few exceptions and limitations to choosing a VM size:

* Some VM series aren't supported in Azure Machine Learning.
* There are some VM series, such as GPUs and other special SKUs, which may not initially appear in your list of available VMs.  But you can still use them, once you request a quota change. For more information about requesting quotas, see [Request quota increases](how-to-manage-quotas.md#request-quota-increases).
See the following table to learn more about supported series.

| **Supported VM series** | **Category** | **Supported by** |
|------------|------------|------------|------------|
| [DDSv4](../virtual-machines/ddv4-ddsv4-series.md#ddsv4-series) | General purpose | Compute clusters and instance |
| [Dv2](../virtual-machines/dv2-dsv2-series.md#dv2-series) | General purpose | Compute clusters and instance |
| [Dv3](../virtual-machines/dv3-dsv3-series.md#dv3-series) | General purpose | Compute clusters and instance |
| [DSv2](../virtual-machines/dv2-dsv2-series.md#dsv2-series) | General purpose | Compute clusters and instance |
| [DSv3](../virtual-machines/dv3-dsv3-series.md#dsv3-series) | General purpose | Compute clusters and instance |
| [EAv4](../virtual-machines/eav4-easv4-series.md) | Memory optimized | Compute clusters and instance |
| [Ev3](../virtual-machines/ev3-esv3-series.md) | Memory optimized | Compute clusters and instance |
| [ESv3](../virtual-machines/ev3-esv3-series.md) | Memory optimized | Compute clusters and instance |
| [FSv2](../virtual-machines/fsv2-series.md) | Compute optimized | Compute clusters and instance |
| [FX](../virtual-machines/fx-series.md) | Compute optimized | Compute clusters |
| [H](../virtual-machines/h-series.md) | High performance compute | Compute clusters and instance |
| [HB](../virtual-machines/hb-series.md) | High performance compute | Compute clusters and instance |
| [HBv2](../virtual-machines/hbv2-series.md) | High performance compute | Compute clusters and instance |
| [HBv3](../virtual-machines/hbv3-series.md) |  High performance compute | Compute clusters and instance |
| [HC](../virtual-machines/hc-series.md) |  High performance compute | Compute clusters and instance |
| [LSv2](../virtual-machines/lsv2-series.md) |  Storage optimized | Compute clusters and instance |
| [M](../virtual-machines/m-series.md) | Memory optimized | Compute clusters and instance |
| [NC](../virtual-machines/nc-series.md) |  GPU | Compute clusters and instance |
| [NC Promo](../virtual-machines/nc-series.md) | GPU | Compute clusters and instance |
| [NCv2](../virtual-machines/ncv2-series.md) | GPU | Compute clusters and instance |
| [NCv3](../virtual-machines/ncv3-series.md) | GPU | Compute clusters and instance |
| [ND](../virtual-machines/nd-series.md) | GPU | Compute clusters and instance |
| [NDv2](../virtual-machines/ndv2-series.md) | GPU | Compute clusters and instance |
| [NV](../virtual-machines/nv-series.md) | GPU | Compute clusters and instance |
| [NVv3](../virtual-machines/nvv3-series.md) | GPU | Compute clusters and instance |
| [NCasT4_v3](../virtual-machines/nct4-v3-series.md) | GPU | Compute clusters and instance |
| [NDasrA100_v4](../virtual-machines/nda100-v4-series.md) | GPU | Compute clusters and instance |


While Azure Machine Learning supports these VM series, they might not be available in all Azure regions. To check whether VM series are available, see [Products available by region](https://azure.microsoft.com/global-infrastructure/services/?products=virtual-machines).
