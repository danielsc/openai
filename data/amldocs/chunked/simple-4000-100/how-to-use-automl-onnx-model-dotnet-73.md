    In this case, the name of the ONNX model file is *automl-model.onnx*.

1. Open the *Program.cs* file and add the following line inside the `Program` class.

    ```csharp
    static string ONNX_MODEL_PATH = "automl-model.onnx";
    ```

## Initialize MLContext

Inside the `Main` method of your `Program` class, create a new instance of [`MLContext`](xref:Microsoft.ML.MLContext).

```csharp
MLContext mlContext = new MLContext();
```

The [`MLContext`](xref:Microsoft.ML.MLContext) class is a starting point for all ML.NET operations, and initializing `mlContext` creates a new ML.NET environment that can be shared across the model lifecycle. It's similar, conceptually, to DbContext in Entity Framework.

## Define the model data schema

Your model expects your input and output data in a specific format. ML.NET allows you to define the format of your data via classes. Sometimes you may already know what that format looks like. In cases when you don't know the data format, you can use tools like Netron to inspect your ONNX model.

The model used in this sample uses data from the NYC TLC Taxi Trip dataset. A sample of the data can be seen below:

|vendor_id|rate_code|passenger_count|trip_time_in_secs|trip_distance|payment_type|fare_amount|
|---|---|---|---|---|---|---|
|VTS|1|1|1140|3.75|CRD|15.5|
|VTS|1|1|480|2.72|CRD|10.0|
|VTS|1|1|1680|7.8|CSH|26.5|

### Inspect the ONNX model (optional)

Use a tool like Netron to inspect your model's inputs and outputs.

1. Open Netron.
1. In the top menu bar, select **File > Open** and use the file browser to select your model.
1. Your model opens. For example, the structure of the *automl-model.onnx* model looks like the following:

    :::image type="content" source="media/how-to-use-automl-onnx-model-dotnet/netron-automl-onnx-model.png" alt-text="Netron AutoML ONNX Model":::

1. Select the last node at the bottom of the graph (`variable_out1` in this case) to display the model's metadata. The inputs and outputs on the sidebar show you the model's expected inputs, outputs, and data types. Use this information to define the input and output schema of your model.

### Define model input schema

Create a new class called `OnnxInput` with the following properties inside the *Program.cs* file.

```csharp
public class OnnxInput
{
    [ColumnName("vendor_id")]
    public string VendorId { get; set; }

    [ColumnName("rate_code"),OnnxMapType(typeof(Int64),typeof(Single))]
    public Int64 RateCode { get; set; }

    [ColumnName("passenger_count"), OnnxMapType(typeof(Int64), typeof(Single))]
    public Int64 PassengerCount { get; set; }

    [ColumnName("trip_time_in_secs"), OnnxMapType(typeof(Int64), typeof(Single))]
    public Int64 TripTimeInSecs { get; set; }

    [ColumnName("trip_distance")]
    public float TripDistance { get; set; }

    [ColumnName("payment_type")]
    public string PaymentType { get; set; }
}
```

Each of the properties maps to a column in the dataset. The properties are further annotated with attributes.

The [`ColumnName`](xref:Microsoft.ML.Data.ColumnNameAttribute) attribute lets you specify how ML.NET should reference the column when operating on the data. For example, although the `TripDistance` property follows standard .NET naming conventions, the model only knows of a column or feature known as `trip_distance`. To address this naming discrepancy, the [`ColumnName`](xref:Microsoft.ML.Data.ColumnNameAttribute) attribute maps the `TripDistance` property to a column or feature by the name `trip_distance`.
  
For numerical values, ML.NET only operates on [`Single`](xref:System.Single) value types. However, the original data type of some of the columns are integers. The [`OnnxMapType`](xref:Microsoft.ML.Transforms.Onnx.OnnxMapTypeAttribute) attribute maps types between ONNX and ML.NET.

To learn more about data attributes, see the [ML.NET load data guide](/dotnet/machine-learning/how-to-guides/load-data-ml-net).

### Define model output schema

Once the data is processed, it produces an output of a certain format. Define your data output schema. Create a new class called `OnnxOutput` with the following properties inside the *Program.cs* file.
