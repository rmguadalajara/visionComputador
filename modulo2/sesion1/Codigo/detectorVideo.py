import cv2
import numpy as np

# Cargar el modelo pre-entrenado
cascade_fn = 'haarcascades/haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_fn)

# Iniciar la captura de video desde la cámara web
cap = cv2.VideoCapture(0)

# Obtener la tasa de fotogramas de la cámara
fps = cap.get(cv2.CAP_PROP_FPS)

# Definir el códec y crear un objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('output.avi', fourcc, fps, (frame_width, frame_height),True)

# Función para pintar los bounding boxes detectados
def draw_rects(img, rects):
    colors = [(i, i, i) for i in range(256)]
    for x1, y1, x2, y2 in rects:
        color = colors[(x1 + y1) % 256]
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 5)
    

while True:
    # Leer un nuevo fotograma
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir el fotograma a escala de grises
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.equalizeHist(img_gray)
    # Realizar la detección de rostros
    rects = cascade.detectMultiScale(
    img_gray,
    scaleFactor=1.05,
    minNeighbors=10,
    minSize=(10, 10),
    flags = cv2.CASCADE_SCALE_IMAGE
    )
    if len(rects) > 0:
        rects[:, 2:] += rects[:, :2]
    draw_rects(frame, rects)
    
    # Mostrar el fotograma
    cv2.imshow('Video', frame)

    # Escribir el fotograma en el archivo 'output.avi'
    out.write(frame)

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los objetos de captura de video y escritura de video
cap.release()
out.release()

# Cerrar todas las ventanas de OpenCV
cv2.destroyAllWindows()