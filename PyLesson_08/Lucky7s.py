num = int(input("Please enter a number here: "))

def luck(number):
    if number > 0:
        if number % 10 == 7:
            return 1 + luck(int(number / 10))
        else:
            return luck(int(number /  10))
    else:
        return 0

print(luck(num))


