    :::image type="content" source="./media/tutorial-create-secure-workspace-template/connect-bastion.png" alt-text="Screenshot of selecting to connect using Bastion.":::

1. When prompted, provide the __username__ and __password__ you specified when configuring the template and then select __Connect__.

    > [!IMPORTANT]
    > The first time you connect to the DSVM desktop, a PowerShell window opens and begins running a script. Allow this to complete before continuing with the next step.

1. From the DSVM desktop, start __Microsoft Edge__ and enter `https://ml.azure.com` as the address. Sign in to your Azure subscription, and then select the workspace created by the template. The studio for your workspace is displayed.

## Troubleshooting

### Error: Windows computer name cannot be more than 15 characters long, be entirely numeric, or contain the following characters

This error can occur when the name for the DSVM jump box is greater than 15 characters or includes one of the following characters: `~ ! @ # $ % ^ & * ( ) = + _ [ ] { } \ | ; : . ' " , < > / ?`.

When using the Bicep template, the jump box name is generated programmatically using the prefix value provided to the template. To make sure the name does not exceed 15 characters or contain any invalid characters, use a prefix that is 5 characters or less and do not use any of the following characters in the prefix: `~ ! @ # $ % ^ & * ( ) = + _ [ ] { } \ | ; : . ' " , < > / ?`.

When using the Terraform template, the jump box name is passed using the `dsvm_name` parameter. To avoid this error, use a name that is not greater than 15 characters and does not use any of the following characters as part of the name: `~ ! @ # $ % ^ & * ( ) = + _ [ ] { } \ | ; : . ' " , < > / ?`.

## Next steps

> [!IMPORTANT]
> The Data Science Virtual Machine (DSVM) and any compute instance resources bill you for every hour that they are running. To avoid excess charges, you should stop these resources when they are not in use. For more information, see the following articles:
> 
> * [Create/manage VMs (Linux)](../virtual-machines/linux/tutorial-manage-vm.md).
> * [Create/manage VMs (Windows)](../virtual-machines/windows/tutorial-manage-vm.md).
> * [Create/manage compute instance](how-to-create-manage-compute-instance.md).

To continue learning how to use the secured workspace from the DSVM, see [Tutorial: Azure Machine Learning in a day](tutorial-azure-ml-in-a-day.md).

To learn more about common secure workspace configurations and input/output requirements, see [Azure Machine Learning secure workspace traffic flow](concept-secure-network-traffic-flow.md).
