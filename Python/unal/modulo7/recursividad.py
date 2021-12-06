# def alfa(X):
#     m = X - 9
#     return 3*[m]

# def beta(Y):
#     n = len(Y)
#     s = 0
#     for e in Y:
#         s += e*n
#         n -= 1
#     return s    

# L = [6, 3, 10, 4, 9]
# print(alfa(beta(L)))

def fact(X):
    if X == 1:
        return 1
    return X * fact(X-1)

print(fact(4))