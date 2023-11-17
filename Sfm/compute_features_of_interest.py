# This code aims to implement interesting point eatures from openpose results
# Let's take first 10 frames, use the csv file to have for each point the pose estimation
# load csv file
import csv,json
import matplotlib.pyplot as plt
import numpy as np
import cv2
n_frames=10
csv_file="2022-CFJe-hiver-solo-qualif-duhaudt-openpose.csv"
def extract_features(csv_file="2022-CFJe-hiver-solo-qualif-duhaudt-openpose.csv",n_frames=10):
    d={}
    f=open(csv_file,'r')
    df = csv.reader(f, delimiter=',')
    # extract features, save them to features (24 points) and show them in the 10 frames.
    counter=0
    L=[]
    l1=[0]
    l2=[]
    for row in df:
        if counter==0:
            # don't treat the first row ( text)
            counter+=1 
        else:
            if l1[-1]!=int(row[0]):
                d[l1[-1]]=L
                L=[]
                l1.append(int(row[0]))
            if int(row[0])==n_frames:
                    break
            if int(row[0])<n_frames and int(row[6])==1:
                if int(float(row[3]))==0 and int(float(row[4]))==0:
                    l2.append(int(row[2]))
                # search for features in the first ten frames
                L.append({int(row[2]):[int(float(row[3])),int(float(row[4]))]})
    d1={}
    for a in d.keys():
        d1[a]=[]
        for m in range(len(d[a])):
            if l2.count(list(d[a][m].keys())[0])==0:
                d1[a].append(d[a][m])
    return(d1)
# visualize features on the image
def visualize_and_save_features(dict,n_frames=10,cross_size=3):
    for i in range(n_frames):
        img=cv2.imread("./images/img"+str(i)+".jpg")
        for m in range(len(dict[i])):
            x,y=list(dict[i][m].values())[0][0],list(dict[i][m].values())[0][1]
            cv2.line(img, (x-cross_size, y), (x+cross_size, y), (0, 0, 255), thickness=2)
            cv2.line(img, (x, y-cross_size), (x, y+cross_size), (0, 0, 255), thickness=2)

        # Display the result
        cv2.imshow('Image with features', img)
        cv2.imwrite("./img_features/features_img"+str(i)+".jpg",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def save_json(dict):
    with open('data.json', 'w') as f:
        # Convert the dictionary to a JSON string and write it to the file
        json.dump(dict, f)

