height = int(input("Please enter your height in inches here: "))
weight = int(input("Please enter your weight here: "))
bmi = (weight / (height * height)) * 703

def calcBMI():
    global bmi
    bmi = ("{:0.2f}".format(bmi))
    if float(bmi) < 18.5:
        print("Your BMI is", bmi, "which is underweight")
    elif float(bmi) <= 24.9:
        print("Your BMI is", bmi, "which is normal")
    elif float(bmi) <= 29.9:
        print("Your BMI is", bmi, "which is overweight")
    elif float(bmi) <= 34.9:
        print("Your BMI is", bmi, "which is obese")
    elif float(bmi) <= 39.9:
        print("Your BMI is", bmi, "which is very 0bese")
    else:
        print("Your BMI is", bmi, "which is morbidly obese")

calcBMI()
