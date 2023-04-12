> To learn more about which VM family to request a quota increase for, check out [virtual machine sizes in Azure](../virtual-machines/sizes.md). For instance GPU VM families start with an "N" in their family name (eg. NCv3 series)

The following table shows more limits in the platform. Reach out to the AzureML product team through a **technical** support ticket to request an exception.

| **Resource or Action** | **Maximum limit** |
| --- | --- |
| Workspaces per resource group | 800 |
| Nodes in a single Azure Machine Learning Compute (AmlCompute) **cluster** set up as a non communication-enabled pool (that is, can't run MPI jobs) | 100 nodes but configurable up to 65,000 nodes |
| Nodes in a single Parallel Run Step **run** on an Azure Machine Learning Compute (AmlCompute) cluster | 100 nodes but configurable up to 65,000 nodes if your cluster is set up to scale per above |
| Nodes in a single Azure Machine Learning Compute (AmlCompute) **cluster** set up as a communication-enabled pool | 300 nodes but configurable up to 4000 nodes |
| Nodes in a single Azure Machine Learning Compute (AmlCompute) **cluster** set up as a communication-enabled pool on an RDMA enabled VM Family | 100 nodes |
| Nodes in a single MPI **run** on an Azure Machine Learning Compute (AmlCompute) cluster | 100 nodes but can be increased to 300 nodes |
| Job lifetime | 21 days<sup>1</sup> |
| Job lifetime on a low-priority node | 7 days<sup>2</sup> |
| Parameter servers per node | 1 |

<sup>1</sup> Maximum lifetime is the duration between when a job starts and when it finishes. Completed jobs persist indefinitely. Data for jobs not completed within the maximum lifetime isn't accessible.

<sup>2</sup> Jobs on a low-priority node can be preempted whenever there's a capacity constraint. We recommend that you implement checkpoints in your job.

### Azure Machine Learning managed online endpoints

Azure Machine Learning managed online endpoints have limits described in the following table. 

| **Resource** | **Limit** |
| --- | --- |
| Endpoint name| Endpoint names must <li> Begin with a letter <li> Be 3-32 characters in length  <li> Only consist of letters and numbers <sup>1</sup> |
| Deployment name| Deployment names must <li> Begin with a letter <li> Be 3-32 characters in length  <li>  Only consist of letters and numbers <sup>1</sup> |
| Number of endpoints per subscription | 50 |
| Number of deployments per subscription | 200 |
| Number of deployments per endpoint | 20 |
| Number of instances per deployment | 20 <sup>2</sup> |
| Max request time-out at endpoint level  | 90 seconds |
| Total requests per second at endpoint level for all deployments  | 500 <sup>3</sup> |
| Total connections per second at endpoint level for all deployments  | 500 <sup>3</sup> |
| Total connections active at endpoint level for all deployments  | 500 <sup>3</sup> |
| Total bandwidth at endpoint level for all deployments  | 5 MBPS <sup>3</sup> |

<sup>1</sup> Single dashes like, `my-endpoint-name`, are accepted in endpoint and deployment names.

<sup>2</sup> We reserve 20% extra compute resources for performing upgrades. For example, if you request 10 instances in a deployment, you must have a quota for 12. Otherwise, you'll receive an error.

<sup>3</sup> If you request a limit increase, be sure to calculate related limit increases you might need. For example, if you request a limit increase for requests per second, you might also want to compute the required connections and bandwidth limits and include these limit increases in the same request.

To determine the current usage for an endpoint, [view the metrics](how-to-monitor-online-endpoints.md#metrics). 

To request an exception from the Azure Machine Learning product team, use the steps in the [Request quota increases](#request-quota-increases).


### Azure Machine Learning pipelines
[Azure Machine Learning pipelines](concept-ml-pipelines.md) have the following limits.

| **Resource** | **Limit** |
| --- | --- |
| Steps in a pipeline | 30,000 |
