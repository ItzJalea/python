from ast import Continue


def binario(x):
    x = int(x)
    trybin = ""
    if x >= 128:
        x-=128
        trybin += str(1)
        Continue
    else:
        trybin += str(0)
        Continue 
    if x >= 64:
        x-=64
        trybin += str(1)
        Continue
    else:
        trybin += str(0)
        Continue
    if x >= 32:
        x-= 32
        trybin += str(1)
        Continue
    else:
        trybin += str(0)
        Continue
    if x >= 16:
        x -= 16
        trybin += str(1)
        Continue
    else:
        trybin += str(0)
        Continue
    if x >= 8:
        x -= 8
        trybin += str(1)
        Continue
    else:
        trybin += str(0)
        Continue
    if x >= 4:
        x -= 4
        trybin += str(1)
        Continue
    else:
        trybin += str(0)
        Continue
    if x >= 2:
        x -= 2
        trybin += str(1)
        Continue
    else:
        trybin += str(0)
        Continue
    if x >= 1:
        x -= 1
        trybin += str(1)
        Continue
    else:
        trybin += str(0)
        Continue
    return trybin
    


ipusuario = input("Indique ip: ")
Separador = ipusuario.split(".")
octeto1 = binario(Separador[0])
octeto2 = binario(Separador[1])
octeto3 = binario(Separador[2])
octeto4 = binario(Separador[3])
print(octeto1,".",octeto2,".",octeto3,".",octeto4)
