import pandas as pd
path = r"C:\python_course_projects\Day26_project\nato_phonetic_alphabet.csv"
df = pd.read_csv(path)

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
new_dict = {row.letter: row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()
phonetic = [new_dict[letter] for letter in user_word]
print(phonetic)
