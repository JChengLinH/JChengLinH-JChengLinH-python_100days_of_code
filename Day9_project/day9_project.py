#Silent auction program
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

import day9_project_art as art
print(art.logo)



add_bidder = True
bid_history = {}
while add_bidder == True:
    name = input("What's your name?: ")
    bid = input("What's your bid?: $")

    bid_history[name] = bid

    bidder = input('Is there any other bidders? Type yes or no.').lower()
    if bidder == 'no':
        add_bidder = False
    else:
        clearConsole()

clearConsole()
max_bid = 0
for bidder_name in bid_history:
    if int(bid_history[bidder_name]) > max_bid:
        max_bid = int(bid_history[bidder_name])
        max_bidder_name = bidder_name

print(f"The winner is {max_bidder_name}: {max_bid}")