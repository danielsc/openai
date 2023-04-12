Support for computer vision tasks allows you to easily generate models trained on image data for scenarios like image classification and object detection. 

With this capability you can: 
 
* Seamlessly integrate with the [Azure Machine Learning data labeling](./how-to-create-image-labeling-projects.md) capability
* Use labeled data for generating image models
* Optimize model performance by specifying the model algorithm and tuning the hyperparameters. 
* Download or deploy the resulting model as a web service in Azure Machine Learning. 
* Operationalize at scale, leveraging Azure Machine Learning [MLOps](concept-model-management-and-deployment.md) and [ML Pipelines](concept-ml-pipelines.md) capabilities. 

Authoring AutoML models for vision tasks is supported via the Azure ML Python SDK. The resulting experimentation jobs, models, and outputs can be accessed from the Azure Machine Learning studio UI.

Learn how to [set up AutoML training for computer vision models](how-to-auto-train-image-models.md).

![Computer vision tasks examples. Image from: http://cs231n.stanford.edu/slides/2021/lecture_15.pdf ](./media/concept-automated-ml/automl-computer-vision-tasks.png)
Image from: http://cs231n.stanford.edu/slides/2021/lecture_15.pdf

Automated ML for images supports the following computer vision tasks: 

Task | Description
----|----
Multi-class image classification | Tasks where an image is classified with only a single label from a set of classes - e.g. each image is classified as either an image of a 'cat' or a 'dog' or a 'duck'
Multi-label image classification | Tasks where an image could have one or more labels from a set of labels - e.g. an image could be labeled with both 'cat' and 'dog'
Object detection| Tasks to identify objects in an image and locate each object with a bounding box e.g. locate all dogs and cats in an image and draw a bounding box around each.
Instance segmentation | Tasks to identify objects in an image at the pixel level, drawing a polygon around each object in the image.

<a name="nlp"></a>

### Natural language processing: NLP

Support for natural language processing (NLP) tasks in automated ML allows you to easily generate models trained on text data for text classification and named entity recognition scenarios. Authoring automated ML trained NLP models is supported via the Azure Machine Learning Python SDK. The resulting experimentation jobs, models, and outputs can be accessed from the Azure Machine Learning studio UI.

The NLP capability supports:

* End-to-end deep neural network NLP training with the latest pre-trained BERT models
* Seamless integration with [Azure Machine Learning data labeling](how-to-create-text-labeling-projects.md)
* Use labeled data for generating NLP models
* Multi-lingual support with 104 languages
* Distributed training with Horovod

Learn how to [set up AutoML training for NLP models](how-to-auto-train-nlp-models.md). 


## Training, validation and test data 

With automated ML you provide the **training data** to train ML models, and you can specify what type of model validation to perform. Automated ML performs model validation as part of training. That is, automated ML uses **validation data** to tune model hyperparameters based on the applied algorithm to find the combination that best fits the training data. However, the same validation data is used for each iteration of tuning, which introduces model evaluation bias since the model continues to improve and fit to the validation data. 

To help confirm that such bias isn't applied to the final recommended model, automated ML supports the use of **test data** to evaluate the final model that automated ML recommends at the end of your experiment. When you provide test data as part of your AutoML experiment configuration, this recommended model is tested by default at the end of your experiment (preview). 

>[!IMPORTANT]
> Testing your models with a test dataset to evaluate generated models is a preview feature. This capability is an [experimental](/python/api/overview/azure/ml/#stable-vs-experimental) preview feature, and may change at any time.
