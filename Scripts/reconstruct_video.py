# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:54:33 2023

@author: R I B
"""

import cv2
import numpy as np
import glob
 
img_array = []
for filename in glob.glob('output_hauteur_bis/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),30, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()