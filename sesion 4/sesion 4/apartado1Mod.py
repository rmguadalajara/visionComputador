# coding: utf-8
import cv2
import sys

# Variables globales
color = (0, 0, 255)
rect_start = None
rect_end = None
drawing = False
thickness = 1
filled = False


# Función para atender los eventos del ratón
def EventoRaton(evento, x, y, flags, datos):
    global color, rect_start, rect_end, drawing, thickness, filled

    if evento == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # Si estamos dibujando, actualizamos la posición de la esquina opuesta
            rect_end = (x, y)
    elif evento == cv2.EVENT_LBUTTONDOWN:
        # Si se ha pulsado el botón izquierdo, guardamos la posición de la esquina inicial
        rect_start = (x, y)
        drawing = True
    elif evento == cv2.EVENT_LBUTTONUP:
        # Si se ha soltado el botón izquierdo, guardamos la posición de la esquina final
        rect_end = (x, y)
        drawing = False
        # Dibujamos el rectángulo sobre la imagen
        if filled:
            cv2.rectangle(img, rect_start, rect_end, color, -1)
        else:
            cv2.rectangle(img, rect_start, rect_end, color, thickness)

    # Refrescamos la imagen en pantalla.
    cv2.imshow("Imagen", img)


# Abrimos la imagen indicada en el primer argumento
try:
    img = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)
except:
    print("ERROR al abrir la imagen\n")
    sys.exit(1)

# Comprobamos si la imagen se ha abierto correctamente.
if img is None:
    print("ERROR: Imagen: ", sys.argv[1], " no existe\n")
else:
    # Creamos una ventana donde mostrar la imagen.
    cv2.namedWindow("Imagen", cv2.WINDOW_AUTOSIZE)
    # Mostramos la imagen en pantalla.
    cv2.imshow("Imagen", img)

    # Asociamos la función de manejo de eventos a esta ventana.
    # Pasamos la imagen como argumento a la función. Tener en
    # cuenta la conversión a puntero void para poder realizar
    # el paso. Observar en la callback como se deshace la
    # conversión.
    cv2.setMouseCallback("Imagen", EventoRaton)
    # Variable en la que capturaremos la tecla pulsada.
    c = 0
    # Creamos un bucle infinito, que sólo finalizará al pulsar Esc.
    while not c == 27:
        # Esperamos a que el usuario pulse una tecla.
        c = cv2.waitKey(0) & 0xFF
        # Imprimimos la tecla pulsada.
        print(c, "\n")
        # Cambiamos el color de los puntos según la tecla pulsada
        if c == ord('r'):
            color = (0, 0, 255)  # Rojo
        elif c == ord('g'):
            color = (0, 255, 0)  # Verde
        elif c == ord('b'):
            color = (255, 0, 0)  # Azul
        elif c == ord('+'):
            thickness += 1
        elif c == ord('-'):
            thickness -= 1
            if thickness < 0:
                filled = True
                thickness = -thickness
        # Mostramos el grosor actual del rectángulo
        print("Grosor: ", thickness, "\n")

    # Liberamos la ventana creada.
    cv2.destroyWindow("Imagen")