start = int(input("Please enter the starting number here: "))
size = int(input("Please enter the size of the sequence here: "))
seq = []
list = ""

for i in range(0, size):
    if i == 0 or i == 1:
        seq.append(start)
    else:
        seq.append(seq[i - 1] + seq[i - 2])

    list += str(seq[i]) + " "

print("""The fibonacci sequence from your input is...
""")
print(list)
