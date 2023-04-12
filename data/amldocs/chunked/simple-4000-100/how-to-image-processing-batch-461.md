> * MLflow models should expect to recieve a `np.ndarray` as input that will match the dimensions of the input image. In order to support multiple image sizes on each batch, the batch executor will invoke the MLflow model once per image file.
> * MLflow models are highly encouraged to include a signature, and if they do it must be of type `TensorSpec`. Inputs are reshaped to match tensor's shape if available. If no signature is available, tensors of type `np.uint8` are inferred.
> * For models that include a signature and are expected to handle variable size of images, then include a signature that can guarantee it. For instance, the following signature will allow batches of 3 channeled images. Specify the signature when you register the model with `mlflow.<flavor>.log_model(..., signature=signature)`.

```python
import numpy as np
import mlflow
from mlflow.models.signature import ModelSignature
from mlflow.types.schema import Schema, TensorSpec

input_schema = Schema([
  TensorSpec(np.dtype(np.uint8), (-1, -1, -1, 3)),
])
signature = ModelSignature(inputs=input_schema)
```

For more information about how to use MLflow models in batch deployments read [Using MLflow models in batch deployments](how-to-mlflow-batch.md).

## Next steps

* [Using MLflow models in batch deployments](how-to-mlflow-batch.md)
* [NLP tasks with batch deployments](how-to-nlp-processing-batch.md)
