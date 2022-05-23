##############
#### Main ####
##############

import random

# Words to choose from
words = ["aardvark", "baboon", "camel"]
# List to hold all the "_" and then letters
display = []

# Variable declaration
chosen_word = random.choice(words)
print(f"Chosen word is {chosen_word}")

# Adding "_" to the list
for _ in range(len(chosen_word)):
    display.append("_")

# Allowing the user to keep guessing until they win or they lose
while "_" in display:
    guess = input("Guess a letter: ").lower()

    # Check for match between guess and chosen_word and appending correct answer to list
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess
        # else:
        #     print(display)

    print(display)

print("You Win!!")