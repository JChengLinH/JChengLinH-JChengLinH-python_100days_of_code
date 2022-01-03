from turtle import Turtle, Screen, color, width
import random



color_list = [(237, 241, 245), (238, 246, 244), (249, 243, 247), (1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 
207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]

paint = Turtle()
paint.shape("arrow")
paint.shapesize(1, 1, 0.5)
paint.speed("fastest")
paint.hideturtle()

screen = Screen()
screen.colormode(255)
y_axis = -250
x_axis = -250
height = 10
width = 10
space = 50
while y_axis < -250 + height * space:
    paint.penup()
    paint.sety(y_axis)
    paint.setx(x_axis)

    for _ in range(10):
        paint.color(random.choice(color_list))
        paint.penup()
        paint.dot(20)
        paint.fd(50)
    y_axis += space
    


screen.exitonclick()
