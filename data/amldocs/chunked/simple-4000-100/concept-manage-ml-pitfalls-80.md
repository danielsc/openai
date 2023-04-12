[Confusion Matrix](how-to-understand-automated-ml.md#confusion-matrix)| Evaluates the correctly classified labels against the actual labels of the data. 
[Precision-recall](how-to-understand-automated-ml.md#precision-recall-curve)| Evaluates the ratio of correct labels against the ratio of found label instances of the data 
[ROC Curves](how-to-understand-automated-ml.md#roc-curve)| Evaluates the ratio of correct labels against the ratio of false-positive labels.

## Handle imbalanced data 

As part of its goal of simplifying the machine learning workflow, **automated ML has built in capabilities** to help deal with imbalanced data such as, 

- A **weight column**: automated ML supports a column of weights as input, causing rows in the data to be weighted up or down, which can be used to make a class more or less "important".

- The algorithms used by automated ML detect imbalance when the number of samples in the minority class is equal to or fewer than 20% of the number of samples in the majority class, where minority class refers to the one with fewest samples and majority class refers to the one with most samples. Subsequently, AutoML will run an experiment with sub-sampled data to check if using class weights would remedy this problem and improve performance. If it ascertains a better performance through this experiment, then this remedy is applied.

- Use a performance metric that deals better with imbalanced data. For example, the AUC_weighted is a primary metric that calculates the contribution of every class based on the relative number of samples representing that class, hence is more robust against imbalance.

The following techniques are additional options to handle imbalanced data **outside of automated ML**. 

- Resampling to even the class imbalance, either by up-sampling the smaller classes or down-sampling the larger classes. These methods require expertise to process and analyze.

- Review performance metrics for imbalanced data. For example, the F1 score is the harmonic mean of precision and recall. Precision measures a classifier's exactness, where higher precision indicates fewer false positives, while recall measures a classifier's completeness, where higher recall indicates fewer false negatives.

## Next steps

See examples and learn how to build models using automated machine learning:

+ Follow the [Tutorial: Train an object detection model with AutoML and Python](tutorial-auto-train-image-models.md).

+ Configure the settings for automatic training experiment:
  + In Azure Machine Learning studio, [use these steps](how-to-use-automated-ml-for-ml-models.md).
  + With the Python SDK, [use these steps](how-to-configure-auto-train.md).
