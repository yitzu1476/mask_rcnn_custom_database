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
To convert all the files at a time, clone my [labelme_json_all_in_once.py](https://github.com/yitzu1476/mask_rcnn_custom_database/blob/master/labelme_json_all_in_once.py) file to any directory with some changes mention below.<br>
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

5. Create mask from png files in labelme_json using my file [img_16to8.py](https://github.com/yitzu1476/mask_rcnn_custom_database/blob/master/img_16to8.py) with some changes mention below, and the result files will be saved in `cv2_mask`.
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

# Training Process

Several command lines in [training_maskrcnn_custom_database.py](https://github.com/yitzu1476/mask_rcnn_custom_database/blob/master/training_maskrcnn_custom_database.py) must be changed  before training, which are marked below.
```python
class ShapesConfig(Config):
    NAME = "shapes"
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

    # Number of classes (including background)
    NUM_CLASSES = 1 + 1  # background + 1 shapes, shapes number depends on the number of target / object

    IMAGE_MIN_DIM = 320
    IMAGE_MAX_DIM = 384
```
```python
def load_shapes(self, count, img_floder, mask_floder, imglist, dataset_root_path):
    # Add classes
    self.add_class("shapes", 1, "rov")
    # self.add_class("shapes", 2, "new_object_name")
    # self.add_class("shapes", 3, "another_new_object_name")
```
```python
def load_mask(self, image_id):
    global iter_num
    print("image_id",image_id)
    info = self.image_info[image_id]
    count = 1  # number of object
    img = Image.open(info['mask_path'])
    num_obj = self.get_obj_index(img)
    mask = np.zeros([info['height'], info['width'], num_obj], dtype=np.uint8)
    mask = self.draw_mask(num_obj, mask, img,image_id)
    occlusion = np.logical_not(mask[:, :, -1]).astype(np.uint8)
    for i in range(count - 2, -1, -1):
        mask[:, :, i] = mask[:, :, i] * occlusion
        occlusion = np.logical_and(occlusion, np.logical_not(mask[:, :, i]))
    labels = []
    labels = self.from_yaml_get_class(image_id)
    labels_form = []
    for i in range(len(labels)):
        if labels[i].find("rov") != -1:
            labels_form.append("rov")
            # labels_form.append("new_object_name")
            # labels_form.append("another_new_object_name")
```
```python
dataset_root_path="imgs_for_training/" # where your training pics are 
img_floder = dataset_root_path + "pic"
mask_floder = dataset_root_path + "cv2_mask"
imglist = os.listdir(img_floder)
count = len(imglist)
print('img_floder ,',img_floder)
```

# Model Testing
After the training, the model is ready to detect your target in the images with 


