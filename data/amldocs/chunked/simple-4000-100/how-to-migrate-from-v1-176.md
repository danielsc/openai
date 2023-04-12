With v2, you should separate your machine learning code from the control plane code. This separation allows for easier iteration and allows for easier transition between local and cloud. We also recommend using MLflow for tracking and model logging. See the [MLflow concept article](concept-mlflow.md) for details.

### Production model deployment

We recommend v2 for production model deployment. Managed endpoints abstract the IT overhead and provide a performant solution for deploying and scoring models, both for online (near real-time) and batch (massively parallel) scenarios.

Kubernetes deployments are supported in v2 through AKS or Azure Arc, enabling Azure cloud and on-premises deployments managed by your organization.

### Machine learning operations (MLOps)

A MLOps workflow typically involves CI/CD through an external tool. Typically a CLI is used in CI/CD, though you can alternatively invoke Python or directly use REST.

The solution accelerator for MLOps with v2 is being developed at https://github.com/Azure/mlops-v2 and can be used as reference or adopted for setup and automation of the machine learning lifecycle.

### A note on GitOps with v2

A key paradigm with v2 is serializing machine learning entities as YAML files for source control with `git`, enabling better GitOps approaches than were possible with v1. For instance, you could enforce policy by which only a service principal used in CI/CD pipelines can create/update/delete some or all entities, ensuring changes go through a governed process like pull requests with required reviewers. Since the files in source control are YAML, they're easy to diff and track changes over time. You and your team may consider shifting to this paradigm as you upgrade to v2.

You can obtain a YAML representation of any entity with the CLI via `az ml <entity> show --output yaml`. Note that this output will have system-generated properties, which can be ignored or deleted.

## Next steps

- [Get started with the CLI (v2)](how-to-configure-cli.md)
- [Get started with the Python SDK (v2)](https://aka.ms/sdk-v2-install)
