import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

speed = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

turtle = Player()
screen.listen()
screen.onkey(turtle.move, "Up")
score_board = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    #Turtle reaches final line
    if turtle.ycor() > 280:
        turtle.reset()
        score_board.increase_level()
        car_manager.increase_speed()
    
    #If turtle got hit by car
    if car_manager.collision_detection(turtle):
        score_board.game_over()
        game_is_on = False


screen.exitonclick()

