import smtplib, ssl
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()


def send(data):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = os.getenv("senderEmail")
    receiver_email = os.getenv("receiverEmail")
    receiver_email2 = os.getenv("receiverEmail2")
    password = os.getenv("password")
    message = """
{rows} """

    msg = MIMEText(message.format(rows=rows(len(data), data)))

    msg['Subject'] = 'Free Games'
    msg['From'] = os.getenv("senderEmail")
    msg['To'] = os.getenv("receiverEmail")
    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com", port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, os.getenv("password"))
        server.sendmail(sender_email, receiver_email, msg.as_string())
        # server.sendmail(sender_email, receiver_email2, msg.as_string())
        print("Successfully sent email")

def rows(number, data):
    msg = ''
    for i in range(0, number):
        text = data[i][0]
        link = data[i][1]
        msg = msg + f"{text} : {link} \n\n"
    return msg
