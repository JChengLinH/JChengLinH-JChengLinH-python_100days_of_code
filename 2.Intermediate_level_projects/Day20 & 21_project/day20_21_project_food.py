# Spawning the food object at random places in the frame.

from turtle import Turtle, shape
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.goto(random.randint(-250, 250), random.randint(-250, 250))

    def respawn(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))