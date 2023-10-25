# -*- coding: utf-8 -*-
import cv2
import sys


img1=cv2.imread('Imagenes/Pez.jpg')
if img1 is None: #Si está vacía es que no se ha leíd
    print('Imagen1 no encontrada\n')
    sys.exit(1)
 
img2=cv2.imread('Imagenes/flor.jpg')
if img2 is None: #Si está vacía es que no se ha leído
    print('Imagen2 no encontrada\n')
    sys.exit(1)

if img1 is not None and img2 is not None:
    if img1.shape!=img2.shape:
        print ("Imágenes deben ser del mismo tamaño\n")
        sys.exit(1)
    
    alpha=0.5
    #Realiza la fusión de imágenes
    suma=cv2.addWeighted(img1,alpha,img2,1-alpha,0)
   
    cv2.imshow("Fusion", suma)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
