# Git integration for Azure Machine Learning

[Git](https://git-scm.com/) is a popular version control system that allows you to share and collaborate on your projects. 

Azure Machine Learning fully supports Git repositories for tracking work - you can clone repositories directly onto your shared workspace file system, use Git on your local workstation, or use Git from a CI/CD pipeline.

When submitting a job to Azure Machine Learning, if source files are stored in a local git repository then information about the repo is tracked as part of the training process.

Since Azure Machine Learning tracks information from a local git repo, it isn't tied to any specific central repository. Your repository can be cloned from GitHub, GitLab, Bitbucket, Azure DevOps, or any other git-compatible service.

> [!TIP]
> Use Visual Studio Code to interact with Git through a graphical user interface. To connect to an Azure Machine Learning remote compute instance using Visual Studio Code, see [Connect to an Azure Machine Learning compute instance in Visual Studio Code (preview)](how-to-set-up-vs-code-remote.md)
>
> For more information on Visual Studio Code version control features, see [Using Version Control in VS Code](https://code.visualstudio.com/docs/editor/versioncontrol) and [Working with GitHub in VS Code](https://code.visualstudio.com/docs/editor/github).

## Clone Git repositories into your workspace file system
Azure Machine Learning provides a shared file system for all users in the workspace.
To clone a Git repository into this file share, we recommend that you create a compute instance & [open a terminal](how-to-access-terminal.md).
Once the terminal is opened, you have access to a full Git client and can clone and work with Git via the Git CLI experience.

We recommend that you clone the repository into your user directory so that others will not make collisions directly on your working branch.

> [!TIP]
> There is a performance difference between cloning to the local file system of the compute instance or cloning to the mounted filesystem (mounted as  the `~/cloudfiles/code` directory). In general, cloning to the local filesystem will have better performance than to the mounted filesystem. However, the local filesystem is lost if you delete and recreate the compute instance. The mounted filesystem is kept if you delete and recreate the compute instance.

You can clone any Git repository you can authenticate to (GitHub, Azure Repos, BitBucket, etc.)

For more information about cloning, see the guide on [how to use Git CLI](https://guides.github.com/introduction/git-handbook/).

## Authenticate your Git Account with SSH
### Generate a new SSH key
1) [Open the terminal window](./how-to-access-terminal.md) in the Azure Machine Learning Notebook Tab.

2) Paste the text below, substituting in your email address.

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

This creates a new ssh key, using the provided email as a label.

```
> Generating public/private rsa key pair.
```

3) When you're prompted to "Enter a file in which to save the key" press Enter. This accepts the default file location.

4) Verify that the default location is '/home/azureuser/.ssh' and press enter. Otherwise specify the location '/home/azureuser/.ssh'.

> [!TIP]
> Make sure the SSH key is saved in '/home/azureuser/.ssh'. This file is saved on the compute instance is only accessible by the owner of the Compute Instance

```
> Enter a file in which to save the key (/home/azureuser/.ssh/id_rsa): [Press enter]
```

5) At the prompt, type a secure passphrase. We recommend you add a passphrase to your SSH key for added security

```
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
```

### Add the public key to Git Account
1) In your terminal window, copy the contents of your public key file. If you renamed the key, replace id_rsa.pub with the public key file name.

```bash
cat ~/.ssh/id_rsa.pub
```
