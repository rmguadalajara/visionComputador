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

# Function to handle trackbar events
def on_trackbar(r,g,b):
    global img

    img[:] = [b,g,r]
    cv2.imshow("Imagen", img)

# Function to handle trackbar switch
def on_trackbar_switch(val):
    global img

    img[:] = val

    cv2.imshow("Imagen", img)

# Crear una imagen de fondo negro y una ventana
cv2.namedWindow("Imagen")

# Creamos las barras para cada color
def update_image(x):
    if cv2.getTrackbarPos("R", "Imagen") is not None:
        r = cv2.getTrackbarPos("R", "Imagen")
    if cv2.getTrackbarPos("G", "Imagen") is not None:
        g = cv2.getTrackbarPos("G", "Imagen")
    if cv2.getTrackbarPos("B", "Imagen") is not None:
        b = cv2.getTrackbarPos("B", "Imagen")
    on_trackbar(r, g, b)

#Declaracion de trackbars
cv2.createTrackbar("R", "Imagen", 50, 255, update_image)
cv2.createTrackbar("G", "Imagen", 100, 255, update_image)
cv2.createTrackbar("B", "Imagen", 150, 255, update_image)

# Creamos un botón interruptor ON/OFF
cv2.createTrackbar(switch, "Imagen", 1, 1, lambda x: on_trackbar_switch(cv2.getTrackbarPos(switch, "Imagen")))

# Mostramos la imagen inicial
on_trackbar_switch(0)

while 1:
    # Miramos la tecla pulsada. Si es Esc nos salimos
    k = cv2.waitKey(1) & 0xFF  
    if k == 27:
        break

cv2.destroyAllWindows()
