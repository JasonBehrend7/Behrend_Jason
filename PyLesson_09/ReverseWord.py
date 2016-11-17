words = ["Word", "Baseball", "Sports", "Python", "Swift"]

print("In order...")
for i in words:
    print(i)
print("")

def reverse(list):
    length = len(list) - 1
    for i in range(length, -1, -1):
        print(list[i])

reverse(words)
