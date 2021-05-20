import random
number=random.randint(0,9)
chances=0
guess=0
while chances < 5:
        if guess == number:
                print("Congrats")
                break
        if not chances < 5:
                print("you have lost the game!, :(", number)


