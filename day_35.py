import requests
import os
from twilio.rest import Client

ENDPOINT = " https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ["OWM_API_KEY"]
MY_LAT = 4.815554
MY_LONG = 7.049844
ACCOUNT_SID = os.environ["ACCOUNT_SID"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
}

response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
next_twelve = data["list"][:4]

will_rain = False
for forecast in next_twelve:
    weather_id = forecast["weather"][0]["id"]
    if weather_id < 600:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to carry an umbrella☔☔.",
        from_="+12246434390",
        to="+2348026718076"
    )

    print(message.status)
