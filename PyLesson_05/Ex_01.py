import random

playerRoll = random.randint(1,6)
compRoll = random.randint(1,6)

def rollDice():
    global playerRoll, compRoll
    print("You rolled a", playerRoll)
    print("The computer rolled a", compRoll)
    if playerRoll > compRoll:
        print("You Won!")

    elif playerRoll < compRoll:
        print("You lost.")

    else:
        print("It's a tie")

rollDice()
