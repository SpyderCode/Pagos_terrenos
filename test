import smtplib, ssl
import time
port = 465  # For SSL
Email=""
password=""

# Create a secure SSL context


def SendEmail(Destination,message):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(Email, password)
        print("Sending mail to:"+Destination)
        msg="Subject:El Intercambio\n\n"+message
        time.sleep(10)
        #print(msg)
        server.sendmail(Email, Destination, str(msg))
        print("Email Sent")
