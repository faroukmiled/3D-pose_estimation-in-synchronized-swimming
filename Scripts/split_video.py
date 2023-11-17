# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 16:32:24 2023

@author: R I B
"""
import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('ouput-openpose-small.mp4')

try:
    if not os.path.exists('split'):
        os.makedirs('split')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './split/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()