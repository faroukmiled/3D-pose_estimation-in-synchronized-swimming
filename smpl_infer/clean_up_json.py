import json
from scipy.io import savemat
import numpy as np
with open("synchro.json","rb") as f:
    data=json.load(f)
l=data['people'][0]['pose_keypoints_2d']
# organise json to be compatible with smpl
l1=[]
l2=[10,9,8,11,13,4,3,2,5,6,7,1]
for i in l2:
    l1.append(l[3*i])
    l1.append(l[3*i+1])
    l1.append(l[3*i+2])
for _ in range(6):
    l1.append(-1)
a=np.array(l1).reshape(14,3)
b=np.ones((10,14,3))
b[0,:,:]=a
mdic={'est_joints':b}
savemat("joints.mat", mdic)


