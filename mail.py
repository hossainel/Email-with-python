import os, smtplib, imghdr
#from email.message import EmailMessage

dic = {} #EmailMessage()
email = 'muktacomputers46@gmail.com'
dic['From'] = email
dic['To'] = 'themuktacomputers@gmail.com'
dic['Subject'] = 'Test'
dic['message'] = 'Testy Test'
password = 'Freedomair'

port = 465
port = 587

#with smtplib.SMTP('smtp.gmail.com', port) as smtp:
#    smtp.login(email, password)
#    smtp.send_message(dic)    
mail = smtplib.SMTP('smtp.gmail.com', port)
mail.ehlo()
mail.starttls()
mail.login(email, password)
mail.sendmail(email, dic['To'], dic['message'])
mail.close()