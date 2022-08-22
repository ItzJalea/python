def binario(x):
    x = int(x)
    trybin = ""
    if x >= 128:
        x-=128
        trybin += str(1)
    else:
        trybin += str(0) 
    if x >= 64:
        x-=64
        trybin += str(1)
    else:
        trybin += str(0)
    if x >= 32:
        x-= 32
        trybin += str(1)
    else:
        trybin += str(0)
    if x >= 16:
        x -= 16
        trybin += str(1)
    else:
        trybin += str(0)
    if x >= 8:
        x -= 8
        trybin += str(1)
    else:
        trybin += str(0)
    if x >= 4:
        x -= 4
        trybin += str(1)
    else:
        trybin += str(0)
    if x >= 2:
        x -= 2
        trybin += str(1)
    else:
        trybin += str(0)
    if x >= 1:
        x -= 1
        trybin += str(1)
    else:
        trybin += str(0)
    return trybin
    


ipusuario = input("Indique ip: ")
Separador = ipusuario.split(".")
Salto = ""
for i in Separador:
    Salto += binario(i) + "."
print(Salto[:-1])
