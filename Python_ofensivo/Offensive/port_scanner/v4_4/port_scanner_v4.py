#!/usr/bin/env python3

import socket
from concurrent.futures import ThreadPoolExecutor
import argparse
from termcolor import colored
import signal
import sys

open_sockets = []

def def_handler(sig, frame):
    
    print(colored(f"\n[-] Terminando procesos correctamente...\n", "yellow"))

    for socket in open_sockets:
        socket.close()

    print(colored(f"\n[!] Saliendo del programa...\n", "red"))
    
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler) # CTRL + C

def get_arguments():
    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", dest="target", required=True, help="Victim target to scan (Ex: 192.168.1.2)")
    parser.add_argument("-p", "--port", dest="port", required=True, help="Ports to scan (Ex: 1-100 or 22,8080,443)")

    options = parser.parse_args()

    return options.target, options.port

def port_scanner(h, p):

    global open_sockets

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    open_sockets.append(s)

    try:

        s.connect((h, p))
        s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
        response = s.recv(1024)
        response = response.decode(errors='ignore').split('\n')[0]

        if not response:
            print(colored(f"[+] {p} - OPEN", 'green'))
        else:
            print(colored(f"[+] {p} - {response}", 'green'))

    except (s.timeout, ConnectionRefusedError):
        pass
    
    finally:
        s.close()

def scan_ports(ports, target):
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(lambda port: port_scanner(target, port), ports)

def parse_ports(ports_str):

    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        return range(start, end+1)
    elif ',' in ports_str:
        return map(int, ports_str.split(','))
    else:
        return (int(ports_str),)

def main():

    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(ports, target)

if __name__ == '__main__':
    main()
