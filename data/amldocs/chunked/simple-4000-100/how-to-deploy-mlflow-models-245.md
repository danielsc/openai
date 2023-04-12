

For more information about MLflow built-in deployment tools, see [MLflow documentation section](https://www.mlflow.org/docs/latest/models.html#built-in-deployment-tools).

## How to customize inference when deploying MLflow models

You may be used to author scoring scripts to customize how inference is executed for your models. However, when deploying MLflow models to Azure Machine Learning, the decision about how inference should be executed is done by the model builder (the person who built the model) rather than by the DevOps engineer (the person who is trying to deploy it). Features like `autolog` in MLflow automatically log models for you at the best of the knowledge of the framework. Those decisions may not be the ones you want in some scenarios.

For those cases, you can either [change how your model is being logged in the training routine](#change-how-your-model-is-logged-during-training) or [customize inference with a scoring script](#customize-inference-with-a-scoring-script).


### Change how your model is logged during training

When you log a model using either `mlflow.autolog` or using `mlflow.<flavor>.log_model`, the flavor used for the model decides how inference should be executed and what gets returned by the model. MLflow doesn't enforce any specific behavior in how the `predict()` function generates results. However, there are scenarios where you probably want to do some pre-processing or post-processing before and after your model is executed. On another scenarios, you may want to change what's returned like probabilities vs classes.

A solution to this scenario is to implement machine learning pipelines that moves from inputs to outputs directly. For instance, [`sklearn.pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) or [`pyspark.ml.Pipeline`](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.Pipeline.html) are popular (and sometimes encourageable for performance considerations) ways to do so. Another alternative is to [customize how your model does inference using a custom model flavor](how-to-log-mlflow-models.md?#logging-custom-models).

### Customize inference with a scoring script

Although MLflow models don't require a scoring script, you can still provide one if needed. You can use it to customize how inference is executed for MLflow models. To learn how to do it, refer to [Customizing MLflow model deployments (Online Endpoints)](how-to-deploy-mlflow-models-online-endpoints.md#customizing-mlflow-model-deployments) and [Customizing MLflow model deployments (Batch Endpoints)](how-to-mlflow-batch.md#customizing-mlflow-models-deployments-with-a-scoring-script).

> [!IMPORTANT]
> When you opt-in to indicate a scoring script for an MLflow model deployment, you also need to provide an environment for it.

## Next steps

To learn more, review these articles:

- [Deploy MLflow models to online endpoints](how-to-deploy-mlflow-models-online-endpoints.md)
- [Progressive rollout of MLflow models](how-to-deploy-mlflow-models-online-progressive.md)
- [Deploy MLflow models to Batch Endpoints](how-to-mlflow-batch.md)
