from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = Paddle((-300, 0))
r_paddle = Paddle((300, 0))

ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 30 and ball.xcor() > 250 or ball.distance(l_paddle) < 30 and ball.xcor() < -250:
        ball.bounce_x()

    if ball.xcor() > 320:
        ball.reset_position()
        score.l_point()
    elif ball.xcor() < -320:
        ball.reset_position()
        score.r_point()

screen.exitonclick()