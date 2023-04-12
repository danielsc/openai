Deploy the model to your AKS cluster and wait for it to create your service. In this example, two registered models are loaded from the registry and deployed to AKS. After deployment, the `score.py` file in the deployment loads these models and uses them to perform inference.

```python
from azureml.core.webservice import AksWebservice, Webservice

c_aspect_lex = Model(ws, 'hotel_aspect_lex')
c_opinion_lex = Model(ws, 'hotel_opinion_lex') 
service_name = "hotel-absa-v2"

aks_service = Model.deploy(workspace=ws,
                           name=service_name,
                           models=[c_aspect_lex, c_opinion_lex],
                           inference_config=inf_config,
                           deployment_config=aks_config,
                           deployment_target=aks_target,
                           overwrite=True)

aks_service.wait_for_deployment(show_output = True)
print(aks_service.state)
```

For more information, see the reference documentation for [Model](/python/api/azureml-core/azureml.core.model.model).

## Issue a sample query to your service

The following example uses the deployment information stored in the `aks_service` variable by the previous code section. It uses this variable to retrieve the scoring URL and authentication token needed to communicate with the service:

```python
import requests
import json

primary, secondary = aks_service.get_keys()

# Test data
input_data = '{"raw_data": {"text": "This is a nice place for a relaxing evening out with friends. The owners seem pretty nice, too. I have been there a few times including last night. Recommend."}}'

# Since authentication was enabled for the deployment, set the authorization header.
headers = {'Content-Type':'application/json',  'Authorization':('Bearer '+ primary)} 

# Send the request and display the results
resp = requests.post(aks_service.scoring_uri, input_data, headers=headers)
print(resp.text)
```

The result returned from the service is similar to the following JSON:

```json
{"sentiment": {"sentence": "This is a nice place for a relaxing evening out with friends. The owners seem pretty nice, too. I have been there a few times including last night. Recommend.", "terms": [{"text": "place", "type": "AS", "polarity": "POS", "score": 1.0, "start": 15, "len": 5}, {"text": "nice", "type": "OP", "polarity": "POS", "score": 1.0, "start": 10, "len": 4}]}}
```

## Connect to Cognitive Search

For information on using this model from Cognitive Search, see the [Build and deploy a custom skill with Azure Machine Learning](../search/cognitive-search-tutorial-aml-custom-skill.md) tutorial.

## Clean up the resources

If you created the AKS cluster specifically for this example, delete your resources after you're done testing it with Cognitive Search.

> [!IMPORTANT]
> Azure bills you based on how long the AKS cluster is deployed. Make sure to clean it up after you are done with it.

```python
aks_service.delete()
aks_target.delete()
```

## Next steps

* [Build and deploy a custom skill with Azure Machine Learning](../search/cognitive-search-tutorial-aml-custom-skill.md)
