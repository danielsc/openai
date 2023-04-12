1. To create a new Azure Resource Group, use the following command. Replace `exampleRG` with your resource group name, and `eastus` with the Azure region you want to use:

    # [Azure CLI](#tab/cli)

    ```azurecli
    az group create --name exampleRG --location eastus
    ```
    # [Azure PowerShell](#tab/ps1)

    ```azurepowershell
    New-AzResourceGroup -Name exampleRG -Location eastus
    ```


1. To run the template, use the following command. Replace the `prefix` with a unique prefix. The prefix will be used when creating Azure resources that are required for Azure Machine Learning. Replace the `securepassword` with a secure password for the jump box. The password is for the login account for the jump box (`azureadmin` in the examples below):

    > [!TIP]
    > The `prefix` must be 5 or less characters. It can't be entirely numeric or contain the following characters: `~ ! @ # $ % ^ & * ( ) = + _ [ ] { } \ | ; : . ' " , < > / ?`.

    # [Azure CLI](#tab/cli)

    ```azurecli
    az deployment group create \
        --resource-group exampleRG \
        --template-file main.bicep \
        --parameters \
        prefix=prefix \
        dsvmJumpboxUsername=azureadmin \
        dsvmJumpboxPassword=securepassword
    ```
    # [Azure PowerShell](#tab/ps1)

    ```azurepowershell
    $dsvmPassword = ConvertTo-SecureString "mysecurepassword" -AsPlainText -Force
    New-AzResourceGroupDeployment -ResourceGroupName exampleRG `
        -TemplateFile ./main.bicep `
        -prefix "prefix" `
        -dsvmJumpboxUsername "azureadmin" `
        -dsvmJumpboxPassword $dsvmPassword
    ```

    > [!WARNING]
    > You should avoid using plain text strings in script or from the command line. The plain text can show up in event logs and command history. For more information, see [ConvertTo-SecureString](/powershell/module/microsoft.powershell.security/convertto-securestring).


# [Terraform](#tab/terraform)

To run the Terraform template, use the following commands from the `201-machine-learning-moderately-secure` directory where the template files are:

1. To initialize the directory for working with Terraform, use the following command:

    ```azurecli
    terraform init
    ```

1. To create a configuration, use the following command. Use the `-var` parameter to set the value for the variables used by the template. For a full list of variables, see the [variables.tf](https://github.com/Azure/terraform/blob/master/quickstart/201-machine-learning-moderately-secure/variables.tf) file:

    ```azurecli
    terraform plan \
        -var name=myworkspace \
        -var environment=dev \
        -var location=westus \
        -var dsvm_name=jumpbox \
        -var dsvm_host_password=secure_password \
        -out azureml.tfplan
    ```

    After this command completes, the configuration is displayed in the terminal. To display it again, use the `terraform show azureml.tfplan` command.

1. To run the template and apply the saved configuration to your Azure subscription, use the following command:

    ```azurecli
    terraform apply azureml.tfplan
    ```

    The progress is displayed as the template is processed.


## Connect to the workspace

After the template completes, use the following steps to connect to the DSVM:

1. From the [Azure portal](https://portal.azure.com), select the Azure Resource Group you used with the template. Then, select the Data Science Virtual Machine that was created by the template. If you have trouble finding it, use the filters section to filter the __Type__ to __virtual machine__.

    :::image type="content" source="./media/tutorial-create-secure-workspace-template/select-vm.png" alt-text="Screenshot of filtering and selecting the vm.":::

1. From the __Overview__ section of the Virtual Machine, select __Connect__, and then select __Bastion__ from the dropdown.

    :::image type="content" source="./media/tutorial-create-secure-workspace-template/connect-bastion.png" alt-text="Screenshot of selecting to connect using Bastion.":::
