def card(first, second):
    
    print("* {:<12}{:>12} *".format(first, second))
    
name = input("Enter your first name: ")
lname = input("Enter your last name: ")
title = input("Enter your title: ")
school = input("Enter the school: ")
year = input("Enter the school year: ")
subject = input("Enter your subject: ")

print("****************************")
card(year, school)
card(name, lname)
card(title, subject)
print("****************************")
