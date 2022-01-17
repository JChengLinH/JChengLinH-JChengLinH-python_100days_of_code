#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import pandas as pd
import os
import datetime as dt
from dotenv import load_dotenv
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

load_dotenv(r"C:\python_course_projects\Day39_Capstone_project_Flight_deal_finder\credentials.env")
sheet = DataManager(os.getenv("SHEET_ENDPOINT"), os.getenv("SHEETY_TOKEN"))

departure_airport = "ARN"
flight_search = FlightSearch(os.getenv("SHEET_ENDPOINT"), os.getenv("SHEETY_TOKEN"), os.getenv("KIWI_API_KEY"))
df_recorded_data = pd.DataFrame(flight_search.sheet.city_list)

flight_tickets = flight_search.search_flights(departure_airport, flight_search.fetch_iata_code())


ticket_currency = flight_tickets["currency"]

ticket_data=[]
for ticket in flight_tickets["data"]:
    ticket_data.append({key: value for (key, value) in ticket.items() if \
    key == "cityFrom" or key == "cityTo" or key == "flyFrom" or key == "flyTo" or \
    key == "price" or key == "utc_departure" or key == "deep_link"})# 

df_ticket_data = pd.DataFrame(ticket_data)
print(flight_tickets["data"])
#print(df_ticket_data)

for index, row in df_ticket_data.iterrows():
    recorded_lowest_price = df_recorded_data[df_recorded_data.city == row["cityTo"]].lowestPrice.values[0]
    #print(recorded_lowest_price)
    object_id = df_recorded_data[df_recorded_data.city == row["cityTo"]].id.values[0]

    if row.price < recorded_lowest_price or recorded_lowest_price == "nan":
        sheet.write_sheet_data(row.flyTo, row.price, object_id)
        msg = f"""Low price flight ticket! Only {row['price']} {ticket_currency} 
to fly from {row.cityFrom}-{row.flyFrom} to {row.cityTo}-{row.flyTo} at {row.utc_departure}.
Booking link: {row.deep_link}"""
        notification = NotificationManager(msg)
        notification.send_mail(os.getenv("SENDER_MAIL"), os.getenv("MAIL_PASSWORD"), os.getenv("receiver_mail"))
        notification.send_sms(os.getenv("TWILIO_NUMBER"), os.getenv("receiver_phone"), os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_KEY"))




