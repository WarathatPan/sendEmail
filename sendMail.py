# - *- coding: utf- 8 - *-
import os
import csv, smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send_email(subject, text, imgFile, imgFile2):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        password = input('Input your password gmail: ')
        server.login('from@gmail.com', password)

        with open("nameFile.csv", mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for name, email in reader:
                msg = MIMEMultipart()
                msg['Subject'] = subject
                msg['From'] = 'from@gmail.com'
                msg['To'] = email
                # msg['Cc'] = 'email@gmail.com'
                print("name: ", name, "emailSend: ", email)
                #text
                msg.attach(MIMEText(text.format(name),'plain'))
                #image
                img_data = open(imgFile, 'rb').read()
                image = MIMEImage(img_data, name=os.path.basename(imgFile))
                msg.attach(image)
                #image2
                img_data2 = open(imgFile2, 'rb').read()
                image2 = MIMEImage(img_data2, name=os.path.basename(imgFile2))
                msg.attach(image2)
                message = msg.as_string()
                server.sendmail(msg['From'], msg['To'], message)

        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")

subject = "Subject Email"
imgFile = "img.jpg"
imgFile2 = "img2.jpg"
text = """
Dear {}
text in email.
"""
send_email(subject, text, imgFile, imgFile2)