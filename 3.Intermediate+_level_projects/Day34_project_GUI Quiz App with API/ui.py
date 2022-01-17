from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        true_image = PhotoImage(file=r"C:\python_course_projects\Day34_project_GUI Quiz App with API\images\true.png")
        false_image = PhotoImage(file=r"C:\python_course_projects\Day34_project_GUI Quiz App with API\images\false.png")
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text="", font=("Arial", 20, "italic"),width=280, fill=THEME_COLOR)
        self.true_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR, command=self.true_button)
        self.false_button = Button(image=false_image, highlightthickness=0, bg=THEME_COLOR, command=self.false_button)
        self.score_count = Label(text="Score: 0", font=("Arial", 12, "normal"), bg=THEME_COLOR, fg="white")

        self.score_count.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.false_button.grid(column=0, row=2)
        self.true_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
    

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
            self.score_count.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    
    def true_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    
    def false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, input):
        if input:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, self.get_next_question)