from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    language_data = pd.read_csv(r"C:\python_course_projects\Day31_flash_card_app_capstone_project\data\words_to_learn.csv")
except FileNotFoundError:
    language_data = pd.read_csv(r"C:\python_course_projects\Day31_flash_card_app_capstone_project\data\french_words.csv")
finally:
    language_data_dict = language_data.to_dict(orient="records")

def remove_learnt_words():
    global language_data_dict, language_data
    try:
        language_data = language_data.drop(language_data[language_data.French == random_word["French"]].index)
        language_data_dict = language_data.to_dict(orient="records")
        language_data.to_csv(r"C:\python_course_projects\Day31_flash_card_app_capstone_project\data\words_to_learn.csv", index=False)
    except NameError:
        print("No More Words to Learn.")


def next_card():
    global random_word, timer
    if len(language_data_dict) > 0:
        window.after_cancel(timer)
        random_word = random.choice(language_data_dict)
        canvas.itemconfig(card_image, image=front_image)
        canvas.itemconfig(language, text="French", fill="black")
        canvas.itemconfig(word, text=random_word["French"], fill="black")
        timer = window.after(3000, func=flip)
    else:
        window.after_cancel(timer)
        canvas.itemconfig(card_image, image=front_image)
        canvas.itemconfig(language, text="No More Words to Learn.", fill="black")

def flip():
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=random_word["English"], fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Images
front_image = PhotoImage(file=r"C:\python_course_projects\Day31_flash_card_app_capstone_project\images\card_front.png")
back_image = PhotoImage(file=r"C:\python_course_projects\Day31_flash_card_app_capstone_project\images\card_back.png")
check_image = PhotoImage(file=r"C:\python_course_projects\Day31_flash_card_app_capstone_project\images\right.png")
cross_image = PhotoImage(file=r"C:\python_course_projects\Day31_flash_card_app_capstone_project\images\wrong.png")

#Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=front_image)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), tag="language")
word = canvas.create_text(400, 300, text= "", font=("Arial", 60, "bold"), tag="word")


#Buttons
check_button = Button(image=check_image, highlightthickness=0, command=lambda:[remove_learnt_words(), next_card()])
cross_button = Button(image=cross_image,highlightthickness=0, command=next_card)

#Layout
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)
cross_button.grid(column=0, row=3)
check_button.grid(column=1, row=3)
timer = window.after(3000, flip)
next_card()





window.mainloop()