# -*- coding: utf-8 -*-
import cv2
import numpy as np

#Creamos un objeto de la clase video-captura
cap = cv2.VideoCapture(0)

#Obtenemos la tasa de fps del objeto
fps = cap.get(cv2.CAP_PROP_FPS)
#Variable time en ms
time=int(1000/fps) 
print("Nº de frames por segundo: ",fps)

#Líneas a añadir para determinar anchura y altura
width=cap.get(3)
height=cap.get(4)
print('Dimensiones de la imagen: %d x %d',(width,height))

#Captura el primer frame
ret, frame = cap.read()

#Definimos el tipo de fuente para escribir texto en vídeo
font = cv2.FONT_HERSHEY_SIMPLEX
  
# posicion original
org = (50, 50)
  
# tamaño fuente
fontScale = 1
   
# seteamos el color a verde
color = (0, 255, 0)
  
# anchura en pixeles
thickness = 2
   
# leemos el logo y lo redimensionamos
logo = cv2.imread('images/Logo_UAH.jpg')
size = 100
logo = cv2.resize(logo, (size, size))

#Comprueba si se ha inicializado correctamente la captura (cap.isOpened()) y
#si el frame se ha leído correctamente (ret).
while(cap.isOpened() and ret):

    #Captura frame a frame    
    ret, frame = cap.read()
    
    #se añade el texto
    cv2.putText(frame, 'Ricardo Martinez Guadalajara', org, font, fontScale, color, thickness, cv2.LINE_AA)
    
    #Se separan los canales
    blue, green, red = cv2.split(frame)
    
    #se genera el mosaico de canales
    color_mosaic = np.hstack([red, green, blue])
    
    if frame is not None:
        #Region donde vamos a insertar el logo    
        roi = frame[-size-10:-10, size-10:size+90]
        #se añade el logo
        roi += logo
        #se muestra el mosaico de canales
        cv2.imshow(' rojo | verde | azul',color_mosaic)
        #se muestra el video original
        cv2.imshow(' Frame original',frame)
    if cv2.waitKey(time) & 0xFF == ord('q'):
        cv2.imwrite('images/deviceLastFrame.jpg',frame)
        break
    
#Se libera el objeto    
cap.release()
cv2.destroyAllWindows()
