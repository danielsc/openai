1. Expand the subscription node that contains your workspace.
1. Expand the **Models** node inside your workspace.
1. Right-click the model you want to delete and select **Remove Model**.
1. A prompt appears confirming you want to remove the model. Select **Ok**.

Alternatively, use the `> Azure ML: Remove Model` command in the command palette.

## Endpoints

For more information, see [endpoints](v1/concept-azure-machine-learning-architecture.md#endpoints).

### Create endpoint

1. Expand the subscription node that contains your workspace.
1. Expand your workspace node.
1. Right-click the **Models** node in your workspace and select **Create Endpoint**.
1. Choose your endpoint type.
1. A specification file appears. Configure the specification file.
1. Right-click the specification file and select **Azure ML: Execute YAML**.

Alternatively, use the `> Azure ML: Create Endpoint` command in the command palette.

### Delete endpoint

1. Expand the subscription node that contains your workspace.
1. Expand the **Endpoints** node inside your workspace.
1. Right-click the deployment you want to remove and select **Remove Service**.
1. A prompt appears confirming you want to remove the service. Select **Ok**.

Alternatively, use the `> Azure ML: Remove Service` command in the command palette.

### View service properties

In addition to creating and deleting deployments, you can view and edit settings associated with the deployment.

1. Expand the subscription node that contains your workspace.
1. Expand the **Endpoints** node inside your workspace.
1. Right-click the deployment you want to manage:
    - To view deployment configuration settings, select **View Service Properties**.

Alternatively, use the `> Azure ML: View Service Properties` command in the command palette.

## Next steps

[Train an image classification model](tutorial-train-deploy-image-classification-model-vscode.md) with the VS Code extension.
