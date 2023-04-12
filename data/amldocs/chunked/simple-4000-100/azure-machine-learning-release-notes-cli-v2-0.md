
# Azure Machine Learning CLI (v2) release notes

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]



In this article, learn about Azure Machine Learning CLI (v2) releases.

__RSS feed__: Get notified when this page is updated by copying and pasting the following URL into your feed reader:
`https://learn.microsoft.com/api/search/rss?search=%22Azure+machine+learning+release+notes-v2%22&locale=en-us`

## 2022-11-08

### Azure Machine Learning CLI (v2) v2.11.0

- The CLI is depending on azure-ai-ml 1.1.0.
- `az ml registry`
  - Added `ml registry delete` command.
  - Adjusted registry experimental tags and imports to avoid warning printouts for unrelated operations.
- `az ml environment`
   - Prevented registering an already existing environment that references conda file.

## 2022-10-10

### Azure Machine Learning CLI (v2) v2.10.0

- The CLI is depending on GA version of azure-ai-ml.
- Dropped support for Python 3.6.
- `az ml registry`
  - New command group added to manage ML asset registries.
- `az ml job`
  - Added `az ml job show-services` command.
  - Added model sweeping and hyperparameter tuning to AutoML NLP jobs.
- `az ml schedule`
  - Added `month_days` property in recurrence schedule.
- `az ml compute`
  - Added custom setup scripts support for compute instances.

## 2022-09-22

### Azure Machine Learning CLI (v2) v2.8.0

- `az ml job`
  - Added spark job support.
  - Added shm_size and docker_args to job.
- `az ml compute`
  - Compute instance supports managed identity.
  - Added idle shutdown time support for compute instance.
- `az ml online-deployment`
  - Added support for data collection for eventhub and data storage.
  - Added syntax validation for scoring script.
- `az ml batch-deployment`
  - Added syntax validation for scoring script.

## 2022-08-10

### Azure Machine Learning CLI (v2) v2.7.0

- `az ml component`
  - Added AutoML component.
- `az ml dataset`
  - Deprecated command group (Use `az ml data` instead).

## 2022-07-16

### Azure Machine Learning CLI (v2) v2.6.0

- Added MoonCake cloud support.
- `az ml job`
  - Allow Git repo URLs to be used as code.
  - AutoML jobs use the same input schema as other job types.
  - Pipeline jobs now supports registry assets.
- `az ml component`
  - Allow Git repo URLs to be used as code.
- `az ml online-endpoint`
  - MIR now supports registry assets.

## 2022-05-24

### Azure Machine Learning CLI (v2) v2.4.0

- The Azure Machine Learning CLI (v2) is now GA.
- `az ml job`
  - The command group is marked as GA.
  - Added AutoML job type in public preview.
  - Added `schedules` property to pipeline job in public preview.
  - Added an option to list only archived jobs.
  - Improved reliability of `az ml job download` command.
- `az ml data`
  - The command group is marked as GA.
  - Added MLTable data type in public preview.
  - Added an option to list only archived data assets.
- `az ml environment`
  - Added an option to list only archived environments.
- `az ml model`
  - The command group is marked as GA.
  - Allow models to be created from job outputs.
  - Added an option to list only archived models.
- `az ml online-deployment`
  - The command group is marked as GA.
  - Removed timeout waiting for deployment creation.
  - Improved online deployment list view.
- `az ml online-endpoint`
  - The command group is marked as GA.
  - Added `mirror_traffic` property to online endpoints in public preview.
  - Improved online endpoint list view.
- `az ml batch-deployment`
  - The command group is marked as GA.
  - Added support for `uri_file` and `uri_folder` as invocation input.
  - Fixed a bug in batch deployment update.
  - Fixed a bug in batch deployment list-jobs output.
- `az ml batch-endpoint`
  - The command group is marked as GA.
  - Added support for `uri_file` and `uri_folder` as invocation input.
  - Fixed a bug in batch endpoint update.
  - Fixed a bug in batch endpoint list-jobs output.
- `az ml component`
  - The command group is marked as GA.
