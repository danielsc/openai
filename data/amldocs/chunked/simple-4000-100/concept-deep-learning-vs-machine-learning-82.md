Text analytics based on deep learning methods involves analyzing large quantities of text data (for example, medical documents or expenses receipts), recognizing patterns, and creating organized and concise information out of it.

Companies use deep learning to perform text analysis to detect insider trading and compliance with government regulations. Another common example is insurance fraud: text analytics has often been used to analyze large amounts of documents to recognize the chances of an insurance claim being fraud.

## Artificial neural networks

Artificial neural networks are formed by layers of connected nodes. Deep learning models use neural networks that have a large number of layers. 

The following sections explore most popular artificial neural network typologies.

### Feedforward neural network

The feedforward neural network is the most simple type of artificial neural network. In a feedforward network, information moves in only one direction from input layer to output layer. Feedforward neural networks transform an input by putting it through a series of hidden layers. Every layer is made up of a set of neurons, and each layer is fully connected to all neurons in the layer before. The last fully connected layer (the output layer) represents the generated predictions.

### Recurrent neural network (RNN)

Recurrent neural networks are a widely used artificial neural network. These networks save the output of a layer and feed it back to the input layer to help predict the layer's outcome. Recurrent neural networks have great learning abilities. They're widely used for complex tasks such as time series forecasting, learning handwriting, and recognizing language.

### Convolutional neural network (CNN)

A convolutional neural network is a particularly effective artificial neural network, and it presents a unique architecture. Layers are organized in three dimensions: width, height, and depth. The neurons in one layer connect not to all the neurons in the next layer, but only to a small region of the layer's neurons. The final output is reduced to a single vector of probability scores, organized along the depth dimension. 

Convolutional neural networks have been used in areas such as video recognition, image recognition, and recommender systems.

### Generative adversarial network (GAN)

Generative adversarial networks are generative models trained to create realistic content such as images. It is made up of two networks known as generator and discriminator. Both networks are trained simultaneously. During training, the generator uses random noise to create new synthetic data that closely resembles real data. The discriminator takes the output from the generator as input and uses real data to determine whether the generated content is real or synthetic. Each network is competing with each other. The generator is trying to generate synthetic content that is indistinguishable from real content and the discriminator is trying to correctly classify inputs as real or synthetic. The output is then used to update the weights of both networks to help them better achieve their respective goals.

Generative adversarial networks are used to solve problems like image to image translation and age progression.

### Transformers

Transformers are a model architecture that is suited for solving problems containing sequences such as text or time-series data. They consist of [encoder and decoder layers](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)#Encoder). The encoder takes an input and maps it to a numerical representation containing information such as context. The decoder uses information from the encoder to produce an output such as translated text. What makes transformers different from other architectures containing encoders and decoders are the attention sub-layers. Attention is the idea of focusing on specific parts of an input based on the importance of their context in relation to other inputs in a sequence. For example, when summarizing a news article, not all sentences are relevant to describe the main idea. By focusing on key words throughout the article, summarization can be done in a single sentence, the headline.
