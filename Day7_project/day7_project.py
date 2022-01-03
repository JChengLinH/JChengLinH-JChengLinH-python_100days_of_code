#Step 1 
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()
import random
import day7_project_hangman_art as hangman_art
import day7_project_hangman_words as hangman_words

logo = hangman_art.logo
word_list = hangman_words.word_list
stages = hangman_art.stages

#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

chosen_word = random.choice(word_list)
print(logo)
print(f'The chosen word is: {chosen_word}')
lives = 6
word_len = len(chosen_word)
hidden_letters = []
guessed_letters = []

for n in range(word_len):
    hidden_letters.append('_')

under_scores_count = [hidden_letters.count('_')]
has_under_scores = True
j = 1
while has_under_scores == True and lives > 0:
    guess = input('Guess a letter: ').lower()
    print(f'Your Guess is the letter: {guess}')

    if guess in guessed_letters:
        print(f"You've already guessed the letter: {guess}")
        print(hidden_letters)
    else:

        for i in range(word_len):
            letter = chosen_word[i]
            if guess == letter:
                hidden_letters[i] = letter

        print(' '.join(hidden_letters))
        under_scores_count.append(hidden_letters.count('_'))

        if under_scores_count[j] == under_scores_count[j-1]: #can also be done with "IN" statement to check if the guessed letter is in the chosen word.
            print(stages[lives])
            lives -= 1
            print("You guessed a, that's not in the word. You lose a life")
            print(f'You have {lives} lives left')
            if lives == 0:
                print(stages[lives])
                print('You lose!')
        
        elif '_' not in hidden_letters:
            has_under_scores = False
            print('You win!')
        j += 1
    guessed_letters.append(guess)