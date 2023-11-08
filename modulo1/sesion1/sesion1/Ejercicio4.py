import sys

#Funcion que devuelve el numero entero de un binario
def binToInt(bin_a):
    return int(bin_a,2)

#Funcion que devuelve si un caracter es vocal o no
def isBinary(string_a):
    p = set(string_a)
    s = {'0','1'}
    if s == p or p == {'0'} or p == {'1'}:
        return True
    else:
        return False;
    
#Programa principal
if(len(sys.argv) < 2 or len(sys.argv) > 2):
    print("El uso del programa es un argumento de entrada")
else:
    if(isBinary(sys.argv[1])):
        print(binToInt(sys.argv[1]))
    else:   
        print("El uso del programa es un argumento que sea binario")
        