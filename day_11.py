##############
#### Main ####
##############

import random
from modules.clear import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_hand(cards):
    """"
    Returns a random card from the deck
    """
    game = []

    game.append([random.choice(cards), random.choice(cards)])
    game.append([random.choice(cards), random.choice(cards)])
    return game

def score(cards):
    """
    Return a total sum of cards from a list a cards.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def check(player_score, computer_score):
    """
    Returns a remark based on player's score and computer's score.
    """
    if player_score == computer_score:
        return "Draw 😪"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack 🤧"
    elif player_score == 0:
        return "You win with Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 🤩"
    elif player_score > computer_score:
        return "You win 😉"
    else:
        return "You lose 😥"

def BlackJack():
    """
    A game of Blackjack
    """
    user = deal_hand(cards)[0]
    system = deal_hand(cards)[1]
    game_over = False

    while not game_over:
        user_score = score(user)
        system_score = score(system)

        print(f"    Your cards are: {user}.  Your score: {user_score}")
        print(f"    Computer's first card is {system[0]}")

        if user_score == 0 or system_score == 0 or user_score > 21:
            game_over = True
        else:
            deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if deal == "y":
                user.append(deal_hand(cards)[0][0])
                print(user)
            else:
                game_over = True

    while system_score != 0 and system_score < 17:
        system.append(deal_hand(cards)[1][0])
        system_score = score(system)

    print(f"    Your final hand is {user} with a score {user_score}")
    print(f"    Computer's final hand is {system} with a score {system_score}")
    print(check(user_score, system_score))

while input("Do you want to play a game of Blackjack. Type 'y' or 'n':  ").lower() == "y":
    clear()
    BlackJack()