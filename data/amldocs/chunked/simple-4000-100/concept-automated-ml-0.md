
# What is automated machine learning (AutoML)?

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
> [!div class="op_single_selector" title1="Select the version of the Azure Machine Learning Python SDK you are using:"]
> * [v1](./v1/concept-automated-ml-v1.md)
> * [v2 (current version)](concept-automated-ml.md)

Automated machine learning, also referred to as automated ML or AutoML, is the process of automating the time-consuming, iterative tasks of machine learning model development. It allows data scientists, analysts, and developers to build ML models with high scale, efficiency, and productivity all while sustaining model quality. Automated ML in Azure Machine Learning is based on a breakthrough from our [Microsoft Research division](https://www.microsoft.com/research/project/automl/).

* For code-experienced customers, [Azure Machine Learning Python SDK](https://aka.ms/sdk-v2-install).  Get started with [Tutorial: Train an object detection model (preview) with AutoML and Python](tutorial-auto-train-image-models.md).


## How does AutoML work?

During training, Azure Machine Learning creates a number of pipelines in parallel that try different algorithms and parameters for you. The service iterates through ML algorithms paired with feature selections, where each iteration produces a model with a training score. The better the score for the metric you want to optimize for, the better the model is considered to "fit" your data.  It will stop once it hits the exit criteria defined in the experiment. 

Using **Azure Machine Learning**, you can design and run your automated ML training experiments with these steps:

1. **Identify the ML problem** to be solved: classification, forecasting, regression, computer vision or NLP.

1. **Choose whether you want a code-first experience or a no-code studio web experience**: Users who prefer a code-first experience can use the [AzureML SDKv2](how-to-configure-auto-train.md) or the [AzureML CLIv2](how-to-train-cli.md). Get started with [Tutorial: Train an object detection model with AutoML and Python](tutorial-auto-train-image-models.md). Users who prefer a limited/no-code experience can use the [web interface](how-to-use-automated-ml-for-ml-models.md) in Azure Machine Learning studio at [https://ml.azure.com](https://ml.azure.com/).  Get started with [Tutorial: Create a classification model with automated ML in Azure Machine Learning](tutorial-first-experiment-automated-ml.md).
    
1. **Specify the source of the labeled training data**: You can bring your data to AzureML in [many different ways](concept-data.md).

1. **Configure the automated machine learning parameters** that determine how many iterations over different models, hyperparameter settings, advanced preprocessing/featurization, and what metrics to look at when determining the best model.  
1. **Submit the training job.**

1. **Review the results** 

The following diagram illustrates this process. 
![Automated Machine learning](./media/concept-automated-ml/automl-concept-diagram2.png)


You can also inspect the logged job information, which [contains metrics](how-to-understand-automated-ml.md) gathered during the job. The training job produces a Python serialized object (`.pkl` file) that contains the model and data preprocessing.

While model building is automated, you can also [learn how important or relevant features are](./v1/how-to-configure-auto-train-v1.md#explain) to the generated models.

## When to use AutoML: classification, regression, forecasting, computer vision & NLP

Apply automated ML when you want Azure Machine Learning to train and tune a model for you using the target metric you specify. Automated ML democratizes the machine learning model development process, and empowers its users, no matter their data science expertise, to identify an end-to-end machine learning pipeline for any problem.

ML professionals and developers across industries can use automated ML to:
+ Implement ML solutions without extensive programming knowledge
