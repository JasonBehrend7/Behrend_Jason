def card(name, lname, title, school, year, subject):

    print("**********************************")
    print("* {:>15}{:>15} *".format(school, year))
    print("* {:>15}{:>15} *".format(name, lname))
    print("* {:>15}{:>15} *".format(title, subject))
    print("**********************************")

name = input("Enter your first name: ")
lname = input("Enter your last name: ")
title = input("Enter your title: ")
school = input("Enter the school: ")
year = input("Enter the chool year: ")
subject = input("Enter your subject: ")

card(name, lname, title, school, year, subject)
