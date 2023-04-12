Transformers are a model architecture that is suited for solving problems containing sequences such as text or time-series data. They consist of [encoder and decoder layers](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)#Encoder). The encoder takes an input and maps it to a numerical representation containing information such as context. The decoder uses information from the encoder to produce an output such as translated text. What makes transformers different from other architectures containing encoders and decoders are the attention sub-layers. Attention is the idea of focusing on specific parts of an input based on the importance of their context in relation to other inputs in a sequence. For example, when summarizing a news article, not all sentences are relevant to describe the main idea. By focusing on key words throughout the article, summarization can be done in a single sentence, the headline.

Transformers have been used to solve natural language processing problems such as translation, text generation, question answering, and text summarization.

Some well-known implementations of transformers are:

- Bidirectional Encoder Representations from Transformers (BERT)
- Generative Pre-trained Transformer 2 (GPT-2)
- Generative Pre-trained Transformer 3 (GPT-3)

## Next steps

The following articles show you more options for using open-source deep learning models in [Azure Machine Learning](./index.yml?WT.mc_id=docs-article-lazzeri):


- [Classify handwritten digits by using a TensorFlow model](./how-to-train-tensorflow.md?WT.mc_id=docs-article-lazzeri) 

- [Classify handwritten digits by using a TensorFlow estimator and Keras](./how-to-train-keras.md?WT.mc_id=docs-article-lazzeri)
