#!/usr/bin/env python3

import socket
import sys
from termcolor import colored

# global variables
host = None
p_1 = None
p_2 = None

def get_variables():
    global host
    global p_1
    global p_2

    if len(sys.argv) == 4:
        host = sys.argv[1]
        try:
            p_1 = int(sys.argv[2])
            p_2 = int(sys.argv[3])

            if not p_1 < p_2:
                return 1
        except:
            print(colored(f"\n[+] PORT could be a number.", 'red'))
    else:
        print(colored('[+] Usage:', 'yellow'))
        print(colored(f"\t{sys.argv[0]} HOST FIRST_PORT FINAL_PORT", 'white'))
        return 2

def port_scanner(h, p):
    if h and p:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        if not s.connect_ex((h, p)):
            print(colored(f"[+] {p} - OPEN", 'green'))
        
        s.close()

def main():
    status = get_variables()

    if status == 1:
        print(colored(f"\n[+] The first port range could be minor than the second.", 'red'))
        exit
    elif status == 2:
        exit
    else:
        for port in range(p_1, p_2+1):
            port_scanner(host, port)

if __name__ == '__main__':
    main()
