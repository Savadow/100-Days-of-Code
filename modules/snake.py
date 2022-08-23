#==== Imports ====#
from turtle import Turtle

#==== Constant Declaration ====#
POS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

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