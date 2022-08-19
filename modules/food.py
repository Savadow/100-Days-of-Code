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
        self.location()

    def location(self):
        """
        Move food to new location
        """
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)