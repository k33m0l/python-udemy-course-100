import requests

HOST = "https://api.sheety.co"
ENDPOINT = "/ENDPOINT/workoutTracking/workouts"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic TOKEN_GOES_HERE"
}

def add_workout(workouts):
    for workout in workouts:
        body = to_request_body(workout)
        response = requests.post(url=f"{HOST}{ENDPOINT}", json=body, headers=headers)
        response.raise_for_status()
        print(response.json())

def to_request_body(workout):
    return {
        "workout": workout
    }
