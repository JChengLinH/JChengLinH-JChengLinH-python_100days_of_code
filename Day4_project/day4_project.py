import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list = [rock, paper, scissors]
choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
computer_choice = random.randint(0, 2)


if choice == computer_choice:
    print(choice_list[choice])
    print(f"computer_choice:\n{choice_list[computer_choice]}\nIt's a tie")

elif choice == 0:
    print(choice_list[choice])
    if computer_choice == 1:
        print(f"computer_choice:\n{choice_list[computer_choice]}\nYou lose")
    else:
        print(f"computer_choice:\n{choice_list[computer_choice]}\nYou won")

elif choice == 1:
    print(choice_list[choice])
    if computer_choice == 2:
        print(f"computer_choice:\n{choice_list[computer_choice]}\nYou lose")
    else:
        print(f"computer_choice:\n{choice_list[computer_choice]}\nYou won")

elif choice == 2:
    print(choice_list[choice])
    if computer_choice == 0:
        print(f"computer_choice:\n{choice_list[computer_choice]}\nYou lose")
    else:
        print(f"computer_choice:\n{choice_list[computer_choice]}\nYou won")
