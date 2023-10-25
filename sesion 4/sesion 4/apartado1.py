# coding: utf-8
import cv2
import sys

#Función para atender los eventos del ratón
def EventoRaton(evento, x, y, flags,datos):
    global color
    if evento == cv2.EVENT_MOUSEMOVE:
    # Este evento se genera cada vez que el ratón se mueve por encima de la
    # ventana. Se pueden generar varios eventos similares por segundo.
    # Por ese motivo, si el evento no es necesario, es conveniente salir
    # inmediatamente de la función para no bloquear la aplicación.
        pass

    elif evento == cv2.EVENT_LBUTTONDBLCLK:
        print("Doble click botón izquierdo\n")
        cv2.circle(img, (x,y), 3, color, -1)
    elif evento == cv2.EVENT_LBUTTONDOWN:
        print("Pulsar botón izquierdo\n")
    elif evento == cv2.EVENT_LBUTTONUP:
        print("Soltar botón izquierdo\n")
    else:
        print("Otro evento\n")

    print("Coordenadas: x=", x, ", y=", y, "\n")
    #Refrescamos la imagen en pantalla.
    cv2.imshow("Imagen", img);



#Abrimos la imagen indicada en el primer argumento
try:
    img=cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED);
except:
    print("ERROR al abrir la imagen\n")
    sys.exit(1)

#Comprobamos si la imagen se ha abierto correctamente.
if img is None:
    print("ERROR: Imagen: ", sys.argv[1], " no existe\n")
else:
    #Creamos una ventana donde mostrar la imagen.
    cv2.namedWindow("Imagen", cv2.WINDOW_AUTOSIZE)
    #Mostramos la imagen en pantalla.
    cv2.imshow("Imagen", img)

    #  Asociamos la función de manejo de eventos a esta ventana.
    #  Pasamos la imagen como argumento a la función. Tener en
    #  cuenta la conversión a puntero void para poder realizar
    #  el paso. Observar en la callback como se deshace la
    #  conversión.
    color=(0,0,255)
    cv2.setMouseCallback("Imagen", EventoRaton)
    #Variable en la que capturaremos la tecla pulsada.
    c=0
    #Creamos un bucle infinito, que sólo finalizará al pulsar Esc.
    while not c==27:
        #Esperamos a que el usuario pulse una tecla.
        c=cv2.waitKey(0) & 0xFF
        #Imprimimos la tecla pulsada.
        print(c,"\n")
        

    #Liberamos la ventana creada.
    cv2.destroyWindow("Imagen")

