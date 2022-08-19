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
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Savadow's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.location()
        snake.extend()
        score.track()

    # Detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        score.game_over()

screen.exitonclick()