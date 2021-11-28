# Tablas de multiplicar
N = int(input())

for i in range(1, 21):
    if N > 20:
        break
    print (f'{N} x {i} = {N*i}')

#División de bienes
X = float(input())

if X > 10:
    acumulador = 0

    while X >= 10:
        X = X/2
        acumulador += 1
    print (int(acumulador))

# Area de lotes
x = float(input())
y = float(input())
z = float(input())

area = y**2
acumulador = y
i = 2

while i<=x:
    acumulador+=z
    area += acumulador**2
    i+=1
    
print(f'El area total es de {area} metros cuadrados')

#Elefantes se balanceaban

x = float(input())
i = int(input())

acumulador = 0
elefantes = 0
for j in range(1, i+1):
    h = 0
    h = float(input())
    acumulador+=h 
    
    if acumulador<=x:
        elefantes+=1

print(elefantes)