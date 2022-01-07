# Day 21 - The pong game

from turtle import Screen
from day21_project_paddle import Paddle
from day21_project_pong import Pong
from day21_project_scoreboard import ScoreBoard
import random
import time

START_POS = [(370, 0), (-370, 0)]
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

ball_speed = 1
paddle_1 = Paddle(START_POS[0])
paddle_2 = Paddle(START_POS[1])
pong = Pong()
refresh_speed = 0.1
score_board = ScoreBoard()
screen.listen()
screen.onkey(key = "Up", fun = paddle_1.up)
screen.onkey(key = "Down", fun = paddle_1.down)
screen.onkey(key = "w", fun = paddle_2.up)
screen.onkey(key = "s", fun = paddle_2.down)


screen.update()
game_is_on = True

pong.setheading(random.randint(0, 360))
while game_is_on:
    time.sleep(refresh_speed)
    screen.update()
    pong.move()

    #Detect wall collision
    if pong.ycor() > 290 or pong.ycor() < -290:
        pong.bounce_wall()

    #Detect collision with paddles
    if (pong.distance(paddle_1) <= 30 and pong.xcor() >= 345) or (pong.distance(paddle_2) <= 30 and pong.xcor() <= -345):
        pong.bounce_paddle()
        refresh_speed *= 0.9

    #Detect the ball passing the paddles
    if pong.xcor() > 400:
        score_board.increase_score_left()
        refresh_speed = 0.1
        pong.home()
        pong.setheading(random.randint(0, 360))
    elif pong.xcor() < -400:
        score_board.increase_score_right()
        refresh_speed = 0.1
        pong.home()
        pong.setheading(random.randint(0, 360))

screen.exitonclick()