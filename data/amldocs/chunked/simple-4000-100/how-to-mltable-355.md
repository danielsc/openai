1. Next, navigate to the container (filesystem) that has your data, and select the **Open in Explorer** button:
    :::image type="content" source="media/how-to-mltable/vscode-storage-ext-2.png" alt-text="Screenshot highlighting the container to open in explorer.":::
1. Next, select **Add to Workspace**:
    :::image type="content" source="media/how-to-mltable/vscode-storage-ext-3.png" alt-text="Screenshot highlighting Add to Workspace.":::
1. In the **Explorer**, you can see your data in cloud storage, and it will appear alongside your code files:
1. To author an `MLTable` *in* cloud storage directly, navigate to the folder that contains the data, and then right-select **New File**. Name the file `MLTable` and proceed.
        :::image type="content" source="media/how-to-mltable/vscode-storage-ext-4.png" alt-text="Screenshot highlighting the data folder that will store the MLTable file.":::

##### Option 2: Upload `MLTable` file to cloud storage

The `azcopy` utility - pre-installed on Azure ML Compute Instance and DSVM - allows you to upload/download files from Azure Storage to your compute instance:

```bash
azcopy login

SOURCE=<path-to-mltable-file> # for example: ./MLTable
DEST=https://<account_name>.blob.core.windows.net/<container>/<path>
azcopy cp $SOURCE $DEST
```

If you author files locally (or in a DSVM), you can use `azcopy` or the [Azure Storage Explorer](https://azure.microsoft.com/products/storage/storage-explorer/), which allows you to manage files in Azure Storage with a Graphical User Interface (GUI). Once you download and install Azure Storage Explorer, select the storage account and container where you want to upload the `MLTable` file to. Next:

1. On the main pane's toolbar, select **Upload**, and then select **Upload Files**.
    :::image type="content" source="../media/vs-azure-tools-storage-explorer-blobs/blob-upload-files-menu.png" alt-text="Screenshot highlighting upload files.":::
1. In the **Select files to upload** dialog box, select the `MLTable` file you want to upload.
1. Select **Open** to begin the upload.

#### Supported transformations

##### Read transformations

|Read Transformation  | Parameters |
|---------|---------|
|`read_delimited` | `infer_column_types`: Boolean to infer column data types. Defaults to True. Type inference requires that the current compute can access the data source. Currently, type inference will only pull the first 200 rows.<br><br>`encoding`: Specify the file encoding. Supported encodings: `utf8`, `iso88591`, `latin1`, `ascii`, `utf16`, `utf32`, `utf8bom` and `windows1252`. Default encoding: `utf8`.<br><br>`header`: user can choose one of the following options: `no_header`, `from_first_file`, `all_files_different_headers`, `all_files_same_headers`. Defaults to `all_files_same_headers`.<br><br>`delimiter`: The separator used to split columns.<br><br>`empty_as_string`: Specify if empty field values should load as empty strings. The default (False) will read empty field values as nulls. Passing this setting as *True* will read empty field values as empty strings. If the values are converted to numeric or datetime, then this setting has no effect, as empty values will be converted to nulls.<br><Br>`include_path_column`: Boolean to keep path information as column in the table. Defaults to False. This setting is useful when reading multiple files, and you want to know from which file a specific record originated. Additionally, you can keep useful information in the file path.<br><br>`support_multi_line`: By default (`support_multi_line=False`), all line breaks, including line breaks in quoted field values, will be interpreted as a record break. This approach to data reading increases speed, and it offers optimization for parallel execution on multiple CPU cores. However, it may result in silent production of more records with misaligned field values. Set this value to True when the delimited files are known to contain quoted line breaks. |
| `read_parquet` | `include_path_column`: Boolean to keep path information as a table column. Defaults to False. This setting helps when you read multiple files, and you want to know from which file a specific record originated. Additionally, you can keep useful information in the file path. |
