Changes required in AML:
- allow the job to react to cancellation by the user, such that the fine_tune get's cancelled, too
- enable the injection of keys into environment variables
- enable the download of named outputs from a command job
- designer to support dpv2 components
- vscode to help checking ${{inputs.foo}} expressions
- need file as outputs, not just folders -- type object, really

smaller things:
- yaml schema: outputs don't account for type: 'none'
- az ml job create --stream gives no useful logs -- in fact, no logs at all

MLFlow:
- MLflow.save_model insists on creating the folder the model is saved to

Changes to a service:
- provide metrics incrementally to enable early-stopping through hyperdrive