# -*- coding: utf-8 -*-
import cv2
import numpy as np

# Creamos un objeto de video-captura
cap = cv2.VideoCapture(0)

# Leo dos primeras imágenes
ret1, img_ref = cap.read()
ret2, img = cap.read()

# Dimensiones de la imagen capturada por la cámara
[alto, ancho] = img.shape[0:2]

while ret1 and ret2:

    # Conversión a escala de gris de la imagen actual img
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Conversión a escala de gris de la imagen de referencia del frame anterior img_ref
    img_ref_gray = cv2.cvtColor(img_ref, cv2.COLOR_BGR2GRAY)

    # Calcular diferencia de imágenes: img_gray e img_ref_gray
    dif = cv2.absdiff(img_gray, img_ref_gray)

    # Inicializar imagen umbral de diferencia de imágenes (dif_threshold)
    dif_threshold = np.zeros((alto, ancho, 1), np.uint8)

    # Fijar valor umbral para detección de movimiento de manera experimental
    threshold = 30

    # Fijar valor de dif_threshold a blanco cuando se supera el umbral
    dif_threshold[dif > threshold] = 255

    # Obtener las dimensiones de la imagen original
    height, width, _ = img.shape

    # Redimensionar la imagen de detección de movimiento para que tenga la misma altura que la imagen original
    dif_threshold_resized = cv2.resize(dif_threshold, (width, height))

    # Convertir la imagen original a escala de grises
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Generar el mosaico de reproducciones debido a que la imagen original es en color
    cap_mosaic = np.hstack([img_gray, dif_threshold_resized])

    #se muetra la imagen original y la de detección
    cv2.imshow('Original y detección', cap_mosaic)

    # Visualizar la imagen original en una ventana
    cv2.imshow('Img Original', img)

    # Visualizar la imagen de detección de movimiento en otra ventana
    cv2.imshow('Detección de movimiento', dif_threshold)

    # En cada iteración, la imagen anterior se convierte en referencia (clonación de imágenes)
    ref = img_ref.copy()

    # Lectura de imagen actual (img)
    ret2, img = cap.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar objetos
cap.release()
cv2.destroyAllWindows()