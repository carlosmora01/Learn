# i = int(input())
# j = int(input())
# lista = []

# def fib(n):
#     a = 2
#     b = 1
    
#     for k in range(n):
#         c = b+a
#         a = b
#         b = c
        
#     return a

# for x in range(j+1):
#     if fib(x) <= j:    
#         if fib(x) <= j and fib(x) >= i:
#             lista.append(fib(x))
#     else:
#         break

# print(len(lista))


# EJercicio 3 

# N = int(input())
# lista = []
# cont = 0

# while cont < N:
#     num = int(input())
#     lista.append(num)
#     cont += 1

# def armstrong(x):
#     divi = [int(a) for a in str(x)]
#     y = len(divi) 

#     cont = 0

#     for i in divi:
#         cont += i**y

#     if cont == x:
#         return True
#     else:
#         return False

# for u in lista:
#     if (armstrong(u)):
#         print(f'{u} es Armstrong')
#     else:
#         print(f'{u} no es Armstrong')

# Ejercicio 5
# x = int(input())
# listcamp = []
# sortedlist = []

# for i in range(x):
#     h = float(input())
#     listcamp.append(h)
#     sortedlist.append(h)
    
# h = len(listcamp)
# sortedlist.sort()

# for i in sortedlist:
#     print(listcamp.index(i) + 1)


# lista = []

# while True:
#     numero = int(input())
#     lista.append(numero)
#     if numero == 0:
#         lista.pop()
#         break

# def multidigito(x):
#     numeroMultidigito = []
#     divi = [int(a) for a in str(x)]

#     for i in range(1, 6):
#         for j in divi:
#             if i == j and j not in numeroMultidigito:
#                 numeroMultidigito.append(i)

#     return numeroMultidigito

# for x in lista:
#     if multidigito(x) == [1,2,3,4,5]:
#         print("Multidigito")
#     else:
#         print("No es multidigito")

#Ejercicio 7

def dividers(n):
    dividersList = []
    for i in range(1, n+1):
        if n % 1 == 0:
            dividersList.append(i)
    number = len(dividersList)
    return number

def julianachi(n):
    julianachiList = [1]
    for i in range(0,n):
        nextElement = julianachiList[i] + dividers(julianachiList[i])
        julianachiList.append(nextElement)
    return julianachiList

n = int(input())
if n in julianachi(n):
    print("Pertenece a la serie de Julianachi")
else:
    print("No pertenece a la serie de Julianachi")