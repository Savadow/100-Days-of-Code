################
#### Part 1 ####
################

# number = int(input("Enter number: "))

# if number % 2 == 0:
#     print("Number is EVEN!!")
# else:
#     print("ODD!!")

################
#### Part 2 ####
################

# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your weight in m: "))
# bmi = round(weight / height ** 2, 1)

# if bmi > 35:
#     print(f"Your bmi is {bmi} and you are Clinically Obese")
# elif bmi > 30 and bmi < 35:
#     print(f"Your bmi is {bmi} and you are Obese")
# elif bmi > 20 and bmi < 30:
#     print(f"Your bmi is {bmi} and you are Overweight")
# elif bmi > 18.5 and bmi < 25:
#     print(f"Your bmi is {bmi} and you are Normal Weight")
# else:
#     print(f"Your bmi is {bmi} and you are Underweight")

################
#### Part 3 ####
################

# year = int(input("Enter year: "))
   
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0: 
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")

################
#### Part 4 ####
################

# print("Welcome to The Pizza Deliveries")

# size = input("What size of pizza do you want? S, M, or L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# else:
#     bill = 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}")

################
#### Part 4 ####
################

# height = int(input("Enter your height: "))
# bill = 0

# if height > 120:
#     print("You can ride a rollercoaster")
#     age = int(input("Enter your age: "))
#     if age < 12:
#         bill = 5
#     elif age <= 18:
#         bill = 7
#     elif age  >= 45  and age <= 55:
#         bill = 0. 
#     else:
#         bill = 12

#     photo = input("Do you want a photo taken? Y or N: ")
#     if photo == "Y":
#         bill += 3
    
#     print(f"Your final bill is {bill}")
# else:
#     print("You can't ride a rollercoaster")

################
#### Part 5 ####
################

# print("Welcome to the Love Calculator!!")

# name = input("Enter your name: ").lower()
# partner = input("Enter your partner's name: ").lower()
# match = name + partner
# true = 0
# love = 0

# true += match.count("t")
# true += match.count("r")
# true += match.count("u")
# true += match.count("e")

# love += match.count("l")
# love += match.count("o")
# love += match.count("v")
# love += match.count("e")

# num = str(true) + str(love)
# if int(num) < 10 or int(num) > 90:
#     print(f"Your score is {num}, you go together like coke and mentos")
# elif int(num) >= 40 and int(num) <= 50:
#     print(f"Your score is {num}, you are alright together")
# else:
#     print(f"Your score is {num}")

################
#### Main ####
################

print("Welcome to Treasure Island!!\nYour mission is to find the treasure")

direction = input('Choose one of the paths before you. Type "right" or "left".\n').lower()

if direction == "left":
    path = input('You have reached a large body of water. What do you want to do? Type "swim" or "wait".\n').lower()

    if path == "wait":
        scale = input('A mountain looms ahead of you. Type "climb" or "around" to climb or go around it.\n').lower()

        if scale == "climb":
            door = input('You have been carried to the other side. This is your last challenge. Pick a door. Type "red", "yellow" or "blue".\n').lower()

            if door == "yellow":
                print("Yay!! You found the treasure. You Win!!")
            elif door == "red":
                print("The monster ate you. Game Over!!")
            elif door == "blue":
                print("The poison killed you. Game Over!!")
            else:
                print("You ran into a wall. Game Over!!")
        
        else:
            print("Your were killed by thorns. Game Over!!")

    else:
        print("You drowned. Game Over!!")

else:
    print("You walked into a sea of flames. Game Over!!")

