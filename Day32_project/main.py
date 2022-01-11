import smtplib
import datetime as dt
import random
import pandas as pd
##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv

birthday_file = pd.read_csv(r"C:\python_course_projects\Day32_project\birthdays.csv")
today = dt.datetime.today()

for index, row in birthday_file.iterrows():
# 2. Check if today matches a birthday in the birthdays.csv
    if row.month == today.month and row.day == today.day:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_nr = random.randint(1,3)
        print(letter_nr)
        with open(fr"C:\python_course_projects\Day32_project\letter_templates\letter_{letter_nr}.txt") as letter:
            message = letter.read().replace("[NAME]", row["name"])
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            sender_email = "youremail@gmail.com"
            password = "yourpassword"
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(from_addr=sender_email, to_addrs=row.email, msg=f"Subject:Happy Bday\
                \n\n{message}")





    
