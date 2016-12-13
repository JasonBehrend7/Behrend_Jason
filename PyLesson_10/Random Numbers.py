import random

numsList = []
for i in range(0,4):
    numsList.append([])
    for j in range(0,4):
        numsList[i].append(random.randrange(1,101))


    
for nums in numsList:
    output = ""
    for num in nums:
        output += str(num) + "\t"
    print(output)

print("\n" + str(numsList))
