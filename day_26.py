##########
#### 1 ####
##########
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)

##########
#### 2 ####
##########
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

##########
#### 3 ####
##########
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split(" ")
# result = {word:len(word) for word in words}
# print(result)

##########
#### 4 ####
##########
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
#
# weather_f = {day:(temp * 9 / 5) + 32 for day, temp in weather_c.items()}
# print(weather_f)

##########
#### 5 ####
##########
# import pandas
#
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# student_df = pandas.DataFrame(student_dict)
# print(student_df)
#
# for index, row in student_df.iterrows():
#     print(row.student)

############
#### Main ####
############
#==== Imports ====#
import pandas

#==== Declarations ====#
data = pandas.read_csv("modules/day_26/nato_phonetic_alphabet.csv")
word = input("Enter a word: ").upper()

#==== Body ====#
data_dict = {row.letter: row.code for index, row in data.iterrows()}
code_list = [data_dict[letter] for letter in word]
print(code_list)