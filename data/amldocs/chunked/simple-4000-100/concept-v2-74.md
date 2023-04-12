    Azure ML offers [endpoints](concept-endpoints.md) to streamline model deployments for both real-time and batch inference deployments. This functionality is available only via CLI v2 and SDK v2.

## Should I use v1 or v2?

### CLI v2

The Azure Machine Learning CLI v1 has been deprecated. We recommend you to use CLI v2 if:

* You were a CLI v1 user
* You want to use new features like - reusable components, managed inferencing
* You don't want to use a Python SDK - CLI v2 allows you to use YAML with scripts in python, R, Java, Julia or C#
* You were a user of R SDK previously - Azure ML won't support an SDK in `R`. However, the CLI v2 has support for `R` scripts.
* You want to use command line based automation/deployments
* You don't need Spark Jobs. This feature is currently available in preview in CLI v2.

### SDK v2

The Azure Machine Learning Python SDK v1 doesn't have a planned deprecation date. If you have significant investments in Python SDK v1 and don't need any new features offered by SDK v2, you can continue to use SDK v1. However, you should consider using SDK v2 if:

* You want to use new features like - reusable components, managed inferencing
* You're starting a new workflow or pipeline - all new features and future investments will be introduced in v2
* You want to take advantage of the improved usability of the Python SDK v2 - ability to compose jobs and pipelines using Python functions, easy evolution from simple to complex tasks etc.
* You don't need Spark Jobs. This feature is currently available in preview in SDK v2.

## Next steps

* [How to upgrade from v1 to v2](how-to-migrate-from-v1.md)
* Get started with CLI v2

    * [Install and set up CLI (v2)](how-to-configure-cli.md)
    * [Train models with the CLI (v2)](how-to-train-model.md)
    * [Deploy and score models with online endpoints](how-to-deploy-online-endpoints.md)
    
* Get started with SDK v2

    * [Install and set up SDK (v2)](https://aka.ms/sdk-v2-install)
    * [Train models with the Azure ML Python SDK v2](how-to-train-model.md)
    * [Tutorial: Create production ML pipelines with Python SDK v2 in a Jupyter notebook](tutorial-pipeline-python-sdk.md)
