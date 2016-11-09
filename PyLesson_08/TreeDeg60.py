word = input("Please enter a word here: ")
stop = len(word)

def tree(word, start, stop):
    space = " " * (stop - start)
    if start <= stop:
        print(space + word[0:start])
        start += 1
        tree(word, start, stop)

tree(word, 0, stop)

