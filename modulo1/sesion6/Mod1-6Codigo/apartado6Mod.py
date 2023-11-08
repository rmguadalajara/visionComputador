import cv2
import sys

img = cv2.imread("Imagenes/Lenna.png")
if img is None:
    print('Imagen no encontrada\n')
    sys.exit(0)

height, width = img.shape[:2]

interpolations = [cv2.INTER_CUBIC, cv2.INTER_AREA, cv2.INTER_LINEAR, cv2.INTER_LANCZOS4]
names = ["CUBIC", "AREA", "LINEAR", "LANCZOS4"]

for interp, name in zip(interpolations, names):
    resized = cv2.resize(img, (int(width/2), int(height/2)), interpolation = interp)
    resized_back = cv2.resize(resized, (width, height), interpolation = interp)
    psnr = cv2.PSNR(img, resized_back)
    print(f"PSNR for {name}: ", psnr)