Now that you have a pipeline, it's time to use it to make predictions. ML.NET provides a convenience API for making predictions on a single data instance called [`PredictionEngine`](xref:Microsoft.ML.PredictionEngine%602).

1. Inside the `Main` method, create a [`PredictionEngine`](xref:Microsoft.ML.PredictionEngine%602) by using the [`CreatePredictionEngine`](xref:Microsoft.ML.ModelOperationsCatalog.CreatePredictionEngine%2A) method.

    ```csharp
    var onnxPredictionEngine = mlContext.Model.CreatePredictionEngine<OnnxInput, OnnxOutput>(onnxPredictionPipeline);
    ```

1. Create a test data input.

    ```csharp
    var testInput = new OnnxInput
    {
        VendorId = "CMT",
        RateCode = 1,
        PassengerCount = 1,
        TripTimeInSecs = 1271,
        TripDistance = 3.8f,
        PaymentType = "CRD"
    };
    ```

1. Use the `predictionEngine` to make predictions based on the new `testInput` data using the [`Predict`](xref:Microsoft.ML.PredictionEngineBase%602.Predict%2A) method.

    ```csharp
    var prediction = onnxPredictionEngine.Predict(testInput);
    ```

1. Output the result of your prediction to the console.

    ```csharp
    Console.WriteLine($"Predicted Fare: {prediction.PredictedFare.First()}");
    ```

1. Use the .NET Core CLI to run your application.

    ```dotnetcli
    dotnet run
    ```

    The result should look as similar to the following output:

    ```text
    Predicted Fare: 15.621523
    ```

To learn more about making predictions in ML.NET, see the [use a model to make predictions guide](/dotnet/machine-learning/how-to-guides/machine-learning-model-predictions-ml-net).

## Next steps

- [Deploy your model as an ASP.NET Core Web API](/dotnet/machine-learning/how-to-guides/serve-model-web-api-ml-net)
- [Deploy your model as a serverless .NET Azure Function](/dotnet/machine-learning/how-to-guides/serve-model-serverless-azure-functions-ml-net)