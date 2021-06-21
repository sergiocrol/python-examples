import os
from twilio.rest import Client
from dotenv import load_dotenv

project_folder = os.path.expanduser('./')
load_dotenv(os.path.join(project_folder, '.env'))

account_sid = 'ACc7464de0a39c708ec77e4d639f4ed642'
auth_token = os.environ.get('AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGd7a1a3d7400c56fa6c165060ee42c20b',
    body='Sending from codeeeeee',
    to=os.environ.get('NUMBER')
)

print(message.sid)