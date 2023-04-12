Once the data is processed, it produces an output of a certain format. Define your data output schema. Create a new class called `OnnxOutput` with the following properties inside the *Program.cs* file.

```csharp
public class OnnxOutput
{
    [ColumnName("variable_out1")]
    public float[] PredictedFare { get; set; }
}
```

Similar to `OnnxInput`, use the [`ColumnName`](xref:Microsoft.ML.Data.ColumnNameAttribute) attribute to map the `variable_out1` output to a more descriptive name `PredictedFare`.

## Define a prediction pipeline

A pipeline in ML.NET is typically a series of chained transformations that operate on the input data to produce an output. To learn more about data transformations, see the [ML.NET data transformation guide](/dotnet/machine-learning/resources/transforms).

1. Create a new method called `GetPredictionPipeline` inside the `Program` class

    ```csharp
    static ITransformer GetPredictionPipeline(MLContext mlContext)
    {

    }
    ```

1. Define the name of the input and output columns. Add the following code inside the `GetPredictionPipeline` method.

    ```csharp
    var inputColumns = new string []
    {
        "vendor_id", "rate_code", "passenger_count", "trip_time_in_secs", "trip_distance", "payment_type"
    };

    var outputColumns = new string [] { "variable_out1" };
    ```

1. Define your pipeline. An [`IEstimator`](xref:Microsoft.ML.IEstimator%601) provides a blueprint of the operations, input, and output schemas of your pipeline.

    ```csharp
    var onnxPredictionPipeline =
        mlContext
            .Transforms
            .ApplyOnnxModel(
                outputColumnNames: outputColumns,
                inputColumnNames: inputColumns,
                ONNX_MODEL_PATH);
    ```

    In this case, [`ApplyOnnxModel`](xref:Microsoft.ML.OnnxCatalog.ApplyOnnxModel%2A) is the only transform in the pipeline, which takes in the names of the input and output columns as well as the path to the ONNX model file.

1. An [`IEstimator`](xref:Microsoft.ML.IEstimator%601) only defines the set of operations to apply to your data. What operates on your data is known as an [`ITransformer`](xref:Microsoft.ML.ITransformer). Use the `Fit` method to create one from your `onnxPredictionPipeline`.

    ```csharp
    var emptyDv = mlContext.Data.LoadFromEnumerable(new OnnxInput[] {});

    return onnxPredictionPipeline.Fit(emptyDv);
    ```

    The [`Fit`](xref:Microsoft.ML.IEstimator%601.Fit%2A) method expects an [`IDataView`](xref:Microsoft.ML.IDataView) as input to perform the operations on. An [`IDataView`](xref:Microsoft.ML.IDataView) is a way to represent data in ML.NET using a tabular format. Since in this case the pipeline is only used for predictions, you can provide an empty [`IDataView`](xref:Microsoft.ML.IDataView) to give the [`ITransformer`](xref:Microsoft.ML.ITransformer) the necessary input and output schema information. The fitted [`ITransformer`](xref:Microsoft.ML.ITransformer) is then returned for further use in your application.

    > [!TIP]
    > In this sample, the pipeline is defined and used within the same application. However, it is recommended that you use separate applications to define and use your pipeline to make predictions. In ML.NET your pipelines can be serialized and saved for further use in other .NET end-user applications. ML.NET supports various deployment targets such as desktop applications, web services, WebAssembly applications*, and many more. To learn more about saving pipelines, see the [ML.NET save and load trained models guide](/dotnet/machine-learning/how-to-guides/save-load-machine-learning-models-ml-net).
    >
    > *WebAssembly is only supported in .NET Core 5 or greater

1. Inside the `Main` method, call the `GetPredictionPipeline` method with the required parameters.

    ```csharp
    var onnxPredictionPipeline = GetPredictionPipeline(mlContext);
    ```

## Use the model to make predictions

Now that you have a pipeline, it's time to use it to make predictions. ML.NET provides a convenience API for making predictions on a single data instance called [`PredictionEngine`](xref:Microsoft.ML.PredictionEngine%602).
