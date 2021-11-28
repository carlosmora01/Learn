total = 31

X = 7

while True:

    X += 2

    if X % 5 == 0:

        continue

    elif X % 7 == 0:

        break

    total += X

print(total)