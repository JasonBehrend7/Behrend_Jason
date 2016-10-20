i = 0
def printf(word, number):
    print("{:10}{:10.3f}".format(word, number))

word = input("Type in a word here: ")
number = float(input("Type in a number with a decimal here: "))

printf(word, number)

times = int(input("How many times would you like to do this: "))

while times >= i:
    print("")
    word = input("Type in a word here again: ")
    number = float(input("Type in a number with a decimal here again: "))

    printf(word, number)

