> [!TIP]
> **Copy and Paste in Terminal**
> * Windows: `Ctrl-Insert` to copy and use `Ctrl-Shift-v` or `Shift-Insert` to paste.
> * Mac OS: `Cmd-c` to copy and `Cmd-v` to paste.
> * FireFox/IE may not support clipboard permissions properly.

2) Select and copy the SSH key output to your clipboard.
3) Next, follow the steps to add the SSH key to your preferred account type:

+ [GitHub](https://docs.github.com/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)

+ [GitLab](https://docs.gitlab.com/ee/user/ssh.html#add-an-ssh-key-to-your-gitlab-account)

+ [Azure DevOps](/azure/devops/repos/git/use-ssh-keys-to-authenticate#step-2--add-the-public-key-to-azure-devops-servicestfs)  Start at **Step 2**.

+ [BitBucket](https://support.atlassian.com/bitbucket-cloud/docs/set-up-an-ssh-key/#SetupanSSHkey-ssh2). Follow **Step 4**.

### Clone the Git repository with SSH

1) Copy the SSH Git clone URL from the Git repo.

2) Paste the url into the `git clone` command below, to use your SSH Git repo URL. This will look something like:

```bash
git clone git@example.com:GitUser/azureml-example.git
Cloning into 'azureml-example'...
```

You will see a response like:

```bash
The authenticity of host 'example.com (192.30.255.112)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.255.112' (RSA) to the list of known hosts.
```

SSH may display the server's SSH fingerprint and ask you to verify it. You should verify that the displayed fingerprint matches one of the fingerprints in the SSH public keys page.

SSH displays this fingerprint when it connects to an unknown host to protect you from [man-in-the-middle attacks](/previous-versions/windows/it-pro/windows-2000-server/cc959354(v=technet.10)). Once you accept the host's fingerprint, SSH will not prompt you again unless the fingerprint changes.

3) When you are asked if you want to continue connecting, type `yes`. Git will clone the repo and set up the origin remote to connect with SSH for future Git commands.

## Track code that comes from Git repositories

When you submit a training job from the Python SDK or Machine Learning CLI, the files needed to train the model are uploaded to your workspace. If the `git` command is available on your development environment, the upload process uses it to check if the files are stored in a git repository. If so, then information from your git repository is also uploaded as part of the training job. This information is stored in the following properties for the training job:

| Property | Git command used to get the value | Description |
| ----- | ----- | ----- |
| `azureml.git.repository_uri` | `git ls-remote --get-url` | The URI that your repository was cloned from. |
| `mlflow.source.git.repoURL` | `git ls-remote --get-url` | The URI that your repository was cloned from. |
| `azureml.git.branch` | `git symbolic-ref --short HEAD` | The active branch when the job was submitted. |
| `mlflow.source.git.branch` | `git symbolic-ref --short HEAD` | The active branch when the job was submitted. |
| `azureml.git.commit` | `git rev-parse HEAD` | The commit hash of the code that was submitted for the job. |
| `mlflow.source.git.commit` | `git rev-parse HEAD` | The commit hash of the code that was submitted for the job. |
| `azureml.git.dirty` | `git status --porcelain .` | `True`, if the branch/commit is dirty; otherwise, `false`. |

This information is sent for jobs that use an estimator, machine learning pipeline, or script run.

If your training files are not located in a git repository on your development environment, or the `git` command is not available, then no git-related information is tracked.

> [!TIP]
> To check if the git command is available on your development environment, open a shell session, command prompt, PowerShell or other command line interface and type the following command:
