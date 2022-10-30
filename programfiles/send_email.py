import smtplib
from email.message import EmailMessage

def send_email(sender, password, receiver, subject, filename):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    msg.add_attachment(open(filename, "r").read(), filename=filename)


    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(sender, password)
    s.send_message(msg)

