   | **Resource Group** | Yes | **LA-TravelTime-RG** | The [Azure resource group](../azure-resource-manager/management/overview.md) where you create your logic app resource and related resources. This name must be unique across regions and can contain only letters, numbers, hyphens (`-`), underscores (`_`), parentheses (`(`, `)`), and periods (`.`). |
   | **Name** | Yes | **LA-TravelTime** | Your logic app resource name, which must be unique across regions and can contain only letters, numbers, hyphens (`-`), underscores (`_`), parentheses (`(`, `)`), and periods (`.`). |

1. Before you continue making selections, go to the **Plan** section. For **Plan type**, select **Consumption** to show only the settings for a Consumption logic app workflow, which runs in multi-tenant Azure Logic Apps.

   The **Plan type** property also specifies the billing model to use.

   | Plan type | Description |
   |-----------|-------------|
   | **Standard** | This logic app type is the default selection and runs in single-tenant Azure Logic Apps and uses the [Standard billing model](../logic-apps/logic-apps-pricing.md#standard-pricing). |
   | **Consumption** | This logic app type runs in global, multi-tenant Azure Logic Apps and uses the [Consumption billing model](../logic-apps/logic-apps-pricing.md#consumption-pricing). |

1. Now continue with the following selections:

   | Property | Required | Value | Description |
   |----------|----------|-------|-------------|
   | **Region** | Yes | **West US** | The Azure datacenter region for storing your app's information. This example deploys the sample logic app to the **West US** region in Azure. <br><br>**Note**: If your subscription is associated with an integration service environment, this list includes those environments. |
   | **Enable log analytics** | Yes | **No** | This option appears and applies only when you select the **Consumption** logic app type. Change this option only when you want to enable diagnostic logging. For this tutorial, keep the default selection. |

1. When you're done, select **Review + create**. After Azure validates the information about your logic app resource, select **Create**.

1. After Azure deploys your app, select **Go to resource**.

   Azure opens the workflow template selection pane, which shows an introduction video, commonly used triggers, and workflow template patterns.

1. Scroll down past the video and common triggers sections to the **Templates** section, and select **Blank Logic App**.

   ![Screenshot that shows the workflow template selection pane with "Blank Logic App" selected.](../logic-apps/media/tutorial-build-scheduled-recurring-logic-app-workflow/select-logic-app-template.png)


## Configure the workflow parameters

This Logic App will use parameters to store specific pieces of information that you will need to run the batch deployment. 

1. On the workflow designer, under the tool bar, select the option __Parameters__ and configure them as follows:

    :::image type="content" source="./media/how-to-use-event-grid-batch/parameters.png" alt-text="Screenshot of all the parameters required in the workflow.":::

1. To create a parameter, use the __Add parameter__ option:

    :::image type="content" source="./media/how-to-use-event-grid-batch/parameter.png" alt-text="Screenshot showing how to add one parameter in designer.":::
    
1. Create the following parameters.

    | Parameter             | Description  | Sample value |
    | --------------------- | -------------|------------- |
    | `tenant_id`           | Tenant ID where the endpoint is deployed  | `00000000-0000-0000-00000000` |
    | `client_id`           | The client ID of the service principal used to invoke the endpoint  | `00000000-0000-0000-00000000` |
    | `client_secret`       | The client secret of the service principal used to invoke the endpoint  | `ABCDEFGhijkLMNOPQRstUVwz` |
    | `endpoint_uri`        | The endpoint scoring URI  | `https://<endpoint_name>.<region>.inference.ml.azure.com/jobs` |
