import smtplib
from twilio.rest import Client
from email.mime.text import MIMEText

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__ (self, message: str):
        self.sms_message = message
        self.mail_message = MIMEText(_text=message, _charset="UTF-8")
        self.mail_message["Subject"] = "Low Flight Ticket Price"
        

    def send_mail(self, sender_mail: str, sender_mail_password: str, receiver_mail: str):
        self.mail_message["From"] = sender_mail
        self.mail_message["To"] = receiver_mail
        with smtplib.SMTP("smtp.gmail.com", port=587) as mail_connection:
            mail_connection.starttls()
            mail_connection.login(user=sender_mail, password=sender_mail_password)
            mail_connection.sendmail(from_addr=sender_mail, to_addrs=receiver_mail, msg=self.mail_message.as_string())

    
    def send_sms(self, from_nr, to_nr, twilio_sid, auth_token):
        client = Client(twilio_sid, auth_token)
        sms_message = client.messages \
                    .create(
                        body=self.sms_message,
                        from_=from_nr,
                        to=to_nr
                    )
