import requests
from config import SendMail
import datetime as dt
import time

LAT = 59.329323
LNG = 18.068581

send_mail = SendMail()
location = {
    "lat": LAT,
    "lng":  LNG,
    "formatted": 0,
}

while True:
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_position = iss_data["iss_position"]
    lat_diff = abs(location["lat"] - float(iss_position["latitude"]))
    lng_diff = abs(location["lng"] - float(iss_position["longitude"]))

    #Check if iss station is nearby.
    if lat_diff <= 5 and lng_diff <= 5:
        is_nearby = True
    else:
        is_nearby = False


    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=location)
    sun_response.raise_for_status()
    sun_data = sun_response.json()

    sunrise_hour = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    #Check if it's dark.
    if dt.datetime.now().hour >= sunset_hour or dt.datetime.now().hour <= sunset_hour:
        is_dark = True
    else:
        is_dark = False

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
    if is_nearby and is_dark:
        send_mail.send("receiver@email.com")
        
    time.sleep(60)

