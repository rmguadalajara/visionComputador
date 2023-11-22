import cv2
import sys
import time

#PIVC (Procesado de Imagen y Visión por Computador) 
#Modulo 2-Practica 1 - Detector Viola & Jones

#Funcion para pintar los bounding boxes detectados
def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


def detector(img_color):
    print(">>> Cargando imagen...")
    #Tratamos la imagen
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_RGB2GRAY)
    img_gray = cv2.equalizeHist(img_gray)
    print(img_gray.shape)

    # Carga del modelo de deteccion (previamente entrenado)
    cascade_fn = 'haarcascades/haarcascade_frontalface_alt.xml'
    cascade = cv2.CascadeClassifier(cascade_fn)
    
        
    #Llamada al detector
               
    print(">>> Detectando caras...")
    
    rects =  cascade.detectMultiScale(
    img_gray,
    scaleFactor=1.05,
    minNeighbors=10,
    minSize=(5, 5),
    flags = cv2.CASCADE_SCALE_IMAGE
    )
    
    if len(rects) == 0:
        return img_color
    print(rects)
    rects[:, 2:] += rects[:, :2]   
    
        
    img_out = img_color.copy()
    draw_rects(img_out, rects, (0, 255, 0))
    return img_out
    
start_time = time.time()
img_color=cv2.imread(sys.argv[1])
if img_color is None:
    print('Imagen no encontrada\n')
    sys.exit()


img_out = detector(img_color)
cv2.imwrite('resultado_deteccion.jpg', img_out)
height, width = img_out.shape[:2]
resized = cv2.resize(img_out, (int(width/2), int(height/2)), interpolation = cv2.INTER_CUBIC)
print("--- %s seconds ---" % (time.time() - start_time))
#Visualizar caras detectadas
cv2.imshow('Caras detectadas',img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()

