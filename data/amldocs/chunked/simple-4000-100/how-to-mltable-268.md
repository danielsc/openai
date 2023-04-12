You can author `MLTable` files with the Python SDK. You can also directly author the MLTable file in an IDE (like VSCode). This example shows an MLTable file authored with the SDK:

```python

import mltable
from mltable import DataType

data_files = {
    'pattern': './*parquet'
}

tbl = mltable.from_parquet_files(path=[data_files])
# add additional transformations
# tbl = tbl.keep_columns()
# tbl = tbl.filter()

# save to local directory
tbl.save("<local_path>")

```

To directly author `MLTable` files, we recommend VSCode, because VSCode can handle auto-complete. Additionally, VSCode handles Azure Cloud Storage increases to your workspace, for seamless `MLTable` file edits on cloud storage.

To enable autocomplete and intellisense for `MLTable` files in VSCode, you'll need to associate the `MLTable` file with yaml.

In VSCode, select **File**>**Preferences**>**Settings**. In the search bar of the Settings tab, type *associations*:

:::image type="content" source="media/how-to-mltable/vscode-mltable.png" alt-text="file association in VSCode":::

Under **File: Associations** select **Add item** and then enter the following:

- Item: MLTable
- Value: yaml

You can then author MLTable files with autocomplete and intellisense, if you include the following schema at the top of your `MLTable` file.

```yml
$schema: https://azuremlschemas.azureedge.net/latest/MLTable.schema.json
```

> [!TIP]
> The Azure ML VSCode extension will show the available schemas and autocomplete when you type `$schema:`:
> :::image type="content" source="media/how-to-mltable/vscode-storage-ext-0.png" alt-text="Autocomplete":::

#### Where to store the `MLTable` file
We recommend co-location of the `MLTable` file with the underlying data, for example:

```Text
├── my_data
│   ├── MLTable
│   ├── file_1.txt
.
.
.
│   ├── file_n.txt
```

Co-location of the `MLTable` file with the data ensures a **self-contained *artifact*** that stores all needed resources in that one folder, regardless of whether that folder is stored on your local drive, in your cloud store, or on a public http server.

Since the `MLTable` will co-locate with the data, the `paths` defined in the `MLTable` file should be *relative to the location* of the `MLTable` file.  For example, in the above scenario, where the `MLTable` file is in the same folder as the `txt` data, define the paths as:

```yaml
type: mltable

# paths must be relative to the location of the MLTable file
paths:
  - pattern: ./*.txt

transformations:
  - read_delimited:
      delimiter: ','
      header: all_files_same_headers
```

#### How to co-locate `MLTable` files with data in cloud storage

Typically, you'll author your MLTable file either locally in an IDE (such as VSCode), or with a cloud-based VM such as an Azure ML Compute Instance. To create a self-contained MLTable *artifact*, you must store the `MLTable` file with the data. If you place your MLTable artifact (data and `MLTable` file) in your local storage, [Create Data asset](#create-a-data-asset) will become the easiest way to upload that artifact to cloud storage because your artifact will automatically upload.

If you already placed your data in cloud storage, you have some options to co-locate your `MLTable` file with the data.

##### Option 1: Directly author `MLTable` in cloud storage with VSCode

VSCode has an **[Azure Storage VSCode extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurestorage)** that can directly create and author files on Cloud storage. These steps show how to do it:

1. Install the [Azure Storage VSCode extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurestorage).
1. In the left-hand *Activity Bar*, select **Azure**, and find your subscription storage accounts (you can filter the UI by subscriptions):
    :::image type="content" source="media/how-to-mltable/vscode-storage-ext-1.png" alt-text="Screenshot of storage resources.":::
1. Next, navigate to the container (filesystem) that has your data, and select the **Open in Explorer** button:
