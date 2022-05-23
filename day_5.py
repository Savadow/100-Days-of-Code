################
#### Part 1 ####
################

# student_height = input("Input a list of student heights  ").split()

# for n in range(0, len(student_height)):
#     student_height[n] = int(student_height[n])

# count = 0
# for student in student_height:
#     count += 1

# total = 0
# for height in student_height:
#     total += height

# avg = total / count, 1
# print(avg)

################
#### Part 2 ####
################

# student_scores = input("Input a list of student scores  ").split()

# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# largest = student_scores[0]
# for score in student_scores:
#     if score > largest:
#         largest = score
# print(f"The highest score in the class is: {largest}")

################
#### Part 3 ####
################

# total = 0
# for number in range(0, 101, 2):
#     total += number
# print(total)

################
#### Part 4 ####
################

# for num in range(1,101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

##############
#### Main ####
##############

# Password Generator
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
        "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", 
        "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", 
        "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", 
        "V", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!!")

num_letters = int(input("How many letters would you like in your password\n"))
num_symbols = int(input("How many symbols would you like in your password\n"))
num_numbers = int(input("How many numbers would you like in your password\n"))

password = ""

for choice in range(num_letters):
    letter = random.choice(letters)
    password += letter

for choice in range(num_symbols):
    symbol = random.choice(symbols)
    password += symbol

for choice in range(num_numbers):
    number = random.choice(numbers)
    password += number

password_list = [i for i in password]
random.shuffle(password_list)

new_password = ""
for char in password_list:
    new_password += char
print(f"Your password is: {new_password}")