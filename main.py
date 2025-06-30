"""
1-twilio client setup
2-user inputs
3-scheduling logic
4-send message
"""
# step1 importing all libraries

from twilio.rest import Client
from datetime import datetime,timedelta
import time
import os
from dotenv import load_dotenv
load_dotenv()

# step2 twilio credentials
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')  
client=Client(account_sid,auth_token)
#step3 design send msg function
def send_whatsapp_msg(recipient_number,msg_body):
  try:
    message=client.messages.create(
      from_='whatsapp:+14155238886',
      body=msg_body,
      to=f'whatsapp:{recipient_number}'
    )
    print(f'Message sent successfully! Message SID{message.sid}')
  except Exception as e:
    print(f"An error occured {e}")

#step4 user input
name=input("Enter the recipient name : ")
recipient_no=input("Enter the recipient whatsapp no with country code : ")
message_body=input(f'Enter the message you want to send to {name} : ')
#step5 parse date/time and calculate delay

date_str=input("Enter the date to send the message (YYYY-MM-DD): ")
time_str=input("Enter the time to send the message (HH:MM in 24 hours format): ")

#step6 datetime
schedule_datetime=datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")
current_datetime=datetime.now()

# step7 calculate delay
time_difference=schedule_datetime-current_datetime
delay_seconds=time_difference.total_seconds()

if(delay_seconds <=0):
  print("The specified time is the past time. Please enter a future date and time:")
else:
  print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

  # wait until the scheduled time comes
  time.sleep(delay_seconds)

  # send the message
  send_whatsapp_msg(recipient_no,message_body)