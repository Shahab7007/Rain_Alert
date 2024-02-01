import requests
from twilio.rest import Client
import os

account_sid = "ACe0b65fcd412720ac055f76db9bc21d90"
auth_token = os.environ.get("OWM_auth_token")
SENDER_NUMBER = "Twilio phone number insert here"
RECIEVER_NUMBER = "Phone number of person to recieve the alert "
client = Client(account_sid, auth_token)

API_KEY = os.environ.get("OWM_API_KEY")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": 59.9139,    #insert latitude of the city here
    "lon": 10.7522,     #insert longitude of the city here
    "appid": API_KEY
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
will_rain = False
for i in range(0,12):
    if int(data["list"][i]["weather"][0]['id']) > 700:
        will_rain = True
        break


if will_rain:
    message = client.messages.create(
        body="It is going to rain today. Don't forget your umbrella",
        from_=SENDER_NUMBER,
        to=RECIEVER_NUMBER
    )

print(message.status)

# weather_ids= [data["list"][i]["weather"][0]['id']) for i in range(0,11)]