Many models including image classification, object detection, and text processing can be represented as ONNX models. If you run into an issue with a model that cannot be converted successfully, please file an issue in the GitHub of the respective converter that you used. You can continue using your existing format model until the issue is addressed.

## Deploy ONNX models in Azure

With Azure Machine Learning, you can deploy, manage, and monitor your ONNX models. Using the standard [deployment workflow](concept-model-management-and-deployment.md) and ONNX Runtime, you can create a REST endpoint hosted in the cloud. See example Jupyter notebooks at the end of this article to try it out for yourself. 

### Install and use ONNX Runtime with Python

Python packages for ONNX Runtime are available on [PyPi.org](https://pypi.org) ([CPU](https://pypi.org/project/onnxruntime), [GPU](https://pypi.org/project/onnxruntime-gpu)). Please read [system requirements](https://github.com/Microsoft/onnxruntime#system-requirements) before installation.	

 To install ONNX Runtime for Python, use one of the following commands:	
```python	
pip install onnxruntime	      # CPU build
pip install onnxruntime-gpu   # GPU build
```

To call ONNX Runtime in your Python script, use:	
```python
import onnxruntime
session = onnxruntime.InferenceSession("path to model")
```

The documentation accompanying the model usually tells you the inputs and outputs for using the model. You can also use a visualization tool such as [Netron](https://github.com/lutzroeder/Netron) to view the model. ONNX Runtime also lets you query the model metadata, inputs, and outputs:	
```python
session.get_modelmeta()
first_input_name = session.get_inputs()[0].name
first_output_name = session.get_outputs()[0].name
```

To inference your model, use `run` and pass in the list of outputs you want returned (leave empty if you want all of them) and a map of the input values. The result is a list of the outputs.	
```python
results = session.run(["output1", "output2"], {
                      "input1": indata1, "input2": indata2})
results = session.run([], {"input1": indata1, "input2": indata2})
```

For the complete Python API reference, see the [ONNX Runtime reference docs](https://onnxruntime.ai/docs/api/python/api_summary.html).	

## Examples
See [how-to-use-azureml/deployment/onnx](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/deployment/onnx) for example Python notebooks that create and deploy ONNX models.

[!INCLUDE [aml-clone-in-azure-notebook](../../includes/aml-clone-for-examples.md)]

Samples for usage in other languages can be found in the [ONNX Runtime GitHub](https://github.com/microsoft/onnxruntime/tree/master/samples).

## More info

Learn more about **ONNX** or contribute to the project:
+ [ONNX project website](https://onnx.ai)
+ [ONNX code on GitHub](https://github.com/onnx/onnx)

Learn more about **ONNX Runtime** or contribute to the project:
+ [ONNX Runtime project website](https://onnxruntime.ai)
+ [ONNX Runtime GitHub Repo](https://github.com/Microsoft/onnxruntime)
