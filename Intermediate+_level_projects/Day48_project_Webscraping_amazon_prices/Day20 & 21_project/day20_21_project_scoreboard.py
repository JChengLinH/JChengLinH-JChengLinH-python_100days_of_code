# Display the scoreboard and update it.

from turtle import Turtle, mode
ALIGNMENT = "center"
FONT_SCORE = ("Courier", 12, "normal")
FONT_END_GAME = ("Courier", 16, "normal")

class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        with open(r"C:\python_course_projects\Day20 & 21_project\high_score.txt") as score_file:
            self.high_score = int(score_file.read())
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
        self.write(f"Score: {self.score}. High Score: {self.high_score}", align=ALIGNMENT, font=FONT_SCORE)

    
    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"C:\python_course_projects\Day20 & 21_project\high_score.txt", mode="w") as score_file:
                score_file.write(str(self.high_score))

        self.score = 0
        self.write(f"Score: {self.score}. High Score: {self.high_score}", align=ALIGNMENT, font=FONT_SCORE)
    
    def end_game(self):
        self.color("white")
        self.penup()
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_END_GAME)