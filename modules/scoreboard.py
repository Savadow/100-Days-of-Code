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
        self.increment = 1
        self.color("white")
        self.penup()
        self.y = 270
        self.setpos(0, self.y)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = STYLE)

    def game_over(self, name, difficulty):
        self.setpos(0, 0)
        self.write("GAME OVER!!", align=ALIGNMENT, font=STYLE)
        print(f"\n{name}\t{difficulty}\t{self.score}")

    def track(self):
        self.score += self.increment
        self.clear()
        self.update()

    def leaderboard(self, file, name, difficulty):
        with open(file, "a") as f:
            f.write(f"\n{name},{difficulty},{self.score}")