class MilesPerHour:
    def __init__ (self, distance, hours, minutes):
        self.distance = distance
        self.hours = hours
        self.minutes = minutes
        self.mph = 0

    def newvars (self, distance, hours, minutes):
        self.distance = distance
        self.hours = hours
        self.minutes = minutes
        self.mph = 0

    def getHours(self):
        return self.hours
    
    def getMinutes(self):
        return self.minutes
    
    def getDistance(self):
        return self.distance
    
    def getMPH(self):
        self.mph = self.distance/(self.hours + (self.minutes/60))
        return "{:<0.2f}".format(self.mph)
def main():
    distance = int(input("Enter the distance traveled in miles: "))
    hours = int(input("Enter time in hours: "))
    minutes = int(input("Enter the minutes: "))

    speed = MilesPerHour(distance, hours, minutes)

    print(speed.getDistance(), "miles in", speed.getHours(), "miles and", speed.getMinutes(), "minutes =", speed.getMPH(), "mph.")

main()
