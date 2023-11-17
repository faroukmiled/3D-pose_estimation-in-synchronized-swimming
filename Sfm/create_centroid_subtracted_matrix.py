import json
import matplotlib.pyplot as plt
import cv2
import numpy as np
n_frames=10
def load_json(json_name="data.json"):
    with open ("data.json") as f:
        data=json.load(f)
    return(data)


# calculate centroid position for each image, store them in a list
def get_centroids(data,n_frames=10,N=23,viz=False):
    centroids=[]
    x=[]
    y=[]
    for a in data.keys():
        for m in range(len(data[a])):
            x.append(list(data[a][m].values())[0][0])
            y.append(list(data[a][m].values())[0][1])
        x_moy,y_moy=sum(x)/N,sum(y)/N
        x,y=[],[]
        centroids.append((int(x_moy),int(y_moy)))
    # visualise coordinates on the images 
    if viz:
        cross_size=3
        for i in range(n_frames):
            x,y=centroids[i]
            img=cv2.imread("./images/img"+str(i)+".jpg")
            cv2.line(img, (x-cross_size, y), (x+cross_size, y), (0, 0, 255), thickness=2)
            cv2.line(img, (x, y-cross_size), (x, y+cross_size), (0, 0, 255), thickness=2)

            # # Display the result
            cv2.imshow('Image with Red Cross', img)
            cv2.imwrite("./img_features/centroid"+str(i)+".jpg",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    return(centroids)


def compute_observation_matrix(data,centroids,n_frames=10,N=23):
    A=np.zeros((2*n_frames,N))
    for i in data.keys():
        f=data[i]
        x,y=centroids[int(i)]
        for j in range(N):
            A[int(i),j]=list(f[j].values())[0][0]-x
            A[int(i)+n_frames,j]=list(f[j].values())[0][1]-y
    return A