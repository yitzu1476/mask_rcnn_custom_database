# Enviornment Setting

Clone the [Mask RCNN demo files](https://github.com/matterport/Mask_RCNN) first.<br>
Within the files are:
>Mask_RCNN
>>assets<br>
>>build<br>
>>...<br>
>>samples
>>>balloon<br>
>>>coco<br>
>>>...<br>
>>>demo.ipynb<br>
>>>...

Clone my file [training_maskrcnn_custom_database.py](https://github.com/yitzu1476/mask_rcnn_custom_database/blob/master/training_maskrcnn_custom_database.py) to the folder `samples`.

# Data Preparation

1. Create a folder in `samples` for storing data with four folders underneath: `cv2_mask` `json` `labelme_json` `pic`. Here we call name it `imgs_for_training`.<br>
>samples
>>balloon<br>
>>coco<br>
>>...<br>
>>training_maskrcnn_custom_database.py<br>
>>imgs_for_training
>>>cv2_mask<br>
>>>json<br>
>>>labelme_json<br>
>>>pic
