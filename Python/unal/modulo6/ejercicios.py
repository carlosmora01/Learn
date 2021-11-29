#Ejercicio 2

partidos = int(input())
golesMadrid = []
golesBarcelona = []
cont = 0
cont2 = 0

ganadosMadrid = 0 
ganadosBarcelona = 0
    
while cont < partidos:
    golesr = int(input())  
    golesMadrid.append(golesr)
    cont += 1

while cont2 < partidos:
    golesb = int(input())
    golesBarcelona.append(golesb)
    cont2 += 1

for i, j in zip(golesMadrid, golesBarcelona):
    if i > j:
        ganadosMadrid += 2
    elif i < j:
        ganadosBarcelona += 2
    else:
        ganadosMadrid+=1
        ganadosBarcelona+=1


print("Ballenota Futbol Club:", ganadosMadrid)
print("Real Mandril:", ganadosBarcelona)

#Ejercicio 3
cromo = []
archivo = []

while True:
    lamina = int(input())
    cromo.append(lamina)
    if lamina == 0:
        break

for i in range(1, 683):
    for j in cromo:
        if i == j and j not in archivo:
            archivo.append(j)

print(len(archivo))

#Ejercicio 4
salario = []

while True:
    sueldo = int(input())
    salario.append(sueldo)
    if sueldo == 0:
        salario.pop()
        break

salario.sort()

total = (salario[-3] - salario[2])/((len(salario))**2)
print(round(total, 2))

#Ejercicio 5
soldados = int(input())
bando1 = []
bando2 = []
cont = 0
cont2 = 0
sobrevivientes = 0
    
while cont < soldados:
    estatura = int(input())  
    bando1.append(estatura)
    cont += 1

while cont2 < soldados:
    estatura2 = int(input())
    bando2.append(estatura2)
    cont2 += 1

bando1.sort()
bando2.sort(reverse=True)

for i, j in zip(bando1, bando2):
    if i%2 == 0 and j%2 != 0:
        sobrevivientes += 2
    elif i%2 != 0 and j%2 == 0:
        sobrevivientes += 2

print(f'Sobreviven {sobrevivientes} soldados')