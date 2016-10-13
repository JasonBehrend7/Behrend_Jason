choice = input("Do you want to go on an adventure? ")
a = "Yes"
if choice == a:
    where = input("Do you want to go to the mountains? ")
    if where == a:
        mountain = input("Which mountain do you want to go to? ")
        if mountain == "Mammoth":
            print("Alright! That's my favorite mountain! Lets Go!")
        else:
            print("That's not the best, but I guess we can go.")
    else:
        where = input("Than where do you want to go? ")
        if where == "A cruise":
            print("That's the second best option!")
        else:
            print("You're bad at adventures, but lets go.")
else:
    positive = input("Are you sure you don't want to go on a trip? ")
    if positive == a:
        cmon = input("C'mon... It will be fun. ")
        if cmon == "Fine":
            print("YES! It will be so much fun!")
        else:
            print("BOO!")
    else:
        where = input("Yes! Where? ")
        if where == "Mammoth":
            print("YES! Lets Go!")
        else:
            print("Sounds fun!")
