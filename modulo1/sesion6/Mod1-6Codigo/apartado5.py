# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys

def ruido(tipo_ruido,img):
    #Genera ruido gaussiano
    if tipo_ruido == "gauss":
        row,col= img.shape
        mean = 0
        var = 50
        sigma = var**0.5
        gauss = np.random.normal(mean,sigma,(row,col))
        gauss = gauss.reshape(row,col)
        img_noise = np.uint8(img + gauss)
        return img_noise
    #Genera ruido 'Sal y Pimienta'
    elif tipo_ruido == "sp":
        row,col = img.shape
        print(row,col)
        s_vs_p = 0.01
        amount = 0.0001
        img_noise = img.copy()
        # Sal
        num_salt = np.ceil(amount * img.size * s_vs_p)
        coordsSalt = [np.random.randint(0, i - 1, int(num_salt)) for i in img.shape]
        img_noise[coordsSalt] = 255
        # Pimienta
        num_pepper = np.ceil(amount* img.size * (1. - s_vs_p))
        coordsPepper = [np.random.randint(0, i - 1, int(num_pepper)) for i in img.shape]

        img_noise[coordsPepper] = 0
        return img_noise 

def psnr(img1, img2):
    dif=(img1-img2)**2 #Obtenemos el error cuadrático entre las dos imágenes
    dif=np.float32(dif)/img1.size #Hacemos la media para toda la imagen

    if not dif.sum()==0:    
        psnr=10*np.log10(255.0*255.0/dif.sum()) #Obtenemos PSNR
        return psnr
    else:
        print("Imágenes iguales")
        return 10000

img = cv2.imread('Imagenes/Lenna.png',cv2.IMREAD_GRAYSCALE)
if img is None: #Si está vacía es que no se ha leído
	print('Imagen no encontrada\n')
	sys.exit(0)

img2=img.copy()
cv2.imshow("Original",img2)
#Añadimos ruido sal y pimienta
noiseType = sys.argv[1]
img= ruido(noiseType, img)

cv2.imshow(noiseType,img)
#Aplicamos filtro de la mediana
median = cv2.medianBlur(img,3)

#Mostramos el PSNR
print("PSNR median blur:%g" % psnr(img2,median))

# Aplicamos filtro Gaussiano
gaussian = cv2.GaussianBlur(img, (3, 3), 0)

# Mostramos el PSNR
print("PSNR Gaussian:%g" % cv2.PSNR(img2, gaussian))

#Mostramos las imágenes
res = np.hstack((img,median,gaussian ))
cv2.imshow("Ruido y corregido con median blur y con gaussian blur",res)

cv2.waitKey(0)
cv2.destroyAllWindows()
