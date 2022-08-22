# ==== Imports ====#
from turtle import Turtle

# === Body ====#
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        # self.setheading(90)
        # self.shapesize(stretch_len=5)
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.color("white")
        self.penup()
        self.setpos(position)

    def up(self):
        ycor = self.ycor() + 20
        self.goto(self.xcor(), ycor)
        # self.forward(20)

    def down(self):
        ycor = self.ycor() - 20
        self.goto(self.xcor(), ycor)
        # self.back(20)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_increment = 10
        self.y_increment = 10

    def move(self):
        xcor = self.xcor() + self.x_increment
        ycor = self.ycor() + self.y_increment
        self.goto(x = xcor, y = ycor)

    def wall_bounce(self):
        self.y_increment *= -1

    def paddle_bounce(self):
        self.x_increment *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.paddle_bounce()