# -*- coding: utf-8 -*-
"""
Created on Tue May  2 13:53:46 2023

@author: R I B
"""

from math import *
import pandas as pd
from PIL import Image
import csv

def distance_euclidienne(x,y,x1,y1):
    return(sqrt((x-x1)**2+(y-y1)**2))
# Charger les données du fichier CSV
csv_file="data_joint.csv"
f=open(csv_file,'r')
df = csv.reader(f, delimiter=',')
joint_a_verifier=24
#déterminer la hauteur du centre de gravité de la nageuse
count=0 # pour parcourir les lignes du fichier csv
for row in df:
    if count==0:
        count+=1
        # ne pas traiter la première ligne qui contient juste le nom des colonnes
    else:
        if int(row[1])==0 and int(row[2])==joint_a_verifier:
            # on s'intéresse au centre de gavité de la nageuse, le joint 8 correspond à la hanche de la nageuse
            box=(float(row[3])-64,float(row[4])-64,float(row[3])+64,float(row[4])+64)
            img = Image.open('split/frame'+row[0]+'.jpg')
            img2=img.crop(box)
            img2.show()
            
            break
        