import numpy as np
import cv2
from math import *
n=3
point1real=(0,-75.5,0)
X1,Y1,Z1=point1real
point2real=(0,75.5,0)
X2,Y2,Z2=point2real
point3real=(-93,75.5,0)
X3,Y3,Z3=point3real
point4real=(-67,-75.5,0)
X4,Y4,Z4=point4real
point5real=(-24,56,-76)
X5,Y5,Z5=point5real
point6real=(-24,-56,-76)
X6,Y6,Z6=point6real
normalize_param=1920
point1_frame1_camera1=(1212,546)
u11,v11=point1_frame1_camera1
point2_frame1_camera1=(687,218)
u21,v21=point2_frame1_camera1
point3_frame1_camera1=(483,403)
u31,v31=point3_frame1_camera1
point4_frame1_camera1=(1015,624)
u41,v41=point4_frame1_camera1
point5_frame1_camera1=(773,60)
u51,v51=point5_frame1_camera1
point6_frame1_camera1=(1092,323)
u61,v61=point6_frame1_camera1
point1_frame3_camera3=(292,253)
u13,v13=point1_frame3_camera3
point2_frame3_camera3=(269,182)
u23,v23=point2_frame3_camera3
point3_frame3_camera3=(117,172)
u33,v33=point3_frame3_camera3
point4_frame3_camera3=(102,242)
u43,v43=point4_frame3_camera3
point5_frame3_camera3=(225,317)
u53,v53=point5_frame3_camera3
point6_frame3_camera3=(206,425)
u63,v63=point6_frame3_camera3

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
#******************* read video and extract frame ***************
'''
repertoire_video="estimation_pose_3D/"
cap = cv2.VideoCapture(repertoire_video+'camera'+str(n)+'.avi')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      cv2.imwrite("frame"+str(n)+'.png',frame)
      cv2.waitKey(0)
      if 0xFF == ord('q'):
          break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
'''
# ********************** Calculate extrinsic and intrinsic matrix ***************
# write the matrix A for camera 1
A=[]
for i in range(6):
  A.append([eval('X'+str(i+1)),eval('Y'+str(i+1)),eval('Z'+str(i+1)),1,0,0,0,0,eval('-'+'u'+str(10*(i+1)+1)+'*'+'X'+str(i+1)),eval('-'+'u'+str(10*(i+1)+1)+'*'+'Y'+str(i+1)),eval('-'+'u'+str(10*(i+1)+1)+'*'+'Z'+str(i+1)),eval('-u'+str(10*(i+1)+1))])
  A.append([0,0,0,0,eval('X'+str(i+1)),eval('Y'+str(i+1)),eval('Z'+str(i+1)),1,eval('-'+'v'+str(10*(i+1)+1)+'*'+'X'+str(i+1)),eval('-'+'v'+str(10*(i+1)+1)+'*'+'Y'+str(i+1)),eval('-'+'v'+str(10*(i+1)+1)+'*'+'Z'+str(i+1)),eval('-v'+str(10*(i+1)+1))])
# convert A to matrix
A=np.array(A)
# compute At x A
A_ = np.matmul(A.T, A)
# compute its eigenvectors and eigenvalues
eigenvalues, eigenvectors = np.linalg.eig(A_)
# find the eigenvector with the minimum eigenvalue
# (numpy already returns sorted eigenvectors wrt their eigenvalues)
m = eigenvectors[:,11]
# reshape m back to a matrix
M1 = m.reshape(3,4)
P=M1[:,:3]
p1=M1[:,0]
p2=M1[:,1]
p3=M1[:,2]
p4=M1[:,3]
m3=M1[2,:]
X =  np.linalg.det(np.column_stack((p2 ,p3 ,p4)))
Y = -np.linalg.det(np.column_stack((p1 ,p3 ,p4)))
Z =  np.linalg.det(np.column_stack((p1 ,p2 ,p4)))
T = - np.linalg.det(np.column_stack((p1 ,p2 ,p3)))
Pc = np.array([X,Y,Z,T])  
Pc = Pc/Pc[-1] 
Pc = Pc[:3]
print(sqrt(Pc[0]**2+Pc[1]**2+Pc[2]**2))
pp = np.dot(M1,m3);
pp = pp/pp[2]; 
pp = pp[:2];
cx1,cy1=pp
Q,R=np.linalg.qr(M1[:3,:3])
for n in range(0,3):
      if R[n,n] < 0:
          R[:,n] = -R[:,n];
          Q[n,:] = -Q[n,:];
# compute the matrix A for camera 3
print(Q)
print(R)
A=[]
for i in range(6):
  A.append([eval('X'+str(i+1)),eval('Y'+str(i+1)),eval('Z'+str(i+1)),1,0,0,0,0,eval('-'+'u'+str(10*(i+1)+3)+'*'+'X'+str(i+1)),eval('-'+'u'+str(10*(i+1)+3)+'*'+'Y'+str(i+1)),eval('-'+'u'+str(10*(i+1)+3)+'*'+'Z'+str(i+1)),eval('-u'+str(10*(i+1)+3))])
  A.append([0,0,0,0,eval('X'+str(i+1)),eval('Y'+str(i+1)),eval('Z'+str(i+1)),1,eval('-'+'v'+str(10*(i+1)+3)+'*'+'X'+str(i+1)),eval('-'+'v'+str(10*(i+1)+3)+'*'+'Y'+str(i+1)),eval('-'+'v'+str(10*(i+1)+3)+'*'+'Z'+str(i+1)),eval('-v'+str(10*(i+1)+3))])
# convert A to matrix
A=np.array(A)
# compute At x A
A_ = np.matmul(A.T, A)
# compute its eigenvectors and eigenvalues
eigenvalues, eigenvectors = np.linalg.eig(A_)
# find the eigenvector with the minimum eigenvalue
# (numpy already returns sorted eigenvectors wrt their eigenvalues)
m = eigenvectors[:,11]
# reshape m back to a matrix
M2 = m.reshape(3,4)
P=M2[:,:3]
p1=M2[:,0]
p2=M2[:,1]
p3=M2[:,2]
p4=M2[:,3]
m3=M2[2,:]
X =  np.linalg.det(np.column_stack((p2 ,p3 ,p4)))
Y = -np.linalg.det(np.column_stack((p1 ,p3 ,p4)))
Z =  np.linalg.det(np.column_stack((p1 ,p2 ,p4)))
T = - np.linalg.det(np.column_stack((p1 ,p2 ,p3)))
Pc = np.array([X,Y,Z,T])  
Pc = Pc/Pc[-1] 
Pc = Pc[:3]
print(sqrt(Pc[0]**2+Pc[1]**2+Pc[2]**2))
pp = np.dot(M2,m3);
pp = pp/pp[2]; 
pp = pp[:2];  
cx2,cy2=pp
Q,R=np.linalg.qr(M2[:3,:3])
for n in range(0,3):
      if R[n,n] < 0:
          R[:,n] = -R[:,n];
          Q[n,:] = -Q[n,:];
# compute the reverse operation for a given pixel
# pixel coordinates with camera 1
'''
u1 = 1212
v1 = 546
# pixel coordinates to normalized image coordinates
x_norm1 = np.dot(np.linalg.pinv(M1), np.array([u1, v1, 1]))

# ray in camera coordinate system
ray1 = np.array([x_norm1[0], x_norm1[1],x_norm1[2], 1])
# pixel coordinates with camera 3
# pixel coordinates with camera 1
u2 = 292
v2 = 253
# pixel coordinates to normalized image coordinates
x_norm2 = np.dot(np.linalg.pinv(M2), np.array([u2, v2, 1]))

# ray in camera coordinate system
ray2 = np.array([x_norm2[0], x_norm2[1],x_norm2[2], 1])
# homogenous to euclidian
norm1=ray1[2]
norm2=ray2[2]
ray1=ray1[:3]/norm1
ray2=ray2[:3]/norm2
# compute the intersection point of the rays
A = np.vstack((ray1, -ray2)).T
b = tx * ray2[:3]
x = np.linalg.lstsq(A, b, rcond=None)[0]
intersection_point = np.append(x, [1])
'''