Changes required in AML:
- allow the job to react to cancellation by the user, such that the fine_tune get's cancelled, too
- enable the injection of keys into environment variables (both job and deployment)
- scenario polishing, esp. pipelines/designer/components

Changes to a AOAI service:
- provide metrics incrementally to enable early-stopping through hyperdrive

Issues:
- Event Streaming is not working through streaming REST API (connection closes after 2 minutes)
- Job cancellation not working through rest but through Python API (didn't debug deeply)
- Where is the reference documentation for the Python API?