side = int(input("Type in the side length of your cube here: "))

def calcsurf(side):
    sa = 6*(side**2)
    return ("{:0.5f}".format(sa))

def Print(side, sa):
    print("The surface area pf a cube with the side of", side, "is", sa)

Print(side, calcsurf(side))
