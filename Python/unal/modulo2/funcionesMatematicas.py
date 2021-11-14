#Funciones matemáticas "natiavas" (Built-in functions)

# abs(-14) #Valor absoluto de -14 es 14
# max(4, 7, 9) #Mayor de los valores, en este caso 9
# min(4,7,9) #Menos de los valores, en este caso 4
# round(3.7819, 1) #redondea x con d cifras decimales, en este caso 3.8

#Librería math

# cos(x) = coseno de x radianes
# e = constante matemática de Euler e = 2.718281
# factorial(x) = factorial de x
# gcd(a,b) = máximo común divisor de a y b
# log(x,b) = logaritmo de x en base b
# pi = constante matemática 3.1416
# sin(x) = seno de x radianes
# sqrt(x) = raíz cuadrada de x (Equivale a x ** 0.5)
# tan(x) = tangente x de radianes

from math import pi
radio = float(input('Ingrese el radio: '))
area = pi*radio**2

print('El area del circulo es: ', area)