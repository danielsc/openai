Next, decide if you want to use an [Azure Blob storage](../storage/blobs/storage-blobs-introduction.md) account or [Azure Data Lake Storage Gen2](../storage/blobs/data-lake-storage-introduction.md). To create Azure Data Lake Storage Gen2, set `storage_account_hns` to `true`. To create Azure Blob Storage, set `storage_account_hns` to `false`. The `storage_account_hns` field is under each `location` in the `replication_locations` list.

> [!NOTE]
>The `hns` portion of `storage_account_hns` refers to the [hierarchical namespace](../storage/blobs/data-lake-storage-namespace.md) capability of Azure Data Lake Storage Gen2 accounts.

Below is an example YAML that demonstrates this advanced storage configuration:

```YAML
name: DemoRegistry2
description: Registry with additional configuration for storage accounts
tags:
  foo: bar
location: eastus
replication_locations:
  - location: eastus
    storage_config:
      storage_account_hns: False
      storage_account_type: Standard_LRS
  - location: eastus2
    storage_config:
      storage_account_hns: False
      storage_account_type: Standard_LRS
  - location: westus
    storage_config:
      storage_account_hns: False
      storage_account_type: Standard_LRS
```

## Add users to the registry 

Decide if you want to allow users to only use assets (models, environments and components) from the registry or both use and create assets in the registry. Review [steps to assign a role](../role-based-access-control/role-assignments-steps.md) if you aren't familiar how to manage permissions using [Azure role-based access control](../role-based-access-control/overview.md).

### Allow users to use assets from the registry

To let a user only read assets, you can grant the user the built-in __Reader__ role. If don't want to use the built-in role, create a custom role with the following permissions

Permission | Description 
--|--
Microsoft.MachineLearningServices/registries/read | Allows the user to list registries and get registry metadata
Microsoft.MachineLearningServices/registries/assets/read | Allows the user to browse assets and use the assets in a workspace

### Allow users to create and use assets from the registry

To let the user both read and create or delete assets, grant the following write permission in addition to the above read permissions.

Permission | Description 
--|--
Microsoft.MachineLearningServices/registries/assets/write | Create assets in registries
Microsoft.MachineLearningServices/registries/assets/delete| Delete assets in registries

> [!WARNING]
> The built-in __Contributor__ and __Owner__ roles allow users to create, update and delete registries. You must create a custom role if you want the user to create and use assets from the registry, but not create or update registries. Review [custom roles](../role-based-access-control/custom-roles.md) to learn how to create custom roles from permissions.

### Allow users to create and manage registries

To let users create, update and delete registries, grant them the built-in __Contributor__ or __Owner__ role. If you don't want to use built in roles, create a custom role with the following permissions, in addition to all the above permissions to read, create and delete assets in registry.

Permission | Description 
--|--
Microsoft.MachineLearningServices/registries/write| Allows the user to create or update registries
Microsoft.MachineLearningServices/registries/delete | Allows the user to delete registries


## Next steps

* [Learn how to share models, components and environments across workspaces with registries (preview)](./how-to-share-models-pipelines-across-workspaces-with-registries.md)