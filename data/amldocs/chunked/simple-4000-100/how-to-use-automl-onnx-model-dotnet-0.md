
# Make predictions with an AutoML ONNX model in .NET

In this article, you learn how to use an Automated ML (AutoML) Open Neural Network Exchange (ONNX) model to make predictions in a C# .NET Core console application with ML.NET.

[ML.NET](/dotnet/machine-learning/) is an open-source, cross-platform, machine learning framework for the .NET ecosystem that allows you to train and consume custom machine learning models using a code-first approach in C# or F# as well as through low-code tooling like [Model Builder](/dotnet/machine-learning/automate-training-with-model-builder) and the [ML.NET CLI](/dotnet/machine-learning/automate-training-with-cli). The framework is also extensible and allows you to leverage other popular machine learning frameworks like TensorFlow and ONNX.

ONNX is an open-source format for AI models. ONNX supports interoperability between frameworks. This means you can train a model in one of the many popular machine learning frameworks like PyTorch, convert it into ONNX format, and consume the ONNX model in a different framework like ML.NET. To learn more, visit the [ONNX website](https://onnx.ai/).

## Prerequisites

- [.NET Core SDK 3.1 or greater](https://dotnet.microsoft.com/download)
- Text Editor or IDE (such as [Visual Studio](https://visualstudio.microsoft.com/vs/) or [Visual Studio Code](https://code.visualstudio.com/Download))
- ONNX model. To learn how to train an AutoML ONNX model, see the following [bank marketing classification notebook](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/classification-bank-marketing-all-features/auto-ml-classification-bank-marketing-all-features.ipynb).
- [Netron](https://github.com/lutzroeder/netron) (optional)

## Create a C# console application

In this sample, you use the .NET Core CLI to build your application but you can do the same tasks using Visual Studio. Learn more about the [.NET Core CLI](/dotnet/core/tools/).

1. Open a terminal and create a new C# .NET Core console application. In this example, the name of the application is `AutoMLONNXConsoleApp`. A directory is created by that same name with the contents of your application.

    ```dotnetcli
    dotnet new console -o AutoMLONNXConsoleApp
    ```

1. In the terminal, navigate to the *AutoMLONNXConsoleApp* directory.

    ```bash
    cd AutoMLONNXConsoleApp
    ```

## Add software packages

1. Install the **Microsoft.ML**, **Microsoft.ML.OnnxRuntime**, and **Microsoft.ML.OnnxTransformer** NuGet packages using the .NET Core CLI.

    ```dotnetcli
    dotnet add package Microsoft.ML
    dotnet add package Microsoft.ML.OnnxRuntime
    dotnet add package Microsoft.ML.OnnxTransformer
    ```

    These packages contain the dependencies required to use an ONNX model in a .NET application. ML.NET provides an API that uses the [ONNX runtime](https://github.com/Microsoft/onnxruntime) for predictions.

1. Open the *Program.cs* file and add the following `using` statements at the top to reference the appropriate packages.

    ```csharp
    using System.Linq;
    using Microsoft.ML;
    using Microsoft.ML.Data;
    using Microsoft.ML.Transforms.Onnx;
    ```

## Add a reference to the ONNX model

A way for the console application to access the ONNX model is to add it to the build output directory.  To learn more about MSBuild common items, see the [MSBuild guide](/visualstudio/msbuild/common-msbuild-project-items).

Add a reference to your ONNX model file in your application

1. Copy your ONNX model to your application's *AutoMLONNXConsoleApp* root directory.
1. Open the *AutoMLONNXConsoleApp.csproj* file and add the following content inside the `Project` node.

    ```xml
    <ItemGroup>
        <None Include="automl-model.onnx">
            <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
        </None>
    </ItemGroup>
    ```

    In this case, the name of the ONNX model file is *automl-model.onnx*.

1. Open the *Program.cs* file and add the following line inside the `Program` class.
