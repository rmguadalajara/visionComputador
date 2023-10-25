# -*- coding: utf-8 -*-
import cv2
import sys
import copy


# Leemos la imagen
img=cv2.imread('imagenes/cara.png') 

if img is None: #Si está vacía es que no se ha leído
    print('Imagen no encontrada\n')
    sys.exit(0)
else:
    img[180:220,130:200]=(0,0,255)# Ponemos la ROI1 en color rojo
    img[270:290,180:260]=(0,225,0)# Ponemos la ROI2 en color verde
    cv2.imwrite('imagenes/cara_2roi.jpg',img)
    cv2.imshow('ROI',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()