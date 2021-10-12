#Hollar el área de un trapecio
B = float(input("B: "))
b = float(input("b: "))
h = float(input("h: "))

x = ((B+b)*h/2)

print("El lote tiene", x, "metros cuadrados") 

#Me volveré millonario

C = float(input())
i = float(input())
m = float(input())
final = (C * ((1 + i)**m))

print(round(final , -1))

# Vaciado de cilindro

from math import pi

r = float(input("r: "))
h =  float(input("h: "))
v =  float(input("v: "))
m =  float(input("m: "))

volumen = pi*(r**2)*h

vaciado = volumen - (v * m)

if vaciado < 0:
    vaciado = 0

print(round(vaciado, 3))


# Calcular area
from math import sqrt

catetoUno = float(input("lado: "))
diagonal =  float(input("diagonal: "))

catetoDos = sqrt(diagonal**2 - catetoUno**2)

Z = catetoUno * catetoDos

print("El area total es de", round(Z, 2) ,"metros cuadrados")


#segundos a horas.min.segs
segundos = int(input())

horas = int(segundos/3600)
minutos = int((segundos%3600)/60)
segundosFinal = ((segundos%3600) - minutos * 60)

print(horas,minutos,segundosFinal,sep=":")