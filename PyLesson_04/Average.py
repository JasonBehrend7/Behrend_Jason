num = int(input("Type in a number here: "))
num2 = int(input("Type in a second number here: "))
num3 = int(input("Type in a third number here: "))

def average(n, n2, n3):
    return (n + n2 + n3) / 3

def Print(n, n2, n3, average):
    avg = ("{:0.5f}".format(average))
    print("The average of", n, n2, "&", n3, "is", avg)
    
Print(num, num2, num3, average(num, num2, num3))
