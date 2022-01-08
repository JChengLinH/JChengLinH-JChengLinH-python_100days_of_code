#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("/python_course_projects/Day24_project/Input/Names/invited_names.txt") as names:
    names = names.read().splitlines()
with open("/python_course_projects/Day24_project/Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()


for name in names:
    letter_input = letter_content.replace("[name]", name)
    print(name)
    with open(f"/python_course_projects/Day24_project/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
        new_letter.write(letter_input)

