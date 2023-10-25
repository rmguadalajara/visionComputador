# -*- coding: utf-8 -*-
import cv2
import sys

#Imagen Radiografía
mano=cv2.imread("Imagenes/Radiografia.jpeg")
if mano is None: #Si está vacía es que no se ha leído
	print('Imagen no encontrada\n')
	sys.exit(0)

#Patrón corrector de iluminación
ilum=cv2.imread("Imagenes/EscalaGris.png")
if ilum is None: #Si está vacía es que no se ha leído
	print('Imagen no encontrada\n')
	sys.exit(0)


mult=cv2.multiply(...,...,None,...)#Sustituya los puntos por los parámetros adecuados

cv2.imshow("Radiografía", mano)
cv2.imshow("Radiografía Corregida", mult)


cv2.waitKey(0)
cv2.destroyAllWindows()
