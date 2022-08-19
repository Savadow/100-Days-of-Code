#==== Imports ====#
from turtle import Turtle

#==== Constant Declaration ====#
ALIGNMENT = "center"
STYLE = ("Courier", 12, "normal")

#=== Body ====#
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setpos(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = STYLE)

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER!!", align=ALIGNMENT, font=STYLE)

    def track(self):
        self.score += 1
        self.clear()
        self.update()