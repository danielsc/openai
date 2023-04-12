With Azure Machine Learning, you can use automated ML to build a Python model and have it converted to the ONNX format. Once the models are in the ONNX format, they can be run on a variety of platforms and devices. Learn more about [accelerating ML models with ONNX](concept-onnx.md).

See how to convert to ONNX format [in this Jupyter notebook example](https://github.com/Azure/azureml-examples/tree/main/v1/python-sdk/tutorials/automl-with-azureml/classification-bank-marketing-all-features). Learn which [algorithms are supported in ONNX](how-to-configure-auto-train.md#supported-algorithms).

The ONNX runtime also supports C#, so you can use the model built automatically in your C# apps without any need for recoding or any of the network latencies that REST endpoints introduce. Learn more about [using an AutoML ONNX model in a .NET application with ML.NET](./how-to-use-automl-onnx-model-dotnet.md) and [inferencing ONNX models with the ONNX runtime C# API](https://onnxruntime.ai/docs/api/csharp-api.html). 

## Next steps

There are multiple resources to get you up and running with AutoML. 

### Tutorials/ how-tos
Tutorials are end-to-end introductory examples of AutoML scenarios.

+ **For a code first experience**, follow the [Tutorial: Train an object detection model with AutoML and Python](tutorial-auto-train-image-models.md)

+ **For a low or no-code experience**, see the [Tutorial: Train a classification model with no-code AutoML in Azure Machine Learning studio](tutorial-first-experiment-automated-ml.md).
   
How-to articles provide additional detail into what functionality automated ML offers. For example, 

+ Configure the settings for automatic training experiments
    + [Without code in the Azure Machine Learning studio](how-to-use-automated-ml-for-ml-models.md). 
    + [With the Python SDK](how-to-configure-auto-train.md).

+  Learn how to [train computer vision models with Python](how-to-auto-train-image-models.md).

+  Learn how to [view the generated code from your automated ML models](how-to-generate-automl-training-code.md).
   
### Jupyter notebook samples 

Review detailed code examples and use cases in the [GitHub notebook repository for automated machine learning samples](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs.


### Python SDK reference

Deepen your expertise of SDK design patterns and class specifications with the [AutoML Job class reference documentation](/python/api/azure-ai-ml/azure.ai.ml.automl). 

> [!Note]
> Automated machine learning capabilities are also available in other Microsoft solutions such as, 
[ML.NET](/dotnet/machine-learning/automl-overview), 
[HDInsight](../hdinsight/spark/apache-spark-run-machine-learning-automl.md), [Power BI](/power-bi/service-machine-learning-automated) and [SQL Server](https://cloudblogs.microsoft.com/sqlserver/2019/01/09/how-to-automate-machine-learning-on-sql-server-2019-big-data-clusters/)
