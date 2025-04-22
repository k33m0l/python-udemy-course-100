import requests
from datetime import datetime

HOST = "https://trackapi.nutritionix.com"
ENDPOINT = "/v2/natural/exercise"

headers = {
    "x-app-id": "APP_ID_GOES_HERE",
    "x-app-key": "APP_KEY_GOES_HERE"
}

def call_api(text: str):
    data = {
        "query": text,
        "weight_kg": 90,
        "height_cm": 185,
        "age": 26
    }
    response = requests.post(url=f"{HOST}{ENDPOINT}", headers=headers, json=data)
    response.raise_for_status()
    return response.json()["exercises"]

def interpret(excercises):
    return [to_map(excercise["name"], excercise["duration_min"], excercise["nf_calories"]) for excercise in excercises]

def to_map(workout_type: str, duration_in_min: int, calories: int):
    today = datetime.today()
    return {
        "date": today.strftime("%Y-%m-%d"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": workout_type,
        "duration": duration_in_min,
        "calories": calories
    }