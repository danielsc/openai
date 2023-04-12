   | **Headers** | `Authorization` with value `concat('Bearer ', body('Authorize')['access_token'])` | Click on __Add dynamic context__, then __Expression__, to enter this expression. |
   
1. In the parameter __Body__, click on __Add dynamic context__, then __Expression__, to enter the following expression:

   ```fx 
   replace('{
    "properties": {
    	"InputData": {
    		"mnistinput": {
    		 	"JobInputType" : "UriFile",
    	  		"Uri" : "<JOB_INPUT_URI>"
      		}
         }
     }
   }', '<JOB_INPUT_URI>', triggerBody()?[0]['data']['url'])
   ```
   
   The action will look as follows:
   
   :::image type="content" source="./media/how-to-use-event-grid-batch/invoke.png" alt-text="Screenshot of the invoke activity of the Logic App.":::
   
   > [!NOTE]
   > Notice that this last action will trigger the batch deployment job, but it will not wait for its completion. AzureLogic Apps is not designed for long-running applications. If you need to wait for the job to complete, we recommend you to switch to [Invoking batch endpoints from Azure Data Factory](how-to-use-batch-azure-data-factory.md).

1. Click on __Save__.

1. The Logic App is ready to be executed and it will trigger automatically each time a new file is created under the indicated path. You will notice the app has successfully received the event by checking the __Run history__ of it:

   :::image type="content" source="./media/how-to-use-event-grid-batch/invoke-history.png" alt-text="Screenshot of the invoke history of the Logic App.":::

## Next steps

* [Invoking batch endpoints from Azure Data Factory](how-to-use-batch-azure-data-factory.md)
