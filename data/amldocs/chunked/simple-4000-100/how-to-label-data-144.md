    :::image type="content" source="media/how-to-label-data/polygon.gif" alt-text="Create polygons for Cat and Dog":::

To delete a polygon, select the X-shaped target that appears next to the polygon after creation.

If you want to change the tag for a polygon, select the **Move region** tool, select the polygon, and select the correct tag.

You can edit existing polygons. The **Lock/unlock regions** tool ![Edit polygons with the lock/unlock regions tool](./media/how-to-label-data/lock-bounding-boxes-tool.png) or "L" toggles that behavior. If regions are locked, you can only change the shape or location of a new polygon.

Use the **Add or remove polygon points** tool ![This is the add or remove polygon points tool icon.](./media/how-to-label-data/add-remove-points-tool.png) or "U" to adjust an existing polygon. Select the polygon to add or remove a point. If you can't edit a region, you've probably toggled the **Lock/unlock regions** tool.

To delete *all* polygons in the current image, select the **Delete all regions** tool ![Delete all regions tool](./media/how-to-label-data/delete-regions-tool.png).

After you create the polygons for an image, select **Submit** to save your work, or your work in progress won't be saved.

## Label text

When tagging text, use the toolbar to:

* Increase or decrease the text size
* Change the font
* Skip labeling this item and move to the next item

If you realize that you made a mistake after you assign a tag, you can fix it. Select the "**X**" on the label that's displayed below the text to clear the tag.

There are three text project types:

|Project type  | Description  |
|---------|---------|
| Classification Multi-Class | Assign a single tag to the entire text entry.  You can only select one tag for each text item.  Select a tag and then select **Submit** to move to the next entry.  |
| Classification Multi-Label     | Assign one *or more* tags to each text entry.  You can select multiple tags for each text item.   Select all the tags that apply and then select **Submit** to move to the next entry.    |
| Named entity recognition | Tag different words or phrases in each text entry.  See directions in the section below.


To see the project-specific directions, select **Instructions** and go to **View detailed instructions**.

### Tag words and phrases 

If your project is set up for named entity recognition, you tag different words or phrases in each text item. To label text:

1. Select the label or type the number corresponding to the appropriate label
1. Double-click on a word, or use your mouse to select multiple words.

:::image type="content" source="media/how-to-label-data/named-entity-labeling.png" alt-text="Screenshot: Named entity recognition.":::

To change a label, you can:

* Delete the label and start again.
* Change the value for all or some of a specific label in your current item:
    * Select the label itself, which will select all instances of that label.  
    * Select again on the instances of this label to unselect any instances you don't want to change.  
    * Finally, select a new label to change all the labels that are still selected.

When you've tagged all the items in an entry, select **Submit** to move to the next entry.

## Finish up

When you submit a page of tagged data, Azure assigns new unlabeled data to you from a work queue. If there's no more unlabeled data available, you'll get a message noting this along with a link to the portal home page.

When you're done labeling, select your image inside a circle in the upper-right corner of the studio and then select **sign-out**. If you don't sign out, eventually Azure will "time you out" and assign your data to another labeler.

## Next steps

* Learn to [train image classification models in Azure](./tutorial-train-deploy-notebook.md)
