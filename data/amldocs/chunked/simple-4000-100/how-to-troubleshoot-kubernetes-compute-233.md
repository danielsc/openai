*  Find workspace ID in Azure portal or get this ID by running `az ml workspace show` in the command line.
*  Show all azureml-fe pods run by `kubectl get po -n azureml -l azuremlappname=azureml-fe`.
*  Login into any of them run `kubectl exec -it -n azureml {scorin_fe_pod_name} bash`.
*  If the cluster doesn't use proxy run `nslookup {workspace_id}.workspace.{region}.api.azureml.ms`.
If you set up private link from VNet to workspace correctly, then the internal IP in VNet should be responded through the *DNSLookup* tool.

*  If the cluster uses proxy, you can try to `curl` workspace 
 ```bash
curl https://{workspace_id}.workspace.westcentralus.api.azureml.ms/metric/v2.0/subscriptions/{subscription}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/api/2.0/prometheus/post -X POST -x {proxy_address} -d {} -v -k
```

If the proxy and workspace with private link is configured correctly, you can see it's trying to connect to an internal IP. This will return a response with http 401, which is expected when you don't provide token.

## Next steps

- [How to troubleshoot kubernetes extension](how-to-troubleshoot-kubernetes-extension.md)
- [How to troubleshoot online endpoints](how-to-troubleshoot-online-endpoints.md)
- [Deploy and score a machine learning model by using an online endpoint](how-to-deploy-online-endpoints.md)