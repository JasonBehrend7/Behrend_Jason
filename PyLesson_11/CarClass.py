class Car:
    def __init__ (self, color, interior, wheels, windows):
        self.color = color
        self.interior = interior
        self.wheels = wheels
        self.windows = windows

    def setCustom (self, color, interior, wheels, windows):
        self.color = color
        self.interior = interior
        self.wheels = wheels
        self.windows = windows

    def getColor (self):
        return self.color

    def getInterior (self):
        return self.interior

    def getWheels (self):
        return self.wheels

    def getWindows (self):
        return self.windows


def main():
    color = input("What color do you want your car to be? ")
    interior = input("What do you want your interior to be? ")
    wheels = input("What type of wheels do you want? ")
    windows = input("What type of windows do you want? ")

    car1 = Car(color, interior, wheels, windows)

    print("")
    print("Your vehicle is ready...")
    print("Color:  \t", car1.getColor())
    print("Interior: \t", car1.getInterior())
    print("Wheels: \t", car1.getWheels())
    print("Windows: \t", car1.getWindows())

    print("")
    color = input("What color do you want your second car to be? ")
    interior = input("What do you want your interior to be? ")
    wheels = input("What type of wheels do you want? ")
    windows = input("What type of windows do you want? ")

    car2 = Car(color, interior, wheels, windows)

    print("")
    print("Your second vehicle is ready...")
    print("Color:  \t", car2.getColor())
    print("Interior: \t", car2.getInterior())
    print("Wheels: \t", car2.getWheels())
    print("Windows: \t", car2.getWindows())

main()
