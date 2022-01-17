import requests
from twilio.rest import Client

TWILIO_SID = ""
AUTH_TOKEN = ""
OW_API_KEY = ""
sender_nr = "Twilio number"
receiver_nr = "Receiver's number"
ow_parameters = {
    "lat": 59.329323,
    "lon": 18.068581,
    "appid": OW_API_KEY,
    "exclude": "current,minutely,daily"
}

ow_response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=ow_parameters)
ow_response.raise_for_status()
weather_data = ow_response.json()

will_rain = False
for weather_cond in weather_data["hourly"][:11]:
    weather_cond_code = int(weather_cond["weather"][0]["id"])
    if weather_cond_code < 700:
        will_rain = True

if will_rain:   
    client = Client(TWILIO_SID, AUTH_TOKEN)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an umbrella.",
                     from_=sender_nr,
                     to=receiver_nr
                 )