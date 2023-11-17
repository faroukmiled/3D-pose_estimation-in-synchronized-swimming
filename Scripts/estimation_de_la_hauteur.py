# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:56:29 2023

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
m,a,b,c,d=0,0,0,0,0
for row in df:
    if count==0:
        count+=1
        # ne pas traiter la première ligne qui contient juste le nom des colonnes
    else:
        if int(row[0])==e:
           
            if int(row[1])==0 and int(row[2])==joint_hanche:
                a,b=float(row[3]),float(row[4])
            elif int(row[1])==0 and int(row[2]) not in [0,1,2,3,4,5,6,7,8,9,12,15,16,17,18]:
                L.append([float(row[3]),float(row[4])])
               
                    
                
        else:
            try:
                m=L[0][1]
                k=0
                for i in range(1,len(L)):
                    if m>L[i][1]:
                        m=L[i][1]
                        k=i
                c,d=L[k][0],L[k][1]
                # Chargement de l'image
                im = Image.open("split/frame"+str(e)+'.jpg')
    
                # Définition des points de départ et d'arrivée de la ligne
                point1 = (a,b)
                point2 = (c,d)
    
                # Création d'un objet ImageDraw pour dessiner sur l'image
                draw = ImageDraw.Draw(im)
    
                # Tracé de la ligne entre les deux points
                draw.line([point1, point2], fill="red", width=6)
    
                # Enregistrement de l'image modifiée
                im.save("output_hauteur/frame"+str(e)+"_height_estimate.jpg")
                e=int(row[0])
                L=[]
            except:
                e=int(row[0])+1
        count+=1
        
