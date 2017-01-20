import random

class User:
    def __init__(self, fName, lName, avat = ""):
        self.firstName = fName
        self.lastName = lName
        self.avatar = avat
        self.userID = random.randint(0, 1000000)

    def changeAvat(self, avat):
        self.avatar = avat

    def getFName(self):
        return self.fName

    def getLName(self):
        return self.lName

    def getAvat(self):
        return self.avatar

    def getID(self):
        return self.userID

    def __str__(self):
        if self.avatar == "":
            return "Customer Info:\nFirst Name: " + self.firstName +  "\nLast Name: " + self.lastName +  "\nAvatar: " + "None" + "\nUser ID#: " + str(self.userID)
        else:
            return "Customer Info:\nFirst Name: " + self.firstName +  "\nLast Name: " + self.lastName +  "\nAvatar: " + self.avatar + "\nUser ID#: " + str(self.userID)
        

def main():
    fName = input("Please enter your first name: ")
    lName = input("Please enter your last name: ")
    question = input("Do you want a public avatar name(Y or N)? ")
    if question == "Y":    
        avat = input("Please enter your avatar name: ")
        user1 = User(fName, lName, avat)
    else:
        user1 = User(fName, lName)

    print(user1.__str__())

main()
