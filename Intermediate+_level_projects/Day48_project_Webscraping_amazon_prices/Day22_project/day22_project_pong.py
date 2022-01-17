from turtle import Turtle, circle
import random

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        #self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()

    def move(self):
        self.forward(10)
        

    def bounce_wall(self):
        self.setheading(-self.heading())

    
    def bounce_paddle(self):
        self.setheading(180 - abs(self.heading()))