In both ways, you can set [breakpoint](https://code.visualstudio.com/docs/editor/debugging#_breakpoints) and debug step by step.

### End-to-end example
In this section, we'll run the server locally with [sample files](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online/model-1) (scoring script, model file, and environment) in our example repository. The sample files are also used in our article for [Deploy and score a machine learning model by using an online endpoint](how-to-deploy-online-endpoints.md)

1. Clone the sample repository.

    ```bash
    git clone --depth 1 https://github.com/Azure/azureml-examples
    cd azureml-examples/cli/endpoints/online/model-1/
    ```

1. Create and activate a virtual environment with [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html).
    In this example, the `azureml-inference-server-http` package is automatically installed because it's included as a dependent library of the `azureml-defaults` package in `conda.yml` as follows.

    ```bash
    # Create the environment from the YAML file
    conda env create --name model-env -f ./environment/conda.yml
    # Activate the new environment
    conda activate model-env
    ```

1. Review your scoring script.

    __onlinescoring/score.py__  
```python
import os
import logging
import json
import numpy
import joblib


def init():
    """
    This function is called when the container is initialized/started, typically after create/update of the deployment.
    You can write the logic here to perform init operations like caching the model in memory
    """
    global model
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
    # Please provide your model's folder name if there is one
    model_path = os.path.join(
        os.getenv("AZUREML_MODEL_DIR"), "model/sklearn_regression_model.pkl"
    )
    # deserialize the model file back into a sklearn model
    model = joblib.load(model_path)
    logging.info("Init complete")


def run(raw_data):
    """
    This function is called for every invocation of the endpoint to perform the actual scoring/prediction.
    In the example we extract the data from the json input and call the scikit-learn model's predict()
    method and return the result back
    """
    logging.info("model 1: request received")
    data = json.loads(raw_data)["data"]
    data = numpy.array(data)
    result = model.predict(data)
    logging.info("Request processed")
    return result.tolist()

```

1. Run the inference server with specifying scoring script and model file.
   The specified model directory (`model_dir` parameter) will be defined as `AZUREML_MODEL_DIR` variable and retrieved in the scoring script. 
   In this case, we specify the current directory (`./`) since the subdirectory is specified in the scoring script as `model/sklearn_regression_model.pkl`.

    ```bash
    azmlinfsrv --entry_script ./onlinescoring/score.py --model_dir ./
    ```

    The example [startup log](#startup-logs) will be shown if the server launched and the scoring script invoked successfully. Otherwise, there will be error messages in the log.

1. Test the scoring script with a sample data.
    Open another terminal and move to the same working directory to run the command.
    Use the `curl` command to send an example request to the server and receive a scoring result.

    ```bash
    curl --request POST "127.0.0.1:5001/score" --header 'Content-Type: application/json' --data @sample-request.json
    ```

    The scoring result will be returned if there's no problem in your scoring script. If you find something wrong, you can try to update the scoring script, and launch the server again to test the updated script.

## Server Routes

The server is listening on port 5001 (as default) at these routes.

| Name              | Route                       |
| ----------------- | --------------------------- |
