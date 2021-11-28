A = int(input('Ingrese A: '))
divisores = 1
for i in range(2, A+1):
    if A%i == 0:
        divisores += 1
print(divisores)