#Ejercicio 1 
from math import sqrt
c = (1079252848.8)**2
def lorentz(v):
    return 1/(sqrt(1-(v**2/c)))

cont = 0
x = []
N = int(input())

while cont<N:
    valores = float(input())
    x.append(valores)
    cont += 1

for y in x:
    print(round(lorentz(y), 15))

#Ejercicio 2 

from math import sqrt

def f(x):
    return sqrt(2 + 5*x)

def g(x):
    return (4 + x)**3

numeros = []

while True:
    entrada = int(input())
    numeros.append(entrada)
    if entrada == 0:
        numeros.pop()
        break

for y in numeros:
    if y%2 == 0:
        print(f(g(y)))
    else:
        print(g(f(y)))

# Ejercicio 3
def hyperpar(num):
    x = [int(x) for x in str(num)] 
    j = []
    for y in x:
        if y == 0:
            j.append(y)
        elif y%2 == 0:
            j.append(y)
     
    if j == x:
        return True
    else:
        return False

numeros = []

while True:
    entrada = int(input())
    numeros.append(entrada)
    if entrada == -1:
        numeros.pop()
        break

for z in numeros:
    if hyperpar(z) == True:
        print('Hyperpar')
    else:
        print('No es hyperpar')

#Ejercicio 4

def f(x):
    if x%123 == 0:
        return 0
    else:
        return 1 + f(x+23)
        
cont = 0
x = []
N = int(input())

while cont<N:
    valores = int(input())
    x.append(valores)
    cont += 1

for y in x:
    print(f(y))

#Ejercicio 5

from math import sqrt

def PAN(x):
    n = sqrt(5*x + 4)
    a = 3**n 
    return 2*a + 1

cont = 0
x = []
N = int(input())

while cont<N:
    valores = float(input())
    x.append(valores)
    cont += 1

for y in x:
    print(PAN(y))

# Ejercicio 6
def A(m,n):
    if m == 0:
        return n+1
    elif m>0 and n == 0:
        return A(m-1, 1)
    elif m>0 and n>0:
        return A(m-1, A(m,n-1))

cont = 0
x = []
N = int(input())

while cont<N:
    valor1 = int(input())
    valor2 = int(input())
    x.append(valor1)
    x.append(valor2)
    cont += 1

for i in range (0, len(x), 2):
    print(A(x[i], x[i+1]))

#Ejercicio 6

def perf(x):
    suma = [1]
    for i in range(2,x):
        if x%i == 0:
            suma.append(i)
    
    return sum(suma)

cont = 0
num = []
n = int(input())

while cont<n:
    valores = int(input())
    num.append(valores)
    cont += 1

for y in num:
    if y == perf(y):
        print(f'{y} es perfecto')
    else:
        print(f'{y} no es perfecto')

