

### Delta Lake

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/MLTable.schema.json
type: mltable

# Supported paths include:
# local: ./<path>
# blob: wasbs://<container_name>@<account_name>.blob.core.windows.net/<path>
# Public http(s) server: https://<url>
# ADLS gen2: abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>/
# Datastore: azureml://subscriptions/<subid>/resourcegroups/<rg>/workspaces/<ws>/datastores/<datastore_name>/paths/<path>

paths:
- folder: abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>/

# NOTE: for read_delta_lake, you are *required* to provide either
# timestamp_as_of OR version_as_of.
# timestamp should be in RFC-3339/ISO-8601 format (for example:
# "2022-10-01T00:00:00Z", "2022-10-01T00:00:00+08:00",
# "2022-10-01T01:30:00-08:00")
# To get the latest, set the timestamp_as_of at a future point (for example: '2999-08-26T00:00:00Z')

transformations:
 - read_delta_lake:
      timestamp_as_of: '2022-08-26T00:00:00Z'
      # alternative:
      # version_as_of: 1   
```

### JSON
```yaml
$schema: https://azuremlschemas.azureedge.net/latest/MLTable.schema.json
paths:
  - file: ./order_invalid.jsonl
transformations:
  - read_json_lines:
        encoding: utf8
        invalid_lines: drop
        include_path_column: false
```



## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
- [Working with tables in Azure Machine Learning](how-to-mltable.md)