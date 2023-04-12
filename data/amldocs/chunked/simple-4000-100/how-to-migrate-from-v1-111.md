In v2, "experiments", "runs", and "pipelines" are consolidated into jobs. A job has a type. Most jobs are `command` jobs that run a command, like `python main.py`. What runs in a job is agnostic to any programming language, so you can run `bash` scripts, invoke `python` interpreters, run a bunch of `curl` commands, or anything else. Another common type of job is `pipeline`, which defines child jobs that may have input/output relationships, forming a directed acyclic graph (DAG).

For a comparison of SDK v1 and v2 code, see 
* [Run a script](migrate-to-v2-command-job.md)
* [Local runs](migrate-to-v2-local-runs.md)
* [Hyperparameter tuning](migrate-to-v2-execution-hyperdrive.md)
* [Parallel Run](migrate-to-v2-execution-parallel-run-step.md)
* [Pipelines](migrate-to-v2-execution-pipeline.md)
* [AutoML](migrate-to-v2-execution-automl.md)

### Designer

You can use designer to build pipelines using your own v2 custom components and the new prebuilt components from registry. In this situation, you can use v1 or v2 data assets in your pipeline. 

You can continue to use designer to build pipelines using classic prebuilt components and v1 dataset types (tabular, file). You cannot use existing designer classic prebuilt components with v2 data asset.

You cannot build a pipeline using both existing designer classic prebuilt components and v2 custom components.

### Data (datasets in v1)

Datasets are renamed to data assets. *Backwards compatibility* is provided, which means you can use V1 Datasets in V2. When you consume a V1 Dataset in a V2 job you will notice they are automatically mapped into V2 types as follows:

* V1 FileDataset = V2 Folder (`uri_folder`)
* V1 TabularDataset = V2 Table (`mltable`)

It should be noted that *forwards compatibility* is **not** provided, which means you **cannot** use V2 data assets in V1.

This article talks more about handling data in v2 - [Read and write data in a job](how-to-read-write-data-v2.md)

For a comparison of SDK v1 and v2 code, see [Data assets in SDK v1 and v2](migrate-to-v2-assets-data.md).

### Model

Models created from v1 can be used in v2. 

For a comparison of SDK v1 and v2 code, see [Model management in SDK v1 and SDK v2](migrate-to-v2-assets-model.md)

### Environment

Environments created from v1 can be used in v2. In v2, environments have new features like creation from a local Docker context.

## Managing secrets

The management of Key Vault secrets differs significantly in V2 compared to V1. The V1 set_secret and get_secret SDK methods are not available in V2. Instead, direct access using Key Vault client libraries should be used.

For details about Key Vault, see [Use authentication credential secrets in Azure Machine Learning training jobs](how-to-use-secrets-in-runs.md).

## Scenarios across the machine learning lifecycle

There are a few scenarios that are common across the machine learning lifecycle using Azure ML. We'll look at a few and give general recommendations for upgrading to v2.

### Azure setup

Azure recommends Azure Resource Manager templates (often via Bicep for ease of use) to create resources. The same is a good approach for creating Azure ML resources as well.

If your team is only using Azure ML, you may consider provisioning the workspace and any other resources via YAML  files and CLI instead.

### Prototyping models

We recommend v2 for prototyping models. You may consider using the CLI for an interactive use of Azure ML, while your model training code is Python or any other programming language. Alternatively, you may adopt a full-stack approach with Python solely using the Azure ML SDK or a mixed approach with the Azure ML Python SDK and YAML files.

### Production model training

We recommend v2 for production model training. Jobs consolidate the terminology and provide a set of consistency that allows for easier transition between types (for example, `command` to `sweep`) and a GitOps-friendly process for serializing jobs into YAML files.

With v2, you should separate your machine learning code from the control plane code. This separation allows for easier iteration and allows for easier transition between local and cloud. We also recommend using MLflow for tracking and model logging. See the [MLflow concept article](concept-mlflow.md) for details.
