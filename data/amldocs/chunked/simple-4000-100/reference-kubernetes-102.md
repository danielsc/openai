|azureml-fe-v2|	The front-end component that routes incoming inference requests to deployed services.	|Access logs at request level, including request ID, start time, response code, error details and durations for request latency. Trace logs for service metadata changes, service running healthy status, etc. for debugging purpose.|
| gateway	| The gateway is used to communicate and send data back and forth.	| Trace logs on requests from AzureML services to the clusters.|
|healthcheck	|--| 	The logs contain azureml namespace resource (AzureML extension) status to diagnose what make the extension not functional. |
|inference-operator-controller-manager|	Manage the lifecycle of inference endpoints.	|The logs contain AzureML inference endpoint and deployment pod status in the cluster.|
| metrics-controller-manager	| Manage the configuration for Prometheus.|Trace logs for status of uploading training job and inference  deployment metrics on CPU utilization and memory utilization.|
| relay server	| relay server is only needed in arc-connected cluster and will not be installed in AKS cluster.| Relay server works with Azure Relay to communicate with the cloud services.	The logs contain request level info from Azure relay.  |
 	

## AzureML jobs connect with custom data storage

[Persistent Volume (PV) and Persistent Volume Claim (PVC)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) are Kubernetes concept, allowing user to provide and consume various storage resources. 

1. Create PV, take NFS as example,

```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: nfs-pv 
spec:
  capacity:
    storage: 1Gi 
  accessModes:
    - ReadWriteMany 
  persistentVolumeReclaimPolicy: Retain
  storageClassName: ""
  nfs: 
    path: /share/nfs
    server: 20.98.110.84 
    readOnly: false
```
2. Create PVC in the same Kubernetes namespace with ML workloads. In `metadata`, you **must** add label `ml.azure.com/pvc: "true"` to be recognized by AzureML, and add annotation  `ml.azure.com/mountpath: <mount path>` to set the mount path. 

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: nfs-pvc  
  namespace: default
  labels:
    ml.azure.com/pvc: "true"
  annotations:
    ml.azure.com/mountpath: "/mnt/nfs"
spec:
  storageClassName: ""
  accessModes:
  - ReadWriteMany      
  resources:
     requests:
       storage: 1Gi
```
> [!IMPORTANT]
> Only the job pods in the same Kubernetes namespace with the PVC(s) will be mounted the volume. Data scientist is able to access the `mount path` specified in the PVC annotation in the job.


## Supported AzureML taints and tolerations

[Taint and Toleration](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) are Kubernetes concepts that work together to ensure that pods are not scheduled onto inappropriate nodes. 

Kubernetes clusters integrated with Azure Machine Learning (including AKS and Arc Kubernetes clusters) now support specific AzureML taints and tolerations, allowing users to add specific AzureML taints on the AzureML-dedicated nodes, to prevent non-AzureML workloads from being scheduled onto these dedicated nodes.

We only support placing the amlarc-specific taints on your nodes, which are defined as follows: 

| Taint | Key | Value | Effect | Description |
|--|--|--|--|--|
| amlarc overall| ml.azure.com/amlarc	| true| `NoSchddule`, `NoExecute`  or `PreferNoSchedule`| All Azureml workloads, including extension system service pods and machine learning workload pods would tolerate this `amlarc overall` taint.|
| amlarc system | ml.azure.com/amlarc-system |true	| `NoSchddule`, `NoExecute`  or `PreferNoSchedule`| Only Azureml extension system services pods would tolerate this `amlarc system` taint.|
| amlarc workload| 	ml.azure.com/amlarc-workload |true| `NoSchddule`, `NoExecute`  or `PreferNoSchedule`| Only machine learning workload pods would tolerate this `amlarc workload` taint. |
| amlarc resource group| 	ml.azure.com/resource-group | \<resource group name> | `NoSchddule`, `NoExecute`  or `PreferNoSchedule`| Only machine learning workload pods created from the specific resource group would tolerate this `amlarc resource group` taint.|
