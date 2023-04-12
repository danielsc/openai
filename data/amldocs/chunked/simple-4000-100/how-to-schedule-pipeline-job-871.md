Currently there are three action rules related to schedules and you can configure in Azure portal. You can learn more details about [how to manage access to an Azure Machine Learning workspace.](how-to-assign-roles.md#create-custom-role)

| Action | Description                                                                | Rule                                                          |
|--------|----------------------------------------------------------------------------|---------------------------------------------------------------|
| Read   | Get and list schedules in Machine Learning workspace                        | Microsoft.MachineLearningServices/workspaces/schedules/read   |
| Write  | Create, update, disable and enable schedules in Machine Learning workspace | Microsoft.MachineLearningServices/workspaces/schedules/write  |
| Delete | Delete a schedule in Machine Learning workspace                            | Microsoft.MachineLearningServices/workspaces/schedules/delete |

## Frequently asked questions

- Why my schedules created by SDK aren't listed in UI?

    The schedules UI is for v2 schedules. Hence, your v1 schedules won't be listed or accessed via UI.

    However, v2 schedules also support v1 pipeline jobs. You don't have to publish pipeline first, and you can directly set up schedules for a pipeline job.

- Why my schedules don't trigger job at the time I set before?
  - By default schedules will use UTC timezone to calculate trigger time. You can specify timezone in the creation wizard, or update timezone in schedule detail page.
  - If you set the recurrence as the 31st day of every month, in months with less than 31 days, the schedule won't trigger jobs.
  - If you're using cron expressions, MONTH isn't supported. If you pass a value, it will be ignored and treated as *. This is a known limitation.
- Are event-based schedules supported?
  - No, V2 schedule does not support event-based schedules.

## Next steps

* Learn more about the [CLI (v2) schedule YAML schema](./reference-yaml-schedule.md).
* Learn how to [create pipeline job in CLI v2](how-to-create-component-pipelines-cli.md).
* Learn how to [create pipeline job in SDK v2](how-to-create-component-pipeline-python.md).
* Learn more about [CLI (v2) core YAML syntax](reference-yaml-core-syntax.md).
* Learn more about [Pipelines](concept-ml-pipelines.md).
* Learn more about [Component](concept-component.md).
