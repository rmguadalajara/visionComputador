# -*- coding: utf-8 -*-
import cv2
import sys
import copy


# Leemos la imagen
imgCara=cv2.imread('imagenes/cara.png') 
imgSol=cv2.imread('imagenes/sol.jpg') 

#Si está vacía es que no se ha leído
if imgCara is None or imgSol is None: 
    print('Imagen no encontrada\n')
    sys.exit(0)
else:
    imgCaraRecorte=copy.copy(imgCara[80:300,120:300])
    
    #280 290
    # nuevo size
    dsize = (290, 280)
    
    # resize image
    imageResized = cv2.resize(imgCaraRecorte, dsize)
    
    print('image resized size')
    print(imageResized.shape)
    
    imgSol[190:470,480:770]=copy.copy(imageResized)
    print(imgSol[190:470,480:770].shape)
    
    
    cv2.imwrite('imagenes/sol_modificado.jpg',imgSol)
    cv2.imshow('ROI',imgSol)
    cv2.waitKey(0)
    cv2.destroyAllWindows()