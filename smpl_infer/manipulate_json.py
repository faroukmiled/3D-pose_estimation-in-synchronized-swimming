import json
from scipy.io import savemat
import numpy as np
with open("Lebrun_Liang_set1_set_1_point_0_000000000000_keypoints.json","rb") as f:
    data=json.load(f)
n=len(data['people'][0]['pose_keypoints_2d'])
a=np.array(data['people'][0]['pose_keypoints_2d']).reshape(25,3)
mdic={'joints':a}
savemat("matlab_matrix.mat", mdic)
    