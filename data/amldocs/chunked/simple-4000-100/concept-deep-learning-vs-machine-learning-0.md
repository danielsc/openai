
# Deep learning vs. machine learning in Azure Machine Learning

This article explains deep learning vs. machine learning and how they fit into the broader category of artificial intelligence. Learn about deep learning solutions you can build on Azure Machine Learning, such as fraud detection, voice and facial recognition, sentiment analysis, and time series forecasting.

For guidance on choosing algorithms for your solutions, see the [Machine Learning Algorithm Cheat Sheet](./algorithm-cheat-sheet.md?WT.mc_id=docs-article-lazzeri).

## Deep learning, machine learning, and AI

![Relationship diagram: AI vs. machine learning vs. deep learning](./media/concept-deep-learning-vs-machine-learning/ai-vs-machine-learning-vs-deep-learning.png)

Consider the following definitions to understand deep learning vs. machine learning vs. AI:

- **Deep learning** is a subset of machine learning that's based on artificial neural networks. The _learning process_ is _deep_ because the structure of artificial neural networks consists of multiple input, output, and hidden layers. Each layer contains units that transform the input data into information that the next layer can use for a certain predictive task. Thanks to this structure, a machine can learn through its own data processing.

- **Machine learning** is a subset of artificial intelligence that uses techniques (such as deep learning) that enable machines to use experience to improve at tasks. The _learning process_ is based on the following steps:

   1. Feed data into an algorithm. (In this step you can provide additional information to the model, for example, by performing feature extraction.)
   1. Use this data to train a model.
   1. Test and deploy the model.
   1. Consume the deployed model to do an automated predictive task. (In other words, call and use the deployed model to receive the predictions returned by the model.)

- **Artificial intelligence (AI)** is a technique that enables computers to mimic human intelligence. It includes machine learning. 
 
By using machine learning and deep learning techniques, you can build computer systems and applications that do tasks that are commonly associated with human intelligence. These tasks include image recognition, speech recognition, and language translation.

## Techniques of deep learning vs. machine learning 

Now that you have the overview of machine learning vs. deep learning, let's compare the two techniques. In machine learning, the algorithm needs to be told how to make an accurate prediction by consuming more information (for example, by performing feature extraction). In deep learning, the algorithm can learn how to make an accurate prediction through its own data processing, thanks to the artificial neural network structure.

The following table compares the two techniques in more detail:

| |All machine learning |Only deep learning|
|---|---|---|
|  **Number of data points** | Can use small amounts of data to make predictions. | Needs to use large amounts of training data to make predictions. |
|  **Hardware dependencies** | Can work on low-end machines. It doesn't need a large amount of computational power. | Depends on high-end machines. It inherently does a large number of matrix multiplication operations. A GPU can efficiently optimize these operations. |
|  **Featurization process** | Requires features to be accurately identified and created by users. | Learns high-level features from data and creates new features by itself. |
|  **Learning approach** | Divides the learning process into smaller steps. It then combines the results from each step into one output. | Moves through the learning process by resolving the problem on an end-to-end basis. |
|  **Execution time** | Takes comparatively little time to train, ranging from a few seconds to a few hours. | Usually takes a long time to train because a deep learning algorithm involves many layers. |
|  **Output** | The output is usually a numerical value, like a score or a classification. | The output can have multiple formats, like a text, a score or a sound. |
