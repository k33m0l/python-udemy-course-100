import requests

parameters = {
    "amount": 3,
    "type": "boolean",
    "category": 18
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = []

if data["response_code"] == 0:
    question_data = data["results"]
else:
    raise Exception("Failed to parse opentdb response")