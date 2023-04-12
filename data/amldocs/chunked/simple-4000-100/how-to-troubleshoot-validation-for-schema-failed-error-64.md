In the submitted YAML file, go to the “path” parameter and double check whether the file / folder path provided is written correctly (that is, path is complete, no spelling mistakes, no missing file extension, special characters, etc.). Save the YAML file and resubmit the command. If the error still persists, the file / folder doesn't exist in the location provided.

## Error - Missing Field

The submitted YAML file is missing a required parameter. For example – for ml job create (that is, `commandjob` schema), if the “compute” parameter isn't provided, this error will be encountered because compute is required to run a command job.

### Solution - Missing Field

Check the prescribed schema for the asset type you're trying to create or update – check what parameters are required and what their correct value types are. [Here's a list of schemas](reference-yaml-overview.md) for different asset types in AzureML v2. Ensure that the submitted YAML file has all the required parameters needed. Also ensure that the values provided for those parameters are of the correct type, or in the accepted range of values. Save the YAML file and resubmit the command.

## Error - Cannot Parse

The submitted YAML file can't be read, because either the syntax is wrong, formatting is wrong, or there are unwanted characters somewhere in the file. For example – a special character (like a colon or a semicolon) that has been entered by mistake somewhere in the YAML file.

### Solution - Cannot Parse

Double check the contents of the submitted YAML file for correct syntax, unwanted characters, and wrong formatting. Fix all of these, save the YAML file and resubmit the command.

## Error - Resource Not Found

One or more of the resources (for example, file / folder) in the submitted YAML file doesn't exist, or you don't have access to it.

### Solution - Resource Not Found

Double check whether the name of the resource has been specified correctly, and that you have access to it. Make changes if needed, save the YAML file and resubmit the command.

## Error - Cannot Serialize

One or more fields in the YAML can't be serialized (converted) into objects.

### Solution - Cannot Serialize

Double check that your YAML file isn't corrupted and that the file’s contents are properly formatted.
