|`convert_column_types`     |  Adds a transformation step to convert the specified columns into their respective specified new types. | `columns`<br>An array of column names to convert.<br><br>`column_type`<br>The type to which you want to convert (`int`, `float`, `string`, `boolean`, `datetime`) | <code>- convert_column_types:<br>&emsp; &emsp;- columns: [Age]<br>&emsp; &emsp;&emsp; column_type: int</code><br> Convert the Age column to integer.<br><br><code>- convert_column_types:<br>&emsp; &emsp;- columns: date<br>&emsp; &emsp; &emsp;column_type:<br>&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;datetime:<br>&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;formats:<br>&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;- "%d/%m/%Y"</code><br>Convert the date column to the format `dd/mm/yyyy`. Read [`to_datetime`](/python/api/mltable/mltable.datatype#mltable-datatype-to-datetime) for more information about datetime conversion.<br><br><code>- convert_column_types:<br>&emsp; &emsp;- columns: [is_weekday]<br>&emsp; &emsp; &emsp;column_type:<br>&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;boolean:<br>&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;true_values:['yes', 'true', '1']<br>&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;&emsp; &emsp;false_values:['no', 'false', '0']</code><br> Convert the is_weekday column to a boolean; yes/true/1 values in the column will map to `True`, and no/false/0 values in the column will map to `False`. Read [`to_bool`](/python/api/mltable/mltable.datatype#mltable-datatype-to-bool) for more information about boolean conversion.
|`drop_columns`     |   Adds a transformation step to remove desired columns from the dataset. | An array of column names to drop | `- drop_columns: ["col1", "col2"]`
| `keep_columns` | Adds a transformation step to keep the specified columns, and remove all others from the dataset. | An array of column names to keep | `- keep_columns: ["col1", "col2"]` |
|`extract_columns_from_partition_format`   |     Adds a transformation step to use the partition information of each path, and then extract them into columns based on the specified partition format.| partition format to use |`- extract_columns_from_partition_format: {column_name:yyyy/MM/dd/HH/mm/ss}` creates a datetime column, where 'yyyy', 'MM', 'dd', 'HH', 'mm' and 'ss' are used to extract year, month, day, hour, minute and second values for the datetime type |
|`filter`    |    Filter the data, leaving only the records that match the specified expression.    |  An expression as a string. | `- filter: 'col("temperature") > 32 and col("location") == "UK"'` <br>Only leave rows where the temperature exceeds 32, and the location is the UK. |
|`skip`    | Adds a transformation step to skip the first count rows of this MLTable.   | A count of the number of rows to skip | `- skip: 10`<br> Skip first 10 rows
|`take`     | Adds a transformation step to select the first count rows of this MLTable.       | A count of the number of rows from the top of the table to take | `- take: 5`<br> Take the first five rows.
|`take_random_sample`     |    Adds a transformation step to randomly select each row of this MLTable, with probability chance.     | `probability`<br>The probability of selecting an individual row. Must be in the range [0,1].<br><br>`seed`<br>Optional random seed. | <code>- take_random_sample:<br>&emsp; &emsp;probability: 0.10<br>&emsp; &emsp;seed:123</code><br> Take a 10 percent random sample of rows using a random seed of 123.

## Examples

This section provides examples of MLTable use. More examples are available:

- [Working with tables in Azure Machine Learning](how-to-mltable.md)
- in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/sdk/python/assets/data). 

### Quickstart
In this quickstart, you'll read the famous iris dataset from a public https server. The `MLTable` files should be located in a folder, so create the folder and `MLTable` file using:

```bash
mkdir ./iris
cd ./iris
touch ./MLTable
```
