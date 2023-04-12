
#### Accessing data from your Azure Databricks filesystem (`dbfs`)

Filesystem spec (`fsspec`) has a range of [known implementations](https://filesystem-spec.readthedocs.io/en/stable/_modules/index.html), one of which is the Databricks Filesystem (`dbfs`).

To access data from `dbfs` you will need:

- **Instance name**, which is in the form of `adb-<some-number>.<two digits>.azuredatabricks.net`. You can glean this from the URL of your Azure Databricks workspace.
- **Personal Access Token (PAT)**, for more information on creating a PAT, please see [Authentication using Azure Databricks personal access tokens](/azure/databricks/dev-tools/api/latest/authentication)

Once you have these, you will need to create an environment variable on your compute instance for the PAT token:

```bash
export ADB_PAT=<pat_token>
```

You can then access data in Pandas using:

```python
import os
import pandas as pd

pat = os.getenv(ADB_PAT)
path_on_dbfs = '<absolute_path_on_dbfs>' # e.g. /folder/subfolder/file.csv

storage_options = {
    'instance':'adb-<some-number>.<two digits>.azuredatabricks.net', 
    'token': pat
}

df = pd.read_csv(f'dbfs://{path_on_dbfs}', storage_options=storage_options)
```

#### Reading images with `pillow`

```python
from PIL import Image
from azureml.fsspec import AzureMachineLearningFileSystem

# define the URI - update <> placeholders
uri = 'azureml://subscriptions/<subid>/resourcegroups/<rgname>/workspaces/<workspace_name>/datastores/<datastore_name>/paths/<folder>/<image.jpeg>'

# create the filesystem
fs = AzureMachineLearningFileSystem(uri)

with fs.open() as f:
    img = Image.open(f)
    img.show()
```

#### PyTorch custom dataset example

In this example, you create a PyTorch custom dataset for processing images. The assumption is that an annotations file (in CSV format) exists that looks like:

```text
image_path, label
0/image0.png, label0
0/image1.png, label0
1/image2.png, label1
1/image3.png, label1
2/image4.png, label2
2/image5.png, label2
```

The images are stored in subfolders according to their label:

```text
/
└── 📁images
    ├── 📁0
    │   ├── 📷image0.png
    │   └── 📷image1.png
    ├── 📁1
    │   ├── 📷image2.png
    │   └── 📷image3.png
    └── 📁2
        ├── 📷image4.png
        └── 📷image5.png
```

A custom Dataset class in PyTorch must implement three functions: `__init__`, `__len__`, and `__getitem__`, which are implemented below:

```python
import os
import pandas as pd
from PIL import Image
from torch.utils.data import Dataset

class CustomImageDataset(Dataset):
    def __init__(self, filesystem, annotations_file, img_dir, transform=None, target_transform=None):
        self.fs = filesystem
        f = filesystem.open(annotations_file)
        self.img_labels = pd.read_csv(f)
        f.close()
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        f = self.fs.open(img_path)
        image = Image.open(f)
        f.close()
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
```

You can then instantiate the dataset using:

```python
from azureml.fsspec import AzureMachineLearningFileSystem
from torch.utils.data import DataLoader

# define the URI - update <> placeholders
uri = 'azureml://subscriptions/<subid>/resourcegroups/<rgname>/workspaces/<workspace_name>/datastores/<datastore_name>/paths/<folder>/'

# create the filesystem
fs = AzureMachineLearningFileSystem(uri)

# create the dataset
training_data = CustomImageDataset(
    filesystem=fs,
    annotations_file='<datastore_name>/<path>/annotations.csv', 
    img_dir='<datastore_name>/<path_to_images>/'
)

# Preparing your data for training with DataLoaders
train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
```
