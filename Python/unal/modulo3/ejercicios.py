#Calle prohibida

C = int(input())
N = int(input())

if (C%13==0 or C%23==0) or (N%13==0 or N%23==0):
    print("La direccion calle", C, "#", N, "esta prohibida")
else:
    print("La direccion calle", C, "#", N, "no esta prohibida")

#Devuelta
V = int(input())
E = int(input())
X = (E - V)
print(X)

if (X%10==0 or X%15==0) and X%4!=0:
    print("y te lo puedes quedar")

#Inversion
C = int(input())
K = int(input())
X = K - C

P = ((K-C)/C)*100

if P>0:
    print('Hubo una ganancia de $', X ,'correspondiente al', P, '% del capital invertido')
elif P<0:
    print('Hubo una perdida de $', abs(X) ,'correspondiente al',abs(P), '% del capital invertido')
else:
    print("No hubo ni ganancia ni perdida, la inversion fue un desperdicio de tiempo, pero al menos no de dinero")
