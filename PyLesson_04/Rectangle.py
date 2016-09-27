length = int(input("Type in the length of the rectangle: "))
width = int(input("Type in the width of the rectangle: "))
height = int(input("Type in the height of the rectangle: "))

def calcPerim(width, length, height):
    perimeter = (4*(length + width + height))
    return("{:0.5f}".format(perimeter))

def Print():
    print("Your rectangle is", calcPerim(width, length, height), "square feet around")

Print()

