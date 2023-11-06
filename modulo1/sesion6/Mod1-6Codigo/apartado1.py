# -*- coding: utf-8 -*-
import sys
import cv2

# Lectura Imagen 1
img1 = cv2.imread('Imagenes/Pez.jpg')
if img1 is None:  # Si está vacía es que no se ha leído
    print('Imagen no encontrada\n')
    sys.exit(0)

# Lectura Imagen 2
img2 = cv2.imread('Imagenes/Flor.jpg')
if img2 is None:  # Si está vacía es que no se ha leído
    print('Imagen no encontrada\n')
    sys.exit(0)

# Conversión de imágenes a escala de gris
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Suma numpy y suma OpenCV
suma1 = gray1+gray2  # Suma numpy
suma2 = cv2.add(gray1, gray2)  # Suma OpenCV

# La suma con numpy se hace elemento a elemento, mientras que la suma con OpenCV se hace con la función cv2.add(),
# que hace una suma saturada. Esto significa que si el resultado de la suma es mayor que 255 , el resultado se establece en 255. Por lo tanto, la suma 
# con OpenCV puede dar resultados diferentes a la suma con numpy si los valores de los píxeles en las imágenes son grandes.

cv2.imshow("Suma Numpy", suma1)
cv2.imshow("Suma OpenCV", suma2)

cv2.waitKey(0)
cv2.destroyAllWindows()
