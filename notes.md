Changes required in AML:
- allow the job to react to cancellation by the user, such that the fine_tune get's cancelled, too
- enable the injection of keys into environment variables (both job and deployment)
- scenario polishing, esp. pipelines/designer/components

Usability improvements
- enable the download of named outputs from a command job
- vscode to help checking ${{inputs.foo}} expressions
- yaml schema: outputs don't account for type: 'none'
- az ml job create --stream gives no useful logs -- in fact, no logs at all

longer term:
- need file as outputs, not just folders -- type object, really

MLFlow:
- MLflow.save_model insists on creating the folder the model is saved to

Changes to a service:
- provide metrics incrementally to enable early-stopping through hyperdrive