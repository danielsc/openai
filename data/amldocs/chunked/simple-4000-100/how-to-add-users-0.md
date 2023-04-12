
# Add users to your data labeling project

This article shows how to add users to your data labeling project so that they can label data, but can't see the rest of your workspace. These steps can add anyone to your project, whether or not they are from a [data labeling vendor company](how-to-outsource-data-labeling.md).
  
## Prerequisites

* An Azure subscription. If you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free) before you begin.
* An Azure Machine Learning workspace. See [Create workspace resources](quickstart-create-resources.md).

You need certain permission levels to follow the steps in this article. If you can't follow one of the steps because of a permissions issue, contact your administrator to request the appropriate permissions.

* To add a guest user, your organization's external collaboration settings needs the correct configuration to allow you to invite guests.
* To add a custom role, you must have `Microsoft.Authorization/roleAssignments/write` permissions for your subscription - for example, [User Access Administrator](../../articles/role-based-access-control/built-in-roles.md#user-access-administrator) or [Owner](../../articles/role-based-access-control/built-in-roles.md#owner).
* To add users to your workspace, you must be an **Owner** of the workspace.

## Add custom role

To add a custom role, you must have `Microsoft.Authorization/roleAssignments/write` permissions for your subscription - for example, [User Access Administrator](../../articles/role-based-access-control/built-in-roles.md).

1. Open your workspace in [Azure Machine Learning studio](https://ml.azure.com)
1. Open the menu on the top right, and select **View all properties in Azure Portal**. You use the Azure portal for the remaining steps in this article.
1. Select the **Resource group** link in the middle of the page.
1. On the left, select **Access control (IAM)**.
1. At the top, select **+ Add > Add custom role**.
1. For the **Custom role name**, type the name you want to use. For example, **Labeler**.
1. In the **Description** box, add a description. For example, **Labeler access for data labeling projects**.
1. Select **Start from JSON**.
1. At the bottom of the page, select **Next**.
1. Don't do anything for the **Permissions** tab. You add permissions in a later step. Select **Next**.
1. The **Assignable scopes** tab shows your subscription information. Select **Next**.
1. In the **JSON** tab, above the edit box, select **Edit**.
1. Select lines starting with **"actions:"** and **"notActions:"**.

    :::image type="content" source="media/how-to-add-users/replace-lines.png" alt-text="Create custom role: select lines to replace them in the editor.":::

1. Replace these two lines with the `Actions` and `NotActions` from the appropriate role listed at [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md#data-labeling). Make sure to copy from `Actions` through the closing bracket, `],`

1. Select **Save** at the top of the edit box to save your changes.

    > [!IMPORTANT]
    > Don't select **Next** until you've saved your edits.

1. After you save your edits, select **Next**.
1. Select **Create** to create the custom role.
1. Select **OK**.

## Add guest user

If your labelers are outside of your organization, add them, so they can access your workspace. If labelers are already inside your organization, skip this step.

To add a guest user, your organization's external collaboration settings need the correct configuration to allow you to invite guests.

1. In [Azure portal](https://portal.azure.com), in the top-left corner, expand the menu and select **Azure Active Directory**.

    :::image type="content" source="media/how-to-add-users/menu-active-directory.png" alt-text="Select Azure Active Directory from the menu.":::

1. On the left, select **Users**.
1. At the top, select **New user**.
1. Select **Invite external user**.
1. Fill in the name and email address for the user.
