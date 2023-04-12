
# ONNX and Azure Machine Learning: Create and accelerate ML models

Learn how using the [Open Neural Network Exchange](https://onnx.ai) (ONNX) can help optimize the inference of your machine learning model. Inference, or model scoring, is the phase where the deployed model is used for prediction, most commonly on production data. 

Optimizing machine learning models for inference (or model scoring) is difficult since you need to tune the model and the inference library to make the most of the hardware capabilities. The problem becomes extremely hard if you want to get optimal performance on different kinds of platforms (cloud/edge, CPU/GPU, etc.), since each one has different capabilities and characteristics. The complexity increases if you have models from a variety of frameworks that need to run on a variety of platforms. It's very time consuming to optimize all the different combinations of frameworks and hardware. A solution to train once in your preferred framework and run anywhere on the cloud or edge is needed. This is where ONNX comes in.

Microsoft and a community of partners created ONNX as an open standard for representing machine learning models. Models from [many frameworks](https://onnx.ai/supported-tools) including TensorFlow, PyTorch, SciKit-Learn, Keras, Chainer, MXNet, MATLAB, and SparkML can be exported or converted to the standard ONNX format. Once the models are in the ONNX format, they can be run on a variety of platforms and devices.

[ONNX Runtime](https://onnxruntime.ai) is a high-performance inference engine for deploying ONNX models to production. It's optimized for both cloud and edge and works on Linux, Windows, and Mac. Written in C++, it also has C, Python, C#, Java, and JavaScript (Node.js) APIs for usage in a variety of environments. ONNX Runtime supports both DNN and traditional ML models and integrates with accelerators on different hardware such as TensorRT on NVidia GPUs, OpenVINO on Intel processors, DirectML on Windows, and more. By using ONNX Runtime, you can benefit from the extensive production-grade optimizations, testing, and ongoing improvements.

ONNX Runtime is used in high-scale Microsoft services such as Bing, Office, and Azure Cognitive Services. Performance gains are dependent on a number of factors, but these Microsoft services have seen an __average 2x performance gain on CPU__. In addition to Azure Machine Learning services, ONNX Runtime also runs in other products that support Machine Learning workloads, including:
+ Windows: The runtime is built into Windows as part of [Windows Machine Learning](/windows/ai/windows-ml/) and runs on hundreds of millions of devices. 
+ Azure SQL product family: Run native scoring on data in [Azure SQL Edge](../azure-sql-edge/onnx-overview.md) and [Azure SQL Managed Instance](/azure/azure-sql/managed-instance/machine-learning-services-overview).
+ ML.NET: [Run ONNX models in ML.NET](/dotnet/machine-learning/tutorials/object-detection-onnx).


[![ONNX flow diagram showing training, converters, and deployment](./media/concept-onnx/onnx.png)](././media/concept-onnx/onnx.png#lightbox)

## Get ONNX models

You can obtain ONNX models in several ways:
+ Train a new ONNX model in Azure Machine Learning (see examples at the bottom of this article) or by using [automated Machine Learning capabilities](concept-automated-ml.md#automl--onnx)
+ Convert existing model from another format to ONNX (see the [tutorials](https://github.com/onnx/tutorials)) 
+ Get a pre-trained ONNX model from the [ONNX Model Zoo](https://github.com/onnx/models)
+ Generate a customized ONNX model from [Azure Custom Vision service](../cognitive-services/custom-vision-service/index.yml) 

Many models including image classification, object detection, and text processing can be represented as ONNX models. If you run into an issue with a model that cannot be converted successfully, please file an issue in the GitHub of the respective converter that you used. You can continue using your existing format model until the issue is addressed.
