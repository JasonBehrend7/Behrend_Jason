output = ""
upTo = int(input("What number do you want to count up to? "))
by = int(input("What do you want to count by? "))

for i in range(0, (upTo + by), by):
    output = output + str(i) + "\t"
    

print(output)
