r = int(input("Type the radius of a circle here: "))

def calcArea(r):
    a = 3.14159265359*(r**2)
    area = ("{:0.5f}".format(a))
    return area

def Print(r, a):
    print("The area of a circle with a radius of", r, "is", a)

Print(r, calcArea(r))
