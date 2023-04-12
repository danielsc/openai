|ParallelRunStep.output|parallel_run_function.outputs|The outputs of this parallel job.|
|ParallelRunStep.side_inputs|parallel_run_function.inputs|Defined together with `inputs`.|
|ParallelRunStep.arguments|parallel_run_function.task.program_arguments|The arguments of the parallel task.|
|ParallelRunStep.allow_reuse|parallel_run_function.is_deterministic|Specify whether the parallel will return same output given same input.|

## Next steps

For more information, see the documentation here:

* [Parallel run step SDK v1 examples](https://github.com/Azure/MachineLearningNotebooks/tree/master/how-to-use-azureml/machine-learning-pipelines/parallel-run)
* [Parallel job SDK v2 examples](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/pipelines/1g_pipeline_with_parallel_nodes/pipeline_with_parallel_nodes.ipynb)
