##########
#### 1 ####
##########
# with open("modules/day_25/weather_data.csv") as weather:
#     data = weather.readlines()
#     print(data)

##########
#### 2 ####
##########
# import csv
#
# with open("modules/day_25/weather_data.csv") as weather:
#     data = csv.reader(weather)
#
#     temperatures = []
#     for row in data:
#         temp = row[1]
#         if temp == "temp":
#             continue
#         temperatures.append(int(temp))
#
#     print(temperatures)

##########
#### 3 ####
##########
# import pandas

# data = pandas.read_csv("modules/day_25/weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg = data["temp"].mean()
# print(avg)

# print(data["temp"].max())

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# cel = int(monday.temp)
# fahr = ((9 / 5) * cel) + 32
# print(fahr)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("modules/day_25/new_data.csv", index = False)

##########
#### 4 ####
##########
# data = pandas.read_csv("modules/day_25/2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# val = data["Primary Fur Color"].value_counts()
#
# new_dict = {
#     "Fur Color": list(val.index),
#     "Count": list(val.values)
# }
#
# df =  pandas.DataFrame(new_dict)
# df.to_csv("modules/day_25/squirrel_count.csv", index = False)

############
#### Main ####
############
#==== Imports ====#
import turtle
import pandas

#=== Declarations ====#
screen = turtle.Screen()
image = "modules/day_25/blank_states_img.gif"
data = pandas.read_csv("modules/day_25/50_states.csv")
guessed_state = []  # States guessed

#==== Function Definitions ====#
# def mouse_coor(x, y):
#     print(x, y)

#=== Body ====#
screen.title("Savadow's U.S. Guessing Game")
screen.addshape(image)

turtle.shape(image)

# Getting coordinates for turtle screen
# turtle.onscreenclick(mouse_coor)

while len(guessed_state) < 50:
    guess = screen.textinput(title = f"{len(guessed_state)}/50 States correct",
                             prompt = "Enter a state").title()

    if guess == "Exit":
        rem = [state for state in data["state"].values if state not in guessed_state]
        df = pandas.DataFrame({"Names": rem})
        df.to_csv("modules/day_25/states_to_learn.csv", index=False)
        break

    if guess in data["state"].values:
        guessed_state.append(guess)
        ans = turtle.Turtle()
        ans.hideturtle()
        ans.penup()
        cor = data[data["state"] == guess]
        ans.setpos(int(cor.x), int(cor.y))
        ans.write(f"{guess}", align = "center", font = ("Courier", 8, "normal"))