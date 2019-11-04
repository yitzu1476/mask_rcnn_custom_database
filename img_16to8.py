# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:51:23 2019

@author: joyce
"""

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
