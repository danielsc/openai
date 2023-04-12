1. At the top, select **New user**.
1. Select **Invite external user**.
1. Fill in the name and email address for the user.
1. Add a message for the new user.
1. At the bottom of the page, select **Invite**.

    :::image type="content" source="media/how-to-add-users/invite-user.png" alt-text="Invite guest user from Azure Active Directory.":::

Repeat these steps for each of your labelers. You can also use the link at the bottom of the **Invite user** box to invite multiple users in bulk.

> [!TIP]
> Inform your labelers that they will receive this email. They must accept the invitation in order to gain access to your project.

## Add users to your workspace

Now that you added your labelers to the system, you can add them to your workspace. 

To add users to your workspace, you must be an owner of the workspace.

1. In [Azure portal](https://portal.azure.com), in the top search field, type **Machine Learning**. 
1. Select **Machine Learning**.
    :::image type="content" source="media/how-to-manage-workspace/find-workspaces.png" alt-text="Search for Azure Machine Learning workspace.":::

1. Select the workspace that contains your data labeling project.
1. On the left, select **Access control (IAM)**.
1. At the top, select **+ Add > Add role assignment**.

    :::image type="content" source="media/how-to-add-users/add-role-assignment.png" alt-text="Add role assignment from your workspace.":::

1. Select the **Labeler** or **Labeling Team Lead** role in the list. Use **Search** if necessary to find it.
1. Select **Next**.
1. In the middle of the page, next to **Members**, select the **+ Select members** link.
1. Select each of the users you want to add. Use **Search** if necessary to find them.
1. At the bottom of the page, select the **Select** button.
1. Select **Next**.
1. Verify that the **Role** is correct, and that your users appear in the **Members** list.
1. Select **Review + assign**.

## For your labelers

Now, your labelers can begin labeling in your project. However, they still need information from you to access the project.

Be sure to create your labeling project before you contact your labelers.

* [Create an image labeling project](how-to-create-image-labeling-projects.md).
* [Create a text labeling project (preview)](how-to-create-text-labeling-projects.md)

Send the following information to your labelers, after you fill in your workspace and project names:

1. Accept the invite from **Microsoft Invitations (invites@microsoft.com)**.
1. Follow the steps on the web page after you accept. Don't worry if, at the end, you find yourself on a page that says you don't have any apps.
1. Open [Azure Machine Learning studio](https://ml.azure.com).
1. Use the dropdown to select the workspace **\<workspace-name\>**.
1. Select the **Label data** tool for **\<project-name\>**.
    :::image type="content" source="media/how-to-add-users/label-data.png" alt-text="Screenshot showing the label data tool.":::
1. For more information about how to label data, see [Labeling images and text documents](how-to-label-data.md).

## Next steps

* Learn more about [working with a data labeling vendor company](how-to-outsource-data-labeling.md)
* [Create an image labeling project and export labels](how-to-create-image-labeling-projects.md)
* [Create a text labeling project and export labels (preview)](how-to-create-text-labeling-projects.md)