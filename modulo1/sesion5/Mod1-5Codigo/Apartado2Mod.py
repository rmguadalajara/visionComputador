import cv2
import numpy as np
import sys

cap = cv2.VideoCapture('movil.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

umbral = sys.argv[1] # umbral recibido como argumento

#umbral fijo
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, int(umbral), 255, cv2.THRESH_BINARY)
        out.write(thresh)
        cv2.imshow('frame umbral fijo', thresh)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

#a técnica de Otsu2 para calcular el umbral óptimo para cada fotograma.
cap = cv2.VideoCapture('movil.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while(cap.isOpened()):
    ret2, frame = cap.read()
    if ret2 == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret2, thresh2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        out.write(thresh2)
        cv2.imshow('frame umbral otsu', thresh2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
out.release()
