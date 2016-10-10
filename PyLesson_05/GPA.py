math = input("Enter your letter grade for math(Upper Case): ")
english = input("Enter your letter grade for english(Upper Case): ")
PE = input("Enter your letter grade for PE(Upper Case): ")
bio = input("Enter your letter grade for bio(Upper Case): ")
compPro = input("Enter your letter grade for computer programming(Upper Case): ")
spanish = input("Enter your letter grade for spanish(Upper Case): ")
videoFilm = input("Enter your letter grade for video film(Upper Case): ")

gpa = 0

def calcPoints(sub):
    global gpa
    
    if sub == "A":
        sub = 4.0
    elif sub == "B":
        sub = 3.0
    elif sub == "C":
        sub = 2.0
    elif sub == "D":
        sub = 1.0
    elif sub == "F":
        sub = 0.0
    gpa += sub

def Print():
    global gpa

    gpa = gpa/7
    
    print("Your gpa is {:0.1f}".format(gpa))

calcPoints(math)
calcPoints(english)
calcPoints(PE)
calcPoints(bio)
calcPoints(compPro)
calcPoints(spanish)
calcPoints(videoFilm)

Print()
