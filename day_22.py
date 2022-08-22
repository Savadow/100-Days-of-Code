#==== Imports ====#
from turtle import Screen
from modules.pong import Paddle, Ball, Scoreboard
import time

#==== Initialization ====#
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Savadow's Pong Game")
# screen.delay(0)
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
score = Scoreboard()

#==== Body ====#
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game = True
while game:
    time.sleep(ball.play_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50
                                                                and ball.xcor() < -340):
        ball.paddle_bounce()

    # Detect ball out of bounds and scoring
    if ball.xcor() > 390:
        ball.reset_pos()
        score.l_track()

    if ball.xcor() < -390:
        ball.reset_pos()
        score.r_track()

screen.exitonclick()