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
  
# org
org = (50, 50)
  
# fontScale
fontScale = 1
   
# Blue color in BGR
color = (0, 255, 0)
  
# Line thickness of 2 px
thickness = 2
   
# Read logo and resize
logo = cv2.imread('images/Logo_UAH.jpg')
size = 100
logo = cv2.resize(logo, (size, size))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('videoRicardoMartinez2.avi',fourcc, fps, (int(cap.get(3)),int(cap.get(4))))

#Comprueba si se ha inicializado correctamente la captura (cap.isOpened()) y
#si el frame se ha leído correctamente (ret).
while(cap.isOpened() and ret):

    # Using cv2.putText() method

    if cv2.waitKey(time) & 0xFF == ord('q'):
        break
    #Captura frame a frame    
    ret, frame = cap.read()
    cv2.putText(frame, 'Ricardo Martinez Guadalajara', org, font, fontScale, color, thickness, cv2.LINE_AA)
    
    # Region of Image (ROI), where we want to insert logo
    if frame is not None:
        roi = frame[-size-10:-10, size-10:size+90]
        roi += logo
        out.write(frame)
        cv2.imshow("frame",frame)
    
#Se libera el objeto    
cap.release()
cv2.destroyAllWindows()
