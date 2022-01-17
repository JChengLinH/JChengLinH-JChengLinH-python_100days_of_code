import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()
import day11_project_art as art
import random

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card_sum_value(input):
    """Summing the value of cards."""
    sum_value = sum(drawn_cards[input])
    if sum_value > 21 and 11 in drawn_cards[input]:
        drawn_cards[input] = [1 if card == 11 else card for card in drawn_cards[input]]
        sum_value = sum(drawn_cards[input])
    return sum_value

def card_drawer(draw_times, player_or_computer):
    """Draws random cards for player and computer."""
    if player_or_computer == 'player':
        for time in range(draw_times):
            player_cards.append(random.choice(cards))

    elif player_or_computer == 'computer':
        for time in range(draw_times):
            computer_cards.append(random.choice(cards))

def compare(player_score, computer_score):
    if player_score == computer_score:
        print("It's a draw!")
        return False

    elif player_score == 21:
        print("You got 21. You won!")
        return False

    elif computer_score == 21:
        print("Computer got 21. You lose!")
        return False

    elif player_score > 21:
        print("You went over. You lose.")
        return False

    elif computer_score > 21:
        print("Computer went over. You win.")
        return False

    else: 
        return True

def black_jack():
    global player_cards, computer_cards ,drawn_cards
    player_cards = []
    computer_cards = []
    drawn_cards = {
        'player': player_cards, 
        'computer': computer_cards
    }
    print(art.logo)
    round = 1
    play = True
    player_score = 0
    computer_score = 0
    player_input = 'y'
    while play:
        if round == 1:
            cards_drawn = 2
        else:
            cards_drawn = 1

        if player_input == 'y':
            if round == 1:
                for key in drawn_cards:
                    card_drawer(cards_drawn, key)
            else:
                card_drawer(cards_drawn, 'player')
                if computer_score < 17:
                    card_drawer(cards_drawn, 'computer')

            player_score = card_sum_value('player')
            computer_score = card_sum_value('computer')

            print(f"Your hand: {drawn_cards['player']}, score: {player_score}")
            print(f"Computer's card: {computer_cards}, score: {computer_score}")
            play = compare(player_score, computer_score)
            if play == True:
                player_input = input("Do you want to draw another card? Type 'y' or 'n': ")
                round += 1

        else:
            if computer_score < 17:
                card_drawer(cards_drawn, 'computer')
                computer_score = card_sum_value('computer')
            print(f"Your final hand: {drawn_cards['player']}, final score: {player_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            compare(player_score, computer_score)
            if player_score > computer_score:
                print("Your score is higher, you win!")
            else:
                print("Computer's score is higher, you lose!")
            play = False
        round += 1
    if play == False:
        game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if game_start == 'y':
            clearConsole()
            black_jack()

game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if game_start == 'y':
    clearConsole()
    black_jack()




























##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
