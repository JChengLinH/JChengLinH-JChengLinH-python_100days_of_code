from turtle import Turtle, Screen, up
import time



UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.segment_y_position = 20
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.setheading(UP)
        self.penup()
        self.goto(position)
        

    def up(self):
        self.setheading(UP)
        self.forward(20)
        

    def down(self):
        self.setheading(DOWN)
        self.forward(20)