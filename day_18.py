##############
#### Part 1 ####
##############

# from turtle import Turtle, Screen
#
# crinky = Turtle()
# crinky.shape("turtle")
# crinky.color("DarkSlateGray")
# crinky.forward(100)
# crinky.right(90)
# crinky.forward(100)
# crinky.right(90)
# crinky.forward(100)
# crinky.right(90)
# crinky.forward(100)
#
# screen = Screen()
# screen.exitonclick()

##############
#### Part 2 ####
##############

# from turtle import Turtle, Screen
#
# crinky = Turtle()
#
# n = 0
# while n  < 15:
#     crinky.forward(10)
#     crinky.penup()
#     crinky.forward(10)
#     crinky.pendown()
#     n += 1
#
# screen = Screen()
# screen.exitonclick()

##############
#### Part 3 ####
##############

# from turtle import Turtle, Screen
# import random
#
# crinky = Turtle()
#
# n = 3
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
#            "wheat", "SlateGray", "SeaGreen"]
#
# while n <= 10:
#     crinky.color(random.choice(colours))
#     for _ in range(n):
#         crinky.forward(100)
#         crinky.right(360 / n)
#     n += 1
#
# screen = Screen()
# screen.exitonclick()

##############
#### Part 4 ####
##############

# import turtle
# import random
#
# turtle.colormode(255)
# crinky = turtle.Turtle()
# # crinky.pensize(16)  # this can be uncommented if you want a bigger feel
# crinky.speed("fastest")
#
# path = [0, 90, 180, 270]
#
# def pick_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
#
# for _ in range(512):
#     crinky.color(pick_color())
#     crinky.forward(32)
#     crinky.setheading(random.choice(path))
#
# screen = turtle.Screen()
# screen.exitonclick()

##############
#### Part 4 ####
##############

# import turtle
# import random
#
# turtle.colormode(255)
# crinky = turtle.Turtle()
# crinky.speed("fastest")
#
# def pick_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
#
# def spirograph(size):
#     for _ in range(int(360 / size)):
#         crinky.color(pick_color())
#         crinky.circle(100)
#         crinky.setheading(crinky.heading() + size)
#
# spirograph(4)
#
# screen = turtle.Screen()
# screen.exitonclick()