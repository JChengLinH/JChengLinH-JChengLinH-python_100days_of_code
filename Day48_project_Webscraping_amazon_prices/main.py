import os
import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from email.mime.text import MIMEText

url = "https://www.amazon.com/EVGA-GeForce-10G-P5-3897-KL-Technology-Backplate/dp/B097S6JDMV/ref=sr_1_1?crid=2IWYC73232CYU&keywords=rtx+3080&qid=1642430224&sprefix=rtx+3080%2Caps%2C216&sr=8-1"
headers = {
    "Accept-Language": "en-US,en",
    "User-Agent": "Chrome/97.0.4692.71",
}

response = requests.get(url=url, headers=headers)
response.raise_for_status()
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")
product_name = soup.find(name="span", id="productTitle").getText()
product_price_whole = soup.find(name="span", class_="a-price-whole").getText().replace(",", "")
product_price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
product_price = float(f"{product_price_whole}{product_price_fraction}")

price_threshold = 2000

if product_price <= price_threshold:
    load_dotenv(r"C:\python_course_projects\Day48_project_Webscraping_amazon_prices\creds.env")
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as mail_connection:
        message = MIMEText(_text=f"{product_name} is now ${product_price}", _charset="UTF-8")
        message["Subject"] = f"Low Product Price Notification"
        message["To"] = os.getenv("receiver_mail")
        message["From"] = os.getenv("sender_mail")
        

        mail_connection.starttls()
        mail_connection.login(os.getenv("sender_mail"), os.getenv("mail_password"))
        mail_connection.sendmail(
            from_addr=os.getenv("sender_mail"), 
            to_addrs=os.getenv("receiver_mail"),
            msg=message.as_string()
            )
