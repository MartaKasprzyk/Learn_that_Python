import random


def guess():
    """picks a random number and asks user to guess it"""
    guessed = False
    x = random.randint(1, 100)
    while not guessed:
        try:
            n = int(input("Guess the number: "))
            if type(n) is not int:
                print("It's not a number!")
            elif n < x:
                print("Too small!")
            elif n > x:
                print("Too big!")
            elif n == x:
                guessed = True
                return "You win!"
        except ValueError:
            print("Please input integer only!")


print(guess())