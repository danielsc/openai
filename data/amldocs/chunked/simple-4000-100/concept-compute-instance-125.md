> The compute instance has 120GB OS disk. If you run out of disk space and get into an unusable state, please clear at least 5 GB disk space on OS disk (mounted on /) through the compute instance terminal by removing files/folders and then do `sudo reboot`. Temporary disk will be freed after restart; you do not need to clear space on temp disk manually. To access the terminal go to compute list page or compute instance details page and click on **Terminal** link. You can check available disk space by running `df -h` on the terminal. Clear at least 5 GB space before doing `sudo reboot`. Please do not stop or restart the compute instance through the Studio until 5 GB disk space has been cleared. Auto shutdowns, including scheduled start or stop as well as idle shutdowns(preview), will not work if the CI disk is full.

## Next steps

* [Quickstart: Create workspace resources you need to get started with Azure Machine Learning](quickstart-create-resources.md).
* [Tutorial: Train your first ML model](tutorial-1st-experiment-sdk-train.md) shows how to use a compute instance with an integrated notebook.
