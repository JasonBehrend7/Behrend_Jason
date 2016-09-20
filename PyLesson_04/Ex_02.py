def card(name, lname, title, school, year, subject):

    print("****************************")
    print("* {:<12}{:>12} *".format(school, year))
    print("* {:<12}{:>12} *".format(name, lname))
    print("* {:<12}{:>12} *".format(title, subject))
    print("****************************")

name = input("Enter your first name: ")
lname = input("Enter your last name: ")
title = input("Enter your title: ")
school = input("Enter the school: ")
year = input("Enter the school year: ")
subject = input("Enter your subject: ")

card(name, lname, title, school, year, subject)
