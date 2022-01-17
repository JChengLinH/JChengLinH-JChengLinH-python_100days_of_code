#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P



#Eazy level--------------------------------------------------------------------------------
# letter = ''
# symbol = ''
# number = ''
# for letter_nr in range(1, nr_letters + 1):
#     letter += letters[random.randint(0, len(letters) - 1)]

# for symbol_nr in range(1, nr_symbols +1):
#     symbol += symbols[random.randint(0, len(symbols) - 1)]

# for number_nr in range(1, nr_numbers +1):
#     number += numbers[random.randint(0, len(numbers) - 1)]

# print(letter + symbol + number)


#Hard level--------------------------------------------------------------------------------
# tot = []
# str_len = nr_letters + nr_numbers + nr_symbols
# string = ''

# for letter_nr in range(1, nr_letters + 1):
#     tot.append(letters[random.randint(0, len(letters) - 1)])

# for symbol_nr in range(1, nr_symbols +1):
#     tot.append(symbols[random.randint(0, len(symbols) - 1)])

# for number_nr in range(1, nr_numbers +1):
#     tot.append(numbers[random.randint(0, len(numbers) - 1)])

# for char in tot:
#     pos = random.randint(0, str_len - 1)
#     string = "".join((string[:pos], char, string[pos:]))
# print(string[:pos])

#Hard level (short/easier version)---------------------------------------------------------------
password_list =[]

for letter_nr in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for symbol_nr in range(1, nr_symbols +1):
    password_list.append(random.choice(symbols))

for number_nr in range(1, nr_numbers +1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ''
for char in password_list:
    password += char
print(password)