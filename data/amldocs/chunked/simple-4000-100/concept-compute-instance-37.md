Azure Machine Learning compute instance enables you to author, train, and deploy models in a fully integrated notebook experience in your workspace.

You can run Jupyter notebooks in [VS Code](https://techcommunity.microsoft.com/t5/azure-ai/power-your-vs-code-notebooks-with-azml-compute-instances/ba-p/1629630) using compute instance as the remote server with no SSH needed. You can also enable VS Code integration through [remote SSH extension](https://devblogs.microsoft.com/python/enhance-your-azure-machine-learning-experience-with-the-vs-code-extension/).

You can [install packages](how-to-access-terminal.md#install-packages) and [add kernels](how-to-access-terminal.md#add-new-kernels) to your compute instance.

Following tools and environments are already installed on the compute instance:

|General tools & environments|Details|
|----|:----:|
|Drivers|`CUDA`</br>`cuDNN`</br>`NVIDIA`</br>`Blob FUSE` |
|Intel MPI library||
|Azure CLI ||
|Azure Machine Learning samples ||
|Docker||
|Nginx||
|NCCL 2.0 ||
|Protobuf||

|**R** tools & environments|Details|
|----|:----:|
|R kernel||

You can [Add RStudio or Posit Workbench (formerly RStudio Workbench)](how-to-create-manage-compute-instance.md#add-custom-applications-such-as-rstudio-or-posit-workbench-preview) when you create the instance.

|**PYTHON** tools & environments|Details|
|----|----|
|Anaconda Python||
|Jupyter and extensions||
|Jupyterlab and extensions||
[Azure Machine Learning SDK for Python](https://aka.ms/sdk-v2-install)</br>from PyPI|Includes most of the azureml extra packages.  To see the full list, [open a terminal window on your compute instance](how-to-access-terminal.md) and run <br/> `conda list -n azureml_py36 azureml*` |
|Other PyPI packages|`jupytext`</br>`tensorboard`</br>`nbconvert`</br>`notebook`</br>`Pillow`|
|Conda packages|`cython`</br>`numpy`</br>`ipykernel`</br>`scikit-learn`</br>`matplotlib`</br>`tqdm`</br>`joblib`</br>`nodejs`|
|Deep learning packages|`PyTorch`</br>`TensorFlow`</br>`Keras`</br>`Horovod`</br>`MLFlow`</br>`pandas-ml`</br>`scrapbook`|
|ONNX packages|`keras2onnx`</br>`onnx`</br>`onnxconverter-common`</br>`skl2onnx`</br>`onnxmltools`|
|Azure Machine Learning Python samples||

Python packages are all installed in the **Python 3.8 - AzureML** environment. Compute instance has Ubuntu 20.04 as the base OS.

## Accessing files

Notebooks and Python scripts are stored in the default storage account of your workspace in Azure file share.  These files are located under your “User files” directory. This storage makes it easy to share notebooks between compute instances. The storage account also keeps your notebooks safely preserved when you stop or delete a compute instance.

The Azure file share account of your workspace is mounted as a drive on the compute instance. This drive is the default working directory for Jupyter, Jupyter Labs, RStudio, and Posit Workbench. This means that the notebooks and other files you create in Jupyter, JupyterLab, RStudio, or Posit are automatically stored on the file share and available to use in other compute instances as well.

The files in the file share are accessible from all compute instances in the same workspace. Any changes to these files on the compute instance will be reliably persisted back to the file share.

You can also clone the latest Azure Machine Learning samples to your folder under the user files directory in the workspace file share.

Writing small files can be slower on network drives than writing to the compute instance local disk itself.  If you're writing many small files, try using a directory directly on the compute instance, such as a `/tmp` directory. Note these files won't be accessible from other compute instances.

Don't store training data on the notebooks file share. You can use the `/tmp` directory on the compute instance for your temporary data.  However, don't write large files of data on the OS disk of the compute instance. OS disk on compute instance has 128-GB capacity. You can also store temporary training data on temporary disk mounted on /mnt. Temporary disk size is based on the VM size chosen and can store larger amounts of data if a higher size VM is chosen. You can also mount [datastores and datasets](v1/concept-azure-machine-learning-architecture.md#datasets-and-datastores). Any software packages you install are saved on the OS disk of compute instance. Note customer managed key encryption is currently not supported for OS disk. The OS disk for compute instance is encrypted with Microsoft-managed keys. 
