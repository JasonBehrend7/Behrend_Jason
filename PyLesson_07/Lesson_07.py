num = int(input("Enter a number: "))
number = num
digits = 0
while num > 0:
    digits += 1
    num = int(num/10)
print("There are", digits, "digits in the number", number)
