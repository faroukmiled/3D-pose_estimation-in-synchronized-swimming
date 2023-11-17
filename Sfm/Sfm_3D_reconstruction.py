from Compute_SVD import compute_SVD,observation_matrix
import matplotlib.pyplot as plt
import cv2,json
from math import *
def euclidien_distance(x,y,z,echelle):
    x1,x2=x[0],x[1]
    y1,y2=y[0],y[1]
    z1,z2=z[0],z[1]
    return(sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)*echelle)

# we will compute scene points with respect to their centroids
l=[ "Nose" ,  "Neck" ,"Right Shoulder" , "Right Elbow" ,"Right wrist" , "Left Shoulder" , "Left Elbow" ,"Left Wrist" , "Mid Hip" , "Right Hip" , "Right Knee" ,"Right Ankle" ,"Left Hip" ,"Left Knee" ,"Left Ankle" , "Left Eye", "Left Ear" ,"Left Big Toe" ,"Left Small Toe" , "Left Heel" ,"Right Big Toe" , "Right Small Toe" ,"Right Heel"]
adjacency_list=[{0:[18,16,1]},{1:[2,5,8]},{2:[3]},{3:[4]},{5:[6]},{6:[7]},{8:[9,12]},{9:[10]},{10:[11]},{11:[22,23,24]},{12:[13]},{13:[14]},{14:[19,20,21]}]
A=observation_matrix()
M,S=compute_SVD(A)
distance_right_left_soulder=40 # cm
# distance in the 3D plot
dis=sqrt((S[0,2]-S[0,5])**2+(S[1,2]-S[1,5])**2+(S[2,2]-S[2,5])**2)
print(dis)
echelle=distance_right_left_soulder/dis
distance_list=[]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax1 = fig.add_subplot(121)
#img=cv2.imread("./img_features/features_img+centroid0.jpg")
#ax1.imshow(img,cmap="gray")
d1={}
for d in adjacency_list:
    a=list(d.keys())[0]
    d1[a]=[]
    neighbours=list(d.values())[0]
    for joint in neighbours:
        if joint==16:
            x=[S[0,a],S[0,joint-1]]
            y=[S[1,a],S[1,joint-1]]
            z=[S[2,a],S[2,joint-1]]
        elif joint>=18:
            x=[S[0,a],S[0,joint-2]]
            y=[S[1,a],S[1,joint-2]]
            z=[S[2,a],S[2,joint-2]]
        else:
            x=[S[0,a],S[0,joint]]
            y=[S[1,a],S[1,joint]]
            z=[S[2,a],S[2,joint]]
        d1[a].append([joint,round(euclidien_distance(x,y,z,echelle),2)])


        ax.plot(x,y,z,label=str(round(euclidien_distance(x,y,z,echelle),2)))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Scatter Plot with Edges')
ax.legend()
with open("real_distances.json","w") as f:
    json.dump(d1,f)
# Show the plot
plt.show()