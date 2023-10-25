# -*- coding: utf-8 -*-
import cv2
import sys
import copy

img=cv2.imread('imagenes/Minion.jpg') # Leemos la imagen

if img is None: #Si está vacía es que no se ha leído
    print('Imagen no encontrada\n')
    sys.exit(0)
else:
    #img2=img
    img2=copy.copy(img)
    img2[105:245,170:293]=(0,255,0)
    cv2.imwrite("imagenes/Copia.png",img)
    cv2.imwrite("imagenes/Modificada.png",img2)