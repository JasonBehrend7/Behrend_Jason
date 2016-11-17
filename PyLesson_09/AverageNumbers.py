import random
numbers = []
output = ""

for i in range(0,10):
    i = random.randrange(1,101)
    numbers.append(i)

for i in numbers:
    output += str(i) + " "

def average(num):
    avg = 0
    for i in num:
        avg += i
    return(avg / len(num))

print("Numbers...")
print(output)
print("")
print("The average of the above numbers is...")
print(average(numbers))
