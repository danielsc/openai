When there are no more prelabled tasks, you'll stop confirming or correcting labels and go back to manually tagging the items.

## <a name="image-tasks"></a> Image tasks

For image-classification tasks, you can choose to view multiple images simultaneously. Use the icons above the image area to select the layout.

To select all the displayed images simultaneously, use **Select all**. To select individual images, use the circular selection button in the upper-right corner of the image. You must select at least one image to apply a tag. If you select multiple images, any tag that you select will be applied to all the selected images.

Here we've chosen a two-by-two layout and are about to apply the tag "Mammal" to the images of the bear and orca. The image of the shark was already tagged as "Cartilaginous fish," and the iguana hasn't been tagged yet.

![Multiple image layouts and selection](./media/how-to-label-data/layouts.png)

> [!Important]
> Only switch layouts when you have a fresh page of unlabeled data. Switching layouts clears the page's in-progress tagging work.

Azure enables the **Submit** button when you've tagged all the images on the page. Select **Submit** to save your work.

After you submit tags for the data at hand, Azure refreshes the page with a new set of images from the work queue.

## Medical image tasks

> [!IMPORTANT]
> The capability to label DICOM or similar image types is not intended or made available for use as a medical device, clinical support, diagnostic tool, or other technology intended to be used in the diagnosis, cure, mitigation, treatment, or prevention of disease or other conditions, and no license or right is granted by Microsoft to use this capability for such purposes. This capability is not designed or intended to be implemented or deployed as a substitute for professional medical advice or healthcare opinion, diagnosis, treatment, or the clinical judgment of a healthcare professional, and should not be used as such. The customer is solely responsible for any use of Data Labeling for DICOM or similar image types.

Image projects support DICOM image format for X-ray file images.

:::image type="content" source="media/how-to-label-data/x-ray-image.png" alt-text="X-ray DICOM image to be labeled.":::

While you label the medical images with the same tools as any other images, there is an additional tool for DICOM images.  Select the **Window and level** tool to change the intensity of the image. This tool is available only for DICOM images.

:::image type="content" source="media/how-to-label-data/window-level-tool.png" alt-text="Window and level tool for DICOM images.":::

## Tag images for multi-class classification

If your project is of type "Image Classification Multi-Class," you'll assign a single tag to the entire image. To review the directions at any time, go to the **Instructions** page and select **View detailed instructions**.

If you realize that you made a mistake after you assign a tag to an image, you can fix it. Select the "**X**" on the label that's displayed below the image to clear the tag. Or, select the image and choose another class. The newly selected value will replace the previously applied tag.

## Tag images for multi-label classification

If you're working on a project of type "Image Classification Multi-Label," you'll apply one *or more* tags to an image. To see the project-specific directions, select **Instructions** and go to **View detailed instructions**.

Select the image that you want to label and then select the tag. The tag is applied to all the selected images, and then the images are deselected. To apply more tags, you must reselect the images. The following animation shows multi-label tagging:

1. **Select all** is used to apply the "Ocean" tag.
1. A single image is selected and tagged "Closeup."
1. Three images are selected and tagged "Wide angle."

![Animation shows multilabel flow](./media/how-to-label-data/multilabel.gif)

To correct a mistake, select the "**X**" to clear an individual tag or select the images and then select the tag, which clears the tag from all the selected images. This scenario is shown here. Selecting "Land" will clear that tag from the two selected images.
