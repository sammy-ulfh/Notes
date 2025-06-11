#!/usr/bin/env python3

import socket
import sys
import argparse
from termcolor import colored

def get_arguments():
    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", dest="target", help="Victim target to scan (Ex: 192.168.1.2)")
    parser.add_argument("-p", "--port", dest="port", help="Ports to scan (Ex: 1-100 or 22,8080,443)")

    options = parser.parse_args()

    if not options.target or not options.port:
        parser.print_help()
        sys.exit(1)

    return options.target, options.port

def port_scanner(h, p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    if not s.connect_ex((h, p)):
        print(colored(f"[+] {p} - OPEN", 'green'))
    
    s.close()

def scan_ports(ports, target):
    for port in ports:
        port_scanner(target, port)

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
