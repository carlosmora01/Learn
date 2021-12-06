from math import factorial

def fuerte(num):
    x = [int(x) for x in str(num)] 
    suma = 0
    for i in x:
        suma += factorial(i)
    return suma

cont = 0
num = []
n = int(input())

while cont<n:
    valores = int(input())
    num.append(valores)
    cont += 1

for y in num:
    if y == fuerte(y):
        print(f'{y} es fuerte')
    else:
        print(f'{y} no es fuerte')