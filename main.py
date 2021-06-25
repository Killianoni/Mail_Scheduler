import smtplib
import unicodedata

# Function

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')


# Variables

with open('orders.txt', 'r') as file:
    orderstr = file.read().replace('\n', '')
    orders = orderstr.split(',')
with open('content.txt', 'r') as file:
    content = file.read().replace('\n', '')
with open('to.txt', 'r') as file:
    TO = file.read().replace('\n', '')
with open('subject.txt', 'r') as file:
    SUBJECT = file.read().replace('\n', '')

# Gmail Sign In

with open('mail.txt', 'r') as file:
    gmail_sender = file.read().replace('\n', '')
with open('pwd.txt', 'r') as file:
    gmail_passwd = file.read().replace('\n', '')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

# Loop orders

for order in orders:
    
    asciicontent = strip_accents(content).format(order)

    # Send mail

    BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', asciicontent])

    try:
        server.sendmail(gmail_sender, TO.split(","), BODY)
        print('email sent')
    except:
        print('error sending mail')

server.quit()
