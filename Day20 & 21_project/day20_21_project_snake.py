# Creates the logics associated with the snake.

from turtle import Turtle

START_X_POS = 0
START_Y_POS = 0
STARTING_SIZE = 3
STARTING_POS = []
STARTING_POS.append((0, 0))

for n in range(STARTING_SIZE - 1):
    START_X_POS -= 20
    START_Y_POS = 0
    STARTING_POS.append((START_X_POS, START_Y_POS))

class Snake:
    def __init__(self):
        self.snake_segment_list = []
        self.create_snake()
        self.head = self.snake_segment_list[0]


    def create_snake(self):
        for _ in range(STARTING_SIZE):
            self.snake_segment_list.append(Turtle(shape="square"))
            self.snake_segment_list[_].penup()
            self.snake_segment_list[_].color("white")
            self.snake_segment_list[_].goto(STARTING_POS[_])


    def move(self):
        for seg_num in range(len(self.snake_segment_list) - 1 , 0, -1):
            self.new_position = self.snake_segment_list[seg_num - 1].position()
            self.snake_segment_list[seg_num].goto(self.new_position)

        self.head.forward(20)


    def reset(self):
        for segment in self.snake_segment_list:
            segment.goto(1000,1000)
        self.snake_segment_list.clear()
        self.create_snake()
        self.head = self.snake_segment_list[0]
        

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)


    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)  


    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)  


    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)  


    def grow(self):
        self.snake_segment_list.append(Turtle(shape="square"))
        self.snake_segment_list[-1].penup()
        self.snake_segment_list[-1].color("white")
        for seg_num in range(len(self.snake_segment_list) - 1 , 0, -1):
            self.new_position = self.snake_segment_list[seg_num - 1].position()
            self.snake_segment_list[seg_num].goto(self.new_position)