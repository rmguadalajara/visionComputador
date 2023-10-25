# -*- coding: utf-8 -*-
import cv2
import sys

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'Alternativas para redimensionar una imagen con la función cv2.resize
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
img=cv2.imread("Imagenes/Lenna.png")
if img is None: #Si está vacía es que no se ha leído
	print('Imagen no encontrada\n')
	sys.exit(0)

#Opción 1: mediante factor de escala
res = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)

cv2.imshow("Resultado1",res)
cv2.waitKey(0)

#Opción 2: 
height, width = img.shape[:2]

res = cv2.resize(img,(int(width/2), int(height/2)), interpolation = cv2.INTER_LANCZOS4)

cv2.imshow("Resultado2",res)
cv2.waitKey(0)

#Opción 3: dimensiones específicas (cuidado con la relación de aspecto)
res = cv2.resize(img,(640, 480), interpolation = cv2.INTER_AREA)

cv2.imshow("Resultado3",res)
cv2.waitKey(0)

cv2.destroyAllWindows()
