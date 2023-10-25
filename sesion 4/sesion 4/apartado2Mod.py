# coding: utf-8
import cv2
import numpy as np


def on_trackbar(val):
    global img, r, g, b, s, switch
    s = cv2.getTrackbarPos(switch, "Imagen")
    if s == 0:
        img[:] = 0
    else:
        img[:, :, 0] = b
        img[:, :, 1] = g
        img[:, :, 2] = r
    cv2.imshow("Imagen", img)


# Crear una imagen de fondo negro y una ventana
img = np.zeros((480, 640, 3), np.uint8)
cv2.namedWindow("Imagen")

# Creamos las barras para cada color
cv2.createTrackbar("R", "Imagen", 50, 255, on_trackbar)
cv2.createTrackbar("G", "Imagen", 100, 255, on_trackbar)
cv2.createTrackbar("B", "Imagen", 150, 255, on_trackbar)

# Creamos un botón interruptor ON/OFF
switch = "0 : OFF \n1 : ON"
cv2.createTrackbar(switch, "Imagen", 1, 1, on_trackbar)

# Leemos las posiciones iniciales de los 4 trackbars
r = cv2.getTrackbarPos("R", "Imagen")
g = cv2.getTrackbarPos("G", "Imagen")
b = cv2.getTrackbarPos("B", "Imagen")
s = cv2.getTrackbarPos(switch, "Imagen")

# Mostramos la imagen inicial
on_trackbar(0)

while 1:
    k = cv2.waitKey(1) & 0xFF  # Miramos la tecla pulsada. Si es Esc nos salimos
    if k == 27:
        break

cv2.destroyAllWindows()
