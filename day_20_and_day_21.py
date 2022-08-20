############
#### Main ####
############

#==== Imports ====#
from turtle import Screen
from modules.snake import Snake
from modules.food import Food
from modules.scoreboard import Score
import time

#==== Body ====#
FiLE = "leaderboard.csv"

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Savadow's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

name = screen.textinput(title="Name",
                             prompt="Enter your name:  ")

level = screen.textinput(title="Difficulty",
                             prompt="Choose a difficulty(easy/medium/hard): ")

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True

while game:
    screen.update()

    if level == "easy":
        time.sleep(0.5)
        score.increment = 5

    elif level == "medium":
        time.sleep(0.3)
        score.increment = 3

    elif level == "hard":
        time.sleep(0.1)

    else:
        screen.clearscreen()

    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.location()
        snake.extend()
        score.track()

    # Detecting collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 \
            or snake.head.ycor() < -290:
        game = False
        score.game_over()
        score.leaderboard(file = FiLE, name = name, difficulty = level)

    # Detecting collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game = False
            score.game_over()
            score.leaderboard(file=FiLE, name=name, difficulty=level)

screen.exitonclick()