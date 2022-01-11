import requests

LAT = 59.329323
LNG = 18.068581

location = {
    "lat": LAT,
    "lng":  LNG,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=location)
response.raise_for_status()
data = response.json()
print(data)