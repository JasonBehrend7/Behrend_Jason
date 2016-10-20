need = int(input("Input the amount of cookies you need: "))
batchSize = 25
batch = 1

for cookies in range(need, -1, -batchSize):
    print("Cookies Needed: ", cookies)
    print("Batch #", batch)
    batch +=1
print("The cookies are ready!")
