import cv2
import sys

#Leemos la imagen
image=cv2.imread(sys.argv[1],cv2.WINDOW_AUTOSIZE)

#readamos laa ventana donde visualizar la imagen
cv2.namedWindow("Ejemplo1",cv2.WINDOW_AUTOSIZE)

if image is None: #si la imagen esta vacia es que no se ha leido
    print("Imagen no encontrada\n")
else:
    cv2.imshow("Ejemplo1",image)
    
    #Obtenemos las dimensiones de la imagen
    print("Tamaño imagen")
    print(image.shape)
    
    ##Obtenemos tipo de imagen
    print("Tipo Imagen")
    print(image.dtype)
    
    #Guardamos imagen con extensión png
    print("Salvamos imagen con extension .png")
    cv2.imwrite(sys.argv[1].replace('jpg','png'),image)
    
    #Guardamos la imagen redimensionada
    print('Redimensionamos imagen a la mitad')
     
    #escala para resize en tanto por ciento
    scale_percent = 50
    
    #reescalamos altura y anchura
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    
    # nuevo size
    dsize = (width, height)
    
    # resize image
    image_resized = cv2.resize(image, dsize)
    
    print("Tamaño imagen reescalada")
    print(image.shape)
    
    #Guardamos imagen redimensionada
    cv2.imwrite(sys.argv[1].replace('.jpg','_resize.jpg'),image_resized)
    
    #Cambiamos espacio de color    
    image_gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #Guardamos imagen con espacio de color en escala grises
    print("Salvamos imagen con espacio de color en escala grises")
    cv2.imwrite(sys.argv[1].replace('.jpg','_gray.jpg'),image_gray)
    
    #La visualación espera hasta que lusuario presione una tecla
    cv2.waitKey(0)
    
#Cerramos todas las ventanas creadas
cv2.destroyAllWindows()


        
    