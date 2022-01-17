import pandas as pd
path = r"C:\python_course_projects\Day26_project\nato_phonetic_alphabet.csv"
df = pd.read_csv(path)


new_dict = {row.letter: row.code for (index, row) in df.iterrows()}

def func():
    user_word = input("Enter a word: ").upper()
    try:
        phonetic = [new_dict[letter] for letter in user_word]
        
    except KeyError:
        print("Sorry, only the English alphabets please.")
        func()
    else:
        print(phonetic)
    
func()