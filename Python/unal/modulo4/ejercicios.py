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

# Reloj en el espejo

hora = int(input())
minuto = int(input())

if(11>hora>1) and (minuto!=0 and minuto!=30):
    print(11-hora, ":", 60-minuto, sep="")
elif(11 == hora) and (minuto!=0 and minuto!=30):
    print('12:', 60-minuto, sep="")
elif(hora == 12 and minuto==0):
    print('12:0')
elif(hora == 12 and minuto!=0):
    print('11:', 60-minuto, sep="")
elif(hora != 12 and hora!=6) and (minuto == 0):
    print(12-hora, ':0', sep='')
elif(hora == 6 and minuto == 0):
    print('6:0')
elif(hora == 6 and minuto!=0):
    print('5:', 60-minuto, sep='')
elif(hora!=6 and hora!=11) and (minuto==30):
    print(11-hora, ':30', sep='')
elif(hora == 11 and minuto == 30):
    print('12:30')

# Núnmeros primos

x = int(input())

if(x%2 == 0):
    print(f'{x} es multiplo de 2')
elif(x%3 == 0):
    print(f'{x} es multiplo de 3')
elif(x%5 == 0):
    print(f'{x} es multiplo de 5')
elif(x%7 == 0):
    print(f'{x} es multiplo de 7')
else:
    print(f'{x} no es multiplo de ninguno de los primeros cuatro primos')

# Piedra papel o tijera

X = str(input())
Y = str(input())

if (X == 'piedra'):
    if (Y == 'piedra'):
        print("empate")
    elif(Y == 'papel'):
        print(f'{Y} vence {X}')
    elif(Y == 'tijera'):
        print(f'{X} vence {Y}')
elif (X == 'tijera'):
    if (Y == 'tijera'):
        print("empate")
    elif(Y == 'papel'):
        print(f'{X} vence {Y}')
    elif(Y == 'piedra'):
        print(f'{Y} vence {X}')
elif (X == 'papel'):
    if (Y == 'papel'):
        print("empate")
    elif(Y == 'tijera'):
        print(f'{Y} vence {X}')
    elif(Y == 'piedra'):
        print(f'{X} vence {Y}')

# Equivalencia en billetes

