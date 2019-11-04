# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:42:53 2019

@author: joyce
"""

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