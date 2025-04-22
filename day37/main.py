import requests
from datetime import datetime

def current_date() -> str:
    date = datetime.today().strftime('%Y%m%d')
    print(f"Today's date is {date}")
    return date

headers = {
    "X-USER-TOKEN": "REPLACE_ME"
}

body = {
    "date": current_date(),
    "quantity": "2"
}

response = requests.post(url="https://pixe.la/v1/users/k33m0l/graphs/python-graph", json=body, headers=headers)
print(response.json())