# -*- coding: utf-8 -*-
"""
Created on Wed May  3 12:22:14 2023

@author: R I B
"""

from math import *
import pandas as pd
import csv
from PIL import Image, ImageDraw
def distance_euclidienne(x,y,x1,y1):
    return(sqrt((x-x1)**2+(y-y1)**2))
# Charger les données du fichier CSV
csv_file="data_joint.csv"
f=open(csv_file,'r')
df = csv.reader(f, delimiter=',')
joint_hanche=8
#déterminer la hauteur du centre de gravité de la nageuse
count=0 # pour parcourir les lignes du fichier csv
e=0
L=[]
for row in df:
    if count==0:
        count+=1
        # ne pas traiter la première ligne qui contient juste le nom des colonnes
    else:
        if L==[]:
            L.append(int(row[0]))
        elif int(row[0])==L[-1]+1:
            L.append(int(row[0]))
        else:
            if L[-1]+1<int(row[0]):
                print(L[-1]+1)
                break
        count+=1
            