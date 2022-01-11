from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

PASSWORD_FILE = r"C:\python_course_projects\Day29_project\data.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for i in range(random.randint(2, 4))]
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(END, password) 
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    #Get the text inputs in the entries if there are entered information.
    if password_entry.get() and website_entry.get():
        website = website_entry.get().title()
        user = user_entry.get()
        password = password_entry.get()
        new_data = {
            website: {
                "email": user,
                "password": password,
            }
        }
        is_ok = messagebox.askokcancel(title="Confirmation Required", message= f"""These are the details entered: 
        Website: {website}
        Email/Username: {user}
        Password: {password}""")

        if is_ok:
            try:
                with open(PASSWORD_FILE, mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)

            except FileNotFoundError:
                with open(PASSWORD_FILE, mode="w") as file:
                    json.dump(new_data, file, indent=4)

            except ValueError:
                with open(PASSWORD_FILE, mode="w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                with open(PASSWORD_FILE, mode="w") as file:
                    json.dump(data, file, indent=4)


            website_entry.delete(0, END)
            password_entry.delete(0, END)
    
    else:
        messagebox.showwarning(title="Error", message="Please don't leave any fields empty!")

# ---------------------------- SEARCH FUNCTION ------------------------------- #

def search():
    searched_website_name = website_entry.get().title()

    try:
        with open(PASSWORD_FILE, mode="r") as file:
            search_data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="No file for record storage was found. \
            \nPlease add the passwords by clicking on add-button.")
    
    except ValueError:
        messagebox.showinfo(title="Empty File", message="No data in the storage file, the file is empty. \
            \nPlease add the passwords by clicking on add-button.")
    
    else:
        if searched_website_name in search_data:
            search_result_email = search_data[searched_website_name]["email"]
            search_result_password = search_data[searched_website_name]["password"]

        else: 
            messagebox.showinfo(title="Result Not Found", message=f"The website {searched_website_name} you searched for was not found in the file.")
    
    messagebox.showinfo(title="Search Result", message=f"Website: {searched_website_name} \nEmail: {search_result_email} \
    \nPassword: {search_result_password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file = r"C:\python_course_projects\Day29_project\logo.png")
canvas.create_image(100, 100, image=logo)


empty_label_1 = Label(text="")
empty_label_2 = Label(text="")
# empty_label_1.config(padx=20, pady=20)
# empty_label_2.config(padx=20, pady=20)

add_button = Button(text="Add", width=43, command=save)
search_button = Button(text="Search", width=13, command=search)

website_label = Label(text="Website:")
website_entry = Entry(width=32)
website_entry.focus()

user_label = Label(text="Email/Username:")
user_entry = Entry(width=50)
user_entry.insert(END, "youremail@gmail.com")

password_label = Label(text="Password:")
password_entry = Entry(width=32)
password_button = Button(text="Generate Password", width=14, command=generate_password)

empty_label_1.grid(column=0, row=0)
canvas.grid(column=1, row=0)
empty_label_2.grid(column=2, row=0)

website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1)

search_button.grid(column=2, row=1)

user_label.grid(column=0, row=2)
user_entry.grid(column=1, row=2, columnspan=2)

password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)
password_button.grid(column=2, row=3)

add_button.grid(column=1, row=4, columnspan=2)






window.mainloop()