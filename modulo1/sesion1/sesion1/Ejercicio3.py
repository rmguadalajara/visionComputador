import re
import sys

def isVocal(letra):
    if (re.match("[aeiou]", letra)):
        return "Es vocal"
    else:
        return "Es consonante"

if(len(sys.argv) < 2 or len(sys.argv) > 2):
    print("El uso del programa es un argumento de entrada")
else:
    if(len(sys.argv[1])>1):
        print("El uso del programa es un argumento con un solo caracter")
    else:   
        print(isVocal(sys.argv[1]))