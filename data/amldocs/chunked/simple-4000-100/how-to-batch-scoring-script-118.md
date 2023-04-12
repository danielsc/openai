* The amount of memory required to read each file.
* The amount of memory required to read an entire batch of files.
* The memory footprint of the model.
* The memory footprint of the model when running over the input data.
* The available memory in your compute.

Batch deployments distribute work at the file level, which means that a folder containing 100 files with mini-batches of 10 files will generate 10 batches of 10 files each. Notice that this will happen regardless of the size of the files involved. If your files are too big to be processed in large mini-batches we suggest to either split the files in smaller files to achieve a higher level of parallelism or to decrease the number of files per mini-batch. At this moment, batch deployment can't account for skews in the file's size distribution.

### Running inference at the mini-batch, file or the row level

Batch endpoints will call the `run()` function in your scoring script once per mini-batch. However, you will have the power to decide if you want to run the inference over the entire batch, over one file at a time, or over one row at a time (if your data happens to be tabular).

#### Mini-batch level

You will typically want to run inference over the batch all at once when you want to achieve high throughput in your batch scoring process. This is the case for instance if you run inference over a GPU where you want to achieve saturation of the inference device. You may also be relying on a data loader that can handle the batching itself if data doesn't fit on memory, like `TensorFlow` or `PyTorch` data loaders. On those cases, you may want to consider running inference on the entire batch.

> [!WARNING]
> Running inference at the batch level may require having high control over the input data size to be able to correctly account for the memory requirements and avoid out of memory exceptions. Whether you are able or not of loading the entire mini-batch in memory will depend on the size of the mini-batch, the size of the instances in the cluster, the number of workers on each node, and the size of the mini-batch.

For an example about how to achieve it see [High throughput deployments](how-to-image-processing-batch.md#high-throughput-deployments).

#### File level

One of the easiest ways to perform inference is by iterating over all the files in the mini-batch and run your model over it. In some cases, like image processing, this may be a good idea. If your data is tabular, you may need to make a good estimation about the number of rows on each file to estimate if your model is able to handle the memory requirements to not just load the entire data into memory but also to perform inference over it. Remember that some models (specially those based on recurrent neural networks) will unfold and present a memory footprint that may not be linear with the number of rows. If your model is expensive in terms of memory, please consider running inference at the row level.

> [!TIP]
> If file sizes are too big to be readed even at once, please consider breaking down files into multiple smaller files to account for better parallelization.

For an example about how to achieve it see [Image processing with batch deployments](how-to-image-processing-batch.md).

#### Row level (tabular)

For models that present challenges in the size of their inputs, you may want to consider running inference at the row level. Your batch deployment will still provide your scoring script with a mini-batch of files, however, you will read one file, one row at a time. This may look inefficient but for some deep learning models may be the only way to perform inference without scaling up your hardware requirements. 

For an example about how to achieve it see [Text processing with batch deployments](how-to-nlp-processing-batch.md).

### Relationship between the degree of parallelism and the scoring script

Your deployment configuration controls the size of each mini-batch and the number of workers on each node. Take into account them when deciding if you want to read the entire mini-batch to perform inference. When running multiple workers on the same instance, take into account that memory will be shared across all the workers. Usually, increasing the number of workers per node should be accompanied by a decrease in the mini-batch size or by a change in the scoring strategy (if data size remains the same).
