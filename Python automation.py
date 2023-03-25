# program for sending good morning automatically

import requests
import schedule
import time

def send_message():
    resp = requests.post("https://textbelt.com/text", {
        "phone": "08100809125",
        "message": "Rise and shine young blood",
        "key": "textbelt",
    })

    print(resp.json())

schedule.every().day.at('04:30').do(send_message)

#schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)