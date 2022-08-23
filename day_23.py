from turtle import Screen
import time
from modules.turtle_crossing import CarManager, Player, Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.title("Savadow's Turtle Crossing Game")
screen.bgcolor("black")
screen.tracer(0)

obstacle = CarManager()
turtle = Player()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.up, "Up")

game = True
while game:
    time.sleep(0.1)
    screen.update()

    obstacle.create()
    obstacle.move()

    # Detect collision with car
    for car in obstacle.cars:
        if car.distance(turtle) < 20:
             score.game_over()
             game = False

    # Detect finish line
    if turtle.ycor() > turtle.finish:
        turtle.level_up()
        score.update()
        obstacle.increase()


screen.exitonclick()