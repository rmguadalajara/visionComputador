import cv2
import sys

#Leemos la imagen
image=cv2.imread('imagenes/Politecnica.jpg',cv2.WINDOW_AUTOSIZE)

#readamos laa ventana donde visualizar la imagen
cv2.namedWindow("Ejemplo1",cv2.WINDOW_AUTOSIZE)

if image is None: #si la imagen esta vacia es que no se ha leido
    print("Imagen no encontrada\n")
    sys.exit(0)
else:

    image[250:475,275:700]=(0,0,255)# Ponemos la ROI en color rojo
    cv2.imshow('ROI',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
            
    cv2.imwrite('imagenes/Politecnica1.jpg',image)