s = input("Please enter a sentence here: ")

def replace(sentence, num):
    global s
    if num < len(sentence):
        if sentence[num] == " ":
            s = sentence[0: num] + "_" + sentence[num + 1: len(sentence)]
        num += 1
        replace(s, num)
    return s
print(replace(s, 0))
