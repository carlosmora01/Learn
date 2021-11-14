a = int(input())
b = int(input())
c = str(input())

d = (a * 60) + b

if( c == "am"):
    if (a == 12):
        print("Faltan", (1440 - b), "para las 12")
    else:
        print("Faltan", (1440 - d), "para las 12")
else:
    if (a == 12):
        print("Faltan", (720 - b), "para las 12")
    else:
        print("Faltan", (720 - d), "para las 12")