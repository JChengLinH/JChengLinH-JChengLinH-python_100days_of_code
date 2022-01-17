import random
import os
from typing import TextIO
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

def compare():
    global guessing
    if guess > answer:
        return 'Too high.'
    elif guess < answer:
        return 'Too low.'
    else:
        guessing = False
        return f'You got it! The answer was {answer}.'


print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
number_list = list(range(1,101))
answer = random.choice(number_list)
print(f'The answer is: {answer}')
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    tries = 10
else:
    tries = 5

guessing = True
while guessing:
    print(f"You have {tries} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    print(compare())
    tries -= 1
    if tries == 0:
        guessing = False
        print("You've run out of guessses, you lose.")