
# Labeling images and text documents

After your project administrator creates an [image data labeling project](./how-to-create-image-labeling-projects.md) or [text data labeling project](./how-to-create-text-labeling-projects.md) in Azure Machine Learning, you can use the labeling tool to rapidly prepare data for a Machine Learning project. This article describes:

> [!div class="checklist"]
> * How to access your labeling projects
> * The labeling tools
> * How to use the tools for specific labeling tasks

## Prerequisites

* A [Microsoft account](https://account.microsoft.com/account) or an Azure Active Directory account for the organization and project.
* Contributor level access to the workspace that contains the labeling project.

## Sign in to the studio

1. Sign in to [Azure Machine Learning studio](https://ml.azure.com).

1. Select the subscription and the workspace that contains the labeling project.  Get this information from your project administrator.

1. Depending on your access level, you may see multiple sections on the left.  If so, select **Data labeling** on the left-hand side to find the project.  

## Understand the labeling task

In the table of data labeling projects, select the **Label data** link for your project.

You see instructions that are specific to your project. They explain the type of data that you're facing, how you should make your decisions, and other relevant information. After you read this information, at the top of the page select **Tasks**.  Or at the bottom of the page, select **Start labeling**.

## Selecting a label

In all data labeling tasks, you choose an appropriate tag or tags from a set that's specified by the project administrator. You can select the first nine tags by using the number keys on your keyboard.  

## Assisted machine learning

Machine learning algorithms may be triggered during your labeling. If these algorithms are enabled in your project, you may see the following:

* Images

    * After some amount of data have been labeled, you may see **Tasks clustered** at the top of your screen next to the project name.  This means that images are grouped together to present similar images on the same page.  If so, switch to one of the multiple image views to take advantage of the grouping.  
    
    * At a later point, you may see **Tasks prelabeled** next to the project name.  Items will then appear with a suggested label that comes from a machine learning classification model. No machine learning model has 100% accuracy. While we only use data for which the model is confident, these data might still be incorrectly prelabeled.  When you see labels, correct any wrong labels before submitting the page.  
    
    * For object identification models, you may see bounding boxes and labels already present.  Correct any that are incorrect before submitting the page.
    
    * For segmentation models, you may see polygons and labels already present.  Correct any that are incorrect before submitting the page.

* Text
    
    * At some point, you may see **Tasks prelabeled** next to the project name.  Items will then appear with a suggested label that comes from a machine learning classification model. No machine learning model has 100% accuracy. While we only use data for which the model is confident, these data might still be incorrectly prelabeled.  When you see labels, correct any wrong labels before submitting the page.

Especially early in a labeling project, the machine learning model may only be accurate enough to prelabel a small subset of images. Once these images are labeled, the labeling project will return to manual labeling to gather more data for the next round of model training. Over time, the model will become more confident about a higher proportion of images, resulting in more prelabel tasks later in the project.

When there are no more prelabled tasks, you'll stop confirming or correcting labels and go back to manually tagging the items.

## <a name="image-tasks"></a> Image tasks
