x = int(input())

for i in [50000, 20000, 10000, 5000, 2000, 1000]:
    if (x%i == 0):
        y = x/i
        print(f'{y} de {i}')