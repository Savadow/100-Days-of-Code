############
#### Main ####
############

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. ")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
number = random.randint(1, 100)
attempt = 0

if difficulty == "easy":
    attempt += 10
    warning = f"You have {attempt} attempts remaining to guess"
    print(warning)

    play = True
    while play:
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high. \n Guess again.")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess")

        elif guess < number:
            print("Too low. \n Guess again.")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess")

        else:
            print(f"You got it. The answer was {number}")