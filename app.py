import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
load_dotenv()

smtp_server = 'smtp.gmail.com'
smtp_port = 587 #specific port, most email clients use this one
sender_email = os.getenv('email')
sender_password = os.getenv('password')

recipient_email = '3475171648@tmomail.net' #note this suffix is only for tmobile
sms_body = 'Hello, this is a test SMS via email!'

msg = MIMEText(sms_body)
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = 'Test SMS'
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("SMS sent!")
except:
    print('you stupid')
