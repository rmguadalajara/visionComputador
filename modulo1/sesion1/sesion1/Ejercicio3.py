import re
import sys

#Funcion que devuelve si un caracter es vocal o no
def isVocal(letra):
    if (re.match("[aeiou]", letra)):
        return "Es vocal"
    else:
        return "Es consonante"

#Programa principal
if(len(sys.argv) < 2 or len(sys.argv) > 2):
    print("El uso del programa es un argumento de entrada")
else:
    #Comprobamos que el argumento es un solo caracter
    if(len(sys.argv[1])>1):
        print("El uso del programa es un argumento con un solo caracter")
    else:   
        print(isVocal(sys.argv[1]))