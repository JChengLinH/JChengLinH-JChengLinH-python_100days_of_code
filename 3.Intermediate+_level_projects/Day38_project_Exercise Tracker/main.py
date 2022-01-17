import requests
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv(r"C:\python_course_projects\Day38_project_Exercise Tracker\credentials.env")

exercise_headers = {
    "x-app-id": os.getenv("API_ID"),
    "x-app-key": os.getenv("API_KEY"),
    "x-remote-user-id": "0",
}

exercise_params = {
    "query": input("Tell me what you did: ").lower(),
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 173,
    "age": 26,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_headers)
exercise_data = exercise_response.json()

exercise_list = [exercise for exercise in exercise_data["exercises"]]

exercise_name = exercise_data["exercises"][0]["name"]
sheet_endpoint = "https://api.sheety.co/04fb24e7885df456b282ee417cd25aa7/myWorkouts/workouts"
sheet_headers = {
    "Authorization": os.getenv("SHEETY_TOKEN"),
    "Content-Type": "application/json",
}

for exercise in exercise_list:
    sheet_params = {
        "workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().time().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
            }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_params, headers=sheet_headers)
    sheet_response.raise_for_status()