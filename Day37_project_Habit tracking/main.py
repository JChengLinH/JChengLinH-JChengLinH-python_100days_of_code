import datetime as dt
import requests
from dotenv import load_dotenv
import os

load_dotenv(r"C:\python_course_projects\Day37_project_Habit tracking\credentials.env")
USERNAME = os.getenv("USER")
TOKEN = os.getenv("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

date = dt.datetime.now()
quantity = input("How many km did you cycle today? ")
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
graph_config = {
    "date": date.strftime("%Y%m%d"),
    "quantity": quantity,
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)