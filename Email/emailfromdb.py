import sqlite3
import smtplib
import os
import ssl
from email.mime.text import MIMEText
clear = lambda: os.system('cls')
conn = sqlite3.connect('clothinator.db')
c = conn.cursor()
username = "SpencerA"
#c.execute("Select username FROM profiles")
#display = (c.fetchall())
#print(display)
c.execute("SELECT email FROM profiles WHERE username =:username", {'username':username})
email = c.fetchone()
email = email[0]
print(email)

#YAH DOOFUS - IT RETURNS A LIST
#DONT TURN TO STRING AND GET RID OF LAST AND FIRST 2 CHARACTERS
#JUST TAKE 0TH POSITION IN THE LIST VARIABLE TO THE SAME VARIABLE

from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'arthuremailfromdb@gmail.com'
password = 'emailfromdb'
sender = 'arthuremailfromdb@gmail.com'
targets = ['spenceraspencer1@gmail.com', 'spencera@dulwich.org.uk']

msg = MIMEText('Hi, how are you today?')
msg['Subject'] = 'Hello'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()


print("I think it worked")
