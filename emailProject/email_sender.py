import smtplib
import os
from email.message import EmailMessage
# To write string literals
from string import Template
# To access to the index.html file
from pathlib import Path
# To load our env, we need to install the package python_dotenv
from dotenv import load_dotenv

# Load env from our .env file. We need to install python_dotenv
project_folder = os.path.expanduser('./')
load_dotenv(os.path.join(project_folder, '.env'))

# smtplib allows us to create a SMTP server || SMTP = Simple Mail Transfer Protocol, it is the protocol to email
# communication (in the same way that HTTP it is for the web)

# What we are doing here is read index.html content with Path, and we turn into a template
html = Template(Path('index.html').read_text())
# Configuration
email = EmailMessage()
email['from'] = 'Sergio Cordero'
email['to'] = os.environ.get("EMAIL_TO")
email['subject'] = 'Test email!'

# html var is now a template, so we can substitute the variables (and we parse into html again so we can see the email
# in a correct format
email.set_content(html.substitute({'name': 'Sergio', 'prize': 'car'}), 'html')

# SMTP protocol uses, normally, port 587
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # This is part of the protocol, and it is like a hello message to know the connection is made
    smtp.ehlo()
    # Encryption mechanism to a secure connection to the server
    smtp.starttls()

    smtp.login(os.environ.get("EMAIL"), os.environ.get("PASSWORD"))
    smtp.send_message(email)
    print("Email sent!")
