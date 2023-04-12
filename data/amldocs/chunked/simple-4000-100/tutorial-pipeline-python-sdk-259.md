Now deploy your machine learning model as a web service in the Azure cloud, an [`online endpoint`](concept-endpoints.md).
To deploy a machine learning service, you usually need:

* The model assets (filed, metadata) that you want to deploy. You've already registered these assets in your training component.
* Some code to run as a service. The code executes the model on a given input request. This entry script receives data submitted to a deployed web service and passes it to the model, then returns the model's response to the client. The script is specific to your model. The entry script must understand the data that the model expects and returns. When using a MLFlow model, as in this tutorial, this script is automatically created for you

## Create a new online endpoint

Now that you have a registered model and an inference script, it's time to create your online endpoint. The endpoint name needs to be unique in the entire Azure region. For this tutorial, you'll create a unique name using [`UUID`](https://en.wikipedia.org/wiki/Universally_unique_identifier).

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=online_endpoint_name)]

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=endpoint)]

Once you've created an endpoint, you can retrieve it as below:

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=update-endpoint)]

## Deploy the model to the endpoint

Once the endpoint is created, deploy the model with the entry script. Each endpoint can have multiple deployments and direct traffic to these deployments can be specified using rules. Here you'll create a single deployment that handles 100% of the incoming traffic. We have chosen a color name for the deployment, for example, *blue*, *green*, *red* deployments, which is arbitrary.

You can check the *Models* page on the Azure ML studio, to identify the latest version of your registered model. Alternatively, the code below will retrieve the latest version number for you to use.

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=latest_model_version)]

Deploy the latest version of the model.  

> [!NOTE]
> Expect this deployment to take approximately 6 to 8 minutes.

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=model)]

### Test with a sample query

Now that the model is deployed to the endpoint, you can run inference with it.

Create a sample request file following the design expected in the run method in the score script.

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=sample-request.json)]

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=write-sample-request)]

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=ml_client.online_endpoints.invoke)]

## Clean up resources

If you're not going to use the endpoint, delete it to stop using the resource.  Make sure no other deployments are using an endpoint before you delete it.

> [!NOTE]
> Expect this step to take approximately 6 to 8 minutes.

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=ml_client.online_endpoints.begin_delete)]

## Next steps

> [!div class="nextstepaction"]
> Learn more about [Azure ML logging](./how-to-use-mlflow-cli-runs.md).
