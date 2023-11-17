import json
from scipy.io import savemat
import numpy as np
from PIL import Image
with open("Lebrun_Liang_set1_set_1_point_0_000000000000_keypoints.json","rb") as f:
    data=json.load(f)
l=data['people'][0]['pose_keypoints_2d']
x,y=l[39],l[40]
picture = Image.open("0.jpg")
im=picture.crop((int(x)-40,int(y)-40,int(x)+40,int(y)+40))
im.save("test.jpg")