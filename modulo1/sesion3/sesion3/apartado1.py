# -*- coding: utf-8 -*-
import cv2
import sys

print ('Nombre vídeo: ', sys.argv[1])

#Creamos un objeto de la clase video-captura
cap = cv2.VideoCapture(sys.argv[1])

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
print(frame.shape[0])

#Definimos el tipo de fuente para escribir texto en vídeo
font = cv2.FONT_HERSHEY_SIMPLEX
  
# posicion origen texto
org = (50, 50)
  
# tamaño fuente texto
fontScale = 1
   
# ponemos el color en verde
color = (0, 255, 0)
  
# anchura texto en pixeles
thickness = 2
   
# Lectura logo y redimensionado
logo = cv2.imread('images/Logo_UAH.jpg')
size = 100
logo = cv2.resize(logo, (size, size))

# Definimos codec y declaramos video writer
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('videoRicardoMartinez2.avi',fourcc, fps, (int(width),int(height)), True)

#Comprueba si se ha inicializado correctamente la captura (cap.isOpened()) y
#si el frame se ha leído correctamente (ret).
while(cap.isOpened() and ret):

    #presionando q se sale de reproduccion
    if cv2.waitKey(time) & 0xFF == ord('q'):
        break
    
    #Captura frame a frame    
    ret, frame = cap.read()
    
    #añadimos texto con paremetrización anterior
    cv2.putText(frame, 'Ricardo Martinez Guadalajara', org, font, fontScale, color, thickness, cv2.LINE_AA)
    
    if frame is not None:
        #Región de interes para insertar logo
        roi = frame[-size-10:-10, size-10:size+90]
        #insertamos logo
        roi += logo
        #se escribe en fichero de salida fame del video
        out.write(frame)
        #mostramos frame en visor
        cv2.imshow("frame",frame)
    
#Se libera el objeto    
cap.release()
cv2.destroyAllWindows()
