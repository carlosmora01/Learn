T = int(input())
H = int(input())

if H <= 45:
    print("$", T*H)
else:
    print("$", int((T*45) + (H-45)*1.5*T))

