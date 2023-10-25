###############################################
#Detector de bordes mediante algoritmo de Canny
###############################################

import cv2
import sys

img = cv2.imread(sys.argv[1])
if img is None:
    print('Imagen no encontrada')
    sys.exit(0)

bordes = cv2.Canny(img,50,200,apertureSize = 3)

cv2.imshow('Original',img)
cv2.imshow('Bordes',bordes)
img[bordes==255]=(0,255,0)
cv2.imshow('BordesImg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()