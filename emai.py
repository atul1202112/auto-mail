import smtplib
import ssl
from rt import mail
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "enter your mail @gmail.com"
password = input("enter your password:")
recived = mail

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email

def _send():
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()# Can be omitted
    server.starttls(context=context)# Secure the connection
    server.ehlo()# Can be omitted
    server.login(sender_email, password)
    subject = "this is bot message service"
    body = "To verify fill the form :  "

    msg = f"subject:{subject} \n\n {body}"
    server.sendmail(sender_email, recived, msg)
    print("hey email sented")
    server.quit()
x=0
for x in range(1):
    _send()


# server.quit()