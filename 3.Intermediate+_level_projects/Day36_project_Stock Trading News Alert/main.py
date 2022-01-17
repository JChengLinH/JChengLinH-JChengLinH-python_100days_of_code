import os
from time import timezone
import requests
from dotenv import load_dotenv
import datetime as dt
from alert import SendAlert

load_dotenv(r"C:\python_course_projects\Day36_project_Stock Trading News Alert\credentials.env")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")

alert = SendAlert()
from_date = str(dt.datetime.utcnow().date() - dt.timedelta(days=2))
to_date = str(dt.datetime.utcnow().date() - dt.timedelta(days=1))

parameters = {
    "news_api":{
        "qInTitle": COMPANY_NAME,
        #"from": from_date,
        #"to": to_date,
        "sortBy":"relevancy",
        "apiKey": NEWS_API_KEY,
        "language":"en",
    },

    "stock_api": {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY,
    },
}

stock_response = requests.get(url="https://www.alphavantage.co/query", params=parameters["stock_api"])
stock_response.raise_for_status()
stock_data = stock_response.json()

closing_price_from_date = float(stock_data["Time Series (Daily)"][from_date]["4. close"])
closing_price_to_date = float(stock_data["Time Series (Daily)"][to_date]["4. close"])

#Stock change in percent
stock_change = (closing_price_to_date / closing_price_from_date - 1) * 100
msg_list = []
if abs(stock_change) > 3:
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=parameters["news_api"])
    news_response.raise_for_status()
    news_data = news_response.json()
    top_articles = news_data["articles"][:3]

    for article in top_articles:
        msg = f"""{STOCK}: [emoji]{stock_change:0.2f}%
Headline: {article["title"]}
Brief: {article["description"]}
Link: {article["url"]}
"""

        if stock_change > 0:
            msg = msg.replace("[emoji]", "💹")
        else:
            msg = msg.replace("[emoji]", "🔻")

        msg_list.append(msg)

    for msg in msg_list:
        alert.send_mail(os.getenv("sender_mail"), os.getenv("mail_password"), os.getenv("receiver_mail"), msg)
        alert.send_sms(os.getenv("TWILIO_NUMBER"), os.getenv("receiver_phone"), os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_KEY"), msg)
