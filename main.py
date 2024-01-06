import requests
from twilio.rest import Client

weatherapi_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "4efc380539f310e4ebcf421ba83672b6"
account_sid = "AC10c15b2559ab99922a9ba07f31d9351f"
auth_token = "7c9e27ee1f9450913753eeaf5055cbc1"

# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
weather_params = {
    "lat": 47.661290,
    "lon": -122.313130,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(weatherapi_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
text = "Today's weather will be:\n"
datetime_list = []
todays_weather = []

for forecast in weather_data["list"]:
    datetime_list.append(forecast["dt_txt"])
    weather_predictions = forecast["weather"]
    descriptions = [weather["description"] for weather in weather_predictions]
    todays_weather.append(descriptions)


for _ in range(0, 4):
    text += f"{todays_weather[_]} at {datetime_list[_]}\n"


client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='+18443309716',
    body=text,
    to='+14258372741'
)
print(message.status)
# print(text)
