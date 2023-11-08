# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt
'''Ejemplo de normalización del histograma'''

img=cv2.imread("Imagenes/Oscura.tif",cv2.IMREAD_GRAYSCALE)
if img is None: #Si está vacía es que no se ha leído
	print('Imagen no encontrada\n')
	sys.exit(0)

#Obtenemos y mostramos el histograma original
hist,bins = np.histogram(img.flatten(),256,[0,256])
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.show()


min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img)

img2=(img-min_val)/(max_val-min_val)*255.0 #Normalización de la imagen

#Obtenemos y mostramos el histograma normalizado
hist,bins = np.histogram(img2.flatten(),256,[0,256])
plt.hist(img2.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.show()

# Ecualizamos el histograma
img3 = cv2.equalizeHist(img)

# Mostramos la imagen ecualizada
#cv2.imshow("Ecualizada", img3)

# Obtenemos y mostramos el histograma ecualizado
histeq,bins = np.histogram(img3.flatten(),256,[0,256])
plt.hist(img3.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.show()


#Mostramos la dos imágenes juntas
res = np.hstack((img,np.uint8(img2),img3))

cv2.imshow("Corregida y Ecualizada",res)

cv2.waitKey(0)
cv2.destroyAllWindows()

      
