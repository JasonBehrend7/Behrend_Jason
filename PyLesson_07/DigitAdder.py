num = int(input("Please enter a number: "))
sum = 0
number = num

while num > 0:
    sum += (num%10)
    num = int(num/10)

print("The sum of the digits in", number, "is", sum)
