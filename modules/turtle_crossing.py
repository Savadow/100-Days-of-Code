#==== Imports ====#
from turtle import Turtle
import random

#==== Constant Declarations ====#
# CarManager
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Player
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Scoreboard
FONT = ("Courier", 16, "normal")

class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        creation = random.randint(1, 6)
        if creation == 1:
            car = Turtle(shape = "square")
            car.shapesize(stretch_wid = 1, stretch_len = 2)
            car.penup()
            car.color(random.choice(COLORS))
            ycor = random.randint(-250, 250)
            car.goto(300, ycor)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.back(self.car_speed)

    def increase(self):
        self.car_speed += MOVE_INCREMENT

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("pink")
        self.penup()
        self.level_up()
        self.finish = FINISH_LINE_Y

    def level_up(self):
        self.setpos(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("pink")
        self.penup()
        self.setpos(-290, 260)
        self.level = 1
        self.score()

    def score(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "left", font = FONT)

    def update(self):
        self.level += 1
        self.score()

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER!!", align = "center", font = FONT)