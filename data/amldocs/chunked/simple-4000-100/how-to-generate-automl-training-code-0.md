
#  View training code for an Automated ML model

In this article, you learn how to view the generated training code from any automated machine learning trained model. 

Code generation for automated ML trained models allows you to see the following details that automated ML uses to train and build the model for a specific run.

* Data preprocessing
* Algorithm selection
* Featurization
* Hyperparameters 

You can select any automated ML trained model, recommended or child run, and view the generated Python training code that created that specific model.

With the generated model's training code you can, 

* **Learn** what featurization process and hyperparameters the model algorithm uses.
* **Track/version/audit** trained models. Store versioned code to track what specific training code is used with the model that's to be deployed to production.
* **Customize** the training code by changing hyperparameters or applying your ML and algorithms skills/experience, and retrain a new model with your customized code.

The following diagram illustrates that you can generate the code for automated ML experiments with all task types. First select a model. The model you selected will be highlighted, then Azure Machine Learning copies the code files used to create the model, and displays them into your notebooks shared folder. From here, you can view and customize the code as needed. 

:::image type="content" source="media/how-to-generate-automl-training-code/code-generation-demonstration.png" alt-text="Screenshot showing models tab, as well as having a model selected, as explained in the above text.":::

## Prerequisites

* An Azure Machine Learning workspace. To create the workspace, see [Create workspace resources](quickstart-create-resources.md).

* This article assumes some familiarity with setting up an automated machine learning experiment. Follow the [tutorial](tutorial-auto-train-image-models.md) or [how-to](how-to-configure-auto-train.md) to see the main automated machine learning experiment design patterns.

* Automated ML code generation is only available for experiments run on remote Azure ML compute targets. Code generation isn't supported for local runs.

* All automated ML runs triggered through AzureML Studio, SDKv2 or CLIv2 will have code generation enabled.

## Get generated code and model artifacts
By default, each automated ML trained model generates its training code after training completes. Automated ML saves this code in the experiment's `outputs/generated_code` for that specific model. You can view them in the Azure ML studio UI on the **Outputs + logs** tab of the selected model. 

* **script.py** This is the model's training code that you likely want to analyze with the featurization steps, specific algorithm used, and hyperparameters.

* **script_run_notebook.ipynb** Notebook with boiler-plate code to run the model's training code (script.py) in AzureML compute through Azure ML SDKv2.

After the automated ML training run completes, there are you can access the `script.py` and the `script_run_notebook.ipynb` files via the Azure Machine Learning studio UI. 

To do so, navigate to the **Models** tab of the automated ML experiment parent run page. After you select one of the trained models, you can select the **View generated code** button. This button redirects you to the **Notebooks** portal extension, where you can view, edit and run the generated code for that particular selected model.

![parent run models tab view generate code button](./media/how-to-generate-automl-training-code/parent-run-view-generated-code.png)

You can also access to the model's generated code from the top of the child run's page once you navigate into that child run's page of a particular model.

![child run page view generated code button](./media/how-to-generate-automl-training-code/child-run-view-generated-code.png)

If you're using the Python SDKv2, you can also download the "script.py" and the "script_run_notebook.ipynb" by retrieving the best run via MLFlow & downloading the resulting artifacts. 
