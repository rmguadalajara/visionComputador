###############################################
#Detector de bordes mediante algoritmo de Canny
###############################################

import cv2
import sys
import logging
# Configura el nivel de log a INFO
logging.basicConfig(level=logging.INFO)

def on_trackbar_T1(val):
    bordes = cv2.Canny(img,val,200,apertureSize = 3)
    cv2.imshow('Bordes',bordes)
def on_trackbar_T2(val):
    bordes = cv2.Canny(img,50,val,apertureSize = 3)
    cv2.imshow('Bordes',bordes)

img = cv2.imread(sys.argv[1])
if img is None:
    print('Imagen no encontrada')
    sys.exit(0)

bordes = cv2.Canny(img,50,200,apertureSize = 3)



cv2.imshow('Original',img)
cv2.imshow('Bordes',bordes)
img[bordes==255]=(0,255,0)
cv2.imshow('BordesImg',img) 

cv2.createTrackbar("T1", "Bordes", 50, 255, on_trackbar_T1)
cv2.createTrackbar("T2", "Bordes", 50, 255,  on_trackbar_T2)

cv2.waitKey(0)
cv2.destroyAllWindows()