import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG!")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.accel)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    if ball.distance(r_paddle) > 50 and ball.xcor() > 380:
        scoreboard.l_point()
        ball.refresh()
    elif ball.distance(l_paddle) > 50 and ball.xcor() < -380:
        scoreboard.r_point()
        ball.refresh()

screen.exitonclick()
