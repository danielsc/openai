    * [Install the `automl` package yourself](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/README.md#setup-using-a-local-conda-environment), which includes the [default installation](/python/api/overview/azure/ml/install#default-install) of the SDK.

    [!INCLUDE [automl-sdk-version](../../includes/machine-learning-automl-sdk-version.md)]

* This article assumes some familiarity with setting up an automated machine learning experiment. Follow the [how-to](how-to-configure-auto-train.md) to see the main automated machine learning experiment design patterns.


## Select your NLP task 

Determine what NLP task you want to accomplish. Currently, automated ML supports the follow deep neural network NLP tasks. 

Task |AutoML job syntax| Description 
----|----|---
Multi-class text classification | CLI v2: `text_classification`  <br> SDK v2: `text_classification()`| There are multiple possible classes and each sample can be classified as exactly one class. The task is to predict the correct class for each sample. <br> <br> For example, classifying a movie script as "Comedy" or "Romantic". 
Multi-label text classification |  CLI v2: `text_classification_multilabel`  <br> SDK v2: `text_classification_multilabel()`| There are multiple possible classes and each sample can be assigned any number of classes. The task is to predict all the classes for each sample<br> <br> For example, classifying a movie script as "Comedy", or "Romantic", or "Comedy and Romantic". 
Named Entity Recognition (NER)|  CLI v2:`text_ner` <br> SDK v2: `text_ner()`| There are multiple possible tags for tokens in sequences. The task is to predict the tags for all the tokens for each sequence. <br> <br> For example, extracting domain-specific entities from unstructured text, such as contracts or financial documents.

## Thresholding

Thresholding is the multi-label feature that allows users to pick the threshold above which the predicted probabilities will lead to a positive label. Lower values allow for more labels, which is better when users care more about recall, but this option could lead to more false positives. Higher values allow fewer labels and hence better for users who care about precision, but this option could lead to more false negatives.

## Preparing data

For NLP experiments in automated ML, you can bring your data in `.csv` format for multi-class and multi-label classification tasks. For NER tasks, two-column `.txt` files that use a space as the separator and adhere to the CoNLL format are supported. The following sections provide additional detail for the data format accepted for each task. 

### Multi-class

For multi-class classification, the dataset can contain several text columns and exactly one label column. The following example has only one text column.

```
text,labels
"I love watching Chicago Bulls games.","NBA"
"Tom Brady is a great player.","NFL"
"There is a game between Yankees and Orioles tonight","MLB"
"Stephen Curry made the most number of 3-Pointers","NBA"
```

### Multi-label

For multi-label classification, the dataset columns would be the same as multi-class, however there are special format requirements for data in the label column. The two accepted formats and examples are in the following table. 

|Label column format options |Multiple labels| One label | No labels
|---|---|---|---
|Plain text|`"label1, label2, label3"`| `"label1"`|  `""`
|Python list with quotes| `"['label1','label2','label3']"`| `"['label1']"`|`"[]"`

> [!IMPORTANT]
> Different parsers are used to read labels for these formats. If you are using the plain text format, only use alphabetical, numerical and `'_'` in your labels. All other characters are recognized as the separator of labels. 
>
> For example, if your label is `"cs.AI"`, it's read as `"cs"` and `"AI"`. Whereas with the Python list format, the label would be `"['cs.AI']"`, which is read as `"cs.AI"` .


Example data for multi-label in plain text format. 
