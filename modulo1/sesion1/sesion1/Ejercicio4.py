import sys

def binToInt(bin_a):
    return int(bin_a,2)


def isBinary(string_a):
    p = set(string_a)
    s = {'0','1'}
    if s == p or p == {'0'} or p == {'1'}:
        return True
    else:
        return False;
    
if(len(sys.argv) < 2 or len(sys.argv) > 2):
    print("El uso del programa es un argumento de entrada")
else:
    if(isBinary(sys.argv[1])):
        print(binToInt(sys.argv[1]))
    else:   
        print("El uso del programa es un argumento que sea binario")
        