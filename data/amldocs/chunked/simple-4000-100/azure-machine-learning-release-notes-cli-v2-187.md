  - Added support for command components ([command component YAML schema](reference-yaml-component-command.md))
- `az ml online-endpoint`
  - `az ml endpoint` subgroup split into two separate groups: `az ml online-endpoint` and `az ml batch-endpoint`
  - Updated [online endpoint YAML schema](reference-yaml-endpoint-online.md)
  - Added support for local endpoints for dev/test scenarios
  - Added interactive VSCode debugging support for local endpoints (added the `--vscode-debug` flag to `az ml batch-endpoint create/update`)
- `az ml online-deployment`
  - `az ml deployment` subgroup split into two separate groups: `az ml online-deployment` and `az ml batch-deployment`
  - Updated [managed online deployment YAML schema](reference-yaml-deployment-managed-online.md)
  - Added autoscaling support via integration with Azure Monitor Autoscale
  - Added support for updating multiple online deployment properties in the same update operation
  - Added support for performing concurrent operations on deployments under the same endpoint
- `az ml batch-endpoint`
  - `az ml endpoint` subgroup split into two separate groups: `az ml online-endpoint` and `az ml batch-endpoint`
  - Updated [batch endpoint YAML schema](reference-yaml-endpoint-batch.md)
  - Removed `traffic` property; replaced with a configurable default deployment property
  - Added support for input data URIs for `az ml batch-endpoint invoke`
  - Added support for VNet ingress (private link)
- `az ml batch-deployment`
  - `az ml deployment` subgroup split into two separate groups: `az ml online-deployment` and `az ml batch-deployment`
  - Updated [batch deployment YAML schema](reference-yaml-deployment-batch.md)

## 2021-05-25

### Announcing the CLI (v2) for Azure Machine Learning

The `ml` extension to the Azure CLI is the next-generation interface for Azure Machine Learning. It enables you to train and deploy models from the command line, with features that accelerate scaling data science up and out while tracking the model lifecycle. [Install and get started](how-to-configure-cli.md).
