#Encontrar el mayor elemento de una lista de números

miLista = [16, 35, 21, 48, 20]
N = len(miLista)
mayor = miLista[0]
for i in range(1, N):
    if miLista[i] > mayor:
        mayor = miLista[i]
print('El mayor elemento es', mayor)

