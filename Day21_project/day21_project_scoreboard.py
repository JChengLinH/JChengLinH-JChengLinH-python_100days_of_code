from turtle import Turtle, fd

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.score_left = 0
        self.score_right = 0
        self.write(f"{self.score_left} : {self.score_right}", align="center", font=("Courier", 20, "normal"))
    

    def increase_score_left(self):
        self.clear()
        self.score_left += 1
        self.write(f"{self.score_left} : {self.score_right}", align="center", font=("Courier", 20, "normal"))

    def increase_score_right(self):
        self.clear()
        self.score_right += 1
        self.write(f"{self.score_left} : {self.score_right}", align="center", font=("Courier", 20, "normal"))