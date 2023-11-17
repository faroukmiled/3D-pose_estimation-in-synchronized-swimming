from create_centroid_subtracted_matrix import compute_observation_matrix,get_centroids
import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.optimize import root
n_frames=10
N=23 # number of features
def observation_matrix(n_frames=10,N=23):
    with open("data.json") as f:
            data=json.load(f)
    centroids=get_centroids(data,n_frames)
    A=compute_observation_matrix(data,centroids,n_frames,N)
    return(A)
# SVD decomposition
def compute_SVD(A,n_frames=10,N=23,viz=False):
    U,S,VT=np.linalg.svd(A,full_matrices=False)
    s1=np.zeros((3,3))
    s1[0,0]=S[0]
    s1[1,1]=S[1]
    s1[2,2]=S[2]
    U1=U[:,:3]
    V1=VT[:3,:]
    M=np.dot(U1,np.sqrt(s1)) # camera pose estimation motion matrix
    S=np.dot(np.sqrt(s1),V1) # 3D positions with respect to centroid scene structure
    # find Q using Newton's method
    def f(x):
        return([np.dot(np.dot(M[0,:],np.dot(np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]),np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]).T)),M[0,:].T)-1,np.dot(np.dot(M[0,:],np.dot(np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]),np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]).T)),M[n_frames,:].T),np.dot(np.dot(M[n_frames,:],np.dot(np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]),np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]).T)),M[n_frames,:].T)-1,np.dot(np.dot(M[1,:],np.dot(np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]),np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]).T)),M[1,:].T)-1,np.dot(np.dot(M[1,:],np.dot(np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]),np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]).T)),M[1+n_frames,:].T),np.dot(np.dot(M[1+n_frames,:],np.dot(np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]),np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]).T)),M[1+n_frames,:].T)-1,np.dot(np.dot(M[2,:],np.dot(np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]),np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]).T)),M[2,:].T)-1,np.dot(np.dot(M[2,:],np.dot(np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]),np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]).T)),M[2+n_frames,:].T),np.dot(np.dot(M[2+n_frames,:],np.dot(np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]),np.array([[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]).T)),M[2+n_frames,:].T)-1])
    sol=root(f,[1,0,1,1,0,1,1,0,1])
    Q=sol.x.reshape((3,3))
    M=np.dot(M,Q)
    S=np.dot(np.linalg.inv(Q),S)
    if viz :
        # plot 3D points
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        l=[ "Nose" ,  "Neck" ,"Right Shoulder" , "Right Elbow" ,"Right wrist" , "Left Shoulder" , "Left Elbow" ,"Left Wrist" , "Mid Hip" , "Right Hip" , "Right Knee" ,"Right Ankle" ,"Left Hip" ,"Left Knee" ,"Left Ankle" , "Left Eye", "Left Ear" ,"Left Big Toe" ,"Left Small Toe" , "Left Heel" ,"Right Big Toe" , "Right Small Toe" ,"Right Heel"]
        # Plot the points
        for i in range(len(l)):
            ax.scatter(S[0,i],S[1,i],S[2,i])

        # Set the axis labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend(l)
        # Show the plot
        # adjacence 
        plt.show()
    return(M,S)