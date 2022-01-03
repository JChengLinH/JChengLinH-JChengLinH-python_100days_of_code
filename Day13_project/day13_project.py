import os
import day13_project_art as art
from day13_project_data import data
import random
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()



def compare():
    """Comparing the follower's count of the user's choice to the other alternative.\n
    Returns True or False."""
    if user_choice['follower_count'] > choice_b['follower_count']:
        return True
    elif user_choice['follower_count'] < choice_b['follower_count']:
        return False
    elif user_choice['follower_count'] > choice_a['follower_count']:
        return True
    elif user_choice['follower_count'] < choice_a['follower_count']:
        return False


def user_choose(choice_input):
    """Convert the input string to the actual choice."""
    if choice_input == 'A':
        return choice_a
    elif choice_input == 'B':
        return choice_b

def answer_generator():
    """Generates the alternatives randomly from the data dictionary."""
    global choice_a, choice_b
    choice_diff = False
    while choice_diff == False:
        choice_a = random.choice(data)
        choice_b = random.choice(data) 
        if choice_a == choice_b:
            choice_b = random.choice(data)
        else:
            choice_diff = True


score = 0
continue_game = True
while continue_game:
    answer_generator()
    print('--------------------------------------------------------------')
    #print(art.logo)
    print(f"""
    Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}
    {art.vs}
    Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}
    A: {choice_a['follower_count']}, B: {choice_b['follower_count']}
    """)

    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    user_choice = user_choose(user_choice)
    comparision = compare()
    if comparision == True:
        clearConsole()
        print(art.logo)
        print("You're right!")
        score += 1
        print(f"Your current score: {score}")
    else:
        clearConsole()
        print(art.logo)
        print(f"Sorry, that's wrong. You final score: {score}.")
        continue_game = False