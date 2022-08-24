#==== Imports ====#
from turtle import Turtle
import random

#==== Constant Declaration ====#
POS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
ALIGNMENT = "center"
STYLE = ("Courier", 12, "normal")

#=== Body ====#
class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
       for segment in POS:
            self.add_segment(segment)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.setpos(position)
        self.segments.append(snake)

    def reset(self):
        self.segments.clear()
        self.create()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Move snake forwards
        """

        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[segment_num - 1].pos()
            self.segments[segment_num].goto(new_pos)

        self.head.forward(DISTANCE)

    def up(self):
        """
        Move snake up
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Move snake up
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Move snake up
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Move snake up
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


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


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_data.txt") as data:
            self.high_score = int(data.read())
        self.increment = 1
        self.color("white")
        self.penup()
        self.y = 270
        self.setpos(0, self.y)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = STYLE)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update()

    def track(self):
        self.score += self.increment
        self.update()

    def leaderboard(self, file, name, difficulty):
        with open(file, "a") as f:
            f.write(f"\n{name},{difficulty},{self.score}")