num = int(input("Please enter a number: "))
digits = 0
average = 0

def avDigits():
    global digits, average, num
    number = num
    while number > 0:
        digits += 1
        average += (number%10)
        number = int(number/10)

    average = average/digits
    print("The average of the digits in", num, "is", average)

avDigits()
