T = int(input())
H = int(input())

if H <= 45:
    print("$", T*H)
else:
    print("$", int((T*45) + (H-45)*1.5*T))

# Posicion en el plano cartesiano

x = float(input())
y = float(input())

if (x and y != 0):
    if (x > 0):
        if(y > 0):
            print(f'La coordenada ({x}, {y}) se encuentra en el cuadrante 1')
        else:
            print(f'La coordenada ({x}, {y}) se encuentra en el cuadrante 4')
    else:
        if(y > 0):
            print(f'La coordenada ({x}, {y}) se encuentra en el cuadrante 2')
        else: 
            print(f'La coordenada ({x}, {y}) se encuentra en el cuadrante 3')
elif( x == 0 and y == 0):
    print(f'La coordenada ({x}, {y}) corresponde al origen')
else:
    if(x == 0):
        print(f'La coordenada ({x}, {y}) esta sobre el eje Y')
    else: 
        print(f'La coordenada ({x}, {y}) esta sobre el eje X')

#Mediana de un número
a = float(input())
b = float(input())
c = float(input())

if(a == b and b == c):
    print(f'{a} es la mediana')
else:
    if(a>b and b>c):
        print(f'{b} es la mediana')
    elif(b>a and a>c):
        print(f'{a} es la mediana')
    else:
        print(f'{c} es la mediana')

#Falta tanto para las 12

a = int(input())
b = int(input())
c = str(input())

d = (a * 60) + b

if( c == "am"):
    if (a == 12):
        print("Faltan", (1440 - b), "para las 12")
    else:
        print("Faltan", (1440 - d), "para las 12")
else:
    if (a == 12):
        print("Faltan", (720 - b), "para las 12")
    else:
        print("Faltan", (720 - d), "para las 12")