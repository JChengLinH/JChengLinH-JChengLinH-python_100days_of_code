import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()
import day8_project_art as art
import math
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

answer = "yes"
while answer == "yes":

    correct_input = False
    while correct_input == False:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

        if direction == "encode" or direction == "decode":
            correct_input = True
        else:
            print("Sorry, I didn't get that. Please try again.")
            correct_input = False

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(msg, offset, mode):
        text_list = list(msg)
        content_shifted = []
        default_msg_part = 'encrypted'
        if mode == 'decode':
            offset *= -1
            default_msg_part = 'decrypted'

        for i in text_list:
            if i in alphabet:
                shifted_index = alphabet.index(i) + offset

                if shifted_index >= len(alphabet):
                    shifted_index = shifted_index % len(alphabet)

                elif shifted_index < -len(alphabet):
                    shifted_index = shifted_index % -len(alphabet)
                content_shifted += alphabet[shifted_index]

            else:
                content_shifted += i
        
        caesar_msg = ''.join(content_shifted)
        print(f'The {default_msg_part} message is: {caesar_msg}')


    caesar(text, shift, direction)
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if answer == 'no':
        print('Goodbye.')