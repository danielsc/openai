
# Azure Machine Learning compute instance image release notes

In this article, learn about Azure Machine Learning compute instance image releases. Azure Machine Learning maintains host operating system images for [Azure ML compute instance](./concept-compute-instance.md) and [Data Science Virtual Machines](./data-science-virtual-machine/release-notes.md). Due to the rapidly evolving needs and package updates, we target to release new images every month.

Azure Machine Learning checks and validates any machine learning packages that may require an upgrade. Updates incorporate the latest OS-related patches from Canonical as the original Linux OS publisher. In addition to patches applied by the original publisher, Azure Machine Learning updates system packages when updates are available. For details on the patching process, see [Vulnerability Management](./concept-vulnerability-management.md).

Main updates provided with each image version are described in the below sections.

## January 19, 2023
Version: `23.01.19`

Main changes:

- Added new conda environment `jupyter-env`
- Moved jupyter service to new `jupyter-env` conda environment
- `Azure Machine Learning SDK` to version `1.48.0`
 
Main environment specific updates:

- Added `azureml-fsspec` package to `Azureml_py310_sdkv2`
- `CUDA` support resolved for `azureml_py38CUDA` 
- `CUDA` support resolved for `azureml_py38_PT_TF`

## September 22, 2022 
Version `22.09.22`

Main changes:

- `.Net Framework` to version `3.1.423`
- `Azure Cli` to version `2.40.0`
- `Conda` to version `4.14.0`
- `Azure Machine Learning SDK` to version `1.45.0`
 
Main environment specific updates:

`azureml_py38`:
- `azureml-core` to version `1.45.0`
- `tensorflow-gpu` to version `2.2.1`

## August 19, 2022 
Version `22.08.19`

Main changes:
- Base OS level image updates.

## July 22, 2022 
Version `22.07.22`

Main changes:
* `Azcopy` to version `10.16.0`
* `Blob Fuse` to version `1.4.4`
