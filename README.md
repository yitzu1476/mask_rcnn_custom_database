**This tutorial is only suitable for Windows system. (Testing system: Windows 10, 2019 Nov.)** 
# Enviornment Setting

Clone the [Mask RCNN demo files](https://github.com/matterport/Mask_RCNN) first.<br>
Within the files are:
>Mask_RCNN
>>...<br>
>>samples
>>>...<br>
>>>demo.ipynb

Clone my file [training_maskrcnn_custom_database.py](https://github.com/yitzu1476/mask_rcnn_custom_database/blob/master/training_maskrcnn_custom_database.py) to the folder `samples`.

# Data Preparation

1. Create a folder in `samples` for storing data with four folders underneath: `cv2_mask` `json` `labelme_json` `pic`. Here we call name it `imgs_for_training`.<br>
>samples
>>...<br>
>>training_maskrcnn_custom_database.py<br>
>>imgs_for_training
>>>cv2_mask<br>
>>>json<br>
>>>labelme_json<br>
>>>pic

2. Put all your original images for training into folder `pic` with order image names (ex: img_01, img_02 ... etc.)<br>

3. Clone label tool from [here](https://github.com/wkentaro/labelme) and follow the instruction of installion.<br>
After finishing installion, label all your targets in your images which are store in `pic`, and save all the json files in `json`.<br>

4. Convert json files into dataset using labelme_json_to_dataset command.<br>
To convert all the files at a time, clone my [labelme_json_all_in once.py] file to any directory with some changes mention below.<br>
After converting, move all the folders (ex: img_01_json, img_02_json) in `json` to `labelme_json`.
```python
import os
for i in range(23):
# change the range number to the quantity of the files going to be converted.
    num = i + 1
    num_str = str(num)
    if i < 9:
        num_str = '0' + str(num)
    
    file_dir = 'd:/Mask_RCNN/samples/imgs_for_training/json/img_'
    # change file_dir to your own directory with the name of json files without number.
    file_name = file_dir + num_str + '.json'
    command = 'labelme_json_to_dataset ' + file_name
    os.system(command)
```

5. Create mask from png files in labelme_json using my file [img_16to8.py](https://github.com/yitzu1476/mask_rcnn_custom_database/blob/master/img_16to8.py) with some changes mention below.
```python
from PIL import Image
import numpy as np
import os

src_dir = r'd:/Mask_RCNN/samples/imgs_for_training/labelme_json'
dest_dir = r'd:/Mask_RCNN/samples/imgs_for_training/cv2_mask'
# change file_dir to your own directory
k = 0
for child_dir in os.listdir(src_dir):
    k = k + 1
    print(child_dir)
    new_name = child_dir.split('_')[0] + str(k) + '.png'
    old_mask = os.path.join(os.path.join(src_dir, child_dir), 'label.png')
    img = Image.open(old_mask)
    img = Image.fromarray(np.uint8(np.array(img)))
    new_mask = os.path.join(dest_dir, new_name)
    img.save(new_mask)
```

