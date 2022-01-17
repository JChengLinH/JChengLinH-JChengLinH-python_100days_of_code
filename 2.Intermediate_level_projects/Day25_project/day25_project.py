import turtle
import pandas as pd
from pandas.core.dtypes import missing
PIC_PATH = r"C:\python_course_projects\Day25_project\blank_states_img.gif"
DATA_PATH = r"C:\python_course_projects\Day25_project\50_states.csv"
SAVING_PATH = r"C:\python_course_projects\Day25_project\missing_states.csv"

data = pd.read_csv(DATA_PATH)

screen = turtle.Screen()
screen.title("US States Game")
screen.bgcolor("black")
screen.bgpic(PIC_PATH)
total_states = len(data)
score = 0

guessed_states = []
game_is_on = True
while game_is_on:
    user_input = screen.textinput(title=f"{score}/{total_states} States Correct", prompt="What's another state's name? ").title()
    state_list = data.state.to_list()

    #Increase the score with each correct guess and display the correct guess on the map.
    if user_input in state_list:
        score += 1
        guessed_states.append(user_input)
        x_cor = int(data[data.state == user_input].x)
        y_cor = int(data[data.state == user_input].y)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x_cor, y_cor)
        turtle.write(user_input, align="center", font=("Arial", 8, "bold"))

    #Exit the game when the input is "exit" and saves the states which were not guessed by the player into a csv file.
    elif user_input == "Exit":
        not_guessed_states = [state for state in state_list if state not in guessed_states]
        missing_states = {"Missing States": not_guessed_states}
        df_missing_states = pd.DataFrame(missing_states)
        df_missing_states.to_csv(SAVING_PATH)
        game_is_on = False

    #Display the winning text when the player has answered all the states names correctly.
    if score == total_states:
        turtle.hideturtle()
        turtle.home()
        turtle.write("You've won!", align="center", font=("Courier", 20, "normal"))
        game_is_on = False
        screen.exitonclick()
