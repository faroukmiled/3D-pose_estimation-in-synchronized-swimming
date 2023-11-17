import csv,json
csv_file="2022-CFJe-hiver-solo-qualif-duhaudt-openpose.csv"
f=open(csv_file,'r')
df = csv.reader(f, delimiter=',')
d={}
d["people"]=[]
d1={}
d1["pose_keypoints_2d"]=[]
count=0
for row in df:
    if count==0:
        count+=1
    else:
        if int(row[0])!=0:
            break
        else:
            d1["pose_keypoints_2d"].append(float(row[3]))
            d1["pose_keypoints_2d"].append(float(row[4]))
            d1["pose_keypoints_2d"].append(1)

d["people"].append(d1)
with open('synchro.json', 'w') as f:
    # Convert the dictionary to a JSON string and write it to the file
    json.dump(d, f)

