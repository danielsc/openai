| Control/Command + Home        | Go to cell start|                                
| Control/Command + End         | Go to cell end   |                               
| Control/Command + Left        | Go one word left |                               
| Control/Command + Right       | Go one word right |                              
| Control/Command + Backspace   | Delete word before |                             
| Control/Command + Delete      | Delete word after |                              
| Control/Command + /           | Toggle comment on cell

## Troubleshooting

* **Connecting to a notebook**: If you can't connect to a notebook, ensure that web socket communication is **not** disabled. For compute instance Jupyter functionality to work, web socket communication must be enabled. Ensure your [network allows websocket connections](how-to-access-azureml-behind-firewall.md?tabs=ipaddress#microsoft-hosts) to *.instances.azureml.net and *.instances.azureml.ms. 

* **Private endpoint**: When a compute instance is deployed in a workspace with a private endpoint, it can be only be [accessed from within virtual network](./how-to-secure-training-vnet.md). If you're using custom DNS or hosts file, add an entry for < instance-name >.< region >.instances.azureml.ms with the private IP address of your workspace private endpoint. For more information, see the [custom DNS](./how-to-custom-dns.md?tabs=azure-cli) article.

* **Kernel crash**: If your kernel crashed and was restarted, you can run the following command to look at Jupyter log and find out more details: `sudo journalctl -u jupyter`. If kernel issues persist, consider using a compute instance with more memory.

* **Kernel not found** or **Kernel operations were disabled**: When using the default Python 3.8 kernel on a compute instance, you may get an error such as "Kernel not found" or "Kernel operations were disabled". To fix, use one of the following methods:
    * Create a new compute instance. This will use a new image where this problem has been resolved.
    * Use the Py 3.6 kernel on the existing compute instance.
    * From a terminal in the default py38 environment, run  ```pip install ipykernel==6.6.0``` OR ```pip install ipykernel==6.0.3```

* **Expired token**: If you run into an expired token issue, sign out of your Azure ML studio, sign back in, and then restart the notebook kernel.

* **File upload limit**: When uploading a file through the notebook's file explorer, you're limited files that are smaller than 5 TB. If you need to upload a file larger than this, we recommend that you use the SDK to upload the data to a datastore. For more information, see [Create data assets](how-to-create-data-assets.md?tabs=Python-SDK).

## Next steps

* [Run your first experiment](tutorial-1st-experiment-sdk-train.md)
* [Backup your file storage with snapshots](../storage/files/storage-snapshots-files.md)
* [Working in secure environments](./how-to-secure-training-vnet.md)
