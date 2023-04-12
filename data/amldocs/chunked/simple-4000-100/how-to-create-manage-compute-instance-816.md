To keep track of whether an instance's operating system version is current, you could query its version using the Studio UI. In your workspace in Azure Machine Learning studio, select Compute, then select compute instance on the top. Select a compute instance's compute name to see its properties including the current operating system. Enable 'audit and observe compute instance os version' under the previews management panel to see these preview properties.

Administrators can use [Azure Policy](./../governance/policy/overview.md) definitions to audit instances that are running on outdated operating system versions across workspaces and subscriptions. The following is a sample policy:

```json
{
    "mode": "All",
    "policyRule": {
      "if": {
        "allOf": [
          {
            "field": "type",
            "equals": "Microsoft.MachineLearningServices/workspaces/computes"
          },
          {
            "field": "Microsoft.MachineLearningServices/workspaces/computes/computeType",
            "equals": "ComputeInstance"
          },
          {
            "field": "Microsoft.MachineLearningServices/workspaces/computes/osImageMetadata.isLatestOsImageVersion",
            "equals": "false"
          }
        ]
      },
      "then": {
        "effect": "Audit"
      }
    }
}    
```

## Next steps

* [Access the compute instance terminal](how-to-access-terminal.md)
* [Create and manage files](how-to-manage-files.md)
* [Update the compute instance to the latest VM image](concept-vulnerability-management.md#compute-instance)

