from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

#############
#### Part 2 ####
#############

# def move_forward():
#     turtle.forward(10)
#
# screen.listen()
# screen.onkey(key = "space", fun  = move_forward)
#
# screen.exitonclick()

#############
#### Part 2 ####
#############

# def move_forwards():
#     turtle.forward(10)
#
# def move_backwards():
#     turtle.backward(10)
#
# def move_right():
#     turtle.right(10)
#
# def move_left():
#     turtle.left(10)
#
# def clear_screen():
#     turtle.reset()
#
# screen.listen()
#
# screen.onkey(key = "w", fun  = move_forwards)
# screen.onkey(key = "s", fun  = move_backwards)
# screen.onkey(key = "a", fun  = move_left)
# screen.onkey(key = "d", fun  = move_right)
# screen.onkey(key = "c", fun  = clear_screen)
#
# screen.exitonclick()

############
#### Main ####
############

screen.setup(width = 500, height = 400)

race = False
bet = screen.textinput(title = "Make your bet", prompt = "Enter color of turtle to win race: ")
print(bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
pos = -75
turtles = []

for idx in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[idx])
    turtle.penup()
    turtle.goto(x=-240, y=pos)
    turtles.append(turtle)
    pos += 25

if bet:
    race = True

while race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race = False

            winner = turtle.pencolor()
            if winner == bet:
                print(f"You've won! The {winner} turtle is the winner.")
            else:
                print(f"You've lost! The {winner} turtle is the winner.")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()