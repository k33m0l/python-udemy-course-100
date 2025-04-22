import requests

API_KEY = "REPLACE_ME" # TODO replace me before commit!

parameters = {
    "lat": 47.49,
    "lon": 19.04,
    "appid": API_KEY,
    "cnt": 5
}

def fetch_forecast():
    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    data = response.json()
    return data

def rain_check(forecasts) -> bool:
    weather_conditins_with_rain = [forecast for forecast in forecasts if forecast["weather"][0]["id"] < 700]
    print(weather_conditins_with_rain)
    return not not weather_conditins_with_rain # Checks if list is not empty

data = fetch_forecast()
will_rain = rain_check(data["list"])

print(f"Location for forecast is: {data["city"]["name"]} in {data["city"]["country"]}")
if will_rain:
    print("The forecast mention rain")
else:
    print("No rain!")