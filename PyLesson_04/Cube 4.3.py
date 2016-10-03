side = int(input("Type in the side length of your cube here: "))
sa = 0

def calcsurf():
    global sa, side
    sa = 6*(side**2)

def Print(side, sa):
    print("The surface area pf a cube with the side of", side, "is", sa)

calcsurf()
Print(side, sa)
