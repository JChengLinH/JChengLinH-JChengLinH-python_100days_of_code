# Day 20 - Snake Game with Python Turtle Graphics

from turtle import Screen
from day20_21_project_snake import Snake
from day20_21_project_food import Food
from day20_21_project_scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

game_is_on = True
scoreboard = ScoreBoard()
segment_positions = []
while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with tail.
    for part in snake.snake_segment_list[1:]:
        if snake.head.distance(part) < 5:
            scoreboard.reset()
            snake.reset()
            
    # Detect collision with food.
    if snake.head.distance(food) < 13:
        scoreboard.increase_score()
        scoreboard.scoreboard_update()
        snake.grow()
        food.respawn()
    
    # Detect collision with walls.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
    
    

screen.exitonclick()