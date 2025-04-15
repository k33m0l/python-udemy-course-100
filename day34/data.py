import requests

response = requests.get(url="https://opentdb.com/api.php?amount=5&category=18&difficulty=easy&type=boolean")
response.raise_for_status()
data = response.json()
question_data = []

if data["response_code"] == 0:
    question_data = data["results"]
else:
    raise Exception("Failed to parse opentdb response")