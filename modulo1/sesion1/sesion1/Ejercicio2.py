import sys

#Funcion que devuelve la longitud de una cadena
def calclen(stringToCalc):
    length = 0
    for a in stringToCalc:
        length += 1
    return length

#Programa principal
if(len(sys.argv) < 2 or len(sys.argv) > 2) :
    print("El uso del programa es un argumento de entrada")
else:
    print(calclen(sys.argv[1]))