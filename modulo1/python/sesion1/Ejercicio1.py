import sys

def max(num1, num2):
    if (num1 > num2):
        result = num1
    else:
        result = num2

    return result

ok = True
if(len(sys.argv) < 3 or len(sys.argv) > 3):
    print("El uso del programa son dos argumentos numéricos")
    ok=False
else:
    if(sys.argv[1].isdigit() and ok is True):
        arg1 = sys.argv[1]
    else: 
        print("Primer argumento no es un numero: " + sys.argv[1])
        ok=False
    if(sys.argv[2].isdigit() and ok is True):
        arg2 = sys.argv[2]
    else:
        print("Segundo argumento no es un numero: " + sys.argv[2])
        ok=False

if(ok is True):
    print(max(sys.argv[1],sys.argv[2]))