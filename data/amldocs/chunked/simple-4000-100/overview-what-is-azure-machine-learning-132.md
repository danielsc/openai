Hyperparameter optimization, or hyperparameter tuning, can be a tedious task. Azure Machine Learning can automate this task for arbitrary parameterized commands with little modification to your job definition. Results are visualized in the studio.

See [How to tune hyperparameters](how-to-tune-hyperparameters.md).

### Multinode distributed training

Efficiency of training for deep learning and sometimes classical machine learning training jobs can be drastically improved via multinode distributed training. Azure Machine Learning compute clusters offer the latest GPU options.

Supported via Azure ML Kubernetes and Azure ML compute clusters:

* PyTorch
* TensorFlow
* MPI

The MPI distribution can be used for Horovod or custom multinode logic. Additionally, Apache Spark is supported via Azure Synapse Analytics Spark clusters (preview).

See [Distributed training with Azure Machine Learning](concept-distributed-training.md).

### Embarrassingly parallel training

Scaling a machine learning project may require scaling embarrassingly parallel model training. This pattern is common for scenarios like forecasting demand, where a model may be trained for many stores.

## Deploy models

To bring a model into production, it's deployed. Azure Machine Learning's managed endpoints abstract the required infrastructure for both batch or real-time (online) model scoring (inferencing).

### Real-time and batch scoring (inferencing)

*Batch scoring*, or *batch inferencing*, involves invoking an endpoint with a reference to data. The batch endpoint runs jobs asynchronously to process data in parallel on compute clusters and store the data for further analysis.

*Real-time scoring*, or *online inferencing*, involves invoking an endpoint with one or more model deployments and receiving a response in near-real-time via HTTPs. Traffic can be split across multiple deployments, allowing for testing new model versions by diverting some amount of traffic initially and increasing once confidence in the new model is established.    

See:
 * [Deploy a model with a real-time managed endpoint](how-to-deploy-online-endpoints.md)
 * [Use batch endpoints for scoring](batch-inference/how-to-use-batch-endpoint.md) 


## MLOps: DevOps for machine learning 

DevOps for machine learning models, often called MLOps, is a process for developing models for production. A model's lifecycle from training to deployment must be auditable if not reproducible.

### ML model lifecycle 

![Machine learning model lifecycle * MLOps](./media/overview-what-is-azure-machine-learning/model-lifecycle.png)

Learn more about [MLOps in Azure Machine Learning](concept-model-management-and-deployment.md).

### Integrations enabling MLOPs

Azure Machine Learning is built with the model lifecycle in mind. You can audit the model lifecycle down to a specific commit and environment. 

Some key features enabling MLOps include:

* `git` integration
* MLflow integration
* Machine learning pipeline scheduling
* Azure Event Grid integration for custom triggers
* Easy to use with CI/CD tools like GitHub Actions or Azure DevOps

Also, Azure Machine Learning includes features for monitoring and auditing:
* Job artifacts, such as code snapshots, logs, and other outputs
* Lineage between jobs and assets, such as containers, data, and compute resources

## Next steps

Start using Azure Machine Learning:
- [Set up an Azure Machine Learning workspace](quickstart-create-resources.md)
- [Tutorial: Build a first machine learning project](tutorial-1st-experiment-hello-world.md)
- [How to run training jobs](how-to-train-model.md)
