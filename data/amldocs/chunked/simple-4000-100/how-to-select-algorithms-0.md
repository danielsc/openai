# How to select algorithms for Azure Machine Learning

A common question is “Which machine learning algorithm should I use?” The algorithm you select depends primarily on two different aspects of your data science scenario:

 - **What you want to do with your data?** Specifically, what is the business question you want to answer by learning from your past data?

 - **What are the requirements of your data science scenario?** Specifically, what is the accuracy, training time, linearity, number of parameters, and number of features your solution supports?

 ![Considerations for choosing algorithms: What do you want to know? What are the scenario requirements?](./media/how-to-select-algorithms/how-to-select-algorithms.png)

## Business scenarios and the Machine Learning Algorithm Cheat Sheet

The [Azure Machine Learning Algorithm Cheat Sheet](./algorithm-cheat-sheet.md?WT.mc_id=docs-article-lazzeri) helps you with the first consideration: **What you want to do with your data**? On the Machine Learning Algorithm Cheat Sheet, look for task you want to do, and then find a [Azure Machine Learning designer](./concept-designer.md?WT.mc_id=docs-article-lazzeri) algorithm for the predictive analytics solution. 

Machine Learning designer provides a comprehensive portfolio of algorithms, such as [Multiclass Decision Forest](./algorithm-module-reference/multiclass-decision-forest.md?WT.mc_id=docs-article-lazzeri), [Recommendation systems](./algorithm-module-reference/evaluate-recommender.md?WT.mc_id=docs-article-lazzeri), [Neural Network Regression](./algorithm-module-reference/neural-network-regression.md?WT.mc_id=docs-article-lazzeri), [Multiclass Neural Network](./algorithm-module-reference/multiclass-neural-network.md?WT.mc_id=docs-article-lazzeri), and [K-Means Clustering](./algorithm-module-reference/k-means-clustering.md?WT.mc_id=docs-article-lazzeri). Each algorithm is designed to address a different type of machine learning problem. See the [Machine Learning designer algorithm and component reference](./component-reference/component-reference.md?WT.mc_id=docs-article-lazzeri) for a complete list along with documentation about how each algorithm works and how to tune parameters to optimize the algorithm.

> [!NOTE]
> Download the cheat sheet here: [Machine Learning Algorithm Cheat Sheet (11x17 in.)](https://download.microsoft.com/download/3/5/b/35bb997f-a8c7-485d-8c56-19444dafd757/azure-machine-learning-algorithm-cheat-sheet-july-2021.pdf)
> 
> 

Along with guidance in the Azure Machine Learning Algorithm Cheat Sheet, keep in mind other requirements when choosing a machine learning algorithm for your solution. Following are additional factors to consider, such as the accuracy, training time, linearity, number of parameters and number of features.

## Comparison of machine learning algorithms

>[!Note]
> Designer supports two type of components, classic prebuilt components and custom components. These two types of components are not compatible.  
>
>Classic prebuilt components provides prebuilt components majorly for data processing and traditional machine learning tasks like regression and classification. This type of component continues to be supported but will not have any new components added.
>
>
>Custom components allow you to provide your own code as a component. It supports sharing across workspaces and seamless authoring across Studio, CLI, and SDK interfaces.
>
>This article applies to classic prebuilt components. 

Some learning algorithms make particular assumptions about the structure of the data or the desired results. If you can find one that fits your needs, it can give you more useful results, more accurate predictions, or faster training times.

The following table summarizes some of the most important characteristics of algorithms from the classification, regression, and clustering families:

| **Algorithm** | **Accuracy** | **Training time** | **Linearity** | **Parameters** | **Notes** |
| --- |:---:|:---:|:---:|:---:| --- |
