
# Troubleshoot Kubernetes Compute

In this article, you'll learn how to troubleshoot common problems you may encounter with using [Kubernetes compute](./how-to-attach-kubernetes-to-workspace.md) for training jobs and model deployments.

## Inference guide

### How to check sslCertPemFile and sslKeyPemFile is correct?
Use the commands below to run a baseline check for your cert and key. This is to allow for any known errors to be surfaced. Expect the second command to return "RSA key ok" without prompting you for password.

```bash
openssl x509 -in cert.pem -noout -text
openssl rsa -in key.pem -noout -check
```

Run the commands below to verify whether sslCertPemFile and sslKeyPemFile are matched:

```bash
openssl x509 -in cert.pem -noout -modulus | md5sum
openssl rsa -in key.pem -noout -modulus | md5sum
```

### Kubernetes compute errors

Below is a list of error types in **compute scope** that you might encounter when using Kubernetes compute to create online endpoints and online deployments for real-time model inference, which you can trouble shoot by following the guidelines:


* [ERROR: GenericComputeError](#error-genericcomputeerror)
* [ERROR: ComputeNotFound](#error-computenotfound)
* [ERROR: ComputeNotAccessible](#error-computenotaccessible)
* [ERROR: InvalidComputeInformation](#error-invalidcomputeinformation)
* [ERROR: InvalidComputeNoKubernetesConfiguration](#error-invalidcomputenokubernetesconfiguration)


#### ERROR: GenericComputeError
The error message is as below:

```bash
Failed to get compute information.
```

This error should occur when system failed to get the compute information from the Kubernetes cluster. You can check the following items to troubleshoot the issue:
* Check the Kubernetes cluster status. If the cluster isn't running, you need to start the cluster first.
* Check the Kubernetes cluster health.
    * You can view the cluster health check report for any issues, for example, if the cluster is not reachable.
    * You can go to your workspace portal to check the compute status.
* Check if the instance types is information is correct. You can check the supported instance types in the [Kubernetes compute](./how-to-attach-kubernetes-to-workspace.md) documentation.
* Try to detach and reattach the compute to the workspace if applicable.

> [!NOTE]
> To trouble shoot errors by reattaching, please guarantee to reattach with the exact same configuration as previously detached compute, such as the same compute name and namespace, otherwise you may encounter other errors.

#### ERROR: ComputeNotFound

The error message is as follows:

```bash
Cannot find Kubernetes compute.
```

This error should occur when:
* The system can't find the compute when create/update new online endpoint/deployment. 
* The compute of existing online endpoints/deployments have been removed. 

You can check the following items to troubleshoot the issue:
* Try to recreate the endpoint and deployment. 
* Try to detach and reattach the compute to the workspace. Pay attention to more notes on [reattach](#error-genericcomputeerror).


#### ERROR: ComputeNotAccessible
The error message is as follows:

```bash
The Kubernetes compute is not accessible.
```

This error should occur when the workspace MSI (managed identity) doesn't have access to the AKS cluster. You can check if the workspace MSI has the access to the AKS, and if not, you can follow this [document](how-to-identity-based-service-authentication.md) to manage access and identity.

#### ERROR: InvalidComputeInformation

The error message is as follows:

```bash
The compute information is invalid.
```
There is a compute target validation process when deploying models to your Kubernetes cluster. This error should occur when the compute information is invalid when validating, for example the compute target is not found, or the configuration of Azure Machine Learning extension has been updated in your Kubernetes cluster. 

You can check the following items to troubleshoot the issue:
