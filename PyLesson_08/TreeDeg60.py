word = input("Please enter a word here: ")
stop = len(word)

def tree(word, start, stop):
    space = " " * int(stop - start/2)
    if start <= stop:
        print(space + word[0:start])
        start += 1
        tree(word, start, stop)

tree(word, 0, stop)

