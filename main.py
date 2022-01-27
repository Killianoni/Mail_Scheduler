import smtplib
import unicodedata
import time
import os
from getpass import getpass
import re

# Functions

def formatStrip(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
   
def sendMail():
   BODY = '\r\n'.join(['To: %s' % mailRecipient,
                            'From: %s' % mailAddress,
                            'Subject: %s' % mailSubject,
                            '', formatedContent])
   try:
      server.sendmail(mailAddress, mailRecipient.split(","), BODY)
      print("Congrats ! Your email has been scheduled for : ")
      server.quit()
   except:
      print("Error sending mail")
      server.quit()
      

   

# Variables
checkMail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

service = input("What server are you using ? [ 1 - Outlook , 2 - Gmail ] : ")
if int(service) != 1 and int(service) != 2:
   print("Error service not recognized")
   exit()
   
mailAddress = input("What is your mail address ? : \n")
if not re.search(checkMail, mailAddress):
   print("Error mail format not supported")
   exit()
   
mailRecipient = input("What is the mail address of the recipient ? : \n")
if not re.search(checkMail, mailRecipient):
   print("Error mail format not supported")
   exit()
   
mailSubject = input("What is your mail subject ? (50 characters) : \n")
if len(mailSubject) > 50:
   print("Error subject length to high")
   exit()
   
mailContent = input("What is your mail content ? : \n")

mailPwd = getpass("What is your generated password ? : \n")

mailHours = input("When do you want your mail to be sent ? \n Hours : ")
if isinstance(int(mailHours), int) == False:
   print("Error bad time format")

mailMinutes = input("When do you want your mail to be sent ? \n Minutes : ")
if isinstance(int(mailMinutes), int) == False:
   print("Error bad time format")
   
formatedContent = formatStrip(mailContent)

# Send mail

if int(service) == 1:
   server = smtplib.SMTP("smtp-mail.outlook.com", 587)
   server.ehlo()
   server.starttls()
   server.login(mailAddress, mailPwd)
   sendMail()
elif int(service) == 2:
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.ehlo()
   server.starttls()
   server.login(mailAddress, mailPwd)
   sendMail()
