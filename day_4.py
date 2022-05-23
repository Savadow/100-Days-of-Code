################
#### Part 1 ####
################

# import random

# flip = random.randint(0, 1)

# if flip == 0:
#     print("Tails")
# else:
#     print("Heads")

################
#### Part 2 ####
################

# import random

# people = input("Give me everybody's name seperated by a comma and a space:\n")
# names = people.split(", ")

# index = random.randint(0, len(names) - 1)

# print(f"{names[index]} is going to buy the meal today!!")

################
#### Part 3 ####
################

# row1 = ["⬜", "⬜", "⬜"]
# row2 = ["⬜", "⬜", "⬜"]
# row3 = ["⬜", "⬜", "⬜"]
# _map = [row1, row2, row3]

# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure: ")

# column = int(position[0]) - 1
# row = int(position[1]) - 1

# _map[column][row] = "X"
# print(f"{_map[0]}\n{_map[1]}\n{_map[2]}")

##############
#### Main ####
##############
import random

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))
system = random.randint(0, 2)

print(f"You chose {user} and system chose {system}")

if (system == 0 and user == 1) or (system == 1 and user == 2) or (system == 2 and user == 0):
    print("You win")
elif system == user:
    print("Draw")
else:
    print("You lose")