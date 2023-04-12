To correct a mistake, select the "**X**" to clear an individual tag or select the images and then select the tag, which clears the tag from all the selected images. This scenario is shown here. Selecting "Land" will clear that tag from the two selected images.

![A screenshot shows multiple deselections](./media/how-to-label-data/multiple-deselection.png)

Azure will only enable the **Submit** button after you've applied at least one tag to each image. Select **Submit** to save your work.

## Tag images and specify bounding boxes for object detection

If your project is of type "Object Identification (Bounding Boxes)," you'll specify one or more bounding boxes in the image and apply a tag to each box. Images can have multiple bounding boxes, each with a single tag. Use **View detailed instructions** to determine if multiple bounding boxes are used in your project.

1. Select a tag for the bounding box that you plan to create.
1. Select the **Rectangular box** tool ![Rectangular box tool](./media/how-to-label-data/rectangular-box-tool.png) or select "R."
3. Select and drag diagonally across your target to create a rough bounding box. To adjust the bounding box, drag the edges or corners.

![Bounding box creation](./media/how-to-label-data/bounding-box-sequence.png)

To delete a bounding box, select the X-shaped target that appears next to the bounding box after creation.

You can't change the tag of an existing bounding box. If you make a tag-assignment mistake, you have to delete the bounding box and create a new one with the correct tag.

By default, you can edit existing bounding boxes. The **Lock/unlock regions** tool ![Lock/unlock regions tool](./media/how-to-label-data/lock-bounding-boxes-tool.png) or "L" toggles that behavior. If regions are locked, you can only change the shape or location of a new bounding box.

Use the **Regions manipulation** tool ![This is the regions manipulation tool icon - four arrows pointing outward from the center, up, right, down, and left.](./media/how-to-label-data/regions-tool.png) or "M" to adjust an existing bounding box. Drag the edges or corners to adjust the shape. Select in the interior to be able to drag the whole bounding box. If you can't edit a region, you've probably toggled the **Lock/unlock regions** tool.

Use the **Template-based box** tool ![Template-box tool](./media/how-to-label-data/template-box-tool.png) or "T" to create multiple bounding boxes of the same size. If the image has no bounding boxes and you activate template-based boxes, the tool will produce 50-by-50-pixel boxes. If you create a bounding box and then activate template-based boxes, any new bounding boxes will be the size of the last box that you created. Template-based boxes can be resized after placement. Resizing a template-based box only resizes that particular box.

To delete *all* bounding boxes in the current image, select the **Delete all regions** tool ![Delete regions tool](./media/how-to-label-data/delete-regions-tool.png).

After you create the bounding boxes for an image, select **Submit** to save your work, or your work in progress won't be saved.

## Tag images and specify polygons for image segmentation

If your project is of type "Instance Segmentation (Polygon)," you'll specify one or more polygons in the image and apply a tag to each polygon. Images can have multiple bounding polygons, each with a single tag. Use **View detailed instructions** to determine if multiple bounding polygons are used in your project.

1. Select a tag for the polygon that you plan to create.
1. Select the **Draw polygon region** tool ![Draw polygon region tool](./media/how-to-label-data/polygon-tool.png) or select "P."
1. Select for each point in the polygon.  When you've completed the shape, double-click to finish.

    :::image type="content" source="media/how-to-label-data/polygon.gif" alt-text="Create polygons for Cat and Dog":::

To delete a polygon, select the X-shaped target that appears next to the polygon after creation.
