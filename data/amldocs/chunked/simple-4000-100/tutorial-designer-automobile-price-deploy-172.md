* If your inference graph contains "Enter Data Manually" component which is not connected to the same port as “Web service Input” component, the "Enter Data Manually" component will not be executed during HTTP call processing. A workaround is to register the outputs of that "Enter Data Manually" component as dataset, then in the inference pipeline draft, replace the "Enter Data Manually" component with the registered dataset. 

    :::image type="content" source="./media/tutorial-designer-automobile-price-deploy/real-time-inferencepipeline-limitation.png" alt-text="Screenshot showing how to modify inference pipeline containing enter data manually component.":::

## Clean up resources

[!INCLUDE [aml-ui-cleanup](../../includes/aml-ui-cleanup.md)]

## Next steps

In this tutorial, you learned the key steps in how to create, deploy, and consume a machine learning model in the designer. To learn more about how you can use the designer see the following links:

+ [Designer samples](samples-designer.md): Learn how to use the designer to solve other types of problems.
+ [Use Azure Machine Learning studio in an Azure virtual network](how-to-enable-studio-virtual-network.md).
