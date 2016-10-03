length = int(input("Type in the length of the rectangle: "))
width = int(input("Type in the width of the rectangle: "))
height = int(input("Type in the height of the rectangle: "))
perimeter = 0

def calcPerim():
    global length, width, height, perimeter
    perimeter = (4*(length + width + height))
    return perimeter

def Print(perim):
    print("Your rectangle is", perim, "square feet around")

calcPerim()
Print(perimeter)

