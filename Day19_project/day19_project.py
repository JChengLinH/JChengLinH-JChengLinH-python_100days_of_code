## Day 19 project - Turtle race

from turtle import Turtle, Screen
import random

screen = Screen()
screen.title("Turtle Race")
screen.setup(width = 500, height = 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
print(user_bet)

y_coord = -100
turtles_list = []
for turtle_index in range(6):
    y_coord += 35
    turtles_list.append(Turtle(shape = "turtle"))
    turtles_list[turtle_index].color(colors[turtle_index])
    turtles_list[turtle_index].penup()
    turtles_list[turtle_index].goto(x = -240, y = y_coord)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() <= 230:
            step_size = random.randint(0, 10)
            turtle.fd(step_size)
        else:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've Lost! The {winning_turtle} turtle is the winner!")
            
screen.exitonclick()
