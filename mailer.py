import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

sender_email = "...@gmail.com"
receiver_email = "...@gmail.com"
password = '...'

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
I am ..."""
html = """\
<html>
  <body>
    <h1>Hi,<br>
       How are you?<br>
       I am ...
    </h1>
  </body>
</html>
"""

# Turn these into plain/html/img/file MIMEText objects

with open('test.png', 'rb') as fob:
    img = fob.read()
    fob.close()
    
with open('test.zip', 'rb') as fob:
    zips = fob.read()
    fob.close()

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
part3 = MIMEImage(img)
part3.add_header('Content-Disposition', 'attachment', filename="test.png")
part4 = MIMEApplication(zips)
part4.add_header('Content-Disposition', 'attachment', filename="test.zip")


# Add all parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)
message.attach(part3)
message.attach(part4)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
