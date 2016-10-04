r = int(input("Type the radius of a circle here: "))
area = 0

def calcArea():
    global area, r
    a = 3.14159265359*(r**2)
    area = ("{:0.5f}".format(a))

def Print(r, a):
    print("The area of a circle with a radius of", r, "is", a)

calcArea()
Print(r, area)
