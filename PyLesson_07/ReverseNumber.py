num = int(input("Please enter a number: "))
number = num
rev = 0

def getReverse():
    global number, rev
    while number > 0:
        rev *= 10
        rev += (number%10)
        number = int(number/10)

    print("The reverse order of", num, "is", rev)

getReverse()
