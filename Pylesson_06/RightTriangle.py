word = input("Please type in your word here: ")
num = len(word)

for i in range(0, num + 1):
    print(word[num:len(word)])
    num -= 1
