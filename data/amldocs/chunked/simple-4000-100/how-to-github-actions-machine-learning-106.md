
1. Select **View runs**. 
1. Enable workflows by selecting **I understand my workflows, go ahead and enable them**.
1. Select the **cli-jobs-pipelines-nyc-taxi-pipeline workflow** and choose to **Enable workflow**. 
    :::image type="content" source="media/how-to-github-actions-machine-learning/enable-github-actions-ml-workflow.png" alt-text="Screenshot of enable GitHub Actions workflow.":::
1. Select **Run workflow** and choose the option to **Run workflow** now. 
    :::image type="content" source="media/how-to-github-actions-machine-learning/github-actions-run-workflow.png" alt-text="Screenshot of run GitHub Actions workflow.":::

 # [OpenID Connect](#tab/openid)

Your workflow file is made up of a trigger section and jobs:
- A trigger starts the workflow in the `on` section. The workflow runs by default on a cron schedule and when a pull request is made from matching branches and paths. Learn more about [events that trigger workflows](https://docs.github.com/actions/using-workflows/events-that-trigger-workflows). 
- In the jobs section of the workflow, you checkout code and log into Azure with the Azure login action using OpenID Connect.
- The jobs section also includes a setup action that installs and sets up the [Machine Learning CLI (v2)](how-to-configure-cli.md). Once the CLI is installed, the run job action runs your Azure Machine Learning `pipeline.yml` file to train a model with NYC taxi data.

### Enable your workflow

1. In your cloned repository, open `.github/workflows/cli-jobs-pipelines-nyc-taxi-pipeline.yml` and verify that your workflow looks like this.

    ```yaml
    name: cli-jobs-pipelines-nyc-taxi-pipeline
    on:
      workflow_dispatch:
      schedule:
        - cron: "0 0/4 * * *"
      pull_request:
        branches:
          - main
          - sdk-preview
        paths:
          - cli/jobs/pipelines/nyc-taxi/**
          - .github/workflows/cli-jobs-pipelines-nyc-taxi-pipeline.yml
          - cli/run-pipeline-jobs.sh
          - cli/setup.sh
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
        - name: check out repo
          uses: actions/checkout@v2
        - name: azure login
          uses: azure/login@v1
          with:
              client-id: ${{ secrets.AZURE_CLIENT_ID }}
              tenant-id: ${{ secrets.AZURE_TENANT_ID }}
              subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
        - name: setup
          run: bash setup.sh
          working-directory: cli
          continue-on-error: true
        - name: run job
          run: bash -x ../../../run-job.sh pipeline.yml
          working-directory: cli/jobs/pipelines/nyc-taxi
    ```
    
1. Select **View runs**. 
1. Enable workflows by selecting **I understand my workflows, go ahead and enable them**.
1. Select the **cli-jobs-pipelines-nyc-taxi-pipeline workflow** and choose to **Enable workflow**. 

    :::image type="content" source="media/how-to-github-actions-machine-learning/enable-github-actions-ml-workflow.png" alt-text="Screenshot of enable GitHub Actions workflow.":::

1. Select **Run workflow** and choose the option to **Run workflow** now. 

    :::image type="content" source="media/how-to-github-actions-machine-learning/github-actions-run-workflow.png" alt-text="Screenshot of run GitHub Actions workflow.":::

## Step 6: Verify your workflow run

1. Open your completed workflow run and verify that the build job ran successfully. You'll see a green checkmark next to the job. 
1. Open Azure Machine Learning studio and navigate to the **nyc-taxi-pipeline-example**. Verify that each part of your job (prep, transform, train, predict, score) completed and that you see a green checkmark. 

    :::image type="content" source="media/how-to-github-actions-machine-learning/github-actions-machine-learning-nyc-taxi-complete.png" alt-text="Screenshot of successful Machine Learning Studio run.":::

## Clean up resources

When your resource group and repository are no longer needed, clean up the resources you deployed by deleting the resource group and your GitHub repository. 
