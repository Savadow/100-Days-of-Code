################
#### Part 1 ####
################

# num = str(input("Enter a two digit number\n"))

# ans = int(num[0]) + int(num[1])
# print(ans)

################
#### Part 2 ####
################

# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your weight in m: "))

# bmi = weight / height ** 2
# print(int(bmi))

################
#### Part 3 ####
################

# age = int(input("What is your current age?: "))

# rem_age = 90 - age
# days = rem_age * 365
# weeks = rem_age * 52
# months = rem_age * 12

# print(f"You have {days} days, {weeks} weeks, and {months} months left")

##############
#### Main ####
##############

print("Welcome to the Tip Calculator.")

bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
percent = float(input("What percentage tip would you like to give? "))

person = bill / people
increase = (percent / 100) * person
tip = person + increase

print(f"Each person should pay: ${round(tip, 1)}")