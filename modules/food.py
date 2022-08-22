#==== Imports ====#
from turtle import Turtle
import random

#=== Body ====#
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        self.x = [-280, 280]
        self.y = [-280, 280]
        self.location()

    def location(self):
        """
        Move food to new location
        """
        x = random.randint(self.x[0], self.x[1])
        y = random.randint(self.y[0], self.y[1])
        self.goto(x, y)