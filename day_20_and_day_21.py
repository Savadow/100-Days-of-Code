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
FILE = "leaderboard.csv"

screen = Screen()
# screen.setup(width = 600, height = 600)
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
    height = screen.window_height()
    width = screen.window_width()
    xcor = ((width / 2) - 10)
    ycor = ((height / 2) - 10)
    score.y = ycor - 10
    food.x = [((width // 2) - 20) * -1, ((width // 2) - 10)]
    food.y = [((height // 2) - 20) * -1, ((height // 2) - 10)]
    screen.update()

    if level == "easy":
        time.sleep(0.5)
        score.increment = 3

    elif level == "medium":
        time.sleep(0.3)
        score.increment = 2

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
    if snake.head.xcor() > xcor or snake.head.xcor() < (xcor * -1) or snake.head.ycor() > ycor \
            or snake.head.ycor() < (ycor * -1):
        game = False
        score.game_over()
        score.leaderboard(file = FILE, name = name, difficulty = level)

    # Detecting collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game = False
            score.game_over()
            score.leaderboard(file=FILE, name=name, difficulty=level)

screen.exitonclick()