# -*- coding: utf-8 -*-
import cv2
import sys
import copy

# Leemos la imagen
img=cv2.imread('imagenes/Minion.jpg') 

#Si está vacía es que no se ha leído
if img is None: 
    print('Imagen no encontrada\n')
    sys.exit(0)
else:
    #Realiazmos una copia de la imagen
    img2=copy.copy(img)
    #Pintamos un rectángulo verde en la imagen
    img2[105:245,170:293]=(0,255,0)
    #Guardamos la imagen original y la modificada
    cv2.imwrite("imagenes/Copia.png",img)
    cv2.imwrite("imagenes/Modificada.png",img2)