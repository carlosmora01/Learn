# def Par_o_impar(A):
#     if A%2 == 0:
#         print(A, 'es par')
#     else:
#         print(A, 'es impar')

# N = 9
# Par_o_impar(N)

def esPar(B):
    if B%2 == 0:
        return True
    return False

N = 9
if esPar(N):
    print(N, 'es par')
else:
    print(N, 'es impar')