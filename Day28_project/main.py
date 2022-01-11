#Pomodoro timer app
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
symbol = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_button_func():
    global reps
    window.after_cancel(timer)
    canvas.itemconfigure(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN, bg=YELLOW)
    check_mark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_button_func():
    global reps
    reps += 1
    if reps % 8 == 0:
        label.config(text="Break", fg=RED, bg=YELLOW)
        count_down(LONG_BREAK_MIN * 60)

    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK, bg=YELLOW)
        count_down(SHORT_BREAK_MIN * 60)

    else:
        label.config(text="Work", fg=GREEN, bg=YELLOW)
        count_down(WORK_MIN * 60)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global symbol, timer
    count_min = round(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
 

    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    else:
        if reps % 2 != 0:
            symbol += "✔"
            check_mark.config(text=symbol, fg=GREEN, bg=YELLOW)

        start_button_func()
        


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

empty_label = Label(text="")
empty_label.grid(column=0, row=0)

label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic= PhotoImage(file = r"C:\python_course_projects\Day28_project\tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(100, 130, text="00:00",font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)


start_button = Button(text="Start", font=("Arial", 8, "bold"), command=start_button_func)
start_button.grid(column=0, row=3)

check_mark = Label(font=("Arial", 20, "bold"), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

reset_button = Button(text="Reset", font=("Arial", 8, "bold"), command=reset_button_func)
reset_button.grid(column=3, row=3)


window.mainloop()