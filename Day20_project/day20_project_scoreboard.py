# Display the scoreboard and update it.

from turtle import Turtle
ALIGNMENT = "center"
FONT_SCORE = ("Courier", 12, "normal")
FONT_END_GAME = ("Courier", 16, "normal")

class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, 270)
        self.scoreboard_update()


    def increase_score(self):
        self.clear()
        self.score += 1


    def scoreboard_update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT_SCORE)

    
    def end_game(self):
        self.color("white")
        self.penup()
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_END_GAME)