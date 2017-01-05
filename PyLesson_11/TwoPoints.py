import math

class Distance:
    def __init__ (self, x1, y1, x2, y2):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        self.distance = 0


    def newPoints (self, x1, y1, x2, y2):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        self.distance = 0

    def getDistance (self):
        self.distance = math.sqrt((self.xTwo-self.xOne)*(self.xTwo-self.xOne)+(self.yTwo-self.yOne)*(self.yTwo-self.yOne))
        return self.distance

def main():
    x1 = int(input("Set the first x value: "))
    y1 = int(input("Set the first y value: "))
    x2 = int(input("Set the second x value: "))
    y2 = int(input("Set the second y value: "))

    distance = Distance(x1, y1, x2, y2)
    
    print("Distance = {:>0.2f}".format(distance.getDistance()))

    print("""
    """) 

    x1 = int(input("Reset the first x value: "))
    y1 = int(input("Reset the first y value: "))
    x2 = int(input("Reset the second x value: "))
    y2 = int(input("Reset the second y value: "))

    distance.newPoints(x1, y1, x2, y2)

    print("Distance = {:>0.2f}".format(distance.getDistance()))

main()
