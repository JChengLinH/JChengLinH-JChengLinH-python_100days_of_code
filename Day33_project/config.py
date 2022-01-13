import smtplib
class SendMail:
    def __init__(self):
        self.sender_mail = "sender@gmail.com"
        self.password = "sender password"
        self.message = "Look up! The ISS station is above you!"
    
    def send(self, receiver_mail):
        with smtplib.SMTP("smtp.gmail.com", port=587) as self.mail_connection:
            self.mail_connection.starttls()
            self.mail_connection.login(user=self.sender_mail, password=self.password)
            self.mail_connection.sendmail(from_addr=self.sender_mail, to_addrs=receiver_mail, msg=f"Subject:ISS Station \n\n{self.message}")
