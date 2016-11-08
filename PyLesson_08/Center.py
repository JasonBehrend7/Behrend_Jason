first = input("Please enter a word here: ")
second = input("Please enter another word here: ")
third = input("Please enter one last word here: ")

def makeCenter(word):
    if len(word) >= 20:
        print(word)
    else:
        makeCenter(" " + word + " ")

makeCenter(first)
makeCenter(second)
makeCenter(third)
