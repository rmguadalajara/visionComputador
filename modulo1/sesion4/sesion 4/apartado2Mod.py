# coding: utf-8
import cv2
import numpy as np

# Initialize global variables
img = np.zeros((480, 640, 3), np.uint8)
r = 50
g = 100
b = 150
s = 1
switch = "0 : OFF \n1 : ON"

def on_trackbar(r,g,b):
    global img

    img[:] = [b,g,r]
    cv2.imshow("Imagen", img)
    
def on_trackbar_switch(val):
    global img

    img[:] = val

    cv2.imshow("Imagen", img)

# Crear una imagen de fondo negro y una ventana
cv2.namedWindow("Imagen")

# Creamos las barras para cada color
cv2.createTrackbar("R", "Imagen", 50, 255, lambda x: on_trackbar(cv2.getTrackbarPos("R", "Imagen"),cv2.getTrackbarPos("G", "Imagen"),cv2.getTrackbarPos("B", "Imagen")))
cv2.createTrackbar("G", "Imagen", 100, 255, lambda x: on_trackbar(cv2.getTrackbarPos("R", "Imagen"),cv2.getTrackbarPos("G", "Imagen"),cv2.getTrackbarPos("B", "Imagen")))
cv2.createTrackbar("B", "Imagen", 150, 255, lambda x: on_trackbar(cv2.getTrackbarPos("R", "Imagen"),cv2.getTrackbarPos("G", "Imagen"),cv2.getTrackbarPos("B", "Imagen")))

# Creamos un botón interruptor ON/OFF
cv2.createTrackbar(switch, "Imagen", 1, 1, lambda x: on_trackbar_switch(cv2.getTrackbarPos(switch, "Imagen")))



# Mostramos la imagen inicial
on_trackbar_switch(0)

while 1:
    k = cv2.waitKey(1) & 0xFF  # Miramos la tecla pulsada. Si es Esc nos salimos
    if k == 27:
        break

cv2.destroyAllWindows()
