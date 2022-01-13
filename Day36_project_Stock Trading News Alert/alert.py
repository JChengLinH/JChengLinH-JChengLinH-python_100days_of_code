import smtplib
from twilio.rest import Client
from email.mime.text import MIMEText

# import os
# from dotenv import load_dotenv

class SendAlert:


    def __init__(self):
        pass


    def send_mail(self, sender_mail: str, sender_password: str, receiver_mail: str, message: str):
        message = MIMEText(_text=message, _charset="UTF-8")
        message["Subject"] = "Stock Alert"
        message["From"] = sender_mail
        message["To"] = receiver_mail

        with smtplib.SMTP("smtp.gmail.com", port=587) as self.mail_connection:
            self.mail_connection.starttls()
            self.mail_connection.login(user=sender_mail, password=sender_password)
            self.mail_connection.sendmail(from_addr=sender_mail, to_addrs=receiver_mail, msg=message.as_string())


    def send_sms(self, from_nr, to_nr, twilio_sid, auth_token, message):
        client = Client(twilio_sid, auth_token)
        message = client.messages \
                    .create(
                        body=message,
                        from_=from_nr,
                        to=to_nr
                    )