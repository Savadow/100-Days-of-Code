#==== Imports ====#
from modules.day_14.art import *
import random
from modules.day_14.game_data import data
from modules.clear import clear

#==== Body ====#
print(logo)
game = True
score = 0
a = random.choice(data)

#==== Function Definitions====#
def check(guess, count_1, count_2):
    """
    Takes a guess and compares the followers count
    :param guess: User's guess
    :param count_1: Question A follower count
    :param count_2: Question B follower count
    :return: True or False
    """

    if count_1 > count_2:
        return guess == "A"
    else:
        return guess == "B"


while game:
    b = random.choice(data)
    if a == b:
        b = random.choice(data)

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

    user = input("Who has more followers? Type 'A' or 'B': ").upper()
    answer = check(user, a["follower_count"], b["follower_count"])
    clear()
    print(logo)

    if answer:
        score += 1
        print(f"You're right. Current score: {score}")
        a = b
    else:
        game = False
        print(f"Sorry, that's wrong. Final score: {score}")