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
    img2=copy.copy(img[80:300,120:300])
    cv2.imwrite('imagenes/cara_roi_recorte.jpg',img2)
    cv2.imshow('ROI',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()