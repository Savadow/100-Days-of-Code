################
#### Part 1 ####
################

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# student_grades = {}

# for student in student_scores:
#     if student_scores[student] > 90:
#         student_grades[student] = "Outstanding"
#     elif student_scores[student] > 80:
#         student_grades[student] = "Exceeds Expectation"
#     elif student_scores[student] > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print(student_grades)

################
#### Part 2 ####
################

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     }, 
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     }
# ]

# def add_new_country(country, visits, cities):
#     travel_log.append({"country": country, "visits": visits, "cities": cities})

# add_new_country("Russia", 2, ["Moscow, Saint Petersburg"])
# print(travel_log)

##############
#### Main ####
##############

from modules.clear import clear

print("Welcome to the secret auction program")
blind_auction = {}

bid = True
while bid:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    blind_auction[name] = price

    ask = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if ask == "no":
        bid = False
    else:
        clear()

highest = 0
winner = ""
for player in blind_auction:
    i = blind_auction[player]
    if i > highest:
        highest = i
        winner = player

print(f"The winner is {winner} with a bid of ${highest}")