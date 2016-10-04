def converter(w, l, h):

    inch = w*l*h
    feet = inch/1728
    return ("{:
            0.2f}".format(feet))

width = float(input("How wide is the subwoofer box in inches: "))
length = float(input("How long is the subwoofer box in inches: "))
height = float(input("How tall is the subwoofer box in inches: "))

print("The volume of the subwoofer box is", converter(width, length, height), "feet cubed")
