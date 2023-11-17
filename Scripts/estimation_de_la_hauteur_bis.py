# -*- coding: utf-8 -*-
"""
Created on Wed May  3 09:55:01 2023

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

L=[]
e=254
for row in df:
    if count<=16625:
        count+=1
        # ne pas traiter la première ligne qui contient juste le nom des colonnes
    else:
        if int(row[0])==e:
               L.append([int(row[2]),float(row[3]),float(row[4])])
        else:
            if int(row[0])>=240:
                    im = Image.open("split/frame"+str(e)+'.jpg')
                    # Définition des points de départ et d'arrivée de la ligne
                    a,b=0,1080
                    c,d=0,0
                    
                    liste1=[11,14,19,20,21,22,23,24]
                    for j in range(len(liste1)):
                        for k in range(len(L)):
                            if L[k][0]==liste1[j] and b>L[k][2]:
                                b=L[k][2]
                                a=L[k][1]
                    liste2=[1,2,3,4,5,6,7,8,9,10,12,13,15,16,17,18]
                    for j in range(len(liste2)):
                        for k in range(len(L)):
                            if L[k][0]==liste2[j] and d<=L[k][2]:
                                c=L[k][1]
                                d=L[k][2]
                    if b<d and a!=0 and b!=0 :# figure and 
                        point1 = (a,b)
                        point2 = ((2/3)*1920,(2/3)*1080)
                    
        
                        # Création d'un objet ImageDraw pour dessiner sur l'image
                        draw = ImageDraw.Draw(im)
        
                        # Tracé de la ligne entre les deux points
                        draw.line([point1, point2], fill="red", width=6)
        
                        # Enregistrement de l'image modifiée
                        im.save("output_hauteur/frame"+str(e)+"_height_estimate.jpg")
                    L=[]
                    e=int(row[0])
        count+=1
        
                    