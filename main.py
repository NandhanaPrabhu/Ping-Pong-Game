from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')

screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when r_paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    # Detect when l_paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()


screen.exitonclick()
