import random

xAndO = []

for i in range(0,4):
    xAndO.append([])
    for j in range(0,4):
        switch = random.randrange(0, 2)
        if switch == 1:
            xAndO[i].append("X")
        else:
            xAndO[i].append("O")

for values in xAndO:
    output = ""
    for value in values:
        output += str(value) + "\t"
    print(output)
